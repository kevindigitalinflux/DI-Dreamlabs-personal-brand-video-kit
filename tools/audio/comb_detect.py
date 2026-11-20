#!/usr/bin/env python3
"""Detect a comb-filter echo (for example two microphones summed a few milliseconds apart).

Standard library only. Slow on long files, so give it a 16 kHz mono WAV of speech.

Make the input with FFmpeg:
    ffmpeg -i recording.mkv -vn -ac 1 -ar 16000 -c:a pcm_s16le audio16k.wav

Run:
    python comb_detect.py audio16k.wav [--start 0] [--end 120]

How it works: average the power spectrum of loud (speech) frames, remove the smooth
trend, and look at the spectrum of the ripple (a cepstrum). A strong peak at a delay
of a few milliseconds is a comb filter. The delay in samples at 48 kHz is the number
to give comb_fix.py.

Real example: two OBS microphones summed gave a peak at 9.75 ms (468 samples at 48 kHz)
and a hollow voice.
"""
import argparse
import cmath
import math
import struct
import wave


def fft(a):
    n = len(a)
    if n == 1:
        return a
    ev = fft(a[0::2])
    od = fft(a[1::2])
    r = [0] * n
    for k in range(n // 2):
        t = cmath.exp(-2j * math.pi * k / n) * od[k]
        r[k] = ev[k] + t
        r[k + n // 2] = ev[k] - t
    return r


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("wav", help="16 kHz mono 16-bit WAV of speech")
    ap.add_argument("--start", type=float, default=0.0, help="start second (skip silence before you speak)")
    ap.add_argument("--end", type=float, default=None, help="end second")
    ap.add_argument("--energy", type=float, default=1e-3, help="speech frame energy threshold (default about -30 dB)")
    args = ap.parse_args()

    w = wave.open(args.wav)
    sr = w.getframerate()
    n = w.getnframes()
    if w.getnchannels() != 1 or w.getsampwidth() != 2:
        raise SystemExit("Need a mono 16-bit WAV. See the FFmpeg command in the file header.")
    x = [v / 32768 for v in struct.unpack("<%dh" % n, w.readframes(n))]

    N, hop = 2048, 1024
    win = [0.5 - 0.5 * math.cos(2 * math.pi * i / N) for i in range(N)]
    acc = [0.0] * (N // 2)
    cnt = 0
    end = int((args.end if args.end is not None else n / sr) * sr)
    for s in range(int(args.start * sr), end - N, hop):
        seg = x[s:s + N]
        if sum(v * v for v in seg) / N < args.energy:
            continue
        F = fft([seg[i] * win[i] for i in range(N)])
        for k in range(N // 2):
            acc[k] += abs(F[k]) ** 2
        cnt += 1
    if cnt == 0:
        raise SystemExit("No speech frames found. Lower --energy or check --start/--end.")
    print("speech frames used:", cnt)

    db = [10 * math.log10(a / cnt + 1e-12) for a in acc]
    h = 20
    ripple = [db[k] - sum(db[k - h:k + h + 1]) / (2 * h + 1) for k in range(h, len(db) - h)]
    b0 = max(int(100 / (sr / N)) - h, 0)
    b1 = int(6000 / (sr / N)) - h
    rp = ripple[b0:b1]
    M = 1
    while M < len(rp):
        M *= 2
    rp = rp + [0] * (M - len(rp))
    C = fft(rp)
    mag = [abs(c) for c in C[:M // 2]]
    df = sr / N
    best = sorted(range(3, M // 2), key=lambda q: -mag[q])[:6]
    print("ripple std (dB): %.2f" % ((sum(v * v for v in rp) / len(rp)) ** 0.5))
    print("strongest delays (a clear single peak at a few ms means a comb filter):")
    for q in best:
        d = q / (df * M) * 1000
        print("  delay %.2f ms  strength %.1f  = %d samples at 48 kHz" % (d, mag[q], round(d / 1000 * 48000)))


if __name__ == "__main__":
    main()

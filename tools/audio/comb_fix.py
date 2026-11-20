#!/usr/bin/env python3
"""Reduce a comb-filter echo on a whole recording with a feedback filter.

    y[n] = x[n] - g * y[n - D]

D is the delay in samples at 48 kHz (from comb_detect.py). The tool uses g = 0.65 by
default. This REDUCES the hollow sound; it cannot remove it completely. Apply it to the
whole raw recording BEFORE cutting, then cut, then set loudness (build_voice.py).

Needs FFmpeg on PATH and Python 3.10+, standard library only (slow but fine for minutes).

    python comb_fix.py recording.mkv fixed.wav --delay-ms 9.75
"""
import argparse
import array
import os
import subprocess
import tempfile


def ff(args):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-y"] + args, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("ffmpeg failed:\n" + r.stderr[-800:])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", help="recording (any audio or video file FFmpeg can read)")
    ap.add_argument("output", help="output WAV, mono 48 kHz float")
    ap.add_argument("--delay-ms", type=float, required=True, help="delay from comb_detect.py, for example 9.75")
    ap.add_argument("--gain", type=float, default=0.65, help="feedback amount, default 0.65")
    args = ap.parse_args()

    with tempfile.TemporaryDirectory() as tmp:
        raw = os.path.join(tmp, "raw.f32")
        ff(["-i", args.input, "-vn", "-ac", "1", "-ar", "48000", "-f", "f32le", raw])
        x = array.array("f")
        with open(raw, "rb") as f:
            x.fromfile(f, os.path.getsize(raw) // 4)
        D = round(args.delay_ms / 1000 * 48000)
        g = args.gain
        y = array.array("f", [0.0]) * len(x)
        for i in range(len(x)):
            y[i] = x[i] - (g * y[i - D] if i >= D else 0.0)
        fixed = os.path.join(tmp, "fixed.f32")
        with open(fixed, "wb") as f:
            f.write(y.tobytes())
        ff(["-f", "f32le", "-ar", "48000", "-ac", "1", "-i", fixed, "-c:a", "pcm_f32le", args.output])
    print("wrote", args.output, "delay samples", D, "gain", g)


if __name__ == "__main__":
    main()

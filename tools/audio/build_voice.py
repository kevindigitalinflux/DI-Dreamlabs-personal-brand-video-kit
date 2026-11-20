#!/usr/bin/env python3
"""Build the final voice track from a cut list: cut, join, one gain, true-peak limit.

Approved method (talking heads): no EQ, no compression, no noise reduction, no per-clip
level matching. Steps:
  1. cut each segment from the source with 3 ms fade in and out,
  2. join them,
  3. ONE linear gain so integrated loudness is -14 LUFS, measured on DUAL-MONO stereo
     (a mono file reads about 3 LU lower and would make the limiter work too hard),
  4. oversampled true-peak limiter. `level=0` is essential: without it FFmpeg auto-levels
     peaks up to 0 dBFS.
Then it prints loudness and peak of the result (target -14 LUFS, peak at or below -1.5 dB).

Cut list JSON (seconds in the source file):
    {"segments": [{"id": "A01", "srcIn": 13.89, "dur": 2.39}, {"id": "A02", "srcIn": 27.95, "dur": 4.13}]}

    python build_voice.py source.wav cutlist.json voice.wav [--target -14]

Use the comb_fix.py output as the source if the recording was hollow. Cut at real silence
(FFmpeg silencedetect), never inside a phrase. Offer the person A/B files and let them choose.
"""
import argparse
import json
import os
import re
import subprocess
import tempfile


def ff(args):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-y"] + args, capture_output=True, text=True)
    return r.stderr


def measure(path):
    out = ff(["-i", path, "-af", "pan=stereo|c0=c0|c1=c0,ebur128=peak=true", "-f", "null", "-"])
    lufs = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", out)[-1])
    peak = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", out)[-1])
    return lufs, peak


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source")
    ap.add_argument("cutlist")
    ap.add_argument("output")
    ap.add_argument("--target", type=float, default=-14.0, help="integrated LUFS target, default -14")
    ap.add_argument("--limit", type=float, default=0.84, help="limiter ceiling, linear (0.84 is about -1.5 dB)")
    args = ap.parse_args()

    segs = json.load(open(args.cutlist))["segments"]
    with tempfile.TemporaryDirectory() as tmp:
        files = []
        for s in segs:
            f = os.path.join(tmp, "%s.wav" % s["id"])
            d = s["dur"]
            ff(["-ss", str(s["srcIn"]), "-t", str(d), "-i", args.source, "-vn", "-ac", "1", "-ar", "48000",
                "-af", "afade=t=in:d=0.003,afade=t=out:st=%s:d=0.003" % (d - 0.003), "-c:a", "pcm_f32le", f])
            files.append(f)
        lst = os.path.join(tmp, "list.txt")
        open(lst, "w").write("".join("file '%s'\n" % p.replace("\\", "/") for p in files))
        joined = os.path.join(tmp, "joined.wav")
        ff(["-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", joined])
        lufs, _ = measure(joined)
        gain = args.target - lufs
        ff(["-i", joined, "-af",
            "volume=%sdB,aresample=192000,alimiter=limit=%s:attack=1:release=50:level=0,aresample=48000,"
            "pan=stereo|c0=c0|c1=c0" % (gain, args.limit),
            "-c:a", "pcm_s16le", args.output])
    lufs2, peak2 = measure(args.output)
    print("joined loudness %.1f LUFS, gain %.1f dB" % (lufs, gain))
    print("result %.1f LUFS, sample peak %.1f dBFS (check true peak with ffmpeg ebur128=peak=true)" % (lufs2, peak2))


if __name__ == "__main__":
    main()

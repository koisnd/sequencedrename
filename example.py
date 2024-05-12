#!/usr/bin/python3


import argparse
import sequencedrename

ap = argparse.ArgumentParser()
ap.add_argument("target_dir", default="")
ap.add_argument("pattern", default="")
pa = ap.parse_args()

sequencedrename.rename_dir(pa.target_dir, pa.pattern)

# Sequenced rename

* This program renames files with sequence.

## Requirements

* python3-natsort

## Installation

### On Ubuntu

```
# apt update
# apt install -qy python3-natsort
# cd /usr/local/lib/python3*/dist-packages
/usr/local/lib/python3.x/dist-packages# git clone https://github.com/koisnd/sequencedrename.git
```

## Usage

```
import argparse
import sequencedrename

ap = argparse.ArgumentParser()
ap.add_argument("target_dir", default="")
ap.add_argument("pattern", default="")
pa = ap.parse_args()

sequencedrename.rename_dir(pa.target_dir, pa.pattern)
```

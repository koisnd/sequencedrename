#!/usr/bin/python3

"""
requrements:
    apt:
        - python3-natsort
"""

import natsort
import os
import re
import sys


def is_valid(path):
    _r = re.search(r'^(/.*/)?(ep\.)([0-9]+)(\.[^/]+)(\.mp4)$', path, re.I)
    if _r:
        return _r.groups()
    return None

def rename(path=None, pat=None):
    _rp = is_valid(path)
    if not _rp:
        return []
    _rr = re.search(r'([^/]+-episode-)([0-9]*)(\.mp4)?$', pat, re.I)
    if not _rr:
        return []
    repl = _rr.group(1)
    return [path, f'{_rp[0]}{repl}{int(_rp[2]):03d}{_rp[4]}']

def rename_dir(dir_path="", pat=""):
    if not os.path.isdir(dir_path):
        return None
    targets = []
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            targets.append(os.path.join(root, name))
    for _t in natsort.natsorted(targets):
        _r = rename(_t, pat)
        if _r:
            print('Bef:', _r[0])
            print('Aft:', _r[1])
            os.rename(_r[0], _r[1])

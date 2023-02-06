import os
import sys

if sys.hexversion < 0x03080000:
    raise Exception('python 3.8 or newer required')

try:
    with open(os.path.join(os.path.dirname(__file__), '..', 'VERSION'), 'r') as f:
        __version__ = f.read()
except Exception as ex:
    __version__ = "0.2.5"
    print(f"Warning: Missing {os.path.join(os.path.dirname(__file__), '..', 'VERSION')}", ex)

from smali.smali_file import SmaliFile

SmaliFile.__version__ = __version__

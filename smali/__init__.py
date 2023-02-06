import os
import sys

if sys.hexversion < 0x03080000:
    raise Exception('python 3.8 or newer required')

__version__ = "0.2.5"

from smali.smali_file import SmaliFile

SmaliFile.__version__ = __version__

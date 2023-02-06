import os
import sys

if sys.hexversion < 0x03080000:
    raise Exception('python 3.8 or newer required')

# cwilder (12/20/2022) - Ignoring missing VERSION file exception b/c it doesn't matter. TODO: make permanent solution; a.k.a. include the VERSION file
# cwilder (12/20/2022) - Adding an empty VERSION file as an additional/alt. solution.
# Also see 'https://github.com/roytu/pysmali/blob/master/smali/__init__.py' for simple fix
#try:
#    with open(os.path.join(os.path.dirname(__file__), '..', 'VERSION'), 'r') as f:
#        __version__ = f.read()
#except Exception as ex:
#    __version__ = "0.2.5"
#    #print(f'Warning: Missing "{os.path.join(os.path.dirname(__file__), '..', 'VERSION')}"', ex)
__version__ = "0.2.5"

from smali.smali_file import SmaliFile

SmaliFile.__version__ = __version__
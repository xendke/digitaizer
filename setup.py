""" File used by cx_freeze to package python application. """
import sys
from cx_Freeze import setup, Executable

additional_mods = ['numpy.core._methods', 'numpy.lib.format']
include_files = ['src/data/']

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Digitaizer",
    version="1.0",
    description="Handwritten Digit Recognition using Neural Network.",
    author='Juan Xavier Gomez',
    author_email='xendke@gmail.com',
    url='https://www.xendke.io/',
    options={
        'build_exe': {
            'include_files': include_files,
            'includes': additional_mods,
            'path': sys.path.append('src/')
        },
        'bdist_mac': {
            'iconfile': 'icon.icns'
        }
    },
    executables=[Executable("src/main.py", base=base)]
)

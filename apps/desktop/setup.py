""" File used by cx_freeze to package python application. """
import sys
import os
from cx_Freeze import setup, Executable

additional_mods = ['numpy.core._methods', 'numpy.lib.format']
include_files = ['src/data/', 'icon.ico']

base = None
if sys.platform == "win32":
    base = "Win32GUI"
    # building on Windows: copy tcl and tk to the build
    PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
    os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
    os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
    include_files.extend([
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
         ])


setup(
    name="Digitaizer",
    version="1.0",
    description="Handwritten Digit Recognition using a Neural Network.",
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
    executables=[Executable(script="src/main.py", base=base, icon="icon.ico")]
)

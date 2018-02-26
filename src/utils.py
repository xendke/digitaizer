import os
import sys


def project_path():
    """ get full path of where the main.py is located """
    # sys.argv[0] is used instead of __file__ because of unexpected directory when under cx_freeze build
    return os.path.dirname(os.path.realpath(sys.argv[0]))+"/"

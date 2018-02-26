import os.path as path
import sys


def project_path(sub=None, file=None):
    """ get full path of where the main.py is located """
    # sys.argv[0] is used instead of __file__ because of unexpected directory when under cx_freeze build
    project_path = path.dirname(path.realpath(sys.argv[0]))
    return path.join(project_path, path.join(sub, file))

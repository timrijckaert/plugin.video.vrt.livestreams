import sys
import pydevd


def start_debugger():
    sys.path.append('/opt/Pycharm/debug-eggs/pycharm-debug.egg')
    pydevd.settrace('localhost', port=56789, stdoutToServer=True, stderrToServer=True, suspend=False)

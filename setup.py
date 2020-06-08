# -*- coding: utf-8 -*-

# A simple setup script to create an executable running wxPython. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# wxapp.py is a very simple 'Hello, world' type wxPython application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

# how to run this file:
# python setup.py build_exe

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('SeansList0.py', base=base)
]

setup(name='SeansSuperListSetup',
      version='0.9',
      description="Sean's Super List 0.9",
      executables=executables
      )

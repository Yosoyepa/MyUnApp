import os
import sys

from cx_Freeze import setup, Executable

Files = ['src']

exe = Executable(script='main.py', base='Win32GUI')

setup(  name = 'MyUn',
        version = '1.0',
        description = 'MyUn',
        author = 'Los Rodriguez',
        options = {'build_exe': {'include_files': Files}},
        executables = [exe]
)
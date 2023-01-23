import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico']

# targets
target = Executable(
    script="main_app.py",
    base="win32gui",
    icon="icon.ico"
)

# SETUP CX Freeze
setup(
    name="Reporting_Tool",
    version="1.0",
    description="Reporting Application By Xylem.",
    author="Akash Taralkar",
    options={'build_exe': {'include_files': files}},
    executables=[target]

)

from setuptools import setup

APP_NAME = 'X&O'
APP = ['main.py']
DATA_FILES = []
OPTIONS = {
 'iconfile':'xoIcon.icns',
 'argv_emulation': True,
 'packages': ['certifi'],
 'plist': {
     'CFBundleName': 'X&O',
     'CFBundleVersion': '1A stable ',
     'NSHumanReadableCopyright': '© E. Kiselev 2021',

 }
}

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
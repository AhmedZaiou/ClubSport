from setuptools import setup

APP = ['main.py']  # Replace 'main.py' with your script name
DATA_FILES = []    # Include any additional data files your app needs
OPTIONS = {
    'codesign_identity': None,
    'argv_emulation': True,  # Enable command-line arguments in the app
    'packages': ["PyQt5", "pandas","matplotlib","openpyxl"],          # Include necessary packages
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
#python exe.py py2app  
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

hiddenimports = collect_submodules('PySide6.QtTest')
datas = collect_data_files('PySide6')
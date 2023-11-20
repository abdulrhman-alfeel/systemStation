from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('usb')

hiddenimports = ['usb.backend.libusb10', 'usb.backend.libusb01']
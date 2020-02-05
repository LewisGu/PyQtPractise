import baidudisk_tool
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mainWindow = baidudisk_tool.BaiduDiskToolWidget()
    mainWindow.show()
    sys.exit(app.exec_())
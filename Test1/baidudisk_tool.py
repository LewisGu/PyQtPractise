import baidudisktool_ui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QGuiApplication, QClipboard, QDesktopServices
from PyQt5.QtCore import QUrl


class BaiduDiskToolWidget(QWidget):
    def __init__(self):
        super(BaiduDiskToolWidget, self).__init__()
        self.mywidgetui = baidudisktool_ui.Ui_MainWindow()
        self.mywidgetui.setupUi(self)
        self.mywidgetui.pushButtonBaiduOpen.clicked.connect(self.__slotOpenUrl)  # 信号与槽连接
        self.mywidgetui.pushButtonBaiduCopy.clicked.connect(self.__slotCopyUrl)  # 信号与槽连接

        self.board = QGuiApplication.clipboard()

    def __slotOpenUrl(self):
        tempText = self.mywidgetui.labelBaidu.text() + self.mywidgetui.lineEditBaidu.text()
        myurl = QUrl(tempText)
        QDesktopServices.openUrl(myurl)

    def __slotCopyUrl(self):
        tempText = self.mywidgetui.labelBaidu.text() + self.mywidgetui.lineEditBaidu.text()
        self.board.setText(tempText)
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from handn import *

class HanyuForm(QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None):
        super(HanyuForm,self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    hanyu = HanyuForm()
    hanyu.show()
    sys.exit(app.exec_())
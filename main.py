import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication , QFileDialog
from ss import Ui_MainWindow
import pyautogui as p
import datetime

class myApp(QtWidgets.QMainWindow,QDialog):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_ss.clicked.connect(self.ssScreen)
        self.ui.action_path.triggered.connect(self.browsefiles)
        self.pathArea=""
        self.name=1

    def browsefiles (self):
        #Kayıt yeri seçimi amaçlı bu kod bloğu... tekrar bakılacak...
        # options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        # fileName, _ = QFileDialog.getSaveFileName(self,"SAVE AREA...","","", options=options)
        # if fileName:
        #     print(fileName)
            pass

    def ssScreen (self):
        ss=p.screenshot()
        an = datetime.datetime.now()
        name=str(an.hour)+str(an.minute)+str(an.microsecond)
        ss.save("C:/Users/ASUS/Desktop/{}.png".format(name))


def app():
    app = QtWidgets.QApplication(sys.argv)
       
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(myApp())
    
    win = myApp()
    win.show()
    sys.exit(app.exec_())
    
app()


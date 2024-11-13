from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore    import QFile, Qt, QCoreApplication
from PySide6.QtWidgets import QApplication, QPushButton
import sys
import os

if __name__ == "__main__":

    def btn0_act(self):
        QCoreApplication.instance().quit()
    def btn1_act(self):
        ui.btn2.text = ""  
    def btn2_act(self):
        ui.btn2.text = ""


    
    def btnA_act(self):
        os.system("start ../Asset/A1.reg") 
    def btnB_act(self):
        print("q") 
    def btnC_act(self):
        print("q") 
    def btnD_act(self):
        print("q") 



    app = QApplication(sys.argv)
    loader = QUiLoader()
    file = QFile("../UI/Base7,8,10.ui")
    file.open(QFile.ReadOnly)
    ui = loader.load(file)
    file.close()
    ui.setWindowFlags(
        Qt.WindowType.FramelessWindowHint)
        
    ui.show()

    ui.btn0.clicked.connect(btn0_act)
    ui.btn1.clicked.connect(btn1_act)
    ui.btn2.clicked.connect(btn2_act)

    ui.btnA.clicked.connect(btnA_act)
    ui.btnB.clicked.connect(btnB_act)
    ui.btnC.clicked.connect(btnC_act)
    ui.btnD.clicked.connect(btnD_act)
    
    sys.exit(app.exec_())
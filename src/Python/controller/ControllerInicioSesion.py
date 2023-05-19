import sys
from Python.view.xyz import Ui_Window_Inicio 
from PyQt5 import QtCore, QtGui, QtWidgets

def iniciarVista():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_Window_Inicio()
    ui.setupUi(window)    
    

    ui.set_image_opacity(0.44)
    window.show()
    sys.exit(app.exec_())
    
iniciarVista()
import sys
from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic

#import de model

from Python.model.MiembroGrupo import MiembroGrupo

class controllerChat(QMainWindow):
    def __init__(self):
#        self.Inte = MiembroGrupo()
        QMainWindow.__init__(self)
        uic.loadUi('src/resources/interface/Ventana_Chat.ui', self)


#    def set_image_opacity(self, value):
#        graphics_effect = QtWidgets.QGraphicsOpacityEffect(self.label_fondo)
#        graphics_effect.setOpacity(value)
#        self.label_fondo.setGraphicsEffect(graphics_effect)

#    def AjustesAdmin(self):
#        if MiembroGrupo.RevAdmnin == False:


    
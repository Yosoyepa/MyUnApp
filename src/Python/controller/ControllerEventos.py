import sys
import re

from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets, uic

from resources.QRC import images

from Python.controller.ControllerMenu import selectorMenu

from Python.model.CRUD import CRUD
from Python.model.Evento import event, controllerCalendar


class controllerEventos(QMainWindow):
    def __init__(self):
        super(controllerEventos, self).__init__()

        QMainWindow.__init__(self)
        
        self.cambioEvento1()
        self.show()
        
        
        self.menu = selectorMenu()
        self.logicaEvento1()

    def logicaEvento1(self):
        self.cambioEvento1()
        
        calendario = controllerCalendar()
        calendario.crearCalendar()
        id = calendario.getId()
        eventoCalendario = event(id)
        data = eventoCalendario.getEvent()

        if data == None:
            pass
        else:
            self.labelTitulo.setText(data[1])
            self.labelDesc.setText(data[2])
            temp = data[1].split()
            grupo = ''
            for i in range(len(temp)):
                if i > 1:
                    grupo += temp[i] + ' '
            self.labelGrupoMutable.setText(grupo)
            fecha_hora = re.split("[A-Z]+", data[0])
            self.labelFechaMutable.setText(fecha_hora[0])
            self.labelHoraMutable.setText(fecha_hora[1])
        
        self.pushCalendario.clicked.connect(self.logicaEvento2)


    def logicaEvento2(self):
        self.cambioEvento2()





    
        


    def cambioEvento2(self):
        uic.loadUi('src/resources/interface/Ventana_Eventos_2.ui', self)
        self.show()

    def cambioEvento1(self): 
        uic.loadUi('src/resources/interface/Ventana_Eventos_1.ui', self)
        self.show()
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    controladorEventos = controllerEventos()
        
    app.exec_()






    
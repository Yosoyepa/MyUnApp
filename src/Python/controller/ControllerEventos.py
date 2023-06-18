import sys
import re

from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets, uic

from resources.QRC import images

#from Python.controller.ControllerMenu import selectorMenu

from Python.model import CRUD
from Python.model.Evento import event, controllerCalendar
from Python.model.Usuario import Usuario


class controllerEventos(QMainWindow):
    def __init__(self):
        super(controllerEventos, self).__init__()
        QMainWindow.__init__(self)              


    def setUsuario(self, usuario: Usuario):
        self.usuario = usuario


    def logicaEvento1(self):
        self.cambioEvento1()
        
        calendario = controllerCalendar()
        calendario.crearCalendar()
        self.id = calendario.getId()
        self.eventoCalendario = event(self.id)
        data = self.eventoCalendario.getEvent()
        length = self.eventoCalendario.len_events_list()
        index = 0
        print(length)

        if data == None:
            CRUD.mostrarCajaDeMensaje('No se encontro eventos futuros', 'Agrega o crea un nuevo evento', QtWidgets.QMessageBox.Warning)
            #QtWidgets.QMessageBox.Information
        else:
            self.maxLabel.setText(str(length))
            self.labelTitulo.setText(data[0][1])
            self.labelDesc.setText(data[0][2])
            temp = data[0][1].split()
            grupo = ''
            for i in range(len(temp)):
                if i > 1:
                    grupo += temp[i] + ' '
            self.labelGrupoMutable.setText(grupo)
            fecha_hora = re.split("[A-Z]+", data[0][0])
            self.labelFechaMutable.setText(fecha_hora[0])
            self.labelHoraMutable.setText(fecha_hora[1])
        
        self.pushCalendario.clicked.connect(self.logicaEvento2)


    def logicaEvento2(self):
        self.cambioEvento2()
        grupos = CRUD.obtener_nombres_grupo(self.usuario.correo)

        for grupo in grupos:#type: ignore
            self.boxGrupos.addItem(grupo[0])
        self.grupo = self.boxGrupos.currentText()
        self.calendarWidget.selectionChanged.connect(self.agarrar_fecha)

        self.pushListo.clicked.connect(self.enviarEvento)
        self.eventosButton.clicked.connect(self.logicaEvento1)

    def agarrar_fecha(self):
        dateSelected = self.calendarWidget.selectedDate()

        self.labelFecha_Mutable.setText(str(dateSelected.toPyDate()))
        self.fecha_1 = str(dateSelected.toPyDate())


    def enviarEvento(self):
        
        self.agarrar_fecha()
        self.desc = self.textDesc.toPlainText()
        self.hora = self.spinHora.value()
        self.minutos = self.spinMinutos.value()

        

        self.fecha = (self.fecha_1.split('-'))
        for i in range(len(self.fecha)):
            self.fecha[i] = int(self.fecha[i]) #type: ignore

        self.fecha += [self.hora] + [self.minutos]

        try:
            self.eventoCalendario.crearEvent(self.usuario.correo, self.grupo, self.desc, [], self.fecha)
            CRUD.mostrarCajaDeMensaje('Se ha creado tu evento', 'Revisa tu google calendar', QtWidgets.QMessageBox.Information)
        except:
            print('Hubo un error, revisa tu conexion a internet')


    def cambioEvento2(self):
        uic.loadUi('src/resources/interface/Ventana_Eventos_2.ui', self)
        self.show()

    def cambioEvento1(self): 
        uic.loadUi('src/resources/interface/Ventana_Eventos_1.ui', self)
        self.show()
        







    
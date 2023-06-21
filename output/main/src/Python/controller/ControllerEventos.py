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
        self.index = 0         


    def setUsuario(self, usuario: Usuario):
        self.usuario = usuario

    
    def logicaEvento1(self):
        self.cambioEvento1()
        
        calendario = controllerCalendar()
        calendario.crearCalendar()
        self.id = calendario.getId()
        self.eventoCalendario = event(self.id)
        self.data = self.eventoCalendario.getEvent()
        self.length = self.eventoCalendario.len_events_list()
        self.maxLabel.setText(str(self.length))
        


        self.mostrarEvento(self.data, self.index)

        self.leftEvent.clicked.connect(self.res_1)
        self.rightEvent.clicked.connect(self.sum_1)
        
        self.pushCalendario.clicked.connect(self.logicaEvento2)

    

    def mostrarEvento(self, data, index):
        if data == None:
            CRUD.mostrarCajaDeMensaje('No se encontro eventos futuros', 'Agrega o crea un nuevo evento', QtWidgets.QMessageBox.Warning)
            #QtWidgets.QMessageBox.Information
        else:
            
            self.labelTitulo.setText(data[index][1])
            self.labelDesc.setText(data[index][2])
            temp = data[0][1].split()
            grupo = ''
            for i in range(len(temp)):
                if i > 1:
                    grupo += temp[i] + ' '
            self.labelGrupoMutable.setText(grupo)
            fecha_hora = re.split("[A-Z]+", data[index][0])
            temp_0 = fecha_hora[0]
            temp_0 = temp_0.split('-')
            temp_0[2] = str(int(temp_0[2])-1)
            fecha_hora[0] = temp_0[0] + '-' + temp_0[1] + '-' + temp_0[2]
            self.labelFechaMutable.setText(fecha_hora[0])
            temp_1 = fecha_hora[1]
            temp_1 = temp_1.split(':')
            temp_int = int(temp_1[0]) - 5
            if temp_int < 0:
                temp_int = 24 + temp_int
            temp_1[0] = str(temp_int)
            fecha_hora[1] = temp_1[0] + ':' + temp_1[1] + ':' + temp_1[2]
            self.labelHoraMutable.setText(fecha_hora[1])
            
        
        self.pushCalendario.clicked.connect(self.logicaEvento2)


    def logicaEvento2(self):
        self.cambioEvento2()
        grupos = CRUD.obtener_nombres_grupo(self.usuario.correo)

        for grupo in grupos:#type: ignore
            self.boxGrupos.addItem(grupo[0])
        self.calendarWidget.selectionChanged.connect(self.agarrar_fecha)

        self.pushListo.clicked.connect(self.enviarEvento)
        self.eventosButton.clicked.connect(self.logicaEvento1)

    def sum_1(self):

        if self.index <= self.length-2:
            self.index += 1
            self.mostrarEvento(self.data, self.index)
            self.currLabel.setText(str(self.index+1))
            
        else:
            return
        
    def res_1(self):
        

        if self.index >= 1:
            self.index -= 1
            self.mostrarEvento(self.data, self.index)
            self.currLabel.setText(str(self.index+1))

        else: 
            return


    def agarrar_fecha(self):
        dateSelected = self.calendarWidget.selectedDate()

        self.labelFecha_Mutable.setText(str(dateSelected.toPyDate()))
        self.fecha_1 = str(dateSelected.toPyDate())


    def enviarEvento(self):
        
        self.agarrar_fecha()
        self.desc = self.textDesc.toPlainText()
        self.hora = self.spinHora.value()
        self.minutos = self.spinMinutos.value()
        self.grupo_sel = self.boxGrupos.currentText()


        self.fecha = (self.fecha_1.split('-'))
        for i in range(len(self.fecha)):
            self.fecha[i] = int(self.fecha[i]) #type: ignore

        temp_fecha = self.fecha
        self.fecha += [self.hora] + [self.minutos]

        if self.grupo_sel != None and temp_fecha != None and self.hora != None and self.minutos != None:
            self.eventoCalendario.crearEvent(self.usuario.correo, self.grupo_sel, self.desc, [], self.fecha) 
            #hay dos fechas porque una esta dividida y la otra no respectivamente
            CRUD.mostrarCajaDeMensaje('Se ha creado tu evento', 'Revisa tu google calendar', QtWidgets.QMessageBox.Information)
        else: 
            CRUD.mostrarCajaDeMensaje('Campos faltantes', 'Por favor revisa que tus campos importantes no este vacios', QtWidgets.QMessageBox.warning)


    def cambioEvento2(self):
        uic.loadUi('src/resources/interface/Ventana_Eventos_2.ui', self)
        self.show()

    def cambioEvento1(self): 
        uic.loadUi('src/resources/interface/Ventana_Eventos_1.ui', self)
        self.show()
        







    
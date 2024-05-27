#Para la creacion de un sistema de DDBB 
#Primero diseñar la DDBB y la interfaz

from tkinter import *
from tkinter import ttk #Theme TKinter = sirve para widgets mas avanzados
from vistas.navegador import *
from vistas.frame_carrera import *
from vistas.frame_materia import *
from vistas.frame_alumno import *
from vistas.frame_docente import *
from conexion_DDBB.consultas import *


if __name__ == '__main__':
    
    ventana = Tk()
    
    app = Aplicacion(ventana) #Aplicacion importar desde 'navegador.py'
    
    ventana.mainloop()
    
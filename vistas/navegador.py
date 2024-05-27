from tkinter import *
from tkinter import ttk
from vistas.frame_carrera import *
from vistas.frame_materia import *
from vistas.frame_alumno import *
from vistas.frame_docente import *
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

class Aplicacion(ttk.Frame): #Se define una nueva clase 'Aplicacion'
                             #que hereda caracteristicas de FRAME
    def __init__(self, ventana): #Crea una instancia de la clase
        
        super().__init__(ventana) #Devolver un objeto especial
                                  #el ccual permite acceder a
                                  #metodos y atributos del objeto
                                  
        self.ventana_p = ventana  #Se asigna la venta principal de
                                  #la aplicacion (ventana) a un
                                  #atributo de la instancia de la
                                  #clase (self.ventana)
                                  
        self.ventana_p.title('SISTEMA UNIVERSITARIO')
        self.ventana_p.iconbitmap('img/tecba.ico') #img es la carpeta que contiene el archivo 'tecba.ico'
        self.ventana_p.config(bg = 'green')
        
        self.navegador = ttk.Notebook(self)  #Se crea un widget tipo noteboook,
                                            #Es un contenedor organizado por pestañas
                                            
        self.p_inicio = Label(self.navegador , text = 'Pagina de Inicio' , bg = '#F1A053')
        self.navegador.add(self.p_inicio, text= 'INICIO')
        
        self.p_carrera = VistaCarrera(self.navegador)
        self.navegador.add(self.p_carrera, text= 'CARRERAS')
        
        self.p_materia = VistaMateria(self.navegador)
        self.navegador.add(self.p_materia, text= 'MATERIAS')
        
        self.p_docente = VistaDocente(self.navegador)
        self.navegador.add(self.p_docente, text= 'DOCENTES')
        
        self.p_alumno = VistaAlumno(self.navegador)
        self.navegador.add(self.p_alumno, text= 'ALUMNOS')
        
        self.navegador.pack()
        self.pack()
                                       
        
        
        
        
        
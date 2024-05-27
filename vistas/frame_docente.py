from tkinter import *
from tkinter import ttk

class VistaDocente(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        # Editar Campo de Textos 
        def nuevo():
            self.entry_nombre.config(state = "normal")
            self.entry_celular.config(state = "normal")
            self.entry_direccion.config(state = "normal")

        
        #Label de titulo de registrar
        self.label_titulo_registrar = Label(self, text = 'Registrar Nuevo Docente')
        self.label_titulo_registrar.grid(row=0, column=0, columnspan=2 , padx=10, pady=10)
        
        #Label y campo de nombre
        self.label_nombre = Label(self, text = 'Nombre de Docente: ')
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10) 
        self.entry_nombre = Entry(self, state= 'readonly')
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)       

        
        #Label y campo de celular
        self.label_celular = Label(self, text = 'Celular:')
        self.label_celular.grid(row = 2, column=0, padx=10, pady=10)
        self.entry_celular = Entry(self , state= 'readonly')
        self.entry_celular.grid(row=2, column=1 , padx=10, pady=10)
        
        
        #Label y campo de direcion
        self.label_direccion = Label(self, text = 'Direccion:')
        self.label_direccion.grid(row=3, column=0, padx=10, pady=10)
        self.entry_direccion = Entry(self, state= 'readonly')
        self.entry_direccion.grid(row=3 , column=1 , padx=10, pady=10)
        
        #Boton Nuevo
        self.btn_nuevo = Button(self, text = 'REGISTRAR NUEVO PROFESOR', command= nuevo)
        self.btn_nuevo.grid(row=4, column=0,pady = 10, padx = 10)
        
        #Boton Guardar
        self.btn_guardar = Button(self, text = 'GUARDAR')
        self.btn_guardar.grid(row=4, column=1,pady = 10, padx = 10)
        
        #Label titulo de listas
        self.label_titulo_listar = Label(self, text= "Lista de Profesores  ")
        self.label_titulo_listar.grid(row = 5, column = 0,columnspan=4, pady = 10, padx = 10)
        
        #Crear Tablas
        self.tabla = ttk.Treeview(self, columns=('','',''))
        self.tabla.grid(row=6, column=0, columnspan=4 , pady = 10, padx = 10)
        self.tabla.heading('#0', text = "CODIGO DE PROFESOR")
        self.tabla.heading('#1', text = "NOMBRE DE PROFESOR")
        self.tabla.heading('#2', text = "TELEFONO DE PROFESOR")
        self.tabla.heading('#3', text = "DIRECCION DE PROFESOR")
        
        #Btn Editar
        self.boton_editar = Button(self, text = "EDITAR PROFESOR")
        self.boton_editar.grid(row = 7, column = 0, columnspan=4, pady = 10, padx = 10)

        #Boton Eliminar
        self.boton_eliminar = Button(self, text = "ELIMINAR PROFESOR")
        self.boton_eliminar.grid(row = 8, column = 0,columnspan=4, pady = 10, padx = 10 )
        
        
        
        
        
        
        
        
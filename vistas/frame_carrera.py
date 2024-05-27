from tkinter import *
from tkinter import ttk
from conexion_DDBB.consultas import *

class VistaCarrera(ttk.Frame):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs) # *arg y **kwargs se utilizan para que el
                                         #constructir pueda acceder a
                                         # cualquier argumento sin importar su poscion
        
        def nuevo(): #Funcion para cambiar los ENTRY  a estado normal
            self.entry_nombre.config(state= 'normal')
            self.entry_duracion.config(state='normal')
            #self.entry_nombre.delete(0, END)
            #self.entry_duracion.delete(0, END)

        #funcion para agregar una nueva carrera

        def agregar_datos():
            query = 'INSERT INTO carrera VALUES (NULL, ?, ?)'
            parametros = (self.entry_nombre.get(), self.entry_duracion.get())

            conexion = conectar_db()
            conexion.ejecutar_db(query, parametros)

            #limpiar los campos de texto
            self.entry_nombre.delete(0, END)
            self.entry_duracion.delete(0, END)

            #volver a listar los datos
            lista_datos()

        def eliminar_datos():
            codigo = self.tabla.item(self.tabla.selection())['text']
            query = 'DELETE FROM carrera WHERE codigo_c = ?'
            conexion = conectar_db()
            conexion.ejecutar_db(query, (codigo,))

            #volver a listar los datos
            lista_datos()

                
        
        self.label_titulo = Label(self, text = 'REGISTAR NUEVA CARRERA').grid(row=0, column=0, columnspan= 3, padx= 10, pady=10)
        
        #Campo de texto Nombre de la carrera
        Label(self, text= 'Nombre de la carrera: ').grid(row=1, column=0,  padx= 10, pady=10)
        self.entry_nombre = Entry(self , state= 'readonly')
        self.entry_nombre.grid(row=1 , column=1 , padx= 10, pady=10)
        
        #Campo de texto de DURACION de carrera
        Label(self, text= 'Duracion de la carrera: ').grid(row=2, column=0 , padx= 10, pady=10)
        self.entry_duracion = Entry(self , state= 'readonly')
        self.entry_duracion.grid(row=2 , column=1,  padx= 10, pady=10)
        
        #Btn Nuevo
        Button(self, text = 'NUEVO',command = nuevo).grid(row= 3, column=0,  padx= 10, pady=10)
        
        #Btn Guardar
        Button(self, text= 'GUARDAR', command= agregar_datos).grid(row=3, column=1,  padx= 10, pady=10)
        
        #Crear Tablas
        self.tabla = ttk.Treeview(self, columns= ('',''))
        self.tabla.grid(row=4, column=0 ,   columnspan=3)
        self.tabla.heading('#0', text = 'CODIGO DE CARRERA')
        self.tabla.heading('#1', text = 'NOMBRE DE CARRERA')
        self.tabla.heading('#2', text = 'DURACION DE CARRERA')
        
        #Boton editar
        self.boton_editar = Button(self, text ='EDITAR CARRERA')
        self.boton_editar.grid(row=6, column=0,pady = 10, padx = 10)
        
        #Boton Eliminar         
        self.boton_eliminar = Button(self, text = 'ELIMINAR CARRERA', command = eliminar_datos)
        self.boton_eliminar.grid(row=6, column=1,pady = 10, padx = 10)

        def lista_datos():
            #eliminar datos de la tabla
            recorrer_tabla = self.tabla.get_children()
            for elementos in recorrer_tabla:
                self.tabla.delete(elementos)

            #ejecutar la instruccion
            query = 'SELECT * FROM carrera'

            #crear una instancia de la clase conectar_db para ejecutar la consulta

            conexion = conectar_db()

            #ejecutar la consulta
            datos = conexion.ejecutar_db(query)

            for carrera in datos:
                self.tabla.insert('', 0, text = carrera[0], values = (carrera[1], carrera[2]))


        lista_datos()

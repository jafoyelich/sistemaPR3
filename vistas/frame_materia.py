from tkinter import *
from tkinter import ttk
from conexion_DDBB.consultas import *

class VistaMateria(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        # Editar Campo de Textos 
        def nuevo():
            self.entry_nombre.config(state = "normal")
            self.entry_creditos.config(state = "normal")

        def agregar_datos():
            query = 'INSERT INTO materia VALUES (NULL, ?, ?)'
            parametros = (self.entry_nombre.get(), self.entry_creditos.get())
            conexion = conectar_db()
            conexion.ejecutar_db(query, parametros)
            self.entry_nombre.delete(0, END)
            self.entry_creditos.delete(0, END)
            lista_datos()

        def eliminar_datos():
            codigo = self.tabla.item(self.tabla.selection())['text']
            query = 'DELETE FROM materia WHERE codigo_m = ?'
            conexion = conectar_db()
            conexion.ejecutar_db(query, (codigo,))
            lista_datos()

    
    
        #Label de titulo
        self.label_titulo = Label(self, text = 'Registrar nueva Materia')
        self.label_titulo.grid(row = 0, column=0, columnspan=2,pady = 10, padx = 10)
        
        #Label y campo de nombre
        self.label_nombre = Label(self, text= 'Nombre de la carrerar: ')
        self.label_nombre.grid(row= 1, column=0,pady = 10, padx = 10)
        self.entry_nombre = Entry(self, state= 'readonly') 
        self.entry_nombre.grid(row = 1 , column= 1,pady = 10, padx = 10)
        
        #Label y campo de Creditos
        self.label_creditos = Label(self, text = 'Creditos de Materia:')
        self.label_creditos.grid(row = 2 , column=0,pady = 10, padx = 10)
        self.entry_creditos = Entry(self , state= 'readonly')
        self.entry_creditos.grid(row=2,column=1,pady = 10, padx = 10)
        
        #Boton Nuevo
        self.boton_nuevo = Button(self, text= 'REGISTRAR NUEVA MATERIA', command= nuevo)
        self.boton_nuevo.grid(row =3 , column=0,pady = 10, padx = 10)
        
        #Boton Guardar
        self.boton_guardar = Button(self, text= 'GUARDAR' , command = agregar_datos)
        self.boton_guardar.grid(row =3 , column=1,pady = 10, padx = 10)
        
        #Label titulo de listas
        self.label_t = Label(self, text= 'Listas de materias')
        self.grid(row=4, column=0, columnspan=2,pady = 10, padx = 10)
        
        #Crear Tabla
        self.tabla = ttk.Treeview(self, columns= ('',''))
        self.tabla.grid(row=5, column=0,columnspan=3,pady = 10, padx = 10)
        self.tabla.heading('#0', text = 'CODIGO DE LA MATERIA')
        self.tabla.heading('#1', text = 'NOMBRE DE LA MATERIA')
        self.tabla.heading('#2', text = 'DURACION DE MATERIA')

        #Boton editar
        self.boton_editar = Button(self, text ='Editar Materia')
        self.boton_editar.grid(row=6, column=0,pady = 10, padx = 10)
        
        #Boton Eliminar         
        self.boton_eliminar = Button(self, text = 'ELIMINAR MATERIA' , command = eliminar_datos)
        self.boton_eliminar.grid(row=6, column=1,pady = 10, padx = 10)

        def lista_datos():
            #eliminar datos de la tabla
            recorrer_tabla = self.tabla.get_children()
            for elementos in recorrer_tabla:
                self.tabla.delete(elementos)
            #realizar la consulta
            query = 'SELECT * FROM materia'
            conexion = conectar_db()
            datos = conexion.ejecutar_db(query)
            #recorrer los datos
            for fila in datos:
                self.tabla.insert('',0,text = fila[0], values = (fila[1],fila[2]))

        lista_datos()
        
        
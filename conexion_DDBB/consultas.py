import sqlite3

#definir una clase llamada conectar_DB

class conectar_db():
    #definir un atributo de clase que contenga el nombre de la ruta hacia la DDBB
    nombre_db = 'DDBB/base_de_datos.db'
    #definir un metodo que ejecute una consulta SQL de la DDBB

    def ejecutar_db(self, query, parametros = ()):
        #conectar a la DDBB
        with sqlite3.connect(self.nombre_db) as conexion:
            #crear un cursor
            cursor = conexion.cursor()
            #ejecutar la consulta
            datos = cursor.execute(query, parametros)
            #guardar los cambios
            conexion.commit()
            #retornar el cursor

        return cursor
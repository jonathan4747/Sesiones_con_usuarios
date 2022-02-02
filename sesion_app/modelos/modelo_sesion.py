from sesion_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{3}$')

class Usuario:
    def __init__(self,nombre,apellido,email,password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        
    @classmethod
    def agregaUsuario( cls, nuevoUsuario ):
        query = "INSERT INTO usuario(nombre, apellido, email, password) VALUES(%(nombre)s, %(apellido)s, %(email)s, %(password)s);"
        resultado = connectToMySQL( "usuario_sesion" ).query_db( query, nuevoUsuario )
        return 
    #AND password = %(password)s
    @classmethod
    def verificaUsuario( cls, usuario ):
        query = "SELECT * FROM usuario WHERE email = %(email)s;"
        resultado = connectToMySQL( "usuario_sesion" ).query_db( query, usuario )
        print("esto es resultado",resultado)
        if len( resultado ) > 0:
            usuarioResultado = Usuario( resultado[0]["nombre"], resultado[0]["apellido"], resultado[0]["email"], resultado[0]["password"] )
            return usuarioResultado
        else:
            return None
        
    @staticmethod
    def Validacion(nuevo):
        valida= True
        if len(nuevo['nombre']) <= 2:
            valida = False
            flash("El nombre no debe tener menos que 2 caracteres","Registro")
        if len(nuevo['apellido']) <= 2:
            valida= False
            flash("El nombre no debe tener menos que 2 caracteres","Registro")
        if not EMAIL_REGEX.match(nuevo['email']):
            flash("correo invalido,probar otra vez!!!","Registro")
            valida=False
        return valida

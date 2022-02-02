from sesion_app.modelos.modelo_sesion import Usuario
from flask import render_template, request, redirect, session,flash
from flask_bcrypt import Bcrypt  
from sesion_app import app

bcrypt = Bcrypt( app )

@app.route( '/', methods=['GET'] )
def despliegaPagina():
    return render_template( "index.html" )

@app.route( '/dashboard', methods=["GET"] )
def despliegaSesion():
    if 'nombre' in session:
        return render_template( "dashboard.html" )
    else:
        return redirect( '/' )

@app.route( '/registroUsuario', methods=["POST"] )
def registrarUsuario():
    nuevoUsuario = {
        "nombre" : request.form["nombre"],
        "apellido" : request.form["apellido"],
        "email" : request.form["email"],
        "password" :  bcrypt.generate_password_hash( request.form["password"] )
    }
    validar=Usuario.Validacion(nuevoUsuario)
    if not validar:
        return redirect('/')
    else:
        session["nombre"] = request.form["nombre"]
        session["apellido"] = request.form["apellido"]
        resultado = Usuario.agregaUsuario(nuevoUsuario)
        return redirect( '/dashboard' )
        
    
@app.route( '/login', methods=["POST"] )
def loginUsuario():
    loginUsuario = request.form["loginUsuario"]
    passwordUsuario = request.form["passwordUsuario"]
    usuario = {
        "email" : loginUsuario,
    }
    resultado = Usuario.verificaUsuario(usuario)
    if resultado == None:
        flash( "El correo esta escrito incorrectamente", "login" )
        return redirect( '/' )
    else:
        if not bcrypt.check_password_hash(resultado.password,passwordUsuario):
            flash("password incorrecto","login")
            return redirect ('/')
        else:
            session["nombre"] = resultado.nombre
            session["apellido"] = resultado.apellido
            return redirect( '/dashboard' )

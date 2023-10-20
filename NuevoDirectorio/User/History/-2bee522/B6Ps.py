from flask import Flask, url_for,render_template,request
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
import logging

app = Flask(__name__)
logging.basicConfig(filename='error.log', level=logging.DEBUG)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login',methods=["GET","POST"])
def login():
    if(request.method=="POST"):
        redirect('/')
    else:
        return render_template('login.html')
    
@app.route('/juego',methods=["POST"])
def agregarJuego():
    try:
        token=request.headers.get("token")
        app.logger.debug(f"Token: {token}")
        Info = request.get_json()
        nombre=Info["nombre"]
        precio=Info["precio"]
        return f"nombre: {nombre}, precio: {precio}, token: {token}"
    except:
        abort(404)

@app.route('/juego/<int:numero>')
def obtenerJuego(numero):
    return f"numero: {numero}"

@app.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template("error.html", error=error), 404


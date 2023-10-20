from flask import Blueprint,request,redirect,render_template,url_for
from models import Persona
from forms import PersonaForm
from app import db

appersona =  Blueprint('appersona',__name__, template_folder="templates")

@appersona.route('/')
@appersona.route('/index')
def inicio():
    personas = Persona.query.all()
    return render_template('index.html', personas = personas)
@appersona.route('agregar',methods=["GET","POST"])
def agregar():
    persona = Persona()
    personaForm = PersonaForm(obj=persona)
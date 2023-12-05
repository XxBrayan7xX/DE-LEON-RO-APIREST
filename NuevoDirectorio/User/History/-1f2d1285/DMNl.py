from flask import Blueprint,request,jsonify,render_template,redirect
from sqlalchemy import exc 
from models import User
from app import db,bcrypt
from routes.user import appuser
from auth import tokenCheck

appuser=Blueprint('appuser',__name__,template_folder="templates")
@appuser.route("/auth/registro",methods=["POST"])
def registro():
    user=request.get_json()
    userExist=User.query.filter_by(email=user['email']).first()
    if not userExist:
        usuario=User(email=user['email'],password=user['password'])
        try:
            db.session.add(usuario)
            db.sessio.commit()
            mensaje="Usuario creado"
        except exc.SQLAlchemyError as e:
            mensaje="ERROR"+e
    return jsonify({"message":mensaje})

@appuser.route('/auth/login',methods=["POST"])
def login():
    user=request.get_json()
    usuario=User.query.filter_by(email=user['email']).first()
    searchUser=User.query.filter_by(email=user['email']).first()
    if searchUser:
        validation =  bcrypt.check_password_hash(searchUser.password)

@appuser.route('/usuarios',methods=['GET'])
@tokenCheck
def getUsers(usuario):
    pass
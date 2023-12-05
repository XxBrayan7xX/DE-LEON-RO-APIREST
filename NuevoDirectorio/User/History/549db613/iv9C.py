from flask import Blueprint,request,jsonify, render_template
from sqlalchemy import exc
from models import Images
from app import tokenCheck
import base64

imagesUser =  Blueprint('imageUser',__name__,template_folder="templates")
def render_image(data):
    render_image = base64.b64encode(data).decode('ascii')
    return render_image

@imagesUser.route("/displayImage", methods=["GET"])
@tokenCheck
def search_page(usuario):
    searchImage = Images.query.filter_by(user_id=usuario['user_id']).first()
    if searchImage:
        image = searchImage.render_data
        return render_template('PerfilUsuario.html',image=image)
    else:
        return jsonify({'message':'No Image'})

@imagesUser.route('/uploadPerfil',methods=["POST"])
@tokenCheck
def upld(usuario):
    searchImage = Images.query.filter_by(user_id=usuario['user_id']).first()
    if searchImage:
        file= request.files['imputFile']
        data = file.read()
        render_file = render_image(data)
        searchImage.rendered_data = render_file
        searchImage.data = data
        db.session.commit()
        return jsonify({"message":"imagen actualizada"})
    else:
        file=request.files["inputFile"]
        data = file.read()
        render_file = render_image(data)
        newFile = Images()
        newFile.type="Perfil"
        newFile.rendered_data = render_file
        newFile.user_id = usuario['user_id']
        newFile.data = data
        db.session.add(newFile)
        db.session.commit()
        return jsonify({"message":"imagen agregada"})

        
    
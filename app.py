from flask import Flask,request,session,render_template_string,send_from_directory,send_file
from werkzeug.utils import secure_filename
from markupsafe import escape
from cryptography.fernet import Fernet
from Componentes import LibDM_2023
import os
import uuid
import json
import pathlib
import sys
app = Flask(__name__)
import Inicio
PATH_DIR = str(pathlib.Path(__file__).parent.resolve()).replace("\\","/")
@app.route('/recurso/<path:path>')
def recurso(path):
    if ".js" in path:
        return send_from_directory(PATH_DIR+'/static/', path, mimetype='application/javascript')
    elif ".css" in path:
        return send_from_directory(PATH_DIR+'/static/', path, mimetype='text/css')
    else:
        return send_from_directory(PATH_DIR+'/static/', path)
@app.route("/",methods=['GET','POST'])
def index():
    if "IDu" not in session:
        if request.method == "GET":
            return Inicio.Inicio()
        else:
            Datos = {}
            for K in request.form.keys():
                Datos[K] = escape(request.form[K]).striptags()
            return render_template_string(Inicio.Direccionar(Datos))
    else:
        if request.method == "GET":
            return render_template_string(Inicio.Inicio())
        else:
            Datos = {}
            for K in request.form.keys():
                Datos[K] = escape(request.form[K]).striptags()
            return render_template_string(Inicio.Direccionar(Datos))
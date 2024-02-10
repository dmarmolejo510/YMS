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
from ToDo import Inicio as TODO
from YMS import Inicio as YMS
from YMS.Contenedores import Contenedores as YMS_Contenedor, Contenedores_M as YMS_Contenedor_M

app.secret_key = LibDM_2023.Compartido().Dame_K()
fernet = Fernet(LibDM_2023.Compartido().Dame_K2())

PATH_DIR = str(pathlib.Path(__file__).parent.resolve()).replace("\\","/")
UPLOAD_FOLDER = PATH_DIR+'/Files/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
@app.route("/ToDo",methods=['GET','POST'])
def ToDo_root():
    if "IDu" not in session:
        return render_template_string("<script>window.location= '"+str(request.url_root)+"';</script>")
    else:
        if request.method == "GET":
            return render_template_string(TODO.Inicio())
        else:
            Datos = {}
            for K in request.form.keys():
                Datos[K] = escape(request.form[K]).striptags()
            return render_template_string(TODO.Direccionar(Datos))
@app.route("/YMS",methods=['GET','POST'])
def YMS_root():
    if "IDu" not in session:
        return render_template_string("<script>window.location= '"+str(request.url_root)+"';</script>")
    else:
        if request.method == "GET":
            return render_template_string(YMS.Inicio())
        else:
            Datos = {}
            for K in request.form.keys():
                Datos[K] = escape(request.form[K]).striptags()
            return render_template_string(YMS.Direccionar(Datos))
@app.route("/YMS/Container_Control",methods=['GET','POST'])
def YMS_Contenedores():
    if "IDu" not in session:
        return render_template_string("<script>window.location= '"+str(request.url_root)+"';</script>")
    else:
        if request.method == "GET":
            return render_template_string(YMS_Contenedor.Inicio())
        else:
            Datos = {}
            for K in request.form.keys():
                Datos[K] = escape(request.form[K]).striptags()
            return render_template_string(YMS_Contenedor.Direccionar(Datos))
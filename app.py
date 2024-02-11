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
from YMS.Salidas import Estado as YMS_Salida_Estado, Reporte as YMS_Salida_Reporte
from YMS.OSyD import Inicio as YMS_OSyD
from YMS.Reportes import Buscar as YMS_Reportes_Buscar,Diario as YMS_Reportes_Diario,Tiempo as YMS_Reportes_Tiempo, Carrier as YMS_Reportes_Carrier
from YMS.Configuracion import Destinos as YMS_Conf_Destino,Docks as YMS_Conf_Dock, Proveedores as YMS_Conf_Proveedores,Rutas as YMS_Conf_Rutas,Carrier as YMS_Conf_Carrier

app.secret_key = LibDM_2023.Compartido().Dame_K()
fernet = Fernet(LibDM_2023.Compartido().Dame_K2())

PATH_DIR = str(pathlib.Path(__file__).parent.resolve()).replace("\\","/")
UPLOAD_FOLDER = PATH_DIR+'/Files/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/recurso/<path:path>')
def recurso(path):
    if ".js" in path:
        return send_from_directory(PATH_DIR+'/static/', path, mimetype='application/javascript')
    elif ".css" in path:
        return send_from_directory(PATH_DIR+'/static/', path, mimetype='text/css')
    else:
        return send_from_directory(PATH_DIR+'/static/', path)
@app.route('/ProFiles',methods=['GET','POST'])
def ProFiles():
    if request.method == 'POST':
        try:
            if "Fun" in request.form.keys():
                if str(request.form["Fun"]) == "Eliminar":
                    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], request.form["Archivo"]))
                return str(request.form)
            else:
                response = {}
                structuredFiles = []
                File_Name = None
                if 'files[]' not in request.files:
                    response["msg"] = "No hay parte de archivo en la solicitud";
                    response["status"] = "error";
                    response["key"] = None;
                    response["file"] = File_Name;
                    return json.dumps(response),400
                files = request.files.getlist('files[]')
                errors = {}
                success = False
                for file in files:
                    if file and allowed_file(file.filename):
                        Es_Recarga = False
                        filename = secure_filename(file.filename)
                        if len(filename.split("-")) >= 4 and len(filename.split("-")[len(filename.split("-"))-1]) >= 15:
                            Es_Recarga = True
                        if Es_Recarga == False:
                            filename_F = ""
                            Arr = filename.split(".")
                            index = 0
                            for A in Arr:
                                if index == len(Arr)-1:
                                    filename_F += "_" + str(uuid.uuid4())
                                    filename_F += "."+str(A)
                                else:
                                    filename_F += str(A)
                                index += 1
                            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename_F))
                            File_Name = filename_F
                        else:
                            File_Name = filename
                        success = True
                    else:
                        errors[file.filename] = 'File type is not allowed'
                if success and errors:
                    response["msg"] = 'File(s) successfully uploaded'
                    response["status"] = "success";
                    response["key"] = str(uuid.uuid4());
                    response["file"] = File_Name;
                    return json.dumps(response),206
                if success:
                    response["msg"] = 'Files successfully uploaded'
                    response["status"] = "success";
                    response["key"] = str(uuid.uuid4());
                    response["file"] = File_Name;
                    return json.dumps(response),201
                else:
                    response["msg"] = str(errors);
                    response["status"] = "error";
                    response["key"] = None;
                    response["file"] = File_Name;
                    return json.dumps(response),400
        except:
            return str(sys.exc_info())
@app.route('/Portal_File/<path:file>',methods=['GET','POST'])
def downloadFile (file):
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = str(UPLOAD_FOLDER)+str(file)
    return send_file(path, as_attachment=True)


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
@app.route("/YMS/Container_Manager",methods=['GET','POST'])
def YMS_Contenedores_M():
    if "IDu" not in session:
        return render_template_string("<script>window.location= '"+str(request.url_root)+"';</script>")
    else:
        if request.method == "GET":
            return render_template_string(YMS_Contenedor_M.Inicio())
        else:
            Datos = {}
            for K in request.form.keys():
                Datos[K] = escape(request.form[K]).striptags()
            return render_template_string(YMS_Contenedor_M.Direccionar(Datos))
@app.route("/YMS/OutBound/Status",methods=['GET','POST'])
def YMS_Outbound_Estado():
    if "IDu" not in session:
        return render_template_string("<script>window.location= '"+str(request.url_root)+"';</script>")
    else:
        if request.method == "GET":
            return render_template_string(YMS_Salida_Estado.Inicio())
        else:
            Datos = {}
            for K in request.form.keys():
                Datos[K] = escape(request.form[K]).striptags()
            return render_template_string(YMS_Salida_Estado.Direccionar(Datos))
@app.route("/YMS/OutBound/Report",methods=['GET','POST'])
def YMS_Outbound_Reporte():
    if "IDu" not in session:
        return render_template_string("<script>window.location= '"+str(request.url_root)+"';</script>")
    else:
        if request.method == "GET":
            return render_template_string(YMS_Salida_Reporte.Inicio())
        else:
            Datos = {}
            for K in request.form.keys():
                Datos[K] = escape(request.form[K]).striptags()
            return render_template_string(YMS_Salida_Reporte.Direccionar(Datos))
@app.route("/YMS/OSyD",methods=['GET','POST'])
def YMS_OSyDs():
    if "IDu" not in session:
        return render_template_string("<script>window.location= '"+str(request.url_root)+"';</script>")
    else:
        if request.method == "GET":
            return render_template_string(YMS_OSyD.Inicio())
        else:
            Datos = {}
            for K in request.form.keys():
                Datos[K] = escape(request.form[K]).striptags()
            return render_template_string(YMS_OSyD.Direccionar(Datos))

@app.route("/YMS/Report/Container",methods=['GET','POST'])
def YMS_Reporte_Contenedor():
    if "IDu" not in session:
        return render_template_string("<script>window.location= '"+str(request.url_root)+"';</script>")
    else:
        if request.method == "GET":
            return render_template_string(YMS_Reportes_Buscar.Inicio())
        else:
            Datos = {}
            for K in request.form.keys():
                Datos[K] = escape(request.form[K]).striptags()
            return render_template_string(YMS_Reportes_Buscar.Direccionar(Datos))
@app.route("/YMS/Report/Daily",methods=['GET','POST'])
def YMS_Reporte_Daily():
    if "IDu" not in session:
        return render_template_string("<script>window.location= '"+str(request.url_root)+"';</script>")
    else:
        if request.method == "GET":
            return render_template_string(YMS_Reportes_Diario.Inicio())
        else:
            Datos = {}
            for K in request.form.keys():
                Datos[K] = escape(request.form[K]).striptags()
            return render_template_string(YMS_Reportes_Diario.Direccionar(Datos))
@app.route("/YMS/Report/Carrier",methods=['GET','POST'])
def YMS_Reporte_Carrier():
    if "IDu" not in session:
        return render_template_string("<script>window.location= '"+str(request.url_root)+"';</script>")
    else:
        if request.method == "GET":
            return render_template_string(YMS_Reportes_Carrier.Inicio())
        else:
            Datos = {}
            for K in request.form.keys():
                Datos[K] = escape(request.form[K]).striptags()
            return render_template_string(YMS_Reportes_Carrier.Direccionar(Datos))
@app.route("/YMS/Report/Aging",methods=['GET','POST'])
def YMS_Reporte_Aging():
    if "IDu" not in session:
        return render_template_string("<script>window.location= '"+str(request.url_root)+"';</script>")
    else:
        if request.method == "GET":
            return render_template_string(YMS_Reportes_Tiempo.Inicio())
        else:
            Datos = {}
            for K in request.form.keys():
                Datos[K] = escape(request.form[K]).striptags()
            return render_template_string(YMS_Reportes_Tiempo.Direccionar(Datos))

@app.route("/YMS/Conf/Suppliers",methods=['GET','POST'])
def YMS_Cof_Supplier():
    if "IDu" not in session:
        return render_template_string("<script>window.location= '"+str(request.url_root)+"';</script>")
    else:
        if request.method == "GET":
            return render_template_string(YMS_Conf_Proveedores.Inicio())
        else:
            Datos = {}
            for K in request.form.keys():
                Datos[K] = escape(request.form[K]).striptags()
            return render_template_string(YMS_Conf_Proveedores.Direccionar(Datos))
@app.route("/YMS/Conf/Routes",methods=['GET','POST'])
def YMS_Conf_Route():
    if "IDu" not in session:
        return render_template_string("<script>window.location= '"+str(request.url_root)+"';</script>")
    else:
        if request.method == "GET":
            return render_template_string(YMS_Conf_Rutas.Inicio())
        else:
            Datos = {}
            for K in request.form.keys():
                Datos[K] = escape(request.form[K]).striptags()
            return render_template_string(YMS_Conf_Rutas.Direccionar(Datos))
@app.route("/YMS/Conf/Docks",methods=['GET','POST'])
def YMS_Conf_Docks():
    if "IDu" not in session:
        return render_template_string("<script>window.location= '"+str(request.url_root)+"';</script>")
    else:
        if request.method == "GET":
            return render_template_string(YMS_Conf_Dock.Inicio())
        else:
            Datos = {}
            for K in request.form.keys():
                Datos[K] = escape(request.form[K]).striptags()
            return render_template_string(YMS_Conf_Dock.Direccionar(Datos))
@app.route("/YMS/Conf/Destination",methods=['GET','POST'])
def YMS_Conf_Destinos():
    if "IDu" not in session:
        return render_template_string("<script>window.location= '"+str(request.url_root)+"';</script>")
    else:
        if request.method == "GET":
            return render_template_string(YMS_Conf_Destino.Inicio())
        else:
            Datos = {}
            for K in request.form.keys():
                Datos[K] = escape(request.form[K]).striptags()
            return render_template_string(YMS_Conf_Destino.Direccionar(Datos))
@app.route("/YMS/Conf/Carrier",methods=['GET','POST'])
def YMS_Conf_Carriers():
    if "IDu" not in session:
        return render_template_string("<script>window.location= '"+str(request.url_root)+"';</script>")
    else:
        if request.method == "GET":
            return render_template_string(YMS_Conf_Carrier.Inicio())
        else:
            Datos = {}
            for K in request.form.keys():
                Datos[K] = escape(request.form[K]).striptags()
            return render_template_string(YMS_Conf_Carrier.Direccionar(Datos))
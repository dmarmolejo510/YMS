from flask import request,session,render_template
from cryptography.fernet import Fernet
from datetime import datetime,date,timedelta
import sys
import json
import os
from Componentes import LibDM_2023
fernet = Fernet(LibDM_2023.Compartido().Dame_K2())
BD_Nombre = LibDM_2023.Compartido().Dame_Base_Datos("YMS")
Bandera_Dock = "YMS"
def Inicio():
    DB = LibDM_2023.DataBase()
    if "K" in session.keys():
        fernet = Fernet(session["K"])
    Cur = ""
    try:
        Activo = "YMS"
        Compartido = LibDM_2023.Compartido()
        Menu = LibDM_2023.Menu().Menu(Activo,request.url_root,session["IDu"])
        Titulo = LibDM_2023.Menu().Get_Titulo(Activo)
        Contenido = ""
        Destinos = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".cdestinos where cactivo = 1")
        Patio = []
        for Destino in Destinos:
            Opciones = "<div class='text-center'><div class='btn-group' role='group' aria-label='Basic mixed styles example'>"
            Opciones += "<button class='btn btn-sm btn-warning p-0 ps-1 pe-1' onclick='Modificar(\""+str(Destino["cdestino"])+"\")'><i class='mdi mdi-pencil'></i></button>"
            Opciones += "<button class='btn btn-sm btn-danger p-0 ps-1 pe-1' onclick='Eliminar(\""+str(Destino["cdestino"])+"\")'><i class='mdi mdi-trash-can'></i></button>"
            Opciones += "</div></div>"
            Patio.append({"Codigo":str(Destino["cdestino"]),"Lista":str(Destino["ccorreos"]),"Opciones":Opciones})
        Contenido += "<div class='h2 fw-lighter mt-1 mb-1 text-center border-bottom'><i class='mdi mdi-card-bulleted'></i> Destination Master</div>"
        Contenido += """
        <div class='container'>
        <div class='row'>
            <div class='col-12'>
                <div class='text-end mb-1'> <button class='btn btn-success' onclick='Nuevo_Destino()'><i class='mdi mdi-plus'></i> New Destination</button> </div>
                <div id='Tabla_Proveedores' class='border border-dark bg-dark-subtle'></div>
                <script>
                    delete Tabla_Proveedores;
                    var Tabla_Proveedores = new Tabulator("#Tabla_Proveedores", {
                        minHeight:800,
                        layout:"fitColumns",
                        data:"""+str(Patio)+""",
                        columns:[
                            {field:"Codigo","title":"Code",widthGrow:1,headerFilter:"input"},
                            {field:"Lista","title":"Lista de distribución",headerFilter:"input",widthGrow:10},
                            {field:"Opciones","title":"Op",formatter:"html",widthGrow:1}
                        ]
                    });
                    Tabla_Proveedores.on("tableBuilt", function(){ 
                        setTimeout(() => {
                            Tabla_Proveedores.clearFilter();
                            Tabla_Proveedores.redraw();
                        }, 100);
                    });
                </script>
            </div>
        </div>
        </div>
        <script>
            function Nuevo_Destino(){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-plus'></i> New Suppliers");
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm');
                var parametros = {"Fun":'"""+str(fernet.encrypt("Nuevo_Destino".encode()).decode("utf-8"))+"""'};
                $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                    success:  function (response)
                    {
                        var Resultado = JSON.parse(response);
                        $("#Vent_1").modal("show").find(".modal-body").html(Resultado["Contenido"]);
                        $("#Vent_1").find(".modal-footer").find("button").attr('onclick',"$('#Vent_1').modal('hide'); delete table; ")
                        swal.close();
                    },
                    error: function (jqXHR, textStatus, errorThrown )
                    {
                        $("#Vent_1").modal("show").find(".modal-body").html("<i class='mdi mdi-alert'></i> "+ textStatus);
                        swal.close();
                    }
                });
            }
            function Modificar(ID){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-pencil'></i>" + ID);
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm');
                var parametros = {"Fun":'"""+str(fernet.encrypt("Modificar".encode()).decode("utf-8"))+"""',"ID":ID};
                $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                    success:  function (response)
                    {
                        var Resultado = JSON.parse(response);
                        $("#Vent_1").modal("show").find(".modal-body").html(Resultado["Contenido"]);
                        $("#Vent_1").find(".modal-footer").find("button").attr('onclick',"$('#Vent_1').modal('hide'); delete table; ")
                        swal.close();
                    },
                    error: function (jqXHR, textStatus, errorThrown )
                    {
                        $("#Vent_1").modal("show").find(".modal-body").html("<i class='mdi mdi-alert'></i> "+ textStatus);
                        swal.close();
                    }
                });
            }
            function Eliminar(ID){
                Swal.fire({
                    title: 'Are you sure delete ['+ID+']?',
                    buttonsStyling: false,showCancelButton: true,confirmButtonText: "<i class='mdi mdi-check'></i> Yes",cancelButtonText: "<i class='mdi mdi-close'></i> No",showLoaderOnConfirm: true,
                    customClass: {confirmButton: 'btn btn-success ms-1 me-1',cancelButton: 'btn btn-danger ms-1 me-1'},
                    preConfirm: () => {
                        
                        Mostrar_Ventana_Cargando(false);
                            var parametros = {"Fun":'"""+str(fernet.encrypt("Eliminar".encode()).decode("utf-8"))+"""',"ID":ID};
                            $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                                success:  function (response)
                                {
                                    var Resultado = JSON.parse(response);
                                    if(Resultado["Estado"] == 1)
                                    {
                                        $("#Vent_1").modal("hide");
                                        Mensaje(2);
                                        Llamar_Funcion(\""""+str(request.url)+"""\");
                                    }
                                    else
                                        Mensaje(0,Resultado["Contenido"]);
                                        
                                },
                                error: function (jqXHR, textStatus, errorThrown )
                                {
                                    Mensaje(0,textStatus);
                                }
                            });
                        
                    }
                })
            }
        </script>
        """
        Cur += render_template("general.html",Contenido=Contenido,Componentes=Compartido.Complementos(None),Menu=Menu,Titulo=Titulo)
    except:
        Cur += str(sys.exc_info())
    return Cur

def Nuevo_Destino(Datos):
    if "K" in session.keys():
        fernet = Fernet(session["K"])
    DB = LibDM_2023.DataBase()
    Compartido_2023 = LibDM_2023.Compartido()
    Cur = ""
    Resultado = {"Contenido":"","Estado":0}
    try:
        Formulario = {"Col":"12", "Campos": [],"Clase": "Alta_Proveedor" }
        Formulario["Campos"].append({"tipo":"texto","campo":"Codigo","titulo":"Code","Requerido":1,"min":1,"max":30,"valor":""})
        Formulario["Campos"].append({"tipo":"texto","campo":"Nombre","titulo":"Nombre","Requerido":1,"min":1,"max":150,"valor":""})
        Formulario["Campos"].append({"tipo":"multitexto","campo":"Correos","titulo":"E-mail(s) (Separador por ;)","Requerido":0,"min":0,"max":2000,"valor":""})
        Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
        Resultado["Contenido"] += """
        <hr>
        <div class='w-100 text-center'><button class='btn btn-success w-75' onclick='Nuevo_Destino_Guardar()'><i class='mdi mdi-floppy'></i> Save</button></div>
        """
        Resultado["Contenido"] += """
        <script>
            function Nuevo_Destino_Guardar(){
                var Info = Dame_Formulario(".Alta_Proveedor",true);
                if(Info != null)
                {
                    Mostrar_Ventana_Cargando(false);
                    var parametros = {"Fun":'"""+str(fernet.encrypt("Nuevo_Destino_Guardar".encode()).decode("utf-8"))+"""',"Info":JSON.stringify(Info)};
                    $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                        success:  function (response)
                        {
                            var Resultado = JSON.parse(response);
                            if(Resultado["Estado"] == 1)
                            {
                                $("#Vent_1").modal("hide");
                                Mensaje(2);
                                Llamar_Funcion(\""""+str(request.url)+"""\");
                            }
                            else
                                Mensaje(0,Resultado["Contenido"]);
                                
                        },
                        error: function (jqXHR, textStatus, errorThrown )
                        {
                            Mensaje(0,textStatus);
                        }
                    });
                }
            }
        </script>
        """
    except:
         Resultado["Contenido"] = str(sys.exc_info())
    Cur += json.dumps(Resultado)
    return Cur
def Nuevo_Destino_Guardar(Datos):
    DB = LibDM_2023.DataBase()
    Compartido_2023 = LibDM_2023.Compartido()
    Cur = ""
    Resultado = {"Contenido":"","Estado":0}
    try:
        Info_Datos = json.loads(str(Datos["Info"]))
        Existe = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".cdestinos WHERE cdestino = '"+str(Info_Datos["Codigo"])+"'  ")
        if len(Existe) == 0:
            Error = DB.Instruccion("""
            INSERT INTO """+str(BD_Nombre)+""".cdestinos
            (cdestino,ccorreos,cnombre)
            VALUES
            ('"""+str(Info_Datos["Codigo"])+"""','"""+str(Info_Datos["Correos"])+"""','"""+str(Info_Datos["Nombre"])+"""')
            """)
            if Error == "":
                Resultado["Estado"] = 1
            else:
                Resultado["Contenido"] += str(Error)
        else:
            Resultado["Contenido"] += "the supplier ["+str(Info_Datos["Nombre"])+"] already exists!"
    except:
        Resultado["Contenido"] = str(sys.exc_info())
    Cur += json.dumps(Resultado)
    return Cur
def Modificar(Datos):
    if "K" in session.keys():
        fernet = Fernet(session["K"])
    DB = LibDM_2023.DataBase()
    Compartido_2023 = LibDM_2023.Compartido()
    Cur = ""
    Resultado = {"Contenido":"","Estado":0}
    try:
        Info_Actual = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".cdestinos WHERE cdestino = '"+str(Datos["ID"])+"'")[0]
        Formulario = {"Col":"12", "Campos": [],"Clase": "Alta_Proveedor" }
        Formulario["Campos"].append({"tipo":"texto","campo":"Codigo","titulo":"Code","Requerido":1,"min":1,"max":30,"valor":str(Info_Actual["cdestino"]),"editable":False})
        Formulario["Campos"].append({"tipo":"texto","campo":"Nombre","titulo":"Nombre","Requerido":1,"min":1,"max":150,"valor":str(Info_Actual["cnombre"]),"editable":False})
        Formulario["Campos"].append({"tipo":"multitexto","campo":"Correos","titulo":"E-mail(s)","Requerido":0,"min":0,"max":2000,"valor":str(Info_Actual["ccorreos"])})
        Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
        Resultado["Contenido"] += """
        <hr>
        <div class='w-100 text-center'><button class='btn btn-success w-75' onclick='Modificar_Guardar("""+str(Datos["ID"])+""")'><i class='mdi mdi-floppy'></i> Save</button></div>
        """
        Resultado["Contenido"] += """
        <script>
            function Modificar_Guardar(ID){
                var Info = Dame_Formulario(".Alta_Proveedor",true);
                if(Info != null)
                {
                    Mostrar_Ventana_Cargando(false);
                    var parametros = {"Fun": '"""+str(fernet.encrypt("Modificar_Guardar".encode()).decode("utf-8"))+"""',"Info":JSON.stringify(Info),"ID":ID};
                    $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                        success:  function (response)
                        {
                            var Resultado = JSON.parse(response);
                            if(Resultado["Estado"] == 1)
                            {
                                $("#Vent_1").modal("hide");
                                Mensaje(2);
                                Llamar_Funcion(\""""+str(request.url)+"""\");
                            }
                            else
                                Mensaje(0,Resultado["Contenido"]);
                                
                        },
                        error: function (jqXHR, textStatus, errorThrown )
                        {
                            Mensaje(0,textStatus);
                        }
                    });
                }
            }
        </script>
        """
    except:
         Resultado["Contenido"] = str(sys.exc_info())
    Cur += json.dumps(Resultado)
    return Cur
def Modificar_Guardar(Datos):
    DB = LibDM_2023.DataBase()
    Compartido_2023 = LibDM_2023.Compartido()
    Cur = ""
    Resultado = {"Contenido":"","Estado":0}
    try:
        Info_Datos = json.loads(str(Datos["Info"]))
        Error = DB.Instruccion("""
        UPDATE """+str(BD_Nombre)+""".cdestinos SET
        cdestino = '"""+str(Info_Datos["Codigo"])+"""',
        ccorreos = '"""+str(Info_Datos["Correos"])+"""',
        cnombre = '"""+str(Info_Datos["Nombre"])+"""'
        WHERE cdestino = '"""+str(Datos["ID"])+"""'
        """)
        if Error == "":
            Resultado["Estado"] = 1
        else:
            Resultado["Contenido"] += str(Error)
    except:
        Resultado["Contenido"] = str(sys.exc_info())
    Cur += json.dumps(Resultado)
    return Cur
def Eliminar(Datos):
    DB = LibDM_2023.DataBase()
    Compartido_2023 = LibDM_2023.Compartido()
    Cur = ""
    Resultado = {"Contenido":"","Estado":0}
    Error = ""
    try:
        Error = DB.Instruccion("UPDATE "+str(BD_Nombre)+".cdestinos SET cactivo = 0 WHERE cdestino = '"+str(Datos["ID"])+"'")
        if Error == "":
            Resultado["Estado"] = 1
        else:
            Resultado["Contenido"] += str(Error)
    except:
        Resultado["Contenido"] = str(sys.exc_info())
    Cur += json.dumps(Resultado)
    return Cur



def Direccionar(Datos):
    try:
        if "K" in session.keys():
            fernet = Fernet(session["K"])
        else:
            fernet = Fernet(LibDM_2023.Compartido().Dame_K2())
        if Datos is None:
            return Inicio()
        else:
            if "Fun" in Datos:
                Funcion = fernet.decrypt(Datos["Fun"].encode()).decode()
                Par = {}
                for P in Datos.keys():
                    if str(P) != "Fun":
                        Par[str(P)] = Datos[str(P)]
                if "IDu" in session.keys():
                    Par["ID_User"] = session["IDu"]
                return globals()[Funcion](Par)
            else:
                return Inicio()
    except:
        return str(sys.exc_info())

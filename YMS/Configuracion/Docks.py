from flask import request,session,render_template
from cryptography.fernet import Fernet
from datetime import datetime,date,timedelta
import sys
import json
import os
from Componentes import LibDM_2023
BD_Nombre = "public"
Bandera_Dock = "YMS"
fernet = Fernet(LibDM_2023.Compartido().Dame_K2())
def Inicio():
    if "K" in session.keys():
        fernet = Fernet(session["K"])
    Cur = ""
    try:
        DB = LibDM_2023.DataBase()
        Activo = "YMS"
        Compartido = LibDM_2023.Compartido()
        Menu = LibDM_2023.Menu().Menu(Activo,request.url_root,session["IDu"])
        Titulo = LibDM_2023.Menu().Get_Titulo(Activo)
        Contenido = ""
        Docks = []
        for Dock in DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".cdock_asignacion"):
            if Dock["cd_etiqueta"] is None:
                Dock["cd_etiqueta"] = ""
            if int(Dock["cd_activo"]) == 1:
                if str(Dock["cd_ub"]) == str(Bandera_Dock):
                    Opciones = "<div class='text-center'><div class='btn-group' role='group' aria-label='Basic mixed styles example'>"
                    Opciones += "<button class='btn btn-sm btn-warning p-0 ps-1 pe-1' onclick='Modificar("+str(Dock["cd_dock"])+")'><i class='mdi mdi-pencil'></i></button>"
                    Opciones += "<button class='btn btn-sm btn-danger p-0 ps-1 pe-1' onclick='Eliminar("+str(Dock["cd_dock"])+")'><i class='mdi mdi-trash-can'></i></button>"
                    Opciones += "</div></div>"
                elif Dock["cd_ub"] is None:
                    Opciones = "<div class='text-center'><div class='btn-group' role='group' aria-label='Basic mixed styles example'>"
                    Opciones += "<button class='btn btn-sm btn-primary p-0 ps-1 pe-1' onclick='Asignar("+str(Dock["cd_dock"])+")'><i class='mdi mdi-hand-front-right'></i></button>"
                    Opciones += "</div></div>"
                else:
                    Opciones = ""
            else:
                Opciones = "<span class='ms-1 me-1'><i class='mdi mdi-lock'></i></span>"
            if Dock["cd_ub"] is None:
                Dock["cd_ub"] = ""
            Docks.append({"Dock":str(Dock["cd_dock"]),"Label":str(Dock["cd_etiqueta"]),"Opciones":Opciones,"UB":str(Dock["cd_ub"]),"Activo":int(Dock["cd_activo"])})


        Contenido += "<div class='h2 fw-lighter mt-1 mb-1 text-center border-bottom'><i class='mdi mdi mdi-sign-caution'></i> Docks Master</div>"
        Contenido += """
        <div class='container'>
        <div class='row'>
            <div class='col-12'>
                <div id='Tabla_Proveedores' class='border border-dark bg-dark-subtle'></div>
                <script>
                    delete Tabla_Proveedores;
                    var Tabla_Proveedores = new Tabulator("#Tabla_Proveedores", {
                        minHeight:800,
                        layout:"fitColumns",
                        data:"""+str(Docks)+""",
                        rowFormatter:function(row){
                            if(row.getData().Activo == 0){
                                 if(row.getPosition()%2)
                                        row.getElement().style.backgroundColor = "#bfbfbf";
                                    else
                                        row.getElement().style.backgroundColor = "#aeaeae";
                            }
                            else{
                                if(row.getData().UB == \""""+str(Bandera_Dock)+"""\"){
                                    if(row.getPosition()%2)
                                        row.getElement().style.backgroundColor = "#dcf8d7";
                                    else
                                        row.getElement().style.backgroundColor = "#bbf7af";
                                }
                                if(row.getData().UB != "" && row.getData().UB != \""""+str(Bandera_Dock)+"""\"){
                                    if(row.getPosition()%2)
                                        row.getElement().style.backgroundColor = "#f8d7d7";
                                    else
                                        row.getElement().style.backgroundColor = "#f7afaf";
                                }
                            }
                            
                            
                        },
                        columns:[
                            {field:"Dock","title":"DOCK",widthGrow:1,headerFilter:"input"},
                            {field:"Label","title":"Label",headerFilter:"input",widthGrow:10},
                            {field:"UB","title":"UB",headerFilter:"input",widthGrow:10},
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
            function Modificar(Dock){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-pencil'></i>" + Dock);
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm');
                var parametros = {"Fun":'"""+str(fernet.encrypt("Modificar".encode()).decode("utf-8"))+"""',"Dock":Dock};
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
            function Eliminar(Dock){
                Swal.fire({
                    title: 'Are you sure free ['+Dock+']?',
                    buttonsStyling: false,showCancelButton: true,confirmButtonText: "<i class='mdi mdi-check'></i> Yes",cancelButtonText: "<i class='mdi mdi-close'></i> No",showLoaderOnConfirm: true,
                    customClass: {confirmButton: 'btn btn-success ms-1 me-1',cancelButton: 'btn btn-danger ms-1 me-1'},
                    preConfirm: () => {
                        
                        Mostrar_Ventana_Cargando(false);
                            var parametros = {"Fun":'"""+str(fernet.encrypt("Eliminar".encode()).decode("utf-8"))+"""',"Dock":Dock};
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
            function Asignar(Dock){
                Swal.fire({
                    title: 'Are you sure assigned ['+Dock+']?',
                    buttonsStyling: false,showCancelButton: true,confirmButtonText: "<i class='mdi mdi-check'></i> Yes",cancelButtonText: "<i class='mdi mdi-close'></i> No",showLoaderOnConfirm: true,
                    customClass: {confirmButton: 'btn btn-success ms-1 me-1',cancelButton: 'btn btn-danger ms-1 me-1'},
                    preConfirm: () => {
                        
                        Mostrar_Ventana_Cargando(false);
                            var parametros = {"Fun":'"""+str(fernet.encrypt("Asignar".encode()).decode("utf-8"))+"""',"Dock":Dock};
                            $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                                success:  function (response)
                                {
                                    alert(response);
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
def Modificar(Datos):
    if "K" in session.keys():
        fernet = Fernet(session["K"])
    DB = LibDM_2023.DataBase()
    Compartido_2023 = LibDM_2023.Compartido()
    Cur = ""
    Resultado = {"Contenido":"","Estado":0}
    try:
        Info_Actual = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".cdock_asignacion WHERE cd_dock = '"+str(Datos["Dock"])+"'")[0]
        if Info_Actual["cd_etiqueta"] is None:
            Info_Actual["cd_etiqueta"] = ""
        Formulario = {"Col":"12", "Campos": [],"Clase": "Dock" }
        Formulario["Campos"].append({"tipo":"texto","campo":"Etiqueta","titulo":"Label","Requerido":0,"min":0,"max":30,"valor":str(Info_Actual["cd_etiqueta"])})
        Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
        Resultado["Contenido"] += """
        <hr>
        <div class='w-100 text-center'><button class='btn btn-success w-75' onclick='Modificar_Guardar("""+str(Datos["Dock"])+""")'><i class='mdi mdi-floppy'></i> Save</button></div>
        """
        Resultado["Contenido"] += """
        <script>
            function Modificar_Guardar(Dock){
                var Info = Dame_Formulario(".Dock",true);
                if(Info != null)
                {
                    Mostrar_Ventana_Cargando(false);
                    var parametros = {"Fun":'"""+str(fernet.encrypt("Modificar_Guardar".encode()).decode("utf-8"))+"""',"Info":JSON.stringify(Info),"Dock":Dock};
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
        UPDATE """+str(BD_Nombre)+""".cdock_asignacion SET
        cd_etiqueta = '"""+str(Info_Datos["Etiqueta"])+"""'
        WHERE cd_dock = '"""+str(Datos["Dock"])+"""'
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
        Error = DB.Instruccion("UPDATE "+str(BD_Nombre)+".cdock_asignacion SET cd_etiqueta = null, cd_ub = null WHERE cd_dock = '"+str(Datos["Dock"])+"'")
        if Error == "":
            Resultado["Estado"] = 1
        else:
            Resultado["Contenido"] += str(Error)
    except:
        Resultado["Contenido"] = str(sys.exc_info())
    Cur += json.dumps(Resultado)
    return Cur
def Asignar(Datos):
    DB = LibDM_2023.DataBase()
    Compartido_2023 = LibDM_2023.Compartido()
    Cur = ""
    Resultado = {"Contenido":"","Estado":0}
    Error = ""
    try:
        Error = DB.Instruccion("UPDATE "+str(BD_Nombre)+".cdock_asignacion SET cd_etiqueta = null, cd_ub = '"+str(Bandera_Dock)+"' WHERE cd_dock = '"+str(Datos["Dock"])+"'")
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

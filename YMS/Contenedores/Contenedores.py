from flask import request,session,render_template
from cryptography.fernet import Fernet
from datetime import datetime,date,timedelta
import sys
import json
import os
from Componentes import LibDM_2023
Url = ""
fernet = Fernet(LibDM_2023.Compartido().Dame_K2())
BD_Nombre = "public"
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
        Contenedores_Patio = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".ccajas where cc_activo = 1 AND cc_caja_danada = 0 AND cc_bloqueo_rg = 0 AND cc_ubicacion = 'Patio'")
        Contenedores_Dock = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".ccajas where cc_activo = 1 AND cc_caja_danada = 0 AND cc_bloqueo_rg = 0 AND cc_ubicacion = 'Dock'")
        Patio = []
        for Contenedor in Contenedores_Patio:
            Opciones = "<div class='btn-group' role='group' aria-label='Basic mixed styles example'>"
            Info_Actual = json.loads(str(Contenedor["cc_informacion_actual"]))

            Opciones += "<button class='btn btn-sm btn-primary p-0 ps-1 pe-1' onclick='Ver_Historico("+str(Contenedor["cc_id"])+",\""+str(Contenedor["cc_contenedor"])+"\")'><i class='mdi mdi-history'></i></button>"
            if int(Contenedor["cc_bloquear"]) == 0:
                Opciones += "<button class='btn btn-sm btn-warning p-0 ps-1 pe-1' onclick='Modificar("+str(Contenedor["cc_id"])+",\""+str(Contenedor["cc_contenedor"])+"\")'><i class='mdi mdi-pencil'></i></button>"
            else:
                Opciones += "<span class='ms-1 me-1'><i class='mdi mdi-lock'></i></span>"
                

            Sello = ""
            if "Sello Proveedor" in Info_Actual.keys():
                Sello = "<span style='color:blue'><i class='mdi mdi-label'></i></span> "+str(Info_Actual["Sello Proveedor"])
            if "Sello Temporal" in Info_Actual.keys():
                Sello = "<span style='color:#7a7a7a'><i class='mdi mdi-label'></i></span> "+str(Info_Actual["Sello Temporal"])
            if "Sello Blanco" in Info_Actual.keys():
                Sello = "<span><i class='mdi mdi-label-outline'></i></span> "+str(Info_Actual["Sello Temporal"])
            if "Sello Rojo" in Info_Actual.keys():
                Sello = "<span style='color:#ff0000'><i class='mdi mdi-label'></i></span> "+str(Info_Actual["Sello Temporal"])

            Ruta = ""
            Ruta += "<span class='h-100 border' style='width:20px; background:var(--Color_"+str(Contenedor["cc_tipo_actual"])+");Color:var(--Color_"+str(Contenedor["cc_tipo_actual"])+");'>__</span>"
            try:
                Tipo = Info_Actual[Contenedor["cc_tipo_actual"]]
                Ruta += str(Tipo)
                Tipo_1 = Info_Actual[Tipo]
                Ruta += "/"+str(Tipo_1)
                Tipo_2 = Info_Actual[Tipo_1]
                Ruta += "/"+str(Tipo_2)
            except:
                pass
            
            if "Fecha_Salida" in Info_Actual.keys():
                Ruta += " <"+str(Info_Actual["Fecha_Salida"])+">"


            Estado = ""
            if "Etapa" not in Info_Actual.keys():
                if Contenedor["cc_tipo_actual"] is None:
                    Estado = "<span class='fw-bold text-danger'>Not assigned</span>"
                else:
                    Estado = "Waiting"
            else:
                Estado = Info_Actual["Etapa"]
                if Info_Actual["Etapa"] == "Pending Exit":
                    #Opciones += "<button class='btn btn-sm btn-dark p-0 ps-1 pe-1' onclick='Imprimir_Pase("+str(Contenedor["cc_id"])+",\""+str(Contenedor["cc_contenedor"])+"\")'><i class='mdi mdi-printer'></i></button>"
                    Opciones += "<button class='btn btn-sm btn-danger p-0 ps-1 pe-1' onclick='Salida("+str(Contenedor["cc_id"])+",\""+str(Contenedor["cc_contenedor"])+"\")'><i class='mdi mdi-exit-to-app'></i></button>"

            Opciones += "</div>"

            for K in Contenedor.keys():
                if Contenedor[K] is None:
                    Contenedor[K] = ""
            Patio.append({"Tiempo":"<span class='tiempo' tiempo='"+str(Contenedor["cc_ultimo_mov"])+"'></span>","Caja":str(Contenedor["cc_contenedor"]),"Carrier":Info_Actual["Carrier"],"Tipo":Contenedor["cc_tipo_actual"],"Estado":str(Estado),"Sello":Sello,"Ruta":Ruta,"Opciones":"<div class='text-center'>"+str(Opciones)+"</div>"})

        Dock = []
        for Contenedor in Contenedores_Dock:
            Opciones = "<div class='btn-group' role='group' aria-label='Basic mixed styles example'>"
            Info_Actual = json.loads(str(Contenedor["cc_informacion_actual"]))
            Opciones += "<button class='btn btn-sm btn-primary p-0 ps-1 pe-1' onclick='Ver_Historico("+str(Contenedor["cc_id"])+",\""+str(Contenedor["cc_contenedor"])+"\")'><i class='mdi mdi-history'></i></button>"
            if Contenedor["cc_tipo_actual"] == "Empty" and "Empty" in Info_Actual.keys() and Info_Actual["Empty"] == "Ready to Load":
                Opciones += "<button class='btn btn-sm btn-warning p-0 ps-1 pe-1' onclick='Opciones("+str(Contenedor["cc_id"])+",\""+str(Contenedor["cc_contenedor"])+"\")'><i class='mdi mdi-pencil'></i></button>"
            else:
                Opciones += "<button class='btn btn-sm btn-warning p-0 ps-1 pe-1' onclick='Opciones("+str(Contenedor["cc_id"])+",\""+str(Contenedor["cc_contenedor"])+"\")'><i class='mdi mdi-pencil'></i></button>"
            
            Ruta = ""
            Ruta += "<span class='h-100 border' style='width:20px; background:var(--Color_"+str(Contenedor["cc_tipo_actual"])+");Color:var(--Color_"+str(Contenedor["cc_tipo_actual"])+");'>__</span>"
            try:
                Tipo = Info_Actual[Contenedor["cc_tipo_actual"]]
                Ruta += str(Tipo)
                Tipo_1 = Info_Actual[Tipo]
                Ruta += "/"+str(Tipo_1)
                Tipo_2 = Info_Actual[Tipo_1]
                Ruta += "/"+str(Tipo_2)
            except:
                pass
                
            if "Fecha_Salida" in Info_Actual.keys():
                    Ruta += " <"+str(Info_Actual["Fecha_Salida"])+">"

            Sello = ""
            if "Sello Proveedor" in Info_Actual.keys():
                Sello = "<span style='color:blue'><i class='mdi mdi-label'></i></span> "+str(Info_Actual["Sello Proveedor"])
            if "Sello Temporal" in Info_Actual.keys():
                Sello = "<span style='color:#7a7a7a'><i class='mdi mdi-label'></i></span> "+str(Info_Actual["Sello Temporal"])
            if "Sello Blanco" in Info_Actual.keys():
                Sello = "<span><i class='mdi mdi-label-outline'></i></span> "+str(Info_Actual["Sello Temporal"])
            if "Sello Rojo" in Info_Actual.keys():
                Sello = "<span style='color:#ff0000'><i class='mdi mdi-label'></i></span> "+str(Info_Actual["Sello Temporal"])
            
            Estado = ""
            if "Etapa" not in Info_Actual.keys():
                Estado = "Waiting"
            else:
                Estado = Info_Actual["Etapa"]
            
            for K in Contenedor.keys():
                if Contenedor[K] is None:
                    Contenedor[K] = ""

            Dock.append({"Dock":str(Contenedor["cc_dock"]),"Tiempo":"<span class='tiempo' tiempo='"+str(Contenedor["cc_ultimo_mov"])+"'></span>","Caja":str(Contenedor["cc_contenedor"]),"Carrier":Info_Actual["Carrier"],"Tipo":Contenedor["cc_tipo_actual"],"Estado":Estado,"Ruta":Ruta,"Opciones":"<div class='text-center'>"+str(Opciones)+"</div>"})
        Contenido += """<div class='text-end pe-1 pt-1'><small class='link-primary' style='cursor:pointer' onclick='Llamar_Funcion(\""""+str(Dir_Raiz)+"""\");'>Actualizar <i class='mdi mdi-refresh'></i></small></div>"""
        Contenido += "<div class='h2 fw-lighter mt-1 mb-1 text-center border-bottom'><i class='mdi mdi-truck-trailer'></i> Contenedores</div>"
        Contenido += """
        <div class='text-end mb-1'> <button class='btn btn-success' onclick='Nueva_Caja()'><i class='mdi mdi-plus'></i> Nuevo Contenedor</button> </div>
        <div class='row'>
            <div class='col-6'>
                <div class='h3 text-center'><i class='mdi mdi-car-brake-parking'></i> Patio</div>
                <div id='Tabla_Patio' class='border border-dark bg-dark-subtle'></div>
                <script>
                    delete Tabla_Patio;
                    var Tabla_Patio = new Tabulator("#Tabla_Patio", {
                        minHeight:800,
                        layout:"fitColumns",
                        data:"""+str(Patio)+""",
                        columns:[
                            {field:"Tiempo","title":"Ultimo Movement",formatter:"html"},
                            {field:"Caja","title":"Contenedor/Caja",headerFilter:"input"},
                            {field:"Carrier","title":"Carrier"},
                            {field:"Tipo","title":"Tipo"},
                            {field:"Ruta","title":"Ruta",formatter:"html"},
                            {field:"Sello","title":"Sello",formatter:"html"},
                            {field:"Estado","title":"Estado",formatter:"html"},
                            {field:"Opciones","title":"Op",formatter:"html"}
                        ]
                    });
                    Tabla_Patio.on("tableBuilt", function(){ 
                        setTimeout(() => {
                            Tabla_Patio.clearFilter();
                            Tabla_Patio.redraw();
                        }, 100);
                    });
                </script>
            </div>
            <div class='col-6'>
                <div class='h3 text-center'><i class='mdi mdi-sign-caution'></i> Docks</div>
                <div id='Tabla_Docks' class='border border-dark bg-dark-subtle'></div>
                <script>
                    delete Tabla_Docks;
                    var Tabla_Docks = new Tabulator("#Tabla_Docks", {
                        minHeight:800,
                        layout:"fitColumns",
                        data:"""+str(Dock)+""",
                        columns:[
                            {field:"Dock","title":"Dock"},
                            {field:"Tiempo","title":"Ultimo Movement",formatter:"html"},
                            {field:"Caja","title":"Contenedor/Caja",headerFilter:"input"},
                            {field:"Carrier","title":"Carrier"},
                            {field:"Tipo","title":"Tipo"},
                            {field:"Ruta","title":"Ruta",formatter:"html"},
                            {field:"Opciones","title":"Op",formatter:"html"}
                        ]
                    });
                    Tabla_Docks.on("tableBuilt", function(){ 
                        setTimeout(() => {
                            Tabla_Docks.clearFilter();
                            Tabla_Docks.redraw();
                        }, 100);
                    });
                </script>
            </div>
        </div>
        <script>
            function Ver_Historico(ID,Contenedor){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-history'></i> History ["+Contenedor+"]");
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm').addClass('modal-xl');
                var parametros = {"Fun":'"""+str(fernet.encrypt("Ver_Historico".encode()).decode("utf-8"))+"""',"ID":ID};
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
            function Modificar(ID,Contenedor){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-pencil'></i> Modify ["+Contenedor+"]");
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm')
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
            function Opciones(ID,Contenedor){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-menu'></i> Options ["+Contenedor+"]");
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm')
                var parametros = {"Fun":'"""+str(fernet.encrypt("Opciones".encode()).decode("utf-8"))+"""',"ID":ID};
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
            function Regresar(ID,Contenedor){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-history'></i> Return previous ["+Contenedor+"]");
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm').addClass('modal-xl');
                var parametros = {"Fun":'"""+str(fernet.encrypt("Regresar".encode()).decode("utf-8"))+"""',"ID":ID};
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
            function Imprimir_Pase(ID,Contenedor){
                Mostrar_Ventana_Cargando(false);
                var parametros = {"Fun":'"""+str(fernet.encrypt("Imprimir_Pase".encode()).decode("utf-8"))+"""',"ID":ID};
                $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                    success:  function (response)
                    {
                        var Resultado = JSON.parse(response);
                        if(Resultado["Estado"] == 1){
                            if("Pase Salida" in Resultado)
                            {
                                var win1 = window.open(Resultado["Pase Salida"], '_blank');
                                win1.focus();
                            }
                            if("Manifiesto" in Resultado)
                            {
                                var win1 = window.open(Resultado["Manifiesto"], '_blank');
                                win1.focus();
                            }
                            Mensaje(2);
                        }else{
                            Mensaje(0,Resultado["Contenido"]);
                        }
                        
                    },
                    error: function (jqXHR, textStatus, errorThrown ){Mensaje(0,textStatus);}
                });
            }
            function Nueva_Caja(){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-plus'></i> Nuevo Contenedor");
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm');
                var parametros = {"Fun":'"""+str(fernet.encrypt("Nueva_Caja".encode()).decode("utf-8"))+"""'};
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
            function Salida(ID,Contenedor){
                Swal.fire({
                title: '¿Estás seguro de darle salida al contenedor ['+Contenedor+']?',
                buttonsStyling: false,showCancelButton: true,confirmButtonText: "<i class='mdi mdi-check'></i> Si",cancelButtonText: "<i class='mdi mdi-close'></i> No",showLoaderOnConfirm: true,
                customClass: {confirmButton: 'btn btn-success ms-1 me-1',cancelButton: 'btn btn-danger ms-1 me-1'},
                preConfirm: () => {
                    Mostrar_Ventana_Cargando(false);
                    var parametros = {"Fun":'"""+str(fernet.encrypt("Salida".encode()).decode("utf-8"))+"""',"ID":ID};
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

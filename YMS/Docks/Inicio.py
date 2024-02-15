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
Bandera_Dock = "YMS"
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
        Contenido += """<div class='text-end pe-1 pt-1'><small class='link-primary' style='cursor:pointer' onclick='Llamar_Funcion(\""""+str(request.url)+"""\");'>Update <i class='mdi mdi-refresh'></i></small></div>"""
        Contenido += "<div class='h2 fw-lighter mt-1 mb-1 text-center border-bottom'><i class='mdi mdi-sign-caution'></i> Docks</div>"
        Contenido += """
        <style>
            .Dock:hover{
                background:blue;
                color:#ffffff;
                cursor:pointer;
            }
        </style>    
        <div class='row'>
        """
        Cajas_Docks = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".ccajas WHERE cc_dock IS NOT NULL AND cc_activo = 1 ")
        for Dock in DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".cdock_asignacion WHERE cd_ub = '"+str(Bandera_Dock)+"' AND cd_activo = 1 ORDER BY cd_dock"):
            Etiqueta = ""
            if Dock["cd_etiqueta"] is not None:
                Etiqueta = str(Dock["cd_etiqueta"] )
            Caja_Aqui = None
            Color = "#ffffff"
            for C in Cajas_Docks:
                if int(C["cc_dock"]) == int(Dock["cd_dock"]):
                    Caja_Aqui = C
                    Color = "#88ffa0"
                    break
            
            if Caja_Aqui is not None:
                Info_Actual = json.loads(str(Caja_Aqui["cc_informacion_actual"]))
                Contenido += """
                <div class='col-sm-4 col-md-3 col-xl-2 p-1'  onclick='Opciones("""+str(Caja_Aqui["cc_id"])+""",\""""+str(Caja_Aqui["cc_contenedor"])+"""\")'><div class='h-100 border border-dark ps-3 pe-3 pt-1 pb-1 position-relative Dock'>
                    <div class='position-absolute top-50 start-0 translate-middle-y text-dark' style='writing-mode: vertical-lr; -webkit-text-stroke: 0.4px #ffffff;'><small>"""+str(Etiqueta)+"""</small></div>
                    <div class='row h-100' style='background:"""+str(Color)+"""' >
                        <div class='col-auto bg-dark text-white fs-1'>
                            """+str(Dock["cd_dock"])+"""
                        </div>
                        <div class='col'>
                """
            else:
                Contenido += """
                <div class='col-sm-4 col-md-3 col-xl-2 p-1' onclick='Dock("""+str(Dock["cd_dock"])+""")'><div class='h-100 border border-dark ps-3 pe-3 pt-1 pb-1 position-relative Dock'>
                    <div class='position-absolute top-50 start-0 translate-middle-y text-dark' style='writing-mode: vertical-lr; -webkit-text-stroke: 0.4px #ffffff;'><small>"""+str(Etiqueta)+"""</small></div>
                    <div class='row h-100 ' style='background:"""+str(Color)+"""' >
                        <div class='col-auto bg-dark text-white fs-1'>
                            """+str(Dock["cd_dock"])+"""
                        </div>
                        <div class='col'>
                """
            if Caja_Aqui is not None:
                pass
                Info_Actual = json.loads(str(Caja_Aqui["cc_informacion_actual"]))
                Estado = ""
                Estado += "<span class='h-100' style='width:20px; background:var(--Color_"+str(Caja_Aqui["cc_tipo_actual"])+");Color:var(--Color_"+str(Caja_Aqui["cc_tipo_actual"])+");'>__</span>"
                try:
                    Tipo = Info_Actual[Caja_Aqui["cc_tipo_actual"]]
                    Estado += str(Tipo)
                    Tipo_1 = Info_Actual[Tipo]
                    Estado += "/"+str(Tipo_1)
                    Tipo_2 = Info_Actual[Tipo_1]
                    Estado += "/"+str(Tipo_2)
                except:
                    pass
                Contenido += "<div class='border-bottom border-dark text-center fw-bold'>"+str(Caja_Aqui["cc_contenedor"])+"</div>"
                Contenido += "<div class='text-center'>"+str(Caja_Aqui["cc_tipo_actual"])+"</div>"
                Contenido += "<div class='text-center'><small>"+str(Estado)+"</small></div>"
                Contenido += "<div class='text-center'><small class='tiempo' tiempo='"+str(Caja_Aqui["cc_ultimo_mov"]).split(".")[0]+"'></small></div>"
            Contenido += """
                    </div>
                </div>
                
            </div></div>
            """
        Contenido += """
            </div>
        </div>
        <script>
            function Opciones(ID,Contenedor){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-menu'></i> Options ["+Contenedor+"]");
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm')
                var parametros = {"Fun":'"""+str(fernet.encrypt("Opciones".encode()).decode("utf-8"))+"""',"ID":ID};
                $.ajax({data:  parametros,url:\""""+str(request.url_root)+"""/YMS/Container_Control\",type:  "post",
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
            function Dock(Dock){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-menu'></i> Dock ["+Dock+"]");
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm').addClass('modal-lg');
                var parametros = {"Fun":'"""+str(fernet.encrypt("Dock".encode()).decode("utf-8"))+"""',"Dock":Dock};
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
        </script>
        <script>
            $( document ).ready(function() {
                setInterval(Actualizar_Hora_Final, 500)
            });
            function Actualizar_Hora_Final()
            {
                $(".tiempo").each(function() {
                    var Limite = moment($(this).attr('tiempo'));
                    var Ahora = moment('"""+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+"""','YYYY-MM-DD hh:mm:ss'); //todays date
                    var Faltan = moment.duration(Ahora.diff(Limite));
                    var Dias = Faltan.asDays().toString().split(".")[0];
                    var Horas = Faltan.hours();
                    if(Horas.toString().length == 1)
                        Horas = "0"+Horas;
                    var Minutos = Faltan.minutes();
                    if(Minutos.toString().length == 1)
                        Minutos = "0"+Minutos;
                    var Segundos = Faltan.seconds();
                    if(Segundos.toString().length == 1)
                        Segundos = "0"+Segundos;
                    if (Dias == 0)
                        $(this).html("<b>" + Horas +":" + Minutos +":"+ Segundos +"</b>")
                    else
                        $(this).html("<b>" + Dias + " Days, " + Horas +":" + Minutos +":"+ Segundos +"</b>")

                });
            }
        </script>
        """

        Cur += render_template("general.html",Contenido=Contenido,Componentes=Compartido.Complementos(None),Menu=Menu,Titulo=Titulo)
    except:
        Cur += str(sys.exc_info())
    return Cur
def Dock(Datos):
    if "K" in session.keys():
        fernet = Fernet(session["K"])
    DB = LibDM_2023.DataBase()
    Compartido_2023 = LibDM_2023.Compartido()
    Cur = ""
    Resultado = {"Contenido":"","Estado":0}
    try:
        Patio = []
        Contenedores_Patio = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".ccajas where cc_activo = 1 AND cc_caja_danada = 0 AND cc_bloqueo_rg = 0 AND cc_ubicacion = 'Patio' and cc_tipo_actual is not null")
        Patio = []
        for Contenedor in Contenedores_Patio:
            Opciones = "<div class='btn-group' role='group' aria-label='Basic mixed styles example'>"
            Info_Actual = json.loads(str(Contenedor["cc_informacion_actual"]))
            if int(Contenedor["cc_bloquear"]) == 0:
                Opciones += "<button class='btn btn-sm btn-warning p-0 ps-1 pe-1' onclick='Mover_a_Dock("+str(Contenedor["cc_id"])+",\""+str(Contenedor["cc_contenedor"])+"\","+str(Datos["Dock"])+")'><i class='mdi mdi-download'></i></button>"
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

            Estado = ""
            if "Etapa" not in Info_Actual.keys():
                Estado = "Waiting"
            else:
                Estado = Info_Actual["Etapa"]

            Opciones += "</div>"
            Patio.append({"Tiempo":"<span class='tiempo' tiempo='"+str(Contenedor["cc_ultimo_mov"])+"'></span>","Caja":str(Contenedor["cc_contenedor"]),"Carrier":Info_Actual["Carrier"],"Tipo":Contenedor["cc_tipo_actual"],"Estado":str(Estado),"Sello":Sello,"Ruta":Ruta,"Opciones":"<div class='text-center'>"+str(Opciones)+"</div>"})

        Resultado["Contenido"] += """
        <div class='h3 text-center'><i class='mdi mdi-car-brake-parking'></i> Patio</div>
        <div id='Tabla_Patio' class='border border-dark bg-dark-subtle'></div>
        <script>
            delete Tabla_Patio;
            var Tabla_Patio = new Tabulator("#Tabla_Patio", {
                minHeight:800,
                layout:"fitColumns",
                data:"""+str(Patio)+""",
                columns:[
                    {field:"Caja","title":"Container",headerFilter:"input"},
                    /*{field:"Carrier","title":"Carrier"},*/
                    {field:"Tipo","title":"Type"},
                    {field:"Ruta","title":"Ruta",formatter:"html"},
                    {field:"Estado","title":"Status"},
                    {field:"Opciones","title":"Op",formatter:"html"}
                ]
            });
            Tabla_Patio.on("tableBuilt", function(){ 
                setTimeout(() => {
                    Tabla_Patio.clearFilter();
                    Tabla_Patio.redraw();
                }, 100);
            });

            function Mover_a_Dock(ID,Contenedor,Dock){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-history'></i> Mover ["+Contenedor+"] al Dock ["+Dock+"]");
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm').addClass('modal-xl');
                var parametros = {"Fun":'"""+str(fernet.encrypt("Mover_a_Dock".encode()).decode("utf-8"))+"""',"ID":ID,"Dock":Dock};
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
        </script>
        """
    except:
        Resultado["Contenido"] = str(sys.exc_info())
    Cur += json.dumps(Resultado)
    return Cur
def Mover_a_Dock(Datos):
    if "K" in session.keys():
        fernet = Fernet(session["K"])
    DB = LibDM_2023.DataBase()
    Compartido_2023 = LibDM_2023.Compartido()
    Cur = ""
    Resultado = {"Contenido":"","Estado":0}
    try:
        Formulario = {"Col":"12", "Campos": [],"Clase": "Mover_Dock" }
        Formulario["Campos"].append({"tipo":"archivo","campo":"Fotos","titulo":"Photos","Requerido":1,"Col":12,"min":1,"max":5,"tipo_archivo":["image/*"],"valor":""})
        Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
        Resultado["Contenido"] += """
        <hr>
        <div class='w-100 text-center'><button class='btn btn-success w-75' onclick='Mover_a_Dock_Guardar(\""""+str(Datos["ID"])+"""\",\""""+str(Datos["Dock"])+"""\")'><i class='mdi mdi-floppy'></i> Save</button></div>
        <script>
            function Mover_a_Dock_Guardar(ID,Dock){
                var Info = Dame_Formulario(".Mover_Dock",true);
                if(Info != null)
                {
                    Mostrar_Ventana_Cargando(false);
                    var parametros = {"Fun":'"""+str(fernet.encrypt("Mover_a_Dock_Guardar".encode()).decode("utf-8"))+"""',"Info":JSON.stringify(Info),"ID":ID,"Dock":Dock};
                    $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                        success:  function (response)
                        {
                            var Resultado = JSON.parse(response);
                            if(Resultado["Estado"] == 1)
                            {
                                if("Pase Salida" in Resultado)
                                {
                                    var win1 = window.open(Resultado["Pase Salida"], '_blank');
                                    win1.focus();
                                }
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
def Mover_a_Dock_Guardar(Datos):
    DB = LibDM_2023.DataBase()
    Compartido_2023 = LibDM_2023.Compartido()
    Cur = ""
    Resultado = {"Contenido":"","Estado":0}
    try:
        Info_Datos = json.loads(str(Datos["Info"]))
        Caja = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".ccajas WHERE cc_id = '"+str(Datos["ID"])+"'")[0]
        Info_Nueva = json.loads(str(Caja["cc_informacion_actual"]))
        Ubicacion = "Dock"
        Dock = "'"+str(Datos["Dock"])+"'"
        Info_Nueva["Dock"] = str(Datos["Dock"])
        Info_Nueva["Fotos"] = Info_Datos["Fotos"]
        Error = DB.Instruccion("UPDATE "+str(BD_Nombre)+".ccajas SET cc_informacion_actual = '"+str(json.dumps(Info_Nueva))+"',cc_ultimo_mov = NOW(),cc_dock= "+str(Dock)+",cc_ubicacion = '"+str(Ubicacion)+"' WHERE cc_id = '"+str(Datos["ID"])+"' ")
        if Error == "":
            Info_Ahora = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".ccajas WHERE cc_id = '"+str(Datos["ID"])+"'")[0]
            Info_Ahora["cc_dock"] = 'null' if Info_Ahora["cc_dock"] is None else "'"+str(Info_Ahora["cc_dock"])+"'"
            Info_Ahora["cc_tipo_actual"] = 'null' if Info_Ahora["cc_tipo_actual"] is None else "'"+str(Info_Ahora["cc_tipo_actual"])+"'"
            Info_Ahora["cc_zona"] = 'null' if Info_Ahora["cc_zona"] is None else "'"+str(Info_Ahora["cc_zona"])+"'"
            Info_Ahora["cc_negocio"] = 'null' if Info_Ahora["cc_negocio"] is None else "'"+str(Info_Ahora["cc_negocio"])+"'"
            Error = DB.Instruccion(""" 
            INSERT INTO """+str(BD_Nombre)+""".ccajas_moviemiento
            (cch_master,cch_fecha_hora,cch_contenedor,cch_ubicacion,cch_informacion_actual,cch_dock,cch_tipo_actual,cch_zona,cch_negocio,cch_usuario,cch_movimiento)
            VALUES
            ('"""+str(Info_Ahora["cc_id"])+"""',NOW(),'"""+str(Info_Ahora["cc_contenedor"])+"""','"""+str(Info_Ahora["cc_ubicacion"])+"""','"""+str(Info_Ahora["cc_informacion_actual"])+"""',"""+str(Info_Ahora["cc_dock"])+""","""+str(Info_Ahora["cc_tipo_actual"])+""","""+str(Info_Ahora["cc_zona"])+""","""+str(Info_Ahora["cc_negocio"])+""",'"""+str(Datos["ID_User"])+"""','MODIFICAR')
            """)
            if Error == "":
                Resultado["Estado"] = 1
            else:
                Resultado["Contenido"] = Error
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

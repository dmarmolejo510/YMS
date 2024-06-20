from flask import request,session,render_template
from cryptography.fernet import Fernet
from datetime import datetime,date,timedelta
import sys
import json
import os
import hashlib
from Componentes import LibDM_2023
Url = ""
fernet = Fernet(LibDM_2023.Compartido().Dame_K2())
Menu_Activo = "YMS"
BaseDatos = LibDM_2023.Compartido().Dame_Base_Datos("YMS")
Bandera_Docks = "YMS"
def Inicio():
    fernet = Fernet(LibDM_2023.Compartido().Dame_K2())
    if "K" in session.keys():
        fernet = Fernet(session["K"])
    Cur = ""
    try:
        Compartido = LibDM_2023.Compartido()
        Contenido = ""
        if "IDu" not in session.keys():
            Contenido += """
            <body style='height:90%;'>
                <div class='w-100 h-100 position-relative'>
                    <div id='Pag' class='container-fluid pb-5'>
                        <div>
                            <img width='100%' height='auto'  id='Logo_Universal' src='' class='position-absolute top-50 start-50 translate-middle' style='opacity:0.05'></img>
                            
                            <div id='Formulario' class='position-absolute top-50 start-50 translate-middle w-100'>
                                <div class='w-100 text-center row' >
                                <div class='col display-3 fst-italic fw-bold text-nowrap'><i class="mdi mdi-chevron-double-right " style="color:#ED1C24"></i>Scan <span style="color:#ED1C24">U</span></div>
                                </div>

                                <div class='p-3 m-2'>
                                <div class="mb-3">
                                    <label class="form-label"><i class='mdi mdi-account-circle'></i> User</label>
                                    <input type="text" class="form-control focus-ring focus-ring-danger" id='User'>
                                </div>

                                <div class="mb-3">
                                    <label class="form-label"><i class='mdi mdi-form-textbox-password'></i> Password</label>
                                    <input type="password" class="form-control focus-ring focus-ring-danger" id='Pwr'>
                                </div>

                                <div id='Error' class='m-1 p-1 bg-danger p-2 text-white text-center fw-bold' style='display:none;'>
                                    Add User,Email / Password. Please.
                                </div>
                                <hr>
                                <button class="btn btn-lg btn-dark w-100 fw-bold" type="button" onclick='Entrar()'>Sing In <i class="mdi mdi-chevron-double-right " style="color:#ED1C24"></i></button>

                                </div>

                                
                            </div>
                            
                        </div>
                    </div>
                </div>
            </body>

            <script>
                $('#User').focus();
                function Entrar()
                {
                    $("#Error").hide();
                    if($("#User").val().trim() == ""){
                        $("#Error").html('Add User / Password.')
                        $("#Error").show();
                    }
                    else{
                        Mostrar_Ventana_Cargando(false);
                        var parametros = {"Fun":'"""+str(fernet.encrypt("Entrar".encode()).decode("utf-8"))+"""',"Usuario":$("#User").val().trim(),"Pass":$("#Pwr").val().trim()};
                        $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                            success:  function (response)
                            {
                                var Resultado = JSON.parse(response);
                                if(Resultado["Estado"] == 1)
                                {
                                    window.location.reload();
                                }
                                else
                                {
                                    $("#Error").html('Add User,Email / Password.')
                                    $("#Error").show();
                                    swal.close();
                                }
                            },
                            error: function (jqXHR, textStatus, errorThrown )
                            {
                                $("#Error").html('Error ['+textStatus+']')
                                $("#Error").show();
                                swal.close();
                            }
                        });
                    }   
                }
                $('#User').keypress(function(event){
                    var keycode = (event.keyCode ? event.keyCode : event.which);
                    if(keycode == '13'){
                        Entrar();
                    }
                });
            </script>
            """
        else:
            Contenido += """
            <body style='height:90%;'>
                <div class='w-100 h-100 position-relative'>
                    <div style='color: #ebebeb; text-shadow: -1px 0 #8f8f8f, 0 1px #bbbbbb, 1px 0 #8f8f8f, 0 -1px #bbbbbb;' class="fw-bold position-absolute top-50 start-50 translate-middle display-1 z-n1" id='Titulo'>"""+str(Menu_Activo)+"""</div>
                    <div id='Pag' class='container-fluid pb-5'>
                    </div>
                </div>
                <script>
                    $( document ).ready(function() {
                        setInterval(Actualizar_Hora_Final, 500)
                        Docks();
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
                    function Docks(){
                        Mostrar_Ventana_Cargando(false);
                        var parametros = {"Fun":'"""+str(fernet.encrypt("Docks".encode()).decode("utf-8"))+"""'};
                        $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                            success:  function (response)
                            {
                                var Resultado = JSON.parse(response);
                                $("#Pag").html(Resultado["Contenido"]);
                                swal.close();
                            },
                            error: function (jqXHR, textStatus, errorThrown )
                            {
                                $("#Pag").html("<i class='mdi mdi-alert'></i> "+ textStatus);
                                swal.close();
                            }
                        });
                    }
                </script>
            </body>
            """
        Cur += render_template("general_APP.html",Contenido=Contenido,Componentes=Compartido.Complementos(None),Menu="",Titulo=str(Menu_Activo))
    except:
        Cur += str(sys.exc_info())
    return Cur
def Entrar(Datos):
    Cur = ""
    DB = LibDM_2023.DataBase()
    Resultado = {"Estado":0, "Contenido":""}
    try:
        Res = DB.Get_Dato("SELECT * FROM universal_yms.cuser WHERE UPPER(cususuario) = '"+str(Datos["Usuario"]).upper()+"' or UPPER(cuscorreo) = '"+str(Datos["Usuario"]).upper()+"' AND cpss_2 = '"+str(hashlib.md5(str(Datos["Pass"]).encode('utf-8')).hexdigest())+"'")
        if len(Res) > 0:
            Resultado["Estado"] = 1
            session["IDu"] = str(Res[0]["cusrid"])
            session["K"] = str(Fernet.generate_key().decode())
        #Resultado["Contenido"] = str(Datos)
    except:
        Resultado["Contenido"] = str(sys.exc_info())
    Cur += json.dumps(Resultado)
    return Cur
def Docks(Datos):
    if "K" in session.keys():
        fernet = Fernet(session["K"])
    DB = LibDM_2023.DataBase()
    Compartido_2023 = LibDM_2023.Compartido()
    Cur = ""
    Resultado = {"Contenido":"","Estado":0}
    try:
        Resultado["Contenido"] += """
        <div class='text-center display-5 fw-bold'>"""+str(Menu_Activo)+"""</div>
            <div class='row'>
                <div class='col'>
                    <button class='btn btn-primary w-100 fw-bold mb-2' onclick='Docks()'>UPDATE</button>
                </div>
                <div class='col'>
                    <button class='btn btn-danger w-100 fw-bold mb-2' onclick='Cerrar_Sesion()'>SIGN OUT</button>
                </div>
            </div>
            
            <div class='row'>
        """
        Cajas_Docks = DB.Get_Dato("SELECT * FROM "+str(BaseDatos)+".ccajas WHERE cc_dock IS NOT NULL AND cc_activo = 1 ")
        for Dock in DB.Get_Dato("SELECT * FROM "+str(BaseDatos)+".cdock_asignacion WHERE cd_ub = '"+str(Bandera_Docks)+"' AND cd_activo = 1"):
            Caja_Aqui = None
            Color = "#ffffff"
            for C in Cajas_Docks:
                if int(C["cc_dock"]) == int(Dock["cd_dock"]):
                    Caja_Aqui = C
                    Color = "#88ffa0"
                    break
            
            if Caja_Aqui is not None:
                Info_Actual = json.loads(str(Caja_Aqui["cc_informacion_actual"]))
                Resultado["Contenido"] += """
                <div class='col-6 p-1' onclick='Opciones("""+str(Caja_Aqui["cc_id"])+""",\""""+str(Caja_Aqui["cc_contenedor"])+"""\")'><div class='h-100 border border-dark ps-3 pe-3 pt-1 pb-1'>
                    <div class='row h-100 ' style='background:"""+str(Color)+"""' >
                        <div class='col-auto bg-dark text-white fs-1'>
                            """+str(Dock["cd_dock"])+"""
                        </div>
                        <div class='col'>
                """
            else:
                Resultado["Contenido"] += """
                <div class='col-6 p-1' onclick='Dock("""+str(Dock["cd_dock"])+""")'><div class='h-100 border border-dark ps-3 pe-3 pt-1 pb-1'>
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
                Resultado["Contenido"] += "<div class='border-bottom border-dark text-center fw-bold'>"+str(Caja_Aqui["cc_contenedor"])+"</div>"
                Resultado["Contenido"] += "<div class='text-center'>"+str(Caja_Aqui["cc_tipo_actual"])+"</div>"
                Resultado["Contenido"] += "<div class='text-center'><small>"+str(Estado)+"</small></div>"
                Resultado["Contenido"] += "<div class='text-center'><small class='tiempo' tiempo='"+str(Caja_Aqui["cc_ultimo_mov"])+"'></small></div>"
            Resultado["Contenido"] += """
                    </div>
                </div>
                
            </div></div>
            """
        Resultado["Contenido"] += """
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
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm')
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
            function Cerrar_Sesion(){
                    Swal.fire({
                        title: 'Are you sure you want to log out?',
                        buttonsStyling: false,showCancelButton: true,confirmButtonText: "<i class='mdi mdi-check'></i> Si",cancelButtonText: "<i class='mdi mdi-close'></i> No",showLoaderOnConfirm: true,
                        customClass: {confirmButton: 'btn btn-success ms-1 me-1',cancelButton: 'btn btn-danger ms-1 me-1'},
                        preConfirm: () => {
                            Mostrar_Ventana_Cargando(false);
                            var parametros = {"Fun":'"""+str(fernet.encrypt("Cerrar_Sesion".encode()).decode("utf-8"))+"""'};
                            $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                                success:  function (response)
                                {
                                    window.location.reload();
                                },
                                error: function (jqXHR, textStatus, errorThrown ){Mensaje(0,'Process error ['+ jqXHR.status + " | " + textStatus  + " | " + errorThrown +']');}
                            });
                        }
                    })
                }
            function Llamar_Funcion(Direccion,Mensaje=null,P=null){
                Mostrar_Ventana_Cargando(false);
                setTimeout(function(){ window.location.href = \""""+str(request.url)+"""\" },500);
            }
        </script>
        """
    except:
        Resultado["Contenido"] = str(sys.exc_info())
    Cur += json.dumps(Resultado)
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
        Contenedores_Patio = DB.Get_Dato("SELECT * FROM "+str(BaseDatos)+".ccajas where cc_activo = 1 AND cc_caja_danada = 0 AND cc_bloqueo_rg = 0 AND cc_ubicacion = 'Patio' and cc_tipo_actual is not null")
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
                    {field:"Ruta","title":"Route",formatter:"html"},
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
        Caja = DB.Get_Dato("SELECT * FROM "+str(BaseDatos)+".ccajas WHERE cc_id = '"+str(Datos["ID"])+"'")[0]
        Info_Nueva = json.loads(str(Caja["cc_informacion_actual"]))
        Ubicacion = "Dock"
        Dock = "'"+str(Datos["Dock"])+"'"
        Info_Nueva["Dock"] = str(Datos["Dock"])
        Info_Nueva["Fotos"] = Info_Datos["Fotos"]
        Error = DB.Instruccion("UPDATE "+str(BaseDatos)+".ccajas SET cc_informacion_actual = '"+str(json.dumps(Info_Nueva))+"',cc_ultimo_mov = NOW(),cc_dock= "+str(Dock)+",cc_ubicacion = '"+str(Ubicacion)+"' WHERE cc_id = '"+str(Datos["ID"])+"' ")
        if Error == "":
            Info_Ahora = DB.Get_Dato("SELECT * FROM "+str(BaseDatos)+".ccajas WHERE cc_id = '"+str(Datos["ID"])+"'")[0]
            Info_Ahora["cc_dock"] = 'null' if Info_Ahora["cc_dock"] is None else "'"+str(Info_Ahora["cc_dock"])+"'"
            Info_Ahora["cc_tipo_actual"] = 'null' if Info_Ahora["cc_tipo_actual"] is None else "'"+str(Info_Ahora["cc_tipo_actual"])+"'"
            Info_Ahora["cc_zona"] = 'null' if Info_Ahora["cc_zona"] is None else "'"+str(Info_Ahora["cc_zona"])+"'"
            Info_Ahora["cc_negocio"] = 'null' if Info_Ahora["cc_negocio"] is None else "'"+str(Info_Ahora["cc_negocio"])+"'"
            Error = DB.Instruccion(""" 
            INSERT INTO """+str(BaseDatos)+""".ccajas_moviemiento
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
def Cerrar_Sesion(Datos):
    DB = LibDM_2023.DataBase()
    Compartido_2023 = LibDM_2023.Compartido()
    Cur = ""
    Resultado = {"Contenido":"","Estado":0}
    try:
        try:
            session.clear
            session.pop("IDu")
            session.pop("K")
        except:
            pass
    except:
        Resultado["Contenido"] = str(sys.exc_info())
    Cur += json.dumps(Resultado)
    return Cur
def Direccionar(Datos):
    try:
        fernet = Fernet(LibDM_2023.Compartido().Dame_K2())
        if "K" in session.keys():
            fernet = Fernet(session["K"])
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
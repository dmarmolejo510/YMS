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
Menu_Activo = "RILC TOLUCA"

def Inicio():
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
                    <div style='color: #ebebeb; text-shadow: -1px 0 #8f8f8f, 0 1px #bbbbbb, 1px 0 #8f8f8f, 0 -1px #bbbbbb;' class="fw-bold position-absolute top-50 start-50 translate-middle display-1 z-n1" id='Titulo'>"""+str(Menu_Activo)+"""</div>
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
                                if(response*1 == 0){
                                    $("#Error").html('User or Password is incorrect, try again.')
                                    $("#Error").show();
                                    swal.close();
                                }
                                if(response*1 == 1){
                                    $(location).attr('href','YMS/App/Inicio');
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
                            var Ahora = moment(new Date()); //todays date
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
                        var parametros = {"Fun":"Docks"};
                        $.ajax({data:  parametros,url:\""""+str(os.path.basename(__file__))+"""\",type:  "post",
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
        Cur += render_template("general_APP.html",Contenido=Contenido,Componentes=Compartido.Complementos(None),Menu="",Titulo="")
    except:
        Cur += str(sys.exc_info())
    return Cur
def Entrar(Datos):
    Cur = ""
    DB = LibDM_2023.DataBase()
    Resultado = {"Estado":0, "Contenido":""}
    try:
        Res = DB.Get_Dato("SELECT * FROM public.cuser WHERE UPPER(cususuario) = '"+str(Datos["Usuario"]).upper()+"' or UPPER(cuscorreo) = '"+str(Datos["Usuario"]).upper()+"' AND cpss_2 = '"+str(hashlib.md5(str(Datos["Pass"]).encode('utf-8')).hexdigest())+"'")
        if len(Res) > 0:
            Resultado["Estado"] = 1
            session["IDu"] = str(Res[0]["cusrid"])
            session["K"] = str(Fernet.generate_key().decode())
        #Resultado["Contenido"] = str(Datos)
    except:
        Resultado["Contenido"] = str(sys.exc_info())
    Cur += json.dumps(Resultado)
    return Cur


# def Inicio_old(Datos):
#     try:
#         Compartido = LibDM_2023.Compartido()
#         Cur = "content-type: text/html;charset=ISO-8859-1\n\n"
#         Cur += """
#         <!DOCTYPE html>
#         <html class='h-100 w-100'>
#             <head>
#                 <meta name="viewport" content="width=device-width, initial-scale=1">
#                 <title>APP MX ["""+str(Menu_Activo)+"""]</title>
#         """
#         Cur += str(Compartido.Complementos("../../",["07","15","04"]))
#         Cur += """
#             </head>
#             <body style='height:90%;'>
#         """
#         Cur += """
#                 <div class='w-100 h-100 position-relative'>
#                     <div style='color: #ebebeb; text-shadow: -1px 0 #8f8f8f, 0 1px #bbbbbb, 1px 0 #8f8f8f, 0 -1px #bbbbbb;' class="fw-bold position-absolute top-50 start-50 translate-middle display-1 z-n1" id='Titulo'>"""+str(Menu_Activo)+"""</div>
#                     <div id='Pag' class='container-fluid pb-5'>
#                     </div>
#                 </div>
#                 <script>
#                     $( document ).ready(function() {
#                         setInterval(Actualizar_Hora_Final, 500)
#                         Docks();
#                     });
#                     function Actualizar_Hora_Final()
#                     {
#                         $(".tiempo").each(function() {
#                             var Limite = moment($(this).attr('tiempo'));
#                             var Ahora = moment(new Date()); //todays date
#                             var Faltan = moment.duration(Ahora.diff(Limite));
#                             var Dias = Faltan.asDays().toString().split(".")[0];
#                             var Horas = Faltan.hours();
#                             if(Horas.toString().length == 1)
#                                 Horas = "0"+Horas;
#                             var Minutos = Faltan.minutes();
#                             if(Minutos.toString().length == 1)
#                                 Minutos = "0"+Minutos;
#                             var Segundos = Faltan.seconds();
#                             if(Segundos.toString().length == 1)
#                                 Segundos = "0"+Segundos;
#                             if (Dias == 0)
#                                 $(this).html("<b>" + Horas +":" + Minutos +":"+ Segundos +"</b>")
#                             else
#                                 $(this).html("<b>" + Dias + " Days, " + Horas +":" + Minutos +":"+ Segundos +"</b>")

#                         });
#                     }
#                     function Docks(){
#                         Mostrar_Ventana_Cargando(false);
#                         var parametros = {"Fun":"Docks"};
#                         $.ajax({data:  parametros,url:\""""+str(os.path.basename(__file__))+"""\",type:  "post",
#                             success:  function (response)
#                             {
#                                 var Resultado = JSON.parse(response);
#                                 $("#Pag").html(Resultado["Contenido"]);
#                                 swal.close();
#                             },
#                             error: function (jqXHR, textStatus, errorThrown )
#                             {
#                                 $("#Pag").html("<i class='mdi mdi-alert'></i> "+ textStatus);
#                                 swal.close();
#                             }
#                         });
#                     }
#                 </script>
#             </body>
#         </html>
#         """
#     except:
#         Cur = "content-type: text/html;charset=ISO-8859-1\n\n "
#         Cur += str(sys.exc_info())
#     print(Cur)
# def Docks(Datos):
#     DB = LibDM_2023.DataBase()
#     Compartido_2023 = LibDM_2023.Compartido()
#     Cur = "content-type: text/html;charset=ISO-8859-1\n\n "
#     Resultado = {"Contenido":"","Estado":0}
#     try:
#         Resultado["Contenido"] += """
#         <div class='text-center display-5 fw-bold'>"""+str(Menu_Activo)+"""</div>
#             <div class='row'>
#                 <div class='col'>
#                     <button class='btn btn-primary w-100 fw-bold mb-2' onclick='Docks()'>ACTUALIZAR</button>
#                 </div>
#                 <div class='col'>
#                     <button class='btn btn-danger w-100 fw-bold mb-2' onclick='Cerrar_Sesion()'>CERRAR SESION</button>
#                 </div>
#             </div>
            
#             <div class='row'>
#         """
#         Cajas_Docks = DB.Get_Dato("SELECT * FROM rilc_toluca.ccajas WHERE cc_dock IS NOT NULL AND cc_activo = 1 ")
#         for Dock in DB.Get_Dato("SELECT * FROM rilc_toluca.cdock_asignacion WHERE cd_ub = 'RILC Toluca' AND cd_activo = 1"):
#             Caja_Aqui = None
#             Color = "#ffffff"
#             for C in Cajas_Docks:
#                 if int(C["cc_dock"]) == int(Dock["cd_dock"]):
#                     Caja_Aqui = C
#                     Color = "#88ffa0"
#                     break
            
#             if Caja_Aqui is not None:
#                 Info_Actual = json.loads(str(Caja_Aqui["cc_informacion_actual"]))
#                 Resultado["Contenido"] += """
#                 <div class='col-6 p-1' onclick='Opciones("""+str(Caja_Aqui["cc_id"])+""",\""""+str(Caja_Aqui["cc_contenedor"])+"""\")'><div class='h-100 border border-dark ps-3 pe-3 pt-1 pb-1'>
#                     <div class='row h-100 ' style='background:"""+str(Color)+"""' >
#                         <div class='col-auto bg-dark text-white fs-1'>
#                             """+str(Dock["cd_dock"])+"""
#                         </div>
#                         <div class='col'>
#                 """
#             else:
#                 Resultado["Contenido"] += """
#                 <div class='col-6 p-1' onclick='Dock("""+str(Dock["cd_dock"])+""")'><div class='h-100 border border-dark ps-3 pe-3 pt-1 pb-1'>
#                     <div class='row h-100 ' style='background:"""+str(Color)+"""' >
#                         <div class='col-auto bg-dark text-white fs-1'>
#                             """+str(Dock["cd_dock"])+"""
#                         </div>
#                         <div class='col'>
#                 """
#             if Caja_Aqui is not None:
#                 pass
#                 Info_Actual = json.loads(str(Caja_Aqui["cc_informacion_actual"]))
#                 Estado = ""
#                 Estado += "<span class='h-100' style='width:20px; background:var(--Color_"+str(Caja_Aqui["cc_tipo_actual"])+");Color:var(--Color_"+str(Caja_Aqui["cc_tipo_actual"])+");'>__</span>"
#                 try:
#                     Tipo = Info_Actual[Caja_Aqui["cc_tipo_actual"]]
#                     Estado += str(Tipo)
#                     Tipo_1 = Info_Actual[Tipo]
#                     Estado += "/"+str(Tipo_1)
#                     Tipo_2 = Info_Actual[Tipo_1]
#                     Estado += "/"+str(Tipo_2)
#                 except:
#                     pass
#                 Resultado["Contenido"] += "<div class='border-bottom border-dark text-center fw-bold'>"+str(Caja_Aqui["cc_contenedor"])+"</div>"
#                 Resultado["Contenido"] += "<div class='text-center'>"+str(Caja_Aqui["cc_tipo_actual"])+"</div>"
#                 Resultado["Contenido"] += "<div class='text-center'><small>"+str(Estado)+"</small></div>"
#                 Resultado["Contenido"] += "<div class='text-center'><small class='tiempo' tiempo='"+str(Caja_Aqui["cc_ultimo_mov"])+"'></small></div>"
#             Resultado["Contenido"] += """
#                     </div>
#                 </div>
                
#             </div></div>
#             """
#         Resultado["Contenido"] += """
#             </div>
#         </div>
#         <script>
#             function Opciones(ID,Contenedor){
#                 Mostrar_Ventana_Cargando(false);
#                 $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-menu'></i> Options ["+Contenedor+"]");
#                 $("#Vent_1").removeClass('modal-xl modal-lg modal-sm')
#                 var parametros = {"Fun":"Opciones","ID":ID};
#                 $.ajax({data:  parametros,url:\""""+str(os.path.basename(__file__))+"""\",type:  "post",
#                     success:  function (response)
#                     {
#                         var Resultado = JSON.parse(response);
#                         $("#Vent_1").modal("show").find(".modal-body").html(Resultado["Contenido"]);
#                         $("#Vent_1").find(".modal-footer").find("button").attr('onclick',"$('#Vent_1').modal('hide'); delete table; ")
#                         swal.close();
#                     },
#                     error: function (jqXHR, textStatus, errorThrown )
#                     {
#                         $("#Vent_1").modal("show").find(".modal-body").html("<i class='mdi mdi-alert'></i> "+ textStatus);
#                         swal.close();
#                     }
#                 });
#             }
#             function Dock(Dock){
#                 Mostrar_Ventana_Cargando(false);
#                 $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-menu'></i> Dock ["+Dock+"]");
#                 $("#Vent_1").removeClass('modal-xl modal-lg modal-sm')
#                 var parametros = {"Fun":"Dock","Dock":Dock};
#                 $.ajax({data:  parametros,url:\""""+str(os.path.basename(__file__))+"""\",type:  "post",
#                     success:  function (response)
#                     {
#                         var Resultado = JSON.parse(response);
#                         $("#Vent_1").modal("show").find(".modal-body").html(Resultado["Contenido"]);
#                         $("#Vent_1").find(".modal-footer").find("button").attr('onclick',"$('#Vent_1').modal('hide'); delete table; ")
#                         swal.close();
#                     },
#                     error: function (jqXHR, textStatus, errorThrown )
#                     {
#                         $("#Vent_1").modal("show").find(".modal-body").html("<i class='mdi mdi-alert'></i> "+ textStatus);
#                         swal.close();
#                     }
#                 });
#             }
#             function Cerrar_Sesion(){
#                     Swal.fire({
#                         title: 'Seguro que quiere salir?',
#                         buttonsStyling: false,showCancelButton: true,confirmButtonText: "<i class='mdi mdi-check'></i> Si",cancelButtonText: "<i class='mdi mdi-close'></i> No",showLoaderOnConfirm: true,
#                         customClass: {confirmButton: 'btn btn-success ms-1 me-1',cancelButton: 'btn btn-danger ms-1 me-1'},
#                         preConfirm: () => {
#                             Mostrar_Ventana_Cargando(false);
#                             var parametros = {"Fun":"Cerrar_Sesion"};
#                             $.ajax({data:  parametros,url:\""""+str(os.path.basename(__file__))+"""\",type:  "post",
#                                 success:  function (response)
#                                 {
#                                     window.location.href = "inicio.py";
#                                 },
#                                 error: function (jqXHR, textStatus, errorThrown ){Mensaje(0,'Process error ['+ jqXHR.status + " | " + textStatus  + " | " + errorThrown +']');}
#                             });
#                         }
#                     })
#                 }
#         </script>
#         """
#     except:
#         Resultado["Contenido"] = str(sys.exc_info())
#     Cur += json.dumps(Resultado)
#     print(Cur)
# def Dock(Datos):
#     DB = LibDM_2023.DataBase()
#     Compartido_2023 = LibDM_2023.Compartido()
#     Cur = "content-type: text/html;charset=ISO-8859-1\n\n "
#     Resultado = {"Contenido":"","Estado":0}
#     try:
#         Patio = []
#         Contenedores_Patio = DB.Get_Dato("SELECT * FROM rilc_toluca.ccajas where cc_activo = 1 AND cc_caja_danada = 0 AND cc_bloqueo_rg = 0 AND cc_ubicacion = 'Patio' and cc_tipo_actual is not null")
#         Patio = []
#         for Contenedor in Contenedores_Patio:
#             Opciones = "<div class='btn-group' role='group' aria-label='Basic mixed styles example'>"
#             Info_Actual = json.loads(str(Contenedor["cc_informacion_actual"]))
#             if int(Contenedor["cc_bloquear"]) == 0:
#                 Opciones += "<button class='btn btn-sm btn-warning p-0 ps-1 pe-1' onclick='Mover_a_Dock("+str(Contenedor["cc_id"])+",\""+str(Contenedor["cc_contenedor"])+"\","+str(Datos["Dock"])+")'><i class='mdi mdi-download'></i></button>"
#             else:
#                 Opciones += "<span class='ms-1 me-1'><i class='mdi mdi-lock'></i></span>"

#             Sello = ""
#             if "Sello Proveedor" in Info_Actual.keys():
#                 Sello = "<span style='color:blue'><i class='mdi mdi-label'></i></span> "+str(Info_Actual["Sello Proveedor"])
#             if "Sello Temporal" in Info_Actual.keys():
#                 Sello = "<span style='color:#7a7a7a'><i class='mdi mdi-label'></i></span> "+str(Info_Actual["Sello Temporal"])
#             if "Sello Blanco" in Info_Actual.keys():
#                 Sello = "<span><i class='mdi mdi-label-outline'></i></span> "+str(Info_Actual["Sello Temporal"])
#             if "Sello Rojo" in Info_Actual.keys():
#                 Sello = "<span style='color:#ff0000'><i class='mdi mdi-label'></i></span> "+str(Info_Actual["Sello Temporal"])

#             Ruta = ""
#             Ruta += "<span class='h-100 border' style='width:20px; background:var(--Color_"+str(Contenedor["cc_tipo_actual"])+");Color:var(--Color_"+str(Contenedor["cc_tipo_actual"])+");'>__</span>"
#             try:
#                 Tipo = Info_Actual[Contenedor["cc_tipo_actual"]]
#                 Ruta += str(Tipo)
#                 Tipo_1 = Info_Actual[Tipo]
#                 Ruta += "/"+str(Tipo_1)
#                 Tipo_2 = Info_Actual[Tipo_1]
#                 Ruta += "/"+str(Tipo_2)
#             except:
#                 pass

#             Estado = ""
#             if "Etapa" not in Info_Actual.keys():
#                 Estado = "Waiting"
#             else:
#                 Estado = Info_Actual["Etapa"]

#             Opciones += "</div>"
#             Patio.append({"Tiempo":"<span class='tiempo' tiempo='"+str(Contenedor["cc_ultimo_mov"])+"'></span>","Caja":str(Contenedor["cc_contenedor"]),"Carrier":Info_Actual["Carrier"],"Tipo":Contenedor["cc_tipo_actual"],"Estado":str(Estado),"Sello":Sello,"Ruta":Ruta,"Opciones":"<div class='text-center'>"+str(Opciones)+"</div>"})

#         Resultado["Contenido"] += """
#         <div class='h3 text-center'><i class='mdi mdi-car-brake-parking'></i> Patio</div>
#         <div id='Tabla_Patio' class='border border-dark bg-dark-subtle'></div>
#         <script>
#             delete Tabla_Patio;
#             var Tabla_Patio = new Tabulator("#Tabla_Patio", {
#                 minHeight:800,
#                 layout:"fitColumns",
#                 data:"""+str(Patio)+""",
#                 columns:[
#                     {field:"Caja","title":"Container",headerFilter:"input"},
#                     /*{field:"Carrier","title":"Carrier"},*/
#                     {field:"Tipo","title":"Type"},
#                     {field:"Ruta","title":"Ruta",formatter:"html"},
#                     {field:"Estado","title":"Status"},
#                     {field:"Opciones","title":"Op",formatter:"html"}
#                 ]
#             });
#             Tabla_Patio.on("tableBuilt", function(){ 
#                 setTimeout(() => {
#                     Tabla_Patio.clearFilter();
#                     Tabla_Patio.redraw();
#                 }, 100);
#             });

#             function Mover_a_Dock(ID,Contenedor,Dock){
#                 Mostrar_Ventana_Cargando(false);
#                 $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-history'></i> Mover ["+Contenedor+"] al Dock ["+Dock+"]");
#                 $("#Vent_1").removeClass('modal-xl modal-lg modal-sm').addClass('modal-xl');
#                 var parametros = {"Fun":"Mover_a_Dock","ID":ID,"Dock":Dock};
#                 $.ajax({data:  parametros,url:\""""+str(os.path.basename(__file__))+"""\",type:  "post",
#                     success:  function (response)
#                     {
#                         var Resultado = JSON.parse(response);
#                         $("#Vent_1").modal("show").find(".modal-body").html(Resultado["Contenido"]);
#                         $("#Vent_1").find(".modal-footer").find("button").attr('onclick',"$('#Vent_1').modal('hide'); delete table; ")
#                         swal.close();
#                     },
#                     error: function (jqXHR, textStatus, errorThrown )
#                     {
#                         $("#Vent_1").modal("show").find(".modal-body").html("<i class='mdi mdi-alert'></i> "+ textStatus);
#                         swal.close();
#                     }
#                 });
#             }
#         </script>
#         """
#     except:
#         Resultado["Contenido"] = str(sys.exc_info())
#     Cur += json.dumps(Resultado)
#     print(Cur)
# def Mover_a_Dock(Datos):
#     DB = LibDM_2023.DataBase()
#     Compartido_2023 = LibDM_2023.Compartido()
#     Cur = "content-type: text/html;charset=ISO-8859-1\n\n "
#     Resultado = {"Contenido":"","Estado":0}
#     try:
#         Formulario = {"Col":"12", "Campos": [],"Clase": "Mover_Dock" }
#         Formulario["Campos"].append({"tipo":"archivo","campo":"Fotos","titulo":"Photos","Requerido":1,"Col":12,"min":1,"max":5,"tipo_archivo":["image/*"],"valor":""})
#         Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
#         Resultado["Contenido"] += """
#         <hr>
#         <div class='w-100 text-center'><button class='btn btn-success w-75' onclick='Mover_a_Dock_Guardar(\""""+str(Datos["ID"])+"""\",\""""+str(Datos["Dock"])+"""\")'><i class='mdi mdi-floppy'></i> Save</button></div>
#         <script>
#             function Mover_a_Dock_Guardar(ID,Dock){
#                 var Info = Dame_Formulario(".Mover_Dock",true);
#                 if(Info != null)
#                 {
#                     Mostrar_Ventana_Cargando(false);
#                     var parametros = {"Fun":"Mover_a_Dock_Guardar","Info":JSON.stringify(Info),"ID":ID,"Dock":Dock};
#                     $.ajax({data:  parametros,url:\""""+str(os.path.basename(__file__))+"""\",type:  "post",
#                         success:  function (response)
#                         {
#                             var Resultado = JSON.parse(response);
#                             if(Resultado["Estado"] == 1)
#                             {
#                                 if("Pase Salida" in Resultado)
#                                 {
#                                     var win1 = window.open(Resultado["Pase Salida"], '_blank');
#                                     win1.focus();
#                                 }
#                                 $("#Vent_1").modal("hide");
#                                 Mensaje(2);
#                                 Docks();
#                             }
#                             else
#                                 Mensaje(0,Resultado["Contenido"]);
                                
#                         },
#                         error: function (jqXHR, textStatus, errorThrown )
#                         {
#                             Mensaje(0,textStatus);
#                         }
#                     });
#                 }
#             }
#         </script>
#         """
#     except:
#         Resultado["Contenido"] = str(sys.exc_info())
#     Cur += json.dumps(Resultado)
#     print(Cur)
# def Mover_a_Dock_Guardar(Datos):
#     DB = LibDM_2023.DataBase()
#     Compartido_2023 = LibDM_2023.Compartido()
#     Cur = "content-type: text/html;charset=ISO-8859-1\n\n "
#     Resultado = {"Contenido":"","Estado":0}
#     try:
#         Info_Datos = json.loads(str(Datos["Info"]))
#         Caja = DB.Get_Dato("SELECT * FROM rilc_toluca.ccajas WHERE cc_id = '"+str(Datos["ID"])+"'")[0]
#         Info_Nueva = json.loads(str(Caja["cc_informacion_actual"]))
#         Ubicacion = "Dock"
#         Dock = "'"+str(Datos["Dock"])+"'"
#         Info_Nueva["Dock"] = str(Datos["Dock"])
#         Info_Nueva["Fotos"] = Info_Datos["Fotos"]
#         Error = DB.Instruccion("UPDATE rilc_toluca.ccajas SET cc_informacion_actual = '"+str(json.dumps(Info_Nueva))+"',cc_ultimo_mov = NOW(),cc_dock= "+str(Dock)+",cc_ubicacion = '"+str(Ubicacion)+"' WHERE cc_id = '"+str(Datos["ID"])+"' ")
#         if Error == "":
#             Info_Ahora = DB.Get_Dato("SELECT * FROM rilc_toluca.ccajas WHERE cc_id = '"+str(Datos["ID"])+"'")[0]
#             Info_Ahora["cc_dock"] = 'null' if Info_Ahora["cc_dock"] is None else "'"+str(Info_Ahora["cc_dock"])+"'"
#             Info_Ahora["cc_tipo_actual"] = 'null' if Info_Ahora["cc_tipo_actual"] is None else "'"+str(Info_Ahora["cc_tipo_actual"])+"'"
#             Info_Ahora["cc_zona"] = 'null' if Info_Ahora["cc_zona"] is None else "'"+str(Info_Ahora["cc_zona"])+"'"
#             Info_Ahora["cc_negocio"] = 'null' if Info_Ahora["cc_negocio"] is None else "'"+str(Info_Ahora["cc_negocio"])+"'"
#             Error = DB.Instruccion(""" 
#             INSERT INTO rilc_toluca.ccajas_moviemiento
#             (cch_master,cch_fecha_hora,cch_contenedor,cch_ubicacion,cch_informacion_actual,cch_dock,cch_tipo_actual,cch_zona,cch_negocio,cch_usuario,cch_movimiento)
#             VALUES
#             ('"""+str(Info_Ahora["cc_id"])+"""',NOW(),'"""+str(Info_Ahora["cc_contenedor"])+"""','"""+str(Info_Ahora["cc_ubicacion"])+"""','"""+str(Info_Ahora["cc_informacion_actual"])+"""',"""+str(Info_Ahora["cc_dock"])+""","""+str(Info_Ahora["cc_tipo_actual"])+""","""+str(Info_Ahora["cc_zona"])+""","""+str(Info_Ahora["cc_negocio"])+""",'"""+str(Datos["ID_User"])+"""','MODIFICAR')
#             """)
#             if Error == "":
#                 Resultado["Estado"] = 1
#             else:
#                 Resultado["Contenido"] = Error
#         else:
#             Resultado["Contenido"] += str(Error)
#     except:
#         Resultado["Contenido"] = str(sys.exc_info())
#     Cur += json.dumps(Resultado)
#     print(Cur)

# def Opciones(Datos):
#     DB = LibDM_2023.DataBase()
#     Compartido_2023 = LibDM_2023.Compartido()
#     Cur = "content-type: text/html;charset=ISO-8859-1\n\n "
#     Resultado = {"Contenido":"","Estado":0}
#     try:
#         Caja = DB.Get_Dato("SELECT * FROM rilc_toluca.ccajas WHERE cc_id = '"+str(Datos["ID"])+"'")[0]
#         Info_Actual = json.loads(str(Caja["cc_informacion_actual"]))
#         De_Donde = Caja["cc_ubicacion"]
#         if Caja["cc_tipo_actual"] == "Inbound":
#             Resultado["Contenido"] = """
#             <div>Opciones de Contenedor/Caja</div>
#             <div class='row'>
#                 <div class='col-12 p-1'>
#                     <button class='btn btn-dark w-100 btn-lg' onclick='Modificar_A("Ready to Load","","""+str(Datos["ID"])+""");'><div>Empty [Ready to Load]</div><div><small>(Dejar caja en Dock)</small></div></button>
#                 </div>
#                 <div class='col-12 p-1'>
#                     <button class='btn btn-dark w-100 btn-lg' onclick='Modificar_A("Ready to Load","Patio","""+str(Datos["ID"])+""");'><div>Empty [Ready to Load]</div><div><small>(Mover caja a patio)</small></div></button>
#                 </div>
#                 <div class='col-12 p-1'>
#                     <button class='btn btn-dark w-100 btn-lg' onclick='Modificar_A("Return Empty","Patio","""+str(Datos["ID"])+""");'><div>Empty [Return empty]</div><div><small>(Mover caja a patio <span class='text-danger fw-bold'>LISTA PARA SALIR</span>)</small></div></button>
#                 </div>
#                 <div class='col-12 p-1'>
#                     <button class='btn btn-primary w-100 btn-lg' onclick='Modificar_A("Inbound","Patio","""+str(Datos["ID"])+""");'><div>Inbound</div><div><small>(Mover caja a patio <span class='text-warning fw-bold'>CAJA AUN CON MATERIAL DE PROVEEDOR</span>)</small></div></button>
#                 </div>
#                 <div class='col-12 p-1'>
#                     <button class='btn btn-info w-100 btn-lg' onclick='Evidencia("""+str(Datos["ID"])+""");'><div> Add evidence </div><div><small></small></div></button>
#                 </div>
#             </div>
#             <div>Opciones de Material</div>
#             <div class='row'>
#                 <div class='col-6 p-1'>
#                     <button class='btn btn-warning w-100 btn-lg' onclick='Generar_OSyD("Exceso de Material","""+str(Datos["ID"])+""")'>Exceso de Material</button>
#                 </div>
#                 <div class='col-6 p-1'>
#                     <button class='btn btn-warning w-100 btn-lg' onclick='Generar_OSyD("Faltante de Material","""+str(Datos["ID"])+""")'>Faltante de Material</button>
#                 </div>
#                 <div class='col-6 p-1'>
#                     <button class='btn btn-warning w-100 btn-lg' onclick='Generar_OSyD("Material Dañado","""+str(Datos["ID"])+""")'>Material Dañado</button>
#                 </div>
#                 <div class='col-6 p-1'>
#                     <button class='btn btn-warning w-100 btn-lg' onclick='Generar_OSyD("Otra Discrepancia","""+str(Datos["ID"])+""")'>Otra Discrepancia</button>
#                 </div>
#             </div>
#             <script>
#                 function Modificar_A(Poner_En,A_Donde,ID){
#                     Mostrar_Ventana_Cargando(false);
#                     $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-pencil'></i> "+ Poner_En);
#                     $("#Vent_1").removeClass('modal-xl modal-lg modal-sm')
#                     var parametros = {"Fun":"Modificar_A","ID":ID,"Poner_En":Poner_En,"A_Donde":A_Donde};
#                     $.ajax({data:  parametros,url:\""""+str(Dir_Raiz)+"""\",type:  "post",
#                         success:  function (response)
#                         {
#                             var Resultado = JSON.parse(response);
#                             $("#Vent_1").modal("show").find(".modal-body").html(Resultado["Contenido"]);
#                             $("#Vent_1").find(".modal-footer").find("button").attr('onclick',"$('#Vent_1').modal('hide'); delete table; ")
#                             swal.close();
#                         },
#                         error: function (jqXHR, textStatus, errorThrown )
#                         {
#                             $("#Vent_1").modal("show").find(".modal-body").html("<i class='mdi mdi-alert'></i> "+ textStatus);
#                             swal.close();
#                         }
#                     });
#                 }
#                 function Generar_OSyD(Tipo,ID){
#                     Mostrar_Ventana_Cargando(false);
#                     $("#Vent_2").find(".modal-title").html("<i class='mdi mdi-plus'></i> "+ Tipo);
#                     $("#Vent_2").removeClass('modal-xl modal-lg modal-sm')
#                     var parametros = {"Fun":"Generar_OSyD","ID":ID,"Tipo":Tipo};
#                     $.ajax({data:  parametros,url:\""""+str(Dir_Raiz)+"""\",type:  "post",
#                         success:  function (response)
#                         {
#                             var Resultado = JSON.parse(response);
#                             $("#Vent_2").modal("show").find(".modal-body").html(Resultado["Contenido"]);
#                             $("#Vent_2").find(".modal-footer").find("button").attr('onclick',"$('#Vent_2').modal('hide'); delete table; ")
#                             swal.close();
#                         },
#                         error: function (jqXHR, textStatus, errorThrown )
#                         {
#                             $("#Vent_2").modal("show").find(".modal-body").html("<i class='mdi mdi-alert'></i> "+ textStatus);
#                             swal.close();
#                         }
#                     });
#                 }
#             </script>
#             """
#         if Caja["cc_tipo_actual"] == "Outbound":
#             Resultado["Contenido"] = """
#             <div>Opciones de Contenedor</div>
#             <div class='row'>
#                 <div class='col-12 p-1'>
#                     <button class='btn btn-dark w-100 btn-lg' onclick='Modificar_A("Ready to Load","","""+str(Datos["ID"])+""");'><div>Empty [Ready to Load]</div><div><small>(Asignación incorrecta)</small></div></button>
#                 </div>
#                 <div class='col-12 p-1'>
#                     <button class='btn btn-warning w-100 btn-lg' onclick='Modificar_A("Outbound","Patio","""+str(Datos["ID"])+""");'><div>Outbound</div><div><small>(Mover Caja a Patio <span class='fw-bold text-danger'>AÚN FALTA MATERIAL POR CARGAR</span>)</small></div></button>
#                 </div>
#                 <div class='col-12 p-1'>
#                     <button class='btn btn-warning w-100 btn-lg' onclick='Modificar_A("Outbound","Patio","""+str(Datos["ID"])+""",1);'><div>Outbound</div><div><small>(Mover Caja a Patio <span class='fw-bold text-danger'>LISTA PARA SALIR</span>)</small></div></button>
#                 </div>
#                 <div class='col-12 p-1'>
#                     <button class='btn btn-info w-100 btn-lg' onclick='Evidencia("""+str(Datos["ID"])+""",\""""+str(Caja["cc_contenedor"])+"""\");'><div> Add evidence </div><div><small></small></div></button>
#                 </div>
#             </div>
#             <script>
#                 function Modificar_A(Poner_En,A_Donde,ID,Salida=0){
#                     Mostrar_Ventana_Cargando(false);
#                     $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-pencil'></i> "+ Poner_En);
#                     $("#Vent_1").removeClass('modal-xl modal-lg modal-sm')
#                     var parametros = {"Fun":"Modificar_A","ID":ID,"Poner_En":Poner_En,"A_Donde":A_Donde,"Salida":Salida};
#                     $.ajax({data:  parametros,url:\""""+str(Dir_Raiz)+"""\",type:  "post",
#                         success:  function (response)
#                         {
#                             var Resultado = JSON.parse(response);
#                             $("#Vent_1").modal("show").find(".modal-body").html(Resultado["Contenido"]);
#                             $("#Vent_1").find(".modal-footer").find("button").attr('onclick',"$('#Vent_1').modal('hide'); delete table; ")
#                             swal.close();
#                         },
#                         error: function (jqXHR, textStatus, errorThrown )
#                         {
#                             $("#Vent_1").modal("show").find(".modal-body").html("<i class='mdi mdi-alert'></i> "+ textStatus);
#                             swal.close();
#                         }
#                     });
#                 }
#             </script>
#             """
#         if Caja["cc_tipo_actual"] == "Empty":
#             Resultado["Contenido"] = """
#             <div>Opciones de Containedor</div>
#             <div class='row'>
#                 <div class='col-12 p-1'>
#                     <button class='btn btn-dark w-100 btn-lg' onclick='Modificar_A("Ready to Load","Patio","""+str(Datos["ID"])+""");'><div>Empty [Ready to Load]</div><div><small>(Mover caja a patio)</small></div></button>
#                 </div>
#                 <div class='col-12 p-1'>
#                     <button class='btn btn-dark w-100 btn-lg' onclick='Modificar_A("Return Empty","Patio","""+str(Datos["ID"])+""");'><div>Empty [Return empty]</div><div><small>(Mover caja a patio <span class='text-danger fw-bold'>LISTA PARA SALIR</span>)</small></div></button>
#                 </div>
#                 <div class='col-12 p-1'>
#                     <button class='btn btn-warning w-100 btn-lg' onclick='Modificar_A("Outbound","Dock","""+str(Datos["ID"])+""");'><div>Outbound</div><div><small>(Dejar en dock <span class='text-danger fw-bold'>DEFINIR RUTA OUTBOUNT</span>)</small></div></button>
#                 </div>
#                 <div class='col-12 p-1'>
#                     <button class='btn btn-info w-100 btn-lg' onclick='Evidencia("""+str(Datos["ID"])+""",\""""+str(Caja["cc_contenedor"])+"""\");'><div> Add evidence </div><div><small></small></div></button>
#                 </div>
#             </div>
#             <script>
#                 function Modificar_A(Poner_En,A_Donde,ID,Salida=0){
#                     Mostrar_Ventana_Cargando(false);
#                     $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-pencil'></i> "+ Poner_En);
#                     $("#Vent_1").removeClass('modal-xl modal-lg modal-sm')
#                     var parametros = {"Fun":"Modificar_A","ID":ID,"Poner_En":Poner_En,"A_Donde":A_Donde,"Salida":Salida};
#                     $.ajax({data:  parametros,url:\""""+str(Dir_Raiz)+"""\",type:  "post",
#                         success:  function (response)
#                         {
#                             var Resultado = JSON.parse(response);
#                             $("#Vent_1").modal("show").find(".modal-body").html(Resultado["Contenido"]);
#                             $("#Vent_1").find(".modal-footer").find("button").attr('onclick',"$('#Vent_1').modal('hide'); delete table; ")
#                             swal.close();
#                         },
#                         error: function (jqXHR, textStatus, errorThrown )
#                         {
#                             $("#Vent_1").modal("show").find(".modal-body").html("<i class='mdi mdi-alert'></i> "+ textStatus);
#                             swal.close();
#                         }
#                     });
#                 }
#                 function Caja_Danada(ID,Contenedor){
#                      Mostrar_Ventana_Cargando(false);
#                     $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-pipe-leak'></i> "+ Contenedor);
#                     $("#Vent_1").removeClass('modal-xl modal-lg modal-sm')
#                     var parametros = {"Fun":"Caja_Danada","ID":ID};
#                     $.ajax({data:  parametros,url:\""""+str(Dir_Raiz)+"""\",type:  "post",
#                         success:  function (response)
#                         {
#                             var Resultado = JSON.parse(response);
#                             $("#Vent_1").modal("show").find(".modal-body").html(Resultado["Contenido"]);
#                             $("#Vent_1").find(".modal-footer").find("button").attr('onclick',"$('#Vent_1').modal('hide'); delete table; ")
#                             swal.close();
#                         },
#                         error: function (jqXHR, textStatus, errorThrown )
#                         {
#                             $("#Vent_1").modal("show").find(".modal-body").html("<i class='mdi mdi-alert'></i> "+ textStatus);
#                             swal.close();
#                         }
#                     });
#                 }
#             </script>
#             """
#         Resultado["Contenido"] += """
#         <script>
#             function Evidencia(ID,Contenedor){
#                 Mostrar_Ventana_Cargando(false);
#                 $("#Vent_2").find(".modal-title").html("<i class='mdi mdi-camera-burst'></i> "+ Contenedor);
#                 $("#Vent_2").removeClass('modal-xl modal-lg modal-sm')
#                 var parametros = {"Fun":"Evidencia","ID":ID};
#                 $.ajax({data:  parametros,url:\""""+str(Dir_Raiz)+"""\",type:  "post",
#                     success:  function (response)
#                     {
#                         var Resultado = JSON.parse(response);
#                         $("#Vent_2").modal("show").find(".modal-body").html(Resultado["Contenido"]);
#                         $("#Vent_2").find(".modal-footer").find("button").attr('onclick',"$('#Vent_2').modal('hide'); delete table; ")
#                         swal.close();
#                     },
#                     error: function (jqXHR, textStatus, errorThrown )
#                     {
#                         $("#Vent_2").modal("show").find(".modal-body").html("<i class='mdi mdi-alert'></i> "+ textStatus);
#                         swal.close();
#                     }
#                 });
#             }
#         </script>
#         """
#     except:
#          Resultado["Contenido"] = str(sys.exc_info())
#     Cur += json.dumps(Resultado)
#     print(Cur)
# def Modificar_A(Datos):
#     DB = LibDM_2023.DataBase()
#     Compartido_2023 = LibDM_2023.Compartido()
#     Cur = "content-type: text/html;charset=ISO-8859-1\n\n "
#     Resultado = {"Contenido":"","Estado":0}
#     try:
#         if "Salida" not in Datos.keys():
#             Datos["Salida"] = 0
#         if "A_Donde" not in Datos.keys():
#             Datos["A_Donde"] = ""
            
#         Formulario = {"Col":"12", "Campos": [],"Clase": "Modificar_A" }
#         Caja = DB.Get_Dato("SELECT * FROM rilc_toluca.ccajas WHERE cc_id = '"+str(Datos["ID"])+"'")[0]
#         Info_Actual = json.loads(str(Caja["cc_informacion_actual"]))
#         if Datos["Poner_En"] == "Ready to Load" and Datos["A_Donde"] == "":
#             Dock = []
#             Dock_Ya = ""
#             DOCK_DISPONIBLES = DB.Get_Dato("""
#             SELECT * FROM rilc_toluca.cdock_asignacion DOCK 
#             left join rilc_toluca.ccajas CAJAS on CAJAS.cc_activo = 1 and CAJAS.cc_dock = DOCK.cd_dock and CAJAS.cc_id != '"""+str(Datos["ID"])+"""'
#             where DOCK.cd_ub = 'RILC Toluca' and cd_activo = 1 and CAJAS.cc_id is null
#             """)
#             for D in DOCK_DISPONIBLES:
#                 Dock.append(str(D["cd_dock"]))
            
#             if "Dock" in Info_Actual.keys():
#                 Dock_Ya = Info_Actual["Dock"]
#             Formulario["Campos"].append({"tipo":"seleccion","campo":"Dock","titulo":"Dock","Requerido":1,"Tipo_Opciones":"Opciones","Opciones":Dock,"valor":Dock_Ya,"Col":12})

#             if Caja["cc_tipo_actual"] == "Empty" and "Fotos" in Info_Actual.keys():
#                 pass
#             else:
#                 Formulario["Campos"].append({"tipo":"archivo","campo":"Fotos","titulo":"Fotos","Requerido":1,"Col":12,"min":1,"max":5,"tipo_archivo":["image/*"],"valor":""})

#             Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
#             Resultado["Contenido"] += """
#             <hr>
#             <div class='w-100 text-center'><button class='btn btn-success w-75' onclick='Modificar_A_Guardar(\""""+str(Datos["Poner_En"])+"""\",\""""+str(Datos["A_Donde"])+"""\","""+str(Datos["ID"])+""")'><i class='mdi mdi-floppy'></i> Save</button></div>
#             """
#         if Datos["Poner_En"] == "Ready to Load" and Datos["A_Donde"] != "":
#             if Caja["cc_tipo_actual"] == "Empty" and "Fotos" in Info_Actual.keys():
#                 Resultado["Contenido"] += """
#                 <script>
#                     $( document ).ready(function() {
#                         Modificar_A_Guardar(\""""+str(Datos["Poner_En"])+"""\",\""""+str(Datos["A_Donde"])+"""\","""+str(Datos["ID"])+""");
#                     });
#                 </script>
#                 """
#             else:
#                 Formulario["Campos"].append({"tipo":"archivo","campo":"Fotos","titulo":"Photos","Requerido":1,"Col":12,"min":1,"max":5,"tipo_archivo":["image/*"],"valor":""})
#                 Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
#                 Resultado["Contenido"] += """
#                 <hr>
#                 <div class='w-100 text-center'><button class='btn btn-success w-75' onclick='Modificar_A_Guardar(\""""+str(Datos["Poner_En"])+"""\",\""""+str(Datos["A_Donde"])+"""\","""+str(Datos["ID"])+""")'><i class='mdi mdi-floppy'></i> Save</button></div>
#                 """
#         if Datos["Poner_En"] == "Return Empty":
#             Formulario["Campos"].append({"tipo":"archivo","campo":"Fotos","titulo":"Photos","Requerido":1,"Col":12,"min":1,"max":5,"tipo_archivo":["image/*"],"valor":""})
#             Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
#             Resultado["Contenido"] += """
#             <hr>
#             <div class='w-100 text-center'><button class='btn btn-success w-75' onclick='Modificar_A_Guardar(\""""+str(Datos["Poner_En"])+"""\",\""""+str(Datos["A_Donde"])+"""\","""+str(Datos["ID"])+""")'><i class='mdi mdi-floppy'></i> Save</button></div>
#             """
#         if Datos["Poner_En"] == "Inbound":
#             Formulario["Campos"].append({"tipo":"texto","campo":"Sello Temporal","titulo":"Temporary Seal","Requerido":1,"min":1,"max":150,"valor":""})
#             Formulario["Campos"].append({"tipo":"archivo","campo":"Fotos","titulo":"Photos","Requerido":1,"Col":12,"min":1,"max":5,"tipo_archivo":["image/*"],"valor":""})
#             Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
#             Resultado["Contenido"] += """
#             <hr>
#             <div class='w-100 text-center'><button class='btn btn-success w-75' onclick='Modificar_A_Guardar(\""""+str(Datos["Poner_En"])+"""\",\""""+str(Datos["A_Donde"])+"""\","""+str(Datos["ID"])+""")'><i class='mdi mdi-floppy'></i> Save</button></div>
#             """
#         if Datos["Poner_En"] == "Outbound" and Datos["A_Donde"] == "Patio":
#             Formulario["Campos"].append({"tipo":"texto","campo":"Sello Temporal","titulo":"Sello Termporal","Requerido":1,"min":1,"max":150,"valor":""})
#             Formulario["Campos"].append({"tipo":"archivo","campo":"Fotos","titulo":"Fotos","Requerido":1,"Col":12,"min":1,"max":5,"tipo_archivo":["image/*"],"valor":""})
#             if "Fecha_Salida" in Info_Actual.keys():
#                 Formulario["Campos"].append({"tipo":"fecha","campo":"Fecha_Salida","titulo":"Fecha de Salida","Requerido":1,"min":1,"max":30,"valor":Info_Actual["Fecha_Salida"],"editable":False})
#             Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
#             Resultado["Contenido"] += """
#             <hr>
#             <div class='w-100 text-center'><button class='btn btn-success w-75' onclick='Modificar_A_Guardar(\""""+str(Datos["Poner_En"])+"""\",\""""+str(Datos["A_Donde"])+"""\","""+str(Datos["ID"])+""","""+str(Datos["Salida"])+""")'><i class='mdi mdi-floppy'></i> Save</button></div>
#             """
#         if Datos["Poner_En"] == "Outbound" and Datos["A_Donde"] == "Dock":
#             Formulario = {"Col":"12", "Campos": [],"Clase": "Asignar" }
#             Dock = []
#             Dock_Ya = ""
#             DOCK_DISPONIBLES = DB.Get_Dato("""
#             SELECT * FROM rilc_toluca.cdock_asignacion DOCK 
#             left join rilc_toluca.ccajas CAJAS on CAJAS.cc_activo = 1 and CAJAS.cc_dock = DOCK.cd_dock and CAJAS.cc_id != '"""+str(Datos["ID"])+"""'
#             where DOCK.cd_ub = 'RILC Toluca' and cd_activo = 1 and CAJAS.cc_id is null
#             """)
#             for D in DOCK_DISPONIBLES:
#                 Dock.append(str(D["cd_dock"]))
#             if "Dock" in Info_Actual.keys():
#                 Dock_Ya = Info_Actual["Dock"]
#             Formulario["Campos"].append({"tipo":"seleccion","campo":"Dock","titulo":"Dock","Requerido":1,"Tipo_Opciones":"Opciones","Opciones":Dock,"valor":Dock_Ya,"Col":12})
#             Info = DB.Get_Dato("SELECT * FROM rilc_toluca.crutas WHERE cr_tipo = 'Outbound'")[0]["cr_niveles"]
#             if Info is not None:
#                 Info = json.loads(Info)
#                 Opciones = []
#                 for K in Info.keys():
#                     Opciones.append(K)
                
#                 Formulario["Campos"].append({"tipo":"seleccion","id":"Tipo_Nuevo_1","campo":"Outbound","titulo":"Outbound","Requerido":1,"Tipo_Opciones":"Opciones","Opciones":Opciones,"valor":""})
#                 Resultado["Contenido"] += """
#                 <script>
#                     Actualizar_Cambia_Texto();
#                     $("#Tipo_Nuevo_1").on( "change", function() {
#                         Mostrar_Ventana_Cargando(false);
#                         var parametros = {"Fun":"Tipo_Nuevo_1","Tipo":$(this).find('option:selected').val(),"Nivel_1":'Outbound',"Donde":'Dock',"ID":'"""+str(Datos["ID"])+"""',"Info_Actual":JSON.stringify("""+str(Info_Actual)+"""),"De_Donde":'Dock',"Sin_Guardar":0};
#                         $.ajax({data:  parametros,url:\""""+str(Dir_Raiz)+"""\",type:  "post",
#                             success:  function (response)
#                             {
#                                 var Resultado = JSON.parse(response);
#                                 $("#Opciones_1").html(Resultado["Contenido"]);
#                                 swal.close();
#                             },
#                             error: function (jqXHR, textStatus, errorThrown )
#                             {
#                                 $("#Opciones_1").html("<i class='mdi mdi-alert'></i> "+ textStatus);
#                                 swal.close();
#                             }
#                         });

#                     } );
#                 </script>
#                 """
#             Formulario["Campos"].append({"tipo":"archivo","campo":"Fotos","titulo":"Fotos","Requerido":1,"Col":12,"min":1,"max":5,"tipo_archivo":["image/*"],"valor":""})
#             if "Fecha_Salida" in Info_Actual.keys():
#                 Formulario["Campos"].append({"tipo":"fecha","campo":"Fecha_Salida","titulo":"Fecha de Salida","Requerido":1,"min":1,"max":30,"valor":Info_Actual["Fecha_Salida"],"editable":False})
#             Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
#             Resultado["Contenido"] += "<div id='Opciones_1'></div>"
#             Resultado["Contenido"] += """
#             <hr>
#             <div class='w-100 text-center'><button class='btn btn-success w-75' onclick='Modificar_A_Guardar(\""""+str(Datos["Poner_En"])+"""\",\"Dock\","""+str(Datos["ID"])+""","""+str(Datos["Salida"])+""")'><i class='mdi mdi-floppy'></i> Save</button></div>
#             """
#         if Formulario["Clase"] == "Asignar":
#             Resultado["Contenido"] += """
#             <script>
#                 function Modificar_A_Guardar(Poner_En,A_Donde,ID,Salida){
#                     var Info = Dame_Formulario(".Asignar",true);
#                     if(Info != null)
#                     {
#                         Mostrar_Ventana_Cargando(false);
#                         var parametros = {"Fun":"Modificar_A_Guardar","Info":JSON.stringify(Info),"ID":ID,"Poner_En":Poner_En,"A_Donde":A_Donde,"Info_Actual":JSON.stringify("""+str(Info_Actual)+"""),"Salida":Salida};
#                         $.ajax({data:  parametros,url:\""""+str(Dir_Raiz)+"""\",type:  "post",
#                             success:  function (response)
#                             {
#                                 var Resultado = JSON.parse(response);
#                                 if(Resultado["Estado"] == 1)
#                                 {
#                                     if("Pase Salida" in Resultado)
#                                     {
#                                         var win1 = window.open(Resultado["Pase Salida"], '_blank');
#                                         win1.focus();
#                                     }
#                                     $("#Vent_1").modal("hide");
#                                     Mensaje(2);
#                                     Docks();
#                                 }
#                                 else
#                                     Mensaje(0,Resultado["Contenido"]);
                                    
#                             },
#                             error: function (jqXHR, textStatus, errorThrown )
#                             {
#                                 Mensaje(0,textStatus);
#                             }
#                         });
#                     }
#                 }
#             </script>
#             """
#         else:
#             Resultado["Contenido"] += """
#             <script>
#                 function Modificar_A_Guardar(Poner_En,A_Donde,ID,Salida){
#                     var Info = Dame_Formulario(".Modificar_A",true);
#                     if(Info != null)
#                     {
#                         Mostrar_Ventana_Cargando(false);
#                         var parametros = {"Fun":"Modificar_A_Guardar","Info":JSON.stringify(Info),"ID":ID,"Poner_En":Poner_En,"A_Donde":A_Donde,"Info_Actual":JSON.stringify("""+str(Info_Actual)+"""),"Salida":Salida};
#                         $.ajax({data:  parametros,url:\""""+str(Dir_Raiz)+"""\",type:  "post",
#                             success:  function (response)
#                             {
#                                 var Resultado = JSON.parse(response);
#                                 if(Resultado["Estado"] == 1)
#                                 {
#                                     if("Pase Salida" in Resultado)
#                                     {
#                                         var win1 = window.open(Resultado["Pase Salida"], '_blank');
#                                         win1.focus();
#                                     }
#                                     $("#Vent_1").modal("hide");
#                                     Mensaje(2);
#                                     Docks();
#                                 }
#                                 else
#                                     Mensaje(0,Resultado["Contenido"]);
                                    
#                             },
#                             error: function (jqXHR, textStatus, errorThrown )
#                             {
#                                 Mensaje(0,textStatus);
#                             }
#                         });
#                     }
#                 }
#             </script>
#             """
#     except:
#          Resultado["Contenido"] = str(sys.exc_info())
#     Cur += json.dumps(Resultado)
#     print(Cur)
# def Modificar_A_Guardar(Datos):
#     DB = LibDM_2023.DataBase()
#     Compartido_2023 = LibDM_2023.Compartido()
#     Cur = "content-type: text/html;charset=ISO-8859-1\n\n "
#     Resultado = {"Contenido":"","Estado":0}
#     Error = ""
#     try:
#         Info_Datos = json.loads(str(Datos["Info"]))
#         Info_Actual = json.loads(str(Datos["Info_Actual"]))
#         if "A_Donde" not in Datos.keys():
#             Datos["A_Donde"] = ""
#         if Datos["Poner_En"] == "Ready to Load" and Datos["A_Donde"] == "":
#             Info_Nueva = {}
#             Info_Nueva["Carrier"] = Info_Actual["Carrier"]
#             Info_Nueva["Donde"] = "Dock"
#             Info_Nueva["Dock"] = Info_Datos["Dock"]
#             Info_Nueva["Tipo"] = "Empty"
#             Info_Nueva["Empty"] = "Ready to Load"
#             Info_Nueva["Fotos"] = Info_Datos["Fotos"]
#             Ubicacion = "Patio"
#             Dock = "null"
#             if "Dock" in Info_Nueva.keys():
#                 Ubicacion = "Dock"
#                 Dock = "'"+str(Info_Nueva["Dock"])+"'"
#             Error += DB.Instruccion("UPDATE rilc_toluca.ccajas SET cc_informacion_actual = '"+str(json.dumps(Info_Nueva))+"',cc_tipo_actual = 'Empty',cc_ultimo_mov = NOW(),cc_dock= "+str(Dock)+",cc_ubicacion = '"+str(Ubicacion)+"' WHERE cc_id = '"+str(Datos["ID"])+"' ")
#             if Error == "":
#                 Info_Ahora = DB.Get_Dato("SELECT * FROM rilc_toluca.ccajas WHERE cc_id = '"+str(Datos["ID"])+"'")[0]
#                 Info_Ahora["cc_dock"] = 'null' if Info_Ahora["cc_dock"] is None else "'"+str(Info_Ahora["cc_dock"])+"'"
#                 Info_Ahora["cc_tipo_actual"] = 'null' if Info_Ahora["cc_tipo_actual"] is None else "'"+str(Info_Ahora["cc_tipo_actual"])+"'"
#                 Info_Ahora["cc_zona"] = 'null' if Info_Ahora["cc_zona"] is None else "'"+str(Info_Ahora["cc_zona"])+"'"
#                 Info_Ahora["cc_negocio"] = 'null' if Info_Ahora["cc_negocio"] is None else "'"+str(Info_Ahora["cc_negocio"])+"'"
#                 Error = DB.Instruccion(""" 
#                 INSERT INTO rilc_toluca.ccajas_moviemiento
#                 (cch_master,cch_fecha_hora,cch_contenedor,cch_ubicacion,cch_informacion_actual,cch_dock,cch_tipo_actual,cch_zona,cch_negocio,cch_usuario,cch_movimiento)
#                 VALUES
#                 ('"""+str(Info_Ahora["cc_id"])+"""',NOW(),'"""+str(Info_Ahora["cc_contenedor"])+"""','"""+str(Info_Ahora["cc_ubicacion"])+"""','"""+str(Info_Ahora["cc_informacion_actual"])+"""',"""+str(Info_Ahora["cc_dock"])+""","""+str(Info_Ahora["cc_tipo_actual"])+""","""+str(Info_Ahora["cc_zona"])+""","""+str(Info_Ahora["cc_negocio"])+""",'"""+str(Datos["ID_User"])+"""','MODIFICAR')
#                 """)
#         if Datos["Poner_En"] == "Ready to Load" and Datos["A_Donde"] != "":
#             Info_Nueva = {}
#             Info_Nueva["Carrier"] = Info_Actual["Carrier"]
#             Info_Nueva["Donde"] = "Patio"
#             Info_Nueva["Tipo"] = "Empty"
#             Info_Nueva["Empty"] = "Ready to Load"
#             if "Fotos" in Info_Datos.keys():
#                 Info_Nueva["Fotos"] = Info_Datos["Fotos"]
#             Ubicacion = "Patio"
#             Dock = "null"
#             if "Dock" in Info_Nueva.keys():
#                 Ubicacion = "Dock"
#                 Dock = "'"+str(Info_Nueva["Dock"])+"'"
            
#             Error += DB.Instruccion("UPDATE rilc_toluca.ccajas SET cc_informacion_actual = '"+str(json.dumps(Info_Nueva))+"',cc_tipo_actual = 'Empty',cc_ultimo_mov = NOW(),cc_dock= "+str(Dock)+",cc_ubicacion = '"+str(Ubicacion)+"' WHERE cc_id = '"+str(Datos["ID"])+"' ")

#             if Error == "":
#                 Info_Ahora = DB.Get_Dato("SELECT * FROM rilc_toluca.ccajas WHERE cc_id = '"+str(Datos["ID"])+"'")[0]
#                 Info_Ahora["cc_dock"] = 'null' if Info_Ahora["cc_dock"] is None else "'"+str(Info_Ahora["cc_dock"])+"'"
#                 Info_Ahora["cc_tipo_actual"] = 'null' if Info_Ahora["cc_tipo_actual"] is None else "'"+str(Info_Ahora["cc_tipo_actual"])+"'"
#                 Info_Ahora["cc_zona"] = 'null' if Info_Ahora["cc_zona"] is None else "'"+str(Info_Ahora["cc_zona"])+"'"
#                 Info_Ahora["cc_negocio"] = 'null' if Info_Ahora["cc_negocio"] is None else "'"+str(Info_Ahora["cc_negocio"])+"'"
#                 Error = DB.Instruccion(""" 
#                 INSERT INTO rilc_toluca.ccajas_moviemiento
#                 (cch_master,cch_fecha_hora,cch_contenedor,cch_ubicacion,cch_informacion_actual,cch_dock,cch_tipo_actual,cch_zona,cch_negocio,cch_usuario,cch_movimiento)
#                 VALUES
#                 ('"""+str(Info_Ahora["cc_id"])+"""',NOW(),'"""+str(Info_Ahora["cc_contenedor"])+"""','"""+str(Info_Ahora["cc_ubicacion"])+"""','"""+str(Info_Ahora["cc_informacion_actual"])+"""',"""+str(Info_Ahora["cc_dock"])+""","""+str(Info_Ahora["cc_tipo_actual"])+""","""+str(Info_Ahora["cc_zona"])+""","""+str(Info_Ahora["cc_negocio"])+""",'"""+str(Datos["ID_User"])+"""','MODIFICAR')
#                 """)
#         if Datos["Poner_En"] == "Return Empty":
#             Info_Nueva = {}
#             Info_Nueva["Carrier"] = Info_Actual["Carrier"]
#             Info_Nueva["Donde"] = "Patio"
#             Info_Nueva["Tipo"] = "Empty"
#             Info_Nueva["Empty"] = "Return Empty"
#             Info_Nueva["Fotos"] = Info_Datos["Fotos"]
#             Info_Nueva["Etapa"] = "Pending Exit"
#             Ubicacion = "Patio"
#             Dock = "null"
#             if "Dock" in Info_Nueva.keys():
#                 Ubicacion = "Dock"
#                 Dock = "'"+str(Info_Nueva["Dock"])+"'"
            
#             Codigo = str(hashlib.md5(str("LOGISTICS INSIGHT CORPORATION - PASE SALIDA - "+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+" - "+str(Datos["ID"])).encode()).hexdigest())
#             Folio = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))
#             Folio += str(Datos["ID"])
            
#             Error += DB.Instruccion("UPDATE rilc_toluca.ccajas SET cc_informacion_actual = '"+str(json.dumps(Info_Nueva))+"',cc_tipo_actual = 'Empty',cc_ultimo_mov = NOW(),cc_dock= "+str(Dock)+",cc_ubicacion = '"+str(Ubicacion)+"',cc_qr_salida = '"+str(Codigo)+"',cc_folio_salida = '"+str(Folio)+"',cc_bloquear = 1 WHERE cc_id = '"+str(Datos["ID"])+"' ")
#             if Error == "":
#                 Info_Ahora = DB.Get_Dato("SELECT * FROM rilc_toluca.ccajas WHERE cc_id = '"+str(Datos["ID"])+"'")[0]
#                 Info_Ahora["cc_dock"] = 'null' if Info_Ahora["cc_dock"] is None else "'"+str(Info_Ahora["cc_dock"])+"'"
#                 Info_Ahora["cc_tipo_actual"] = 'null' if Info_Ahora["cc_tipo_actual"] is None else "'"+str(Info_Ahora["cc_tipo_actual"])+"'"
#                 Info_Ahora["cc_zona"] = 'null' if Info_Ahora["cc_zona"] is None else "'"+str(Info_Ahora["cc_zona"])+"'"
#                 Info_Ahora["cc_negocio"] = 'null' if Info_Ahora["cc_negocio"] is None else "'"+str(Info_Ahora["cc_negocio"])+"'"
#                 Error += DB.Instruccion(""" 
#                 INSERT INTO rilc_toluca.ccajas_moviemiento
#                 (cch_master,cch_fecha_hora,cch_contenedor,cch_ubicacion,cch_informacion_actual,cch_dock,cch_tipo_actual,cch_zona,cch_negocio,cch_usuario,cch_movimiento)
#                 VALUES
#                 ('"""+str(Info_Ahora["cc_id"])+"""',NOW(),'"""+str(Info_Ahora["cc_contenedor"])+"""','"""+str(Info_Ahora["cc_ubicacion"])+"""','"""+str(Info_Ahora["cc_informacion_actual"])+"""',"""+str(Info_Ahora["cc_dock"])+""","""+str(Info_Ahora["cc_tipo_actual"])+""","""+str(Info_Ahora["cc_zona"])+""","""+str(Info_Ahora["cc_negocio"])+""",'"""+str(Datos["ID_User"])+"""','MODIFICAR')
#                 """)
#                 #Resultado["Pase Salida"] = Generar_Pase_Salida(str(Datos["ID"]),"Pase_Salida")
#         if Datos["Poner_En"] == "Inbound":
#             Info_Nueva = Info_Actual
#             Info_Nueva["Donde"] = "Patio"
#             Info_Nueva["Fotos"] = Info_Datos["Fotos"]
#             Info_Nueva["Sello Temporal"] = Info_Datos["Sello Temporal"]
#             Ubicacion = "Patio"
#             Dock = "null"
            
#             Error += DB.Instruccion("UPDATE rilc_toluca.ccajas SET cc_informacion_actual = '"+str(json.dumps(Info_Nueva))+"',cc_ultimo_mov = NOW(),cc_dock= "+str(Dock)+",cc_ubicacion = '"+str(Ubicacion)+"' WHERE cc_id = '"+str(Datos["ID"])+"' ")
#             if Error == "":
#                 Info_Ahora = DB.Get_Dato("SELECT * FROM rilc_toluca.ccajas WHERE cc_id = '"+str(Datos["ID"])+"'")[0]
#                 Info_Ahora["cc_dock"] = 'null' if Info_Ahora["cc_dock"] is None else "'"+str(Info_Ahora["cc_dock"])+"'"
#                 Info_Ahora["cc_tipo_actual"] = 'null' if Info_Ahora["cc_tipo_actual"] is None else "'"+str(Info_Ahora["cc_tipo_actual"])+"'"
#                 Info_Ahora["cc_zona"] = 'null' if Info_Ahora["cc_zona"] is None else "'"+str(Info_Ahora["cc_zona"])+"'"
#                 Info_Ahora["cc_negocio"] = 'null' if Info_Ahora["cc_negocio"] is None else "'"+str(Info_Ahora["cc_negocio"])+"'"
#                 Error += DB.Instruccion(""" 
#                 INSERT INTO rilc_toluca.ccajas_moviemiento
#                 (cch_master,cch_fecha_hora,cch_contenedor,cch_ubicacion,cch_informacion_actual,cch_dock,cch_tipo_actual,cch_zona,cch_negocio,cch_usuario,cch_movimiento)
#                 VALUES
#                 ('"""+str(Info_Ahora["cc_id"])+"""',NOW(),'"""+str(Info_Ahora["cc_contenedor"])+"""','"""+str(Info_Ahora["cc_ubicacion"])+"""','"""+str(Info_Ahora["cc_informacion_actual"])+"""',"""+str(Info_Ahora["cc_dock"])+""","""+str(Info_Ahora["cc_tipo_actual"])+""","""+str(Info_Ahora["cc_zona"])+""","""+str(Info_Ahora["cc_negocio"])+""",'"""+str(Datos["ID_User"])+"""','MODIFICAR')
#                 """)
#         if Datos["Poner_En"] == "Outbound" and Datos["A_Donde"] == "Patio":
#             Tipo_Modificacion = "MODIFICAR"
#             Info_Nueva = Info_Actual
#             Info_Nueva["Donde"] = "Patio"
#             Info_Nueva["Fotos"] = Info_Datos["Fotos"]
#             Info_Nueva["Sello Temporal"] = Info_Datos["Sello Temporal"]
#             Ubicacion = "Patio"
#             Dock = "null"
#             Codigo = None
#             Folio = None
#             if int(Datos["Salida"]) == 1:
#                 Tipo_Modificacion = "LIBERA OPERACIONES"
#                 Codigo = str(hashlib.md5(str("LOGISTICS INSIGHT CORPORATION - PASE SALIDA - "+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+" - "+str(Datos["ID"])).encode()).hexdigest())
#                 Folio = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))
#                 Folio += str(Datos["ID"])
#                 Info_Nueva["Etapa"] = "Pending Exit"
#                 if Codigo is None:
#                     Error += DB.Instruccion("UPDATE rilc_toluca.ccajas SET cc_informacion_actual = '"+str(json.dumps(Info_Nueva))+"',cc_ultimo_mov = NOW(),cc_dock= "+str(Dock)+",cc_ubicacion = '"+str(Ubicacion)+"',cc_bloquear = 1 WHERE cc_id = '"+str(Datos["ID"])+"' ")
#                 else:
#                     Error += DB.Instruccion("UPDATE rilc_toluca.ccajas SET cc_informacion_actual = '"+str(json.dumps(Info_Nueva))+"',cc_ultimo_mov = NOW(),cc_dock= "+str(Dock)+",cc_ubicacion = '"+str(Ubicacion)+"',cc_qr_salida = '"+str(Codigo)+"', cc_folio_salida = '"+str(Folio)+"',cc_bloquear = 1 WHERE cc_id = '"+str(Datos["ID"])+"' ")
#             else:
#                 Error += DB.Instruccion("UPDATE rilc_toluca.ccajas SET cc_informacion_actual = '"+str(json.dumps(Info_Nueva))+"',cc_ultimo_mov = NOW(),cc_dock= "+str(Dock)+",cc_ubicacion = '"+str(Ubicacion)+"' WHERE cc_id = '"+str(Datos["ID"])+"' ")
#             if Error == "":
#                 Info_Ahora = DB.Get_Dato("SELECT * FROM rilc_toluca.ccajas WHERE cc_id = '"+str(Datos["ID"])+"'")[0]
#                 Info_Ahora["cc_dock"] = 'null' if Info_Ahora["cc_dock"] is None else "'"+str(Info_Ahora["cc_dock"])+"'"
#                 Info_Ahora["cc_tipo_actual"] = 'null' if Info_Ahora["cc_tipo_actual"] is None else "'"+str(Info_Ahora["cc_tipo_actual"])+"'"
#                 Info_Ahora["cc_zona"] = 'null' if Info_Ahora["cc_zona"] is None else "'"+str(Info_Ahora["cc_zona"])+"'"
#                 Info_Ahora["cc_negocio"] = 'null' if Info_Ahora["cc_negocio"] is None else "'"+str(Info_Ahora["cc_negocio"])+"'"
#                 Error += DB.Instruccion(""" 
#                 INSERT INTO rilc_toluca.ccajas_moviemiento
#                 (cch_master,cch_fecha_hora,cch_contenedor,cch_ubicacion,cch_informacion_actual,cch_dock,cch_tipo_actual,cch_zona,cch_negocio,cch_usuario,cch_movimiento)
#                 VALUES
#                 ('"""+str(Info_Ahora["cc_id"])+"""',NOW(),'"""+str(Info_Ahora["cc_contenedor"])+"""','"""+str(Info_Ahora["cc_ubicacion"])+"""','"""+str(Info_Ahora["cc_informacion_actual"])+"""',"""+str(Info_Ahora["cc_dock"])+""","""+str(Info_Ahora["cc_tipo_actual"])+""","""+str(Info_Ahora["cc_zona"])+""","""+str(Info_Ahora["cc_negocio"])+""",'"""+str(Datos["ID_User"])+"""','"""+str(Tipo_Modificacion)+"""')
#                 """)
#         if Datos["Poner_En"] == "Outbound" and Datos["A_Donde"] == "Dock":
#             Info_Nueva = Info_Actual
#             Datos_Info = json.loads(str(Datos["Info"]))
#             del Info_Nueva["Empty"]
#             Info_Nueva["Tipo"] = "Outbound"
#             for k in Datos_Info.keys():
#                 Info_Nueva[k] = Datos_Info[k]
#             Error += str(Datos_Info)
#             Error = DB.Instruccion("UPDATE rilc_toluca.ccajas SET cc_informacion_actual = '"+str(json.dumps(Info_Nueva))+"',cc_tipo_actual = 'Outbound',cc_ultimo_mov = NOW(),cc_dock= "+str(Datos_Info["Dock"])+",cc_ubicacion = 'Dock' WHERE cc_id = '"+str(Datos["ID"])+"' ")
#             if Error == "":
#                 Info_Ahora = DB.Get_Dato("SELECT * FROM rilc_toluca.ccajas WHERE cc_id = '"+str(Datos["ID"])+"'")[0]
#                 Info_Ahora["cc_dock"] = 'null' if Info_Ahora["cc_dock"] is None else "'"+str(Info_Ahora["cc_dock"])+"'"
#                 Info_Ahora["cc_tipo_actual"] = 'null' if Info_Ahora["cc_tipo_actual"] is None else "'"+str(Info_Ahora["cc_tipo_actual"])+"'"
#                 Info_Ahora["cc_zona"] = 'null' if Info_Ahora["cc_zona"] is None else "'"+str(Info_Ahora["cc_zona"])+"'"
#                 Info_Ahora["cc_negocio"] = 'null' if Info_Ahora["cc_negocio"] is None else "'"+str(Info_Ahora["cc_negocio"])+"'"
#                 Error = DB.Instruccion(""" 
#                 INSERT INTO rilc_toluca.ccajas_moviemiento
#                 (cch_master,cch_fecha_hora,cch_contenedor,cch_ubicacion,cch_informacion_actual,cch_dock,cch_tipo_actual,cch_zona,cch_negocio,cch_usuario,cch_movimiento)
#                 VALUES
#                 ('"""+str(Info_Ahora["cc_id"])+"""',NOW(),'"""+str(Info_Ahora["cc_contenedor"])+"""','"""+str(Info_Ahora["cc_ubicacion"])+"""','"""+str(Info_Ahora["cc_informacion_actual"])+"""',"""+str(Info_Ahora["cc_dock"])+""","""+str(Info_Ahora["cc_tipo_actual"])+""","""+str(Info_Ahora["cc_zona"])+""","""+str(Info_Ahora["cc_negocio"])+""",'"""+str(Datos["ID_User"])+"""','MODIFICAR')
#                 """)
#                 if Error == "":
#                     Resultado["Estado"] = 1
#                 else:
#                     Resultado["Contenido"] = Error
#             else:
#                 Resultado["Contenido"] += str(Error)

#         if Error == "":
#             Resultado["Estado"] = 1
#         else:
#             Resultado["Contenido"] += str(Error)
#     except:
#         Resultado["Contenido"] = str(sys.exc_info())
#     Cur += json.dumps(Resultado)
#     print(Cur)
# def Tipo_Nuevo_1(Datos):
#     DB = LibDM_2023.DataBase()
#     Compartido_2023 = LibDM_2023.Compartido()
#     Cur = "content-type: text/html;charset=ISO-8859-1\n\n "
#     Resultado = {"Contenido":"","Estado":0}
#     try:
#         if "Sin_Guardar" not in Datos.keys():
#             Datos["Sin_Guardar"] = 1
#         Info_Actual = json.loads(str(Datos["Info_Actual"]))
#         De_Donde = str(Datos["De_Donde"])
        
#         Info = DB.Get_Dato("SELECT * FROM rilc_toluca.crutas WHERE cr_tipo = '"+str(Datos["Nivel_1"])+"'")[0]["cr_niveles"]
#         Info = json.loads(Info)
#         Opciones = []
#         if Info[Datos["Tipo"]] == 0 or "NOMBRE" in Info[Datos["Tipo"]].keys():
#             if De_Donde == "Patio" and str(Datos["Donde"]) == "Patio":
#                 if str(Datos["Nivel_1"]) == "Empty" and str(Datos["Tipo"]) == "Return Empty":
#                     Formulario = {"Col":"12", "Campos": [],"Clase": "Asignar" }
#                     Formulario["Campos"].append({"tipo":"archivo","campo":"Fotos","titulo":"Photos","Requerido":1,"Col":12,"min":1,"max":5,"tipo_archivo":["image/*"],"valor":""})
#                     Formulario["Campos"].append({"tipo":"checkbox","campo":"Salida","titulo":"¿Lista para salir? (GENERA PASA DE SALIDA)","Requerido":1,"valor":True,"editable":False})
#                     Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
#             if De_Donde == "Patio" and str(Datos["Donde"]) == "Dock":
#                 if str(Datos["Nivel_1"]) == "Empty":
#                     Formulario = {"Col":"12", "Campos": [],"Clase": "Asignar" }
#                     Formulario["Campos"].append({"tipo":"archivo","campo":"Fotos","titulo":"Photos","Requerido":1,"Col":12,"min":1,"max":5,"tipo_archivo":["image/*"],"valor":""})
#                     Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
#             if De_Donde == "Dock" and str(Datos["Donde"]) == "Dock":
#                 if str(Datos["Nivel_1"]) == "Empty":
#                     Formulario = {"Col":"12", "Campos": [],"Clase": "Asignar" }
#                     Formulario["Campos"].append({"tipo":"archivo","campo":"Fotos","titulo":"Photos","Requerido":1,"Col":12,"min":1,"max":5,"tipo_archivo":["image/*"],"valor":""})
#                     Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
#             if int(Datos["Sin_Guardar"]) == 1:
#                 Resultado["Contenido"] += """
#                 <hr>
#                 <div class='w-100 text-center'><button class='btn btn-success w-75' onclick='Modificar_Guardar("""+str(Datos["ID"])+""")'><i class='mdi mdi-floppy'></i> Save</button></div>
#                 """
#         else:
#             for K in Info[Datos["Tipo"]].keys():
#                 Opciones.append(K)
#             Formulario = {"Col":"12", "Campos": [],"Clase": "Asignar" }
#             Formulario["Campos"].append({"tipo":"seleccion","id":"Tipo_Nuevo_2","campo":str(Datos["Tipo"]),"titulo":str(Datos["Tipo"]),"Requerido":1,"Tipo_Opciones":"Opciones","Opciones":Opciones,"valor":""})
#             Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
#             Resultado["Contenido"] += "<div id='Opciones_2'></div>"
#             Resultado["Contenido"] += """
#             <script>
#                 Actualizar_Cambia_Texto();
#                 $("#Tipo_Nuevo_2").on( "change", function() {
#                     Mostrar_Ventana_Cargando(false);
#                     var parametros = {"Fun":"Tipo_Nuevo_2","Tipo":$(this).find('option:selected').val(),"Nivel_1":'"""+str(Datos["Nivel_1"])+"""',"Nivel_2":'"""+str(Datos["Tipo"])+"""',"Donde":'"""+str(Datos["Donde"])+"""',"ID":'"""+str(Datos["ID"])+"""',"Info_Actual":JSON.stringify("""+str(Info_Actual)+"""),"De_Donde":'"""+str(De_Donde)+"""',"Sin_Guardar":'"""+str(Datos["Sin_Guardar"])+"""'};
#                     $.ajax({data:  parametros,url:\""""+str(Dir_Raiz)+"""\",type:  "post",
#                         success:  function (response)
#                         {
#                             var Resultado = JSON.parse(response);
#                             $("#Opciones_2").html(Resultado["Contenido"]);
#                             swal.close();
#                         },
#                         error: function (jqXHR, textStatus, errorThrown )
#                         {
#                             $("#Opciones_2").html("<i class='mdi mdi-alert'></i> "+ textStatus);
#                             swal.close();
#                         }
#                     });

#                 } );
#             """
#             if str(Datos["Tipo"]) in Info_Actual.keys():
#                 Resultado["Contenido"] += """
#                 $( document ).ready(function() {
#                     $("#Tipo_Nuevo_2").val(\""""+str(Info_Actual[str(Datos["Tipo"])])+"""\").trigger("change");
#                 });
#                 """
#             Resultado["Contenido"] += """
#             </script>
#             """
#     except:
#          Resultado["Contenido"] = str(sys.exc_info())
#     Cur += json.dumps(Resultado)
#     print(Cur)
# def Tipo_Nuevo_2(Datos):
#     DB = LibDM_2023.DataBase()
#     Compartido_2023 = LibDM_2023.Compartido()
#     Cur = "content-type: text/html;charset=ISO-8859-1\n\n "
#     Resultado = {"Contenido":"","Estado":0}
#     try:
#         #Resultado["Contenido"] += str(Datos)

#         Info_Actual = json.loads(str(Datos["Info_Actual"]))
#         De_Donde = str(Datos["De_Donde"])
#         if Datos["Nivel_1"] == "Outbound":
#             Formulario = {"Col":"12", "Campos": [],"Clase": "Asignar" }
#             if "Fecha_Salida" in Info_Actual.keys():
#                 Formulario["Campos"].append({"tipo":"fecha","campo":"Fecha_Salida","titulo":"Fecha de Salida","Requerido":1,"valor":str(Info_Actual["Fecha_Salida"]),"editable":False})
#             else:
#                 Formulario["Campos"].append({"tipo":"fecha","campo":"Fecha_Salida","titulo":"Fecha de Salida","Requerido":1,"valor":""})
#             if De_Donde == "Patio" and str(Datos["Donde"]) == "Patio":
#                 Formulario["Campos"].append({"tipo":"checkbox","campo":"Salida","titulo":"¿Lista para salir? (GENERA PASA DE SALIDA)","Requerido":1,"valor":False})
#             Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
#             if De_Donde == "Patio" and str(Datos["Donde"]) == "Patio":
#                 Resultado["Contenido"] += """
#                 <div id='Foto_Lista_Salir'></div>
#                 <script>
#                     $(document).ready(function() {
#                         $('#checkbox_1').change(function() {
#                             if(this.checked) {
#                                 Mostrar_Ventana_Cargando(false);
#                                 var parametros = {"Fun":"Foto_Lista_Salir"};
#                                 $.ajax({data:  parametros,url:\""""+str(Dir_Raiz)+"""\",type:  "post",
#                                     success:  function (response)
#                                     {
#                                         var Resultado = JSON.parse(response);
#                                         $("#Foto_Lista_Salir").html(Resultado["Contenido"]);
#                                         swal.close();
#                                     },
#                                     error: function (jqXHR, textStatus, errorThrown )
#                                     {
#                                         $("#Foto_Lista_Salir").html("<i class='mdi mdi-alert'></i> "+ textStatus);
#                                         swal.close();
#                                     }
#                                 });
#                             }else{
#                                 $("#Foto_Lista_Salir").html("");
#                             }      
#                         });
#                     });
#                 </script>
#                 """

#         if "Sin_Guardar" not in Datos.keys():
#             Datos["Sin_Guardar"] = 1
       

#         Info = DB.Get_Dato("SELECT * FROM rilc_toluca.crutas WHERE cr_tipo = '"+str(Datos["Nivel_1"])+"'")[0]["cr_niveles"]
#         Info = json.loads(Info)
#         Opciones = []
#         if Info[Datos["Nivel_2"]][Datos["Tipo"]] == 0 or "NOMBRE" in Info[Datos["Nivel_2"]][Datos["Tipo"]].keys():
#             if int(Datos["Sin_Guardar"]) == 1:
#                 Resultado["Contenido"] += """
#                 <hr>
#                 <div class='w-100 text-center'><button class='btn btn-success w-75' onclick='Modificar_Guardar("""+str(Datos["ID"])+""")'><i class='mdi mdi-floppy'></i> Save</button></div>
#                 """
#         else:
#             if "DOCKS" in Info[Datos["Nivel_2"]][Datos["Tipo"]].keys() and len(Info[Datos["Nivel_2"]][Datos["Tipo"]]["DOCKS"]) == 0:
#                 for K in Info[Datos["Nivel_2"]][Datos["Tipo"]]["DOCKS"]:
#                     Opciones.append(K)
#                 Formulario = {"Col":"12", "Campos": [],"Clase": "Asignar" }
#                 Formulario["Campos"].append({"tipo":"seleccion","id":"Tipo_Nuevo_3","campo":str(Datos["Tipo"]),"titulo":str(Datos["Tipo"]),"Requerido":1,"Tipo_Opciones":"Opciones","Opciones":Opciones,"valor":""})
#                 Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
#                 if int(Datos["Sin_Guardar"]) == 1:
#                     Resultado["Contenido"] += """
#                     <hr>
#                     <div class='w-100 text-center'><button class='btn btn-success w-75' onclick='Modificar_Guardar("""+str(Datos["ID"])+""")'><i class='mdi mdi-floppy'></i> Save</button></div>
#                     """
#     except:
#          Resultado["Contenido"] = str(sys.exc_info())
#     Cur += json.dumps(Resultado)
#     print(Cur)
# def Evidencia(Datos):
#     DB = LibDM_2023.DataBase()
#     Compartido_2023 = LibDM_2023.Compartido()
#     Cur = "content-type: text/html;charset=ISO-8859-1\n\n "
#     Resultado = {"Contenido":"","Estado":0}
#     try:
#         Formulario = {"Col":"12", "Campos": [],"Clase": "Evidencia_Guardar" }
#         Formulario["Campos"].append({"tipo":"archivo","campo":"Fotos","titulo":"Fotos","Requerido":1,"Col":12,"min":1,"max":5,"tipo_archivo":["image/*"],"valor":""})
#         Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
#         Resultado["Contenido"] += """
#         <hr>
#         <div class='w-100 text-center'><button class='btn btn-success w-75' onclick='Evidencia_Guardar("""+str(Datos["ID"])+""")'><i class='mdi mdi-floppy'></i> Save</button></div>
#         <script>
#             function Evidencia_Guardar(ID){
#                 var Info = Dame_Formulario(".Evidencia_Guardar",true);
#                 if(Info != null)
#                 {
#                     Mostrar_Ventana_Cargando(false);
#                     var parametros = {"Fun":"Evidencia_Guardar","Info":JSON.stringify(Info),"ID":ID};
#                     $.ajax({data:  parametros,url:\""""+str(Dir_Raiz)+"""\",type:  "post",
#                         success:  function (response)
#                         {
#                             var Resultado = JSON.parse(response);
#                             if(Resultado["Estado"] == 1)
#                             {
#                                 if("Pase Salida" in Resultado)
#                                 {
#                                     var win1 = window.open(Resultado["Pase Salida"], '_blank');
#                                     win1.focus();
#                                 }
#                                 $("#Vent_2").modal("hide");
#                                 Mensaje(2);
#                             }
#                             else
#                                 Mensaje(0,Resultado["Contenido"]);
                                
#                         },
#                         error: function (jqXHR, textStatus, errorThrown )
#                         {
#                             Mensaje(0,textStatus);
#                         }
#                     });
#                 }
#             }
#         </script>
#         """
#     except:
#          Resultado["Contenido"] = str(sys.exc_info())
#     Cur += json.dumps(Resultado)
#     print(Cur)
# def Evidencia_Guardar(Datos):
#     DB = LibDM_2023.DataBase()
#     Compartido_2023 = LibDM_2023.Compartido()
#     Cur = "content-type: text/html;charset=ISO-8859-1\n\n "
#     Resultado = {"Contenido":"","Estado":0}
#     Error = ""
#     try:
#         Caja = DB.Get_Dato("SELECT * FROM rilc_toluca.ccajas WHERE cc_id = '"+str(Datos["ID"])+"'")[0]
#         Info_Actual = json.loads(str(Caja["cc_informacion_actual"]))
#         Datos_Info = json.loads(str(Datos["Info"]))
#         #del Info_Actual["Dock"]
#         for k in Datos_Info.keys():
#             Info_Actual[k] = Datos_Info[k]
#         Error = DB.Instruccion("UPDATE rilc_toluca.ccajas SET cc_informacion_actual = '"+str(json.dumps(Info_Actual))+"',cc_ultimo_mov = NOW() WHERE cc_id = '"+str(Datos["ID"])+"' ")
#         if Error == "":
#             Info_Ahora = DB.Get_Dato("SELECT * FROM rilc_toluca.ccajas WHERE cc_id = '"+str(Datos["ID"])+"'")[0]
#             Info_Ahora["cc_dock"] = 'null' if Info_Ahora["cc_dock"] is None else "'"+str(Info_Ahora["cc_dock"])+"'"
#             Info_Ahora["cc_tipo_actual"] = 'null' if Info_Ahora["cc_tipo_actual"] is None else "'"+str(Info_Ahora["cc_tipo_actual"])+"'"
#             Info_Ahora["cc_zona"] = 'null' if Info_Ahora["cc_zona"] is None else "'"+str(Info_Ahora["cc_zona"])+"'"
#             Info_Ahora["cc_negocio"] = 'null' if Info_Ahora["cc_negocio"] is None else "'"+str(Info_Ahora["cc_negocio"])+"'"
#             Error = DB.Instruccion(""" 
#             INSERT INTO rilc_toluca.ccajas_moviemiento
#             (cch_master,cch_fecha_hora,cch_contenedor,cch_ubicacion,cch_informacion_actual,cch_dock,cch_tipo_actual,cch_zona,cch_negocio,cch_usuario,cch_movimiento)
#             VALUES
#             ('"""+str(Info_Ahora["cc_id"])+"""',NOW(),'"""+str(Info_Ahora["cc_contenedor"])+"""','"""+str(Info_Ahora["cc_ubicacion"])+"""','"""+str(Info_Ahora["cc_informacion_actual"])+"""',"""+str(Info_Ahora["cc_dock"])+""","""+str(Info_Ahora["cc_tipo_actual"])+""","""+str(Info_Ahora["cc_zona"])+""","""+str(Info_Ahora["cc_negocio"])+""",'"""+str(Datos["ID_User"])+"""','EVIDENCIA')
#             """)
#             if Error == "":
#                 Resultado["Estado"] = 1
#             else:
#                 Resultado["Contenido"] = Error
#         else:
#             Resultado["Contenido"] += str(Error)
#     except:
#         Resultado["Contenido"] = str(sys.exc_info())
#     Cur += json.dumps(Resultado)
#     print(Cur)
# def Generar_OSyD(Datos):
#     DB = LibDM_2023.DataBase()
#     Compartido_2023 = LibDM_2023.Compartido()
#     Cur = "content-type: text/html;charset=ISO-8859-1\n\n "
#     Resultado = {"Contenido":"","Estado":0}
#     try:
#         Caja = DB.Get_Dato("SELECT * FROM rilc_toluca.ccajas WHERE cc_id = '"+str(Datos["ID"])+"'")[0]
#         Info_Actual = json.loads(str(Caja["cc_informacion_actual"]))
#         Formulario = {"Col":"12", "Campos": [],"Clase": "OSyD" }
#         if Datos["Tipo"] == "Otra Discrepancia":
#             Datos["Tipo"] = ""
#         Formulario["Campos"].append({"tipo":"texto","campo":"Comentario","titulo":"Comentarios","Requerido":1,"min":1,"max":150,"valor":Datos["Tipo"]})
#         Formulario["Campos"].append({"tipo":"archivo","campo":"Fotos","titulo":"Fotos","Requerido":1,"Col":12,"min":1,"max":5,"tipo_archivo":["image/*"],"valor":""})
#         Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
#         Resultado["Contenido"] += """
#         <hr>
#         <div class='w-100 text-center'><button class='btn btn-success w-75' onclick='Guardar_OSyD(\""""+str(Datos["Tipo"])+"""\","""+str(Datos["ID"])+""")'><i class='mdi mdi-floppy'></i> Save</button></div>
#         <script>
#             function Guardar_OSyD(Tipo,ID){
#                 var Info = Dame_Formulario(".OSyD",true);
#                 if(Info != null)
#                 {
#                     Info["Caja"] = '"""+str(Caja["cc_contenedor"])+"""';
#                     Info["Carrier"] = '"""+str(Info_Actual["Carrier"])+"""';
#                     Mostrar_Ventana_Cargando(false);
#                     var parametros = {"Fun":"Guardar_OSyD","Info":JSON.stringify(Info),"ID":ID,"Tipo":Tipo};
#                     $.ajax({data:  parametros,url:\""""+str(Dir_Raiz)+"""\",type:  "post",
#                         success:  function (response)
#                         {
#                             var Resultado = JSON.parse(response);
#                             if(Resultado["Estado"] == 1)
#                             {
#                                 $("#Vent_2").modal("hide");
#                                 Mensaje(2);
#                             }
#                             else
#                                 Mensaje(0,Resultado["Contenido"]);
                                
#                         },
#                         error: function (jqXHR, textStatus, errorThrown )
#                         {
#                             Mensaje(0,textStatus);
#                         }
#                     });
#                 }
#             }
#         </script>
#         """
#     except:
#         Resultado["Contenido"] = str(sys.exc_info())
#     Cur += json.dumps(Resultado)
#     print(Cur)
# def Guardar_OSyD(Datos):
#     DB = LibDM_2023.DataBase()
#     Compartido_2023 = LibDM_2023.Compartido()
#     Cur = "content-type: text/html;charset=ISO-8859-1\n\n "
#     Resultado = {"Contenido":"","Estado":0}
#     Error = ""
#     try:
#         Info_Datos = json.loads(str(Datos["Info"]))
#         Error = ""
#         Error += DB.Instruccion("""
#         INSERT INTO rilc_toluca.cosyd
#         (cosyd_tipo,cosyd_usuario,cosyd_alta,cosyd_caja,cosyd_comentario,cosyd_archivos,cosyd_scac)
#         VALUES
#         ('PRODUCCION','"""+str(Datos["ID_User"])+"""',NOW(),'"""+str(Info_Datos["Caja"])+"""','"""+str(Info_Datos["Comentario"])+"""','"""+str(','.join(Info_Datos["Fotos"]))+"""','"""+str(Info_Datos["Carrier"])+"""')
#         """)
#         if Error == "":
#             ID = DB.Get_Dato("SELECT MAX(cosyd_id) as ID FROM rilc_toluca.cosyd WHERE cosyd_tipo = 'PRODUCCION' AND cosyd_usuario = '"+str(Datos["ID_User"])+"' ")[0]["ID"]
#             Error += DB.Instruccion("""
#             INSERT INTO rilc_toluca.cosyd_historico
#             (cosyd_master,cosyd_usuario,cosyd_comentario,cosyd_evidencia,cosyd_movimiento,cosyd_fecha)
#             VALUES
#             ('"""+str(ID)+"""','"""+str(Datos["ID_User"])+"""','"""+str(Info_Datos["Comentario"])+"""','"""+str(','.join(Info_Datos["Fotos"]))+"""','ALTA',NOW())
#             """)
#         if Error == "":
#             Resultado["Estado"] = 1
#         else:
#             Resultado["Contenido"] = str(Error)
#         Resultado["Contenido"] = str(Datos)
#     except:
#         Resultado["Contenido"] = str(sys.exc_info())
#     Cur += json.dumps(Resultado)
#     print(Cur)

# def Cerrar_Sesion(Datos):
#     try:
#         C = cookies.SimpleCookie()
#         C["K_Portal_U"] = ""
#         C["K_Portal_U"]["path"] = "/"
#         C["K_Portal_U"]["expires"] = "Thu, 01 Jan 1970 00:00:00 GMT"
#         C["Update_Portal_U"] = ""
#         C["Update_Portal_U"]["path"] = "/"
#         C["Update_Portal_U"]["expires"] = "Thu, 01 Jan 1970 00:00:00 GMT"
#         Cur = str(C.output())+"\n"
#         Cur += "content-type: text/html;charset=ISO-8859-1\n\n " + "1"
#     except:
#         Cur = "content-type: text/html;charset=ISO-8859-1\n\n "
#         Cur += str(sys.exc_info())
#     print(Cur)


def Direccionar(Datos):
    try:
        if "K" in session.keys():
            fernet = Fernet(session["K"])
        else:
            fernet = Fernet(LibDM_2023.Compartido().Dame_K2())
        if Datos is None:
            return Inicio_Sesion()
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
                return Inicio_Sesion()
    except:
        return str(sys.exc_info())
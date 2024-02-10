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

        Contenido += """<div class='text-end pe-1 pt-1'><small class='link-primary' style='cursor:pointer' onclick='Cargar_Fecha($("#fecha").val())'>Actualizar <i class='mdi mdi-refresh'></i></small></div>"""
        Contenido += """
        <div class='container'>
        <!--<div class='text-end mb-1'><button class='btn btn-primary' onclick='Agregar_Adicional()'><i class='mdi mdi-plus'></i> Agregar adicional</button> <button class='btn btn-dark' onclick='Crear_Programacion()'><i class='mdi mdi-plus'></i> Crear Programación de Día</button></div>-->
        <table class='table table-bordered table-sm table-striped table-hover'>
            <thead class='table-dark'>
                <tr>
                    <td>Fecha</td>
                    <td>Ruta</td>
                    <td>Caja</td>
                    <td>Carrier</td>
                    <td>Entrada</td>
                    <td>DEFINIR RUTA</span></td>
                    <td class='text-center' style='width:40px;'><span style='writing-mode: vertical-lr;'>OPERACIONES</span></td>
                    <td class='text-center' style='width:40px;'><span style='writing-mode: vertical-lr;'>SALIO</span></td>
                    <td class='text-center' style='width:40px;'><span style='writing-mode: vertical-lr;'>COMPLETO</span></td>
                    <td>CUT TIME</td>
                </tr>
            </thead>
            <tbody>
        """
        Cajas_Aqui = []
        Programacion_Abiertos = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".ccajas WHERE (cc_activo = 1 or cc_informacion_actual LIKE concat('%',DATE(NOW()),'%') ) AND cc_tipo_actual = 'Outbound' AND cc_informacion_actual LIKE '%Fecha_Salida%'")
        for Programacion in Programacion_Abiertos:
            Cajas_Aqui.append(str(Programacion["cc_id"]))
        Movimientos = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".ccajas_moviemiento WHERE cch_master IN ("+str(",".join(Cajas_Aqui))+") ORDER BY cch_fecha_hora")

        for Programacion in Programacion_Abiertos:
            Info_Ahora = json.loads(str(Programacion["cc_informacion_actual"]))

            Ruta = ""
            Ruta += "<span class='h-100 border' style='width:20px; background:var(--Color_"+str(Programacion["cc_tipo_actual"])+");Color:var(--Color_"+str(Programacion["cc_tipo_actual"])+");'>__</span>"
            try:
                Tipo = Info_Ahora[Programacion["cc_tipo_actual"]]
                Ruta += str(Tipo)
                Tipo_1 = Info_Ahora[Tipo]
                Ruta += "/"+str(Tipo_1)
                Tipo_2 = Info_Ahora[Tipo_1]
                Ruta += "/"+str(Tipo_2)
            except:
                pass

            Contenido += """
            <tr class=''>
                <td>"""+str(Info_Ahora["Fecha_Salida"])+"""</td>
                <td>"""+str(Ruta)+"""</td>
                <td>"""+str(Programacion["cc_contenedor"])+"""</td>
                <td>"""+str(Info_Ahora["Carrier"])+"""</td>
                <td>"""+str(Programacion["cc_fecha_hora"])+"""</td>
            """
            Movimientos_Aqui = []
            for M in Movimientos:
                if int(M["cch_master"]) == int(Programacion["cc_id"]):
                    Movimientos_Aqui.append(M)
            
            Definir_Ruta = None
            for M in Movimientos_Aqui:
                if "Fecha_Salida" in str(M["cch_informacion_actual"]):
                    Definir_Ruta = M["cch_fecha_hora"].strftime("%m-%d %H:%M")

            if Definir_Ruta is not None:
                Contenido += "<td>"+str(Definir_Ruta)+"</td>"
            else:
                Contenido += "<td></td>"
           
            Libera_Operaciones = None
            for M in Movimientos_Aqui:
                if M["cch_movimiento"] == "LIBERA OPERACIONES":
                    Libera_Operaciones = M["cch_fecha_hora"].strftime("%m-%d %H:%M")
            
            if Libera_Operaciones is None:
                if Definir_Ruta is not None:
                    if Programacion["cc_dock"] is not None:
                        Contenido += "<td class='align-middle text-center table-warning'><small class='text-danger fw-bold Pulsa_Texto'>"+str(Programacion["cc_dock"])+"</td>"
                    else:
                        Contenido += "<td class='align-middle text-center table-warning'><small class='text-danger fw-bold Pulsa_Texto'><i class='mdi mdi-decagram'></i></small></td>"
                else:
                    Contenido += "<td class='table-danger'></td>"
            else:
                Contenido += "<td class='align-middle text-center table-success'><i class='mdi mdi-check-bold'></i></td>"

            
            Salida_Fecha_Hora = None
            Salida = None
            for M in Movimientos_Aqui:
                if M["cch_movimiento"] == "SALIDA":
                    Salida = M["cch_fecha_hora"].strftime("%m-%d %H:%M")
                    Salida_Fecha_Hora = M["cch_fecha_hora"].strftime("%m-%d %H:%M")
                if M["cch_movimiento"] == "ELIMINADO POR YARD":
                    Salida = M["cch_fecha_hora"].strftime("%m-%d %H:%M")
            if Salida is not None:
                Contenido += "<td class='align-middle text-center table-success'><i class='mdi mdi-check-bold'></i></td>"
            else:
                Contenido += "<td class='table-danger'></td>"


            if Definir_Ruta is not None and Libera_Operaciones is not None and Salida is not None:
                Contenido += "<td class='align-middle text-center table-success'><i class='mdi mdi-check-bold'></i></td>"
            else:
                Contenido += "<td class='table-danger'></td>"
            
            Cut_Time = datetime.strptime(str(Info_Ahora["Fecha_Salida"])+" 23:00:00","%Y-%m-%d %H:%M:%S")

            if DB.Dame_Hora() > Cut_Time:
                Contenido += "<td class='align-middle text-center' style='background:#d70000;color:#ffffff;'>"+str(Cut_Time.strftime("%m-%d %H:%M"))+"</td>"
            elif DB.Dame_Hora() > Cut_Time - timedelta(hours=5):
                Contenido += "<td class='align-middle text-center' style='background:#ffd255;color:#000000;'>"+str(Cut_Time.strftime("%m-%d %H:%M"))+"</td>"
            else:
                Contenido += "<td class='align-middle text-center' style='background:#8dff55;color:#000000;'>"+str(Cut_Time.strftime("%m-%d %H:%M"))+"</td>"



            Contenido += """
            </tr>
            """
        Contenido += """
            </tbody>
        </table>
        """
        Contenido += """
        <script>
            function Re_Asignar(ID,Fecha){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-history'></i> Re-Asignar LOAD ID ["+Fecha+"]");
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm');
                var parametros = {"Fun":'"""+str(fernet.encrypt("Re_Asignar".encode()).decode("utf-8"))+"""',"ID":ID};
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
            function Asignar_Load_ID(ID,Fecha){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-history'></i> Asignar LOAD ID ["+Fecha+"]");
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm');
                var parametros = {"Fun":'"""+str(fernet.encrypt("Asignar_Load_ID".encode()).decode("utf-8"))+"""',"ID":ID};
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
            function Liberar_Operaciones(ID_Caja,Caja){
                Swal.fire({
                title: 'Estas segur@ de liberar la caja ['+Caja+']?',
                buttonsStyling: false,showCancelButton: true,confirmButtonText: "<i class='mdi mdi-check'></i> Yes",cancelButtonText: "<i class='mdi mdi-close'></i> No",showLoaderOnConfirm: true,
                customClass: {confirmButton: 'btn btn-success ms-1 me-1',cancelButton: 'btn btn-danger ms-1 me-1'},
                preConfirm: () => {
                    
                   Mostrar_Ventana_Cargando(false);
                    var parametros = {"Fun":'"""+str(fernet.encrypt("Liberar_Operaciones".encode()).decode("utf-8"))+"""',"ID_Caja":ID_Caja};
                    $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                        success:  function (response)
                        {
                            var Resultado = JSON.parse(response);
                            if(Resultado["Estado"] == 1)
                            {
                                $("#Vent_1").modal("hide");
                                Mensaje(2);
                                Cargar_Fecha($("#fecha").val());
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
            function Documentos_WMS(ID_Caja,Caja){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-history'></i> Documentos WMS ["+Caja+"]");
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm');
                var parametros = {"Fun":'"""+str(fernet.encrypt("Documentos_WMS".encode()).decode("utf-8"))+"""',"ID_Caja":ID_Caja};
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
            function MGO_Actualizado(ID_Caja,Caja){
                Swal.fire({
                title: 'Estas segur@ de que ya está se actualizado la información de la caja  ['+Caja+'] en MGO?',
                buttonsStyling: false,showCancelButton: true,confirmButtonText: "<i class='mdi mdi-check'></i> Yes",cancelButtonText: "<i class='mdi mdi-close'></i> No",showLoaderOnConfirm: true,
                customClass: {confirmButton: 'btn btn-success ms-1 me-1',cancelButton: 'btn btn-danger ms-1 me-1'},
                preConfirm: () => {
                    
                   Mostrar_Ventana_Cargando(false);
                    var parametros = {"Fun":'"""+str(fernet.encrypt("MGO_Actualizado".encode()).decode("utf-8"))+"""',"ID_Caja":ID_Caja};
                    $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                        success:  function (response)
                        {
                            var Resultado = JSON.parse(response);
                            if(Resultado["Estado"] == 1)
                            {
                                $("#Vent_1").modal("hide");
                                Mensaje(2);
                                Cargar_Fecha($("#fecha").val());
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
            function Agregar_Adicional(){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-history'></i> Agregar adicional");
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm');
                var parametros = {"Fun":'"""+str(fernet.encrypt("Agregar_Adicional".encode()).decode("utf-8"))+"""'};
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
            function Crear_Programacion(){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-plus'></i> Crear Programación de Día");
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm');
                var parametros = {"Fun":'"""+str(fernet.encrypt("Crear_Programacion".encode()).decode("utf-8"))+"""'};
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
            function Enviar_Correo(ID,Caja){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-history'></i> Enviar Correos de CAJA LISTA  de la caja ["+Caja+"]");
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm');
                var parametros = {"Fun":'"""+str(fernet.encrypt("Enviar_Correo".encode()).decode("utf-8"))+"""',"ID":ID};
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
            function Re_Enviar_Correo(ID,Caja){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-history'></i> Re-Enviar Correos de CAJA LISTA  de la caja ["+Caja+"]");
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm');
                var parametros = {"Fun":'"""+str(fernet.encrypt("Re_Enviar_Correo".encode()).decode("utf-8"))+"""',"ID":ID};
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
            function Cancelar_Load_ID(Load_ID,ID){
                Swal.fire({
                title: 'Estas segur@ de cancelar este LOAD ID ['+Load_ID+']?',
                input: 'text',buttonsStyling: false,showCancelButton: true,confirmButtonText: "<i class='mdi mdi-check'></i> Yes",cancelButtonText: "<i class='mdi mdi-close'></i> No",showLoaderOnConfirm: true,
                customClass: {confirmButton: 'btn btn-success ms-1 me-1',cancelButton: 'btn btn-danger ms-1 me-1'},
                preConfirm: (Comentario) => {
                    
                    if(Comentario.trim() == ""){
                        Mensaje(1,"Agrega comentario");
                    }else{
                        Mostrar_Ventana_Cargando(false);
                        var parametros = {"Fun":'"""+str(fernet.encrypt("Cancelar_Load_ID".encode()).decode("utf-8"))+"""',"ID":ID,"Comentario":Comentario};
                        $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                            success:  function (response)
                            {
                                var Resultado = JSON.parse(response);
                                if(Resultado["Estado"] == 1)
                                {
                                    $("#Vent_1").modal("hide");
                                    Mensaje(2);
                                    Cargar_Fecha($("#fecha").val());
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
                })
            }

            function Folio_Prisma(Load_ID,Caja,ID){
                Swal.fire({
                title: 'Que folio de Prisma es para LOAD ID ['+Load_ID+'] y Caja ['+Caja+']?',
                input: 'text',buttonsStyling: false,showCancelButton: true,confirmButtonText: "<i class='mdi mdi-check'></i> Yes",cancelButtonText: "<i class='mdi mdi-close'></i> No",showLoaderOnConfirm: true,
                customClass: {confirmButton: 'btn btn-success ms-1 me-1',cancelButton: 'btn btn-danger ms-1 me-1'},
                preConfirm: (Comentario) => {
                    
                    if(Comentario.trim() == ""){
                        Mensaje(1,"Agrega comentario");
                    }else{
                        Mostrar_Ventana_Cargando(false);
                        var parametros = {"Fun":'"""+str(fernet.encrypt("Folio_Prisma".encode()).decode("utf-8"))+"""',"Load_ID":Load_ID,"Comentario":Comentario,"ID":ID};
                        $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                            success:  function (response)
                            {
                                var Resultado = JSON.parse(response);
                                if(Resultado["Estado"] == 1)
                                {
                                    $("#Vent_1").modal("hide");
                                    Mensaje(2);
                                    Cargar_Fecha($("#fecha").val());
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
                })
            }

            function Cancelar_Ruta(ID,Tipo,Ruta){
                Swal.fire({
                title: 'Estas seguro de Cacelar la Ruta ['+Tipo+' '+Ruta+']?',
                input: 'text',buttonsStyling: false,showCancelButton: true,confirmButtonText: "<i class='mdi mdi-check'></i> Yes",cancelButtonText: "<i class='mdi mdi-close'></i> No",showLoaderOnConfirm: true,
                customClass: {confirmButton: 'btn btn-success ms-1 me-1',cancelButton: 'btn btn-danger ms-1 me-1'},
                preConfirm: (Comentario) => {
                    
                    if(Comentario.trim() == ""){
                        Mensaje(1,"Agrega comentario");
                    }else{
                        Mostrar_Ventana_Cargando(false);
                        var parametros = {"Fun":'"""+str(fernet.encrypt("Cancelar_Ruta".encode()).decode("utf-8"))+"""',"ID":ID,"Comentario":Comentario};
                        $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                            success:  function (response)
                            {
                                var Resultado = JSON.parse(response);
                                if(Resultado["Estado"] == 1)
                                {
                                    $("#Vent_1").modal("hide");
                                    Mensaje(2);
                                    Cargar_Fecha($("#fecha").val());
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
                })
            }

        </script>
        </div>
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

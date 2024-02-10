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
                    <td class='text-center' style='width:40px;'><span style='writing-mode: vertical-lr;'>SALIDA</span></td>
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
                if Libera_Operaciones is not None:
                    Contenido += "<td class='align-middle text-center table-warning'><button onclick='Salida("+str(Programacion["cc_id"])+",\""+str(Programacion["cc_contenedor"])+"\")' class='btn btn-sm btn-success p-0 m-0 ps-1 pe-1 Pulsa_Div'><i class='mdi mdi-check'></i></button></td>"
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
        </div>
        """

        Cur += render_template("general.html",Contenido=Contenido,Componentes=Compartido.Complementos(None),Menu=Menu,Titulo=Titulo)
    except:
        Cur += str(sys.exc_info())
    return Cur
def Salida(Datos):
    DB = LibDM_2023.DataBase()
    Compartido_2023 = LibDM_2023.Compartido()
    Cur = ""
    Resultado = {"Contenido":"","Estado":0}
    Error = ""
    try:
        Error += DB.Instruccion("UPDATE "+str(BD_Nombre)+".ccajas SET cc_activo = 0,cc_fecha_hora_salida = NOW(), cc_ultimo_mov = NOW() WHERE cc_id = '"+str(Datos["ID"])+"' ")
        if Error == "":
            Info_Ahora = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".ccajas WHERE cc_id = '"+str(Datos["ID"])+"'")[0]
            Info_Ahora["cc_dock"] = 'null' if Info_Ahora["cc_dock"] is None else "'"+str(Info_Ahora["cc_dock"])+"'"
            Info_Ahora["cc_tipo_actual"] = 'null' if Info_Ahora["cc_tipo_actual"] is None else "'"+str(Info_Ahora["cc_tipo_actual"])+"'"
            Info_Ahora["cc_zona"] = 'null' if Info_Ahora["cc_zona"] is None else "'"+str(Info_Ahora["cc_zona"])+"'"
            Info_Ahora["cc_negocio"] = 'null' if Info_Ahora["cc_negocio"] is None else "'"+str(Info_Ahora["cc_negocio"])+"'"
            Error += DB.Instruccion(""" 
            INSERT INTO """+str(BD_Nombre)+""".ccajas_moviemiento
            (cch_master,cch_fecha_hora,cch_contenedor,cch_ubicacion,cch_informacion_actual,cch_dock,cch_tipo_actual,cch_zona,cch_negocio,cch_usuario,cch_movimiento)
            VALUES
            ('"""+str(Info_Ahora["cc_id"])+"""',NOW(),'"""+str(Info_Ahora["cc_contenedor"])+"""','"""+str(Info_Ahora["cc_ubicacion"])+"""','"""+str(Info_Ahora["cc_informacion_actual"])+"""',"""+str(Info_Ahora["cc_dock"])+""","""+str(Info_Ahora["cc_tipo_actual"])+""","""+str(Info_Ahora["cc_zona"])+""","""+str(Info_Ahora["cc_negocio"])+""",'"""+str(Datos["ID_User"])+"""','SALIDA')
            """)
        if Error == "":
            Resultado["Estado"] = 1

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

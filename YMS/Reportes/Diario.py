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
        Activo = "YMS"
        Compartido = LibDM_2023.Compartido()
        Menu = LibDM_2023.Menu().Menu(Activo,request.url_root,session["IDu"])
        Titulo = LibDM_2023.Menu().Get_Titulo(Activo)
        Contenido = ""
        Contenido += "<div class='h2 fw-lighter mt-1 mb-1 text-center border-bottom'><i class='mdi mdi mdi-book'></i> Daily Reports</div>"
        Formulario = {"Col":"12", "Campos": [],"Clase": "Buscar" }
        #Formulario["Campos"].append({"tipo":"texto","campo":"Container","titulo":"Container","Requerido":1,"min":1,"max":150,"valor":"","Col":6})
        Formulario["Campos"].append({"tipo":"fecha","campo":"Fecha de Rura","titulo":"Arrival Date","Requerido":1,"Col":12,"valor":"","editable":True})
        
        Contenido += "<div class='container'>"
        Contenido += str(Compartido.Formulario(Formulario))
        Contenido += """
        <div class='w-100 text-center mt-2'><button class='btn btn-primary w-75' onclick='Cargar_Reporte()'><i class='mdi mdi-cloud-download'></i> Download Report</button></div>
        <hr>
        <div id='Res'></div>
        """
        Contenido += """
        </div>
        <script>
            function Cargar_Reporte(){
                var Info = Dame_Formulario(".Buscar",true);
                if(Info != null)
                {
                    Mostrar_Ventana_Cargando(false);
                    var parametros = {"Fun":'"""+str(fernet.encrypt("Cargar_Reporte".encode()).decode("utf-8"))+"""',"Info":JSON.stringify(Info)};
                    $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                        success:  function (response)
                        {
                            var Resultado = JSON.parse(response);
                            $("#Res").html(Resultado["Contenido"]);
                            swal.close();
                                
                        },
                        error: function (jqXHR, textStatus, errorThrown )
                        {
                            Mensaje(0,textStatus);
                        }
                    });
                }
            }
            function Ver_Historico(ID,Contenedor){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-history'></i> History ["+Contenedor+"]");
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm').addClass('modal-xl');
                var parametros = {"Fun":'"""+str(fernet.encrypt("Ver_Historico".encode()).decode("utf-8"))+"""',"ID":ID};
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
        </script>
        """
        Cur += render_template("general.html",Contenido=Contenido,Componentes=Compartido.Complementos(None),Menu=Menu,Titulo=Titulo)
    except:
        Cur += str(sys.exc_info())
    return Cur

def Cargar_Reporte(Datos):
    DB = LibDM_2023.DataBase()
    Compartido_2023 = LibDM_2023.Compartido()
    Cur = ""
    Resultado = {"Contenido":"","Estado":0}
    try:
        Datos_Info = json.loads(str(Datos["Info"]))
        Cajas = []
        Cajas_2 = []
        Outbound = []
        Cajas_DB = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".ccajas WHERE DATE(cc_fecha_hora) = '"+str(Datos_Info["Fecha de Rura"])+"'")
        H_Str = []
        for C in Cajas_DB:
            H_Str.append("'"+str(C["cc_id"])+"'")
        Historial = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".ccajas_moviemiento WHERE cch_master IN ("+str(','.join(H_Str))+")")
        
        for Inbound in DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".ccajas_moviemiento where cch_tipo_actual = 'Inbound' and cch_movimiento  = 'ASIGNAR' and DATE(cch_fecha_hora) = '"+str(Datos_Info["Fecha de Rura"])+"'"):
            Tipo_Route = ""
            Route = ""
            Dock = ""
            Opciones = "<div class='btn-group' role='group' aria-label='Basic mixed styles example'>"
            Opciones += "<button class='btn btn-sm btn-primary p-0 ps-1 pe-1' onclick='Ver_Historico("+str(Inbound["cch_master"])+",\""+str(Inbound["cch_contenedor"])+"\")'><i class='mdi mdi-history'></i></button>"
            Opciones += "</div>"
            Info_H = json.loads(str(Inbound["cch_informacion_actual"]))
            Carrier = Info_H["Carrier"]
            Estado = "<span class='h-100 border' style='width:20px; background:var(--Color_"+str(Inbound["cch_tipo_actual"])+");Color:var(--Color_"+str(Inbound["cch_tipo_actual"])+");'>__</span>"
            try:
                Tipo = Info_H[Inbound["cch_tipo_actual"]]
                Tipo_Route = Tipo
                Estado += str(Tipo)
                Tipo_1 = Info_H[Tipo]
                Route = Tipo_1
                Estado += "/"+str(Tipo_1)
                Tipo_2 = Info_H[Tipo_1]
                Dock = Tipo_2
                Estado += "/"+str(Tipo_2)
            except:
                pass
            Cajas.append({"Contenedor":str(Inbound["cch_contenedor"]),"In Date":Inbound["cch_fecha_hora"].strftime("%Y-%m-%d %H:%M:%S"),"Route Type":Tipo_Route,"Route":Route,"Dock":Dock,"In Carrier":Carrier,'Opciones':Opciones})
        
        for Outbound in DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".ccajas_moviemiento where cch_tipo_actual = 'Outbound' and cch_movimiento  = 'SALIDA' and DATE(cch_fecha_hora) = '"+str(Datos_Info["Fecha de Rura"])+"'"):
            Tipo_Route = ""
            Route = ""
            Dock = ""
            Opciones = "<div class='btn-group' role='group' aria-label='Basic mixed styles example'>"
            Opciones += "<button class='btn btn-sm btn-primary p-0 ps-1 pe-1' onclick='Ver_Historico("+str(Outbound["cch_master"])+",\""+str(Outbound["cch_contenedor"])+"\")'><i class='mdi mdi-history'></i></button>"
            Opciones += "</div>"
            Info_H = json.loads(str(Outbound["cch_informacion_actual"]))
            Carrier = Info_H["Carrier"]
            Estado = "<span class='h-100 border' style='width:20px; background:var(--Color_"+str(Outbound["cch_tipo_actual"])+");Color:var(--Color_"+str(Outbound["cch_tipo_actual"])+");'>__</span>"
            try:
                Tipo = Info_H[Outbound["cch_tipo_actual"]]
                Tipo_Route = Tipo
                Estado += str(Tipo)
                Tipo_1 = Info_H[Tipo]
                Route = Tipo_1
                Estado += "/"+str(Tipo_1)
                Tipo_2 = Info_H[Tipo_1]
                Dock = Tipo_2
                Estado += "/"+str(Tipo_2)
            except:
                pass
            Cajas_2.append({"Contenedor":str(Outbound["cch_contenedor"]),"Out Date":Outbound["cch_fecha_hora"].strftime("%Y-%m-%d %H:%M:%S"),"Route Type":Tipo_Route,"Route":Route,"Dock":Dock,"Out Carrier":Carrier,'Opciones':Opciones})

            

                    
        Resultado["Contenido"] += """
        <h1>Inbound</h1>
        <div id='Tabla_Reporte' class='border border-dark bg-dark-subtle'></div>
        <script>
            delete Tabla_Reporte;
            var Tabla_Reporte = new Tabulator("#Tabla_Reporte", {
                minHeight:500,
                layout:"fitColumns",
                data:"""+str(Cajas)+""",
                columns:[
                    {field:"Contenedor","title":"Container"},
                    {field:"In Date","title":"Arrival Date"},
                    {field:"Route Type","title":"Route Type",formatter:"html"},
                    {field:"Route","title":"Route",formatter:"html"},
                    {field:"Dock","title":"Dock",formatter:"html"},
                    {field:"In Carrier","title":"Arrival Carrier"},
                    {field:"Opciones","title":"Op",formatter:"html"}
                ]
            });
            Tabla_Reporte.on("tableBuilt", function(){ 
                setTimeout(() => {
                    Tabla_Reporte.clearFilter();
                    Tabla_Reporte.redraw();
                }, 100);
            });
        </script>
        """
        Resultado["Contenido"] += """
        <h1>Outbound</h1>
        <div id='Tabla_Reporte_2' class='border border-dark bg-dark-subtle'></div>
        <script>
            delete Tabla_Reporte_2;
            var Tabla_Reporte_2 = new Tabulator("#Tabla_Reporte_2", {
                minHeight:500,
                layout:"fitColumns",
                data:"""+str(Cajas_2)+""",
                columns:[
                    {field:"Contenedor","title":"Container"},
                    {field:"Out Date","title":"Departure Date"},
                    {field:"Route Type","title":"Route Type",formatter:"html"},
                    {field:"Route","title":"Route",formatter:"html"},
                    {field:"Dock","title":"Dock",formatter:"html"},
                    {field:"Out Carrier","title":"Departure Carrier"},
                    {field:"Opciones","title":"Op",formatter:"html"}
                ]
            });
            Tabla_Reporte_2.on("tableBuilt", function(){ 
                setTimeout(() => {
                    Tabla_Reporte_2.clearFilter();
                    Tabla_Reporte_2.redraw();
                }, 100);
            });
        </script>
        """
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

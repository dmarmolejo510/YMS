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
        Contenedores_Patio = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".ccajas where cc_activo = 1")
        Patio = []
        for Contenedor in Contenedores_Patio:
            Info_Actual = json.loads(str(Contenedor["cc_informacion_actual"]))
            Opciones = ""
            UB = ""
            Estado = ""
            if Contenedor["cc_negocio"] is None:
                Opciones = "<div class='text-center'><button class='btn btn-primary btn-sm p-0 ps-1 pe-1' onclick='Asignar(\"ODC\","+str(Contenedor["cc_id"])+");'><i class='mdi mdi-hand-front-right'></i></button></div>"
                Contenedor["cc_tipo_actual"] = ""
                Estado = "Not assigned"
            else:
                UB = str(Contenedor["cc_negocio"])
                Estado += "<span class='h-100 border' style='width:20px; background:var(--Color_"+str(Contenedor["cc_tipo_actual"])+");Color:var(--Color_"+str(Contenedor["cc_tipo_actual"])+");'>__</span>"
                try:
                    Tipo = Info_Actual[Contenedor["cc_tipo_actual"]]
                    Estado += str(Tipo)
                    Tipo_1 = Info_Actual[Tipo]
                    Estado += "/"+str(Tipo_1)
                    Tipo_2 = Info_Actual[Tipo_1]
                    Estado += "/"+str(Tipo_2)
                except:
                    pass

            
            Patio.append({"Tiempo":"<span class='tiempo' tiempo='"+str(Contenedor["cc_ultimo_mov"])+"'></span>","Caja":str(Contenedor["cc_contenedor"]),"Carrier":Info_Actual["Carrier"],"Tipo":Contenedor["cc_tipo_actual"],"Estado":Estado,"Opciones":Opciones,"UB":UB})
        Contenido += "<div class='h2 fw-lighter mt-1 mb-1 text-center border-bottom'><i class='mdi mdi-car-brake-parking'></i> Yard</div>"
        Contenido += """
        <div class='container'>
        <div id='Tabla_Patio' class='border border-dark bg-dark-subtle'></div>
        <script>
            delete Tabla_Patio;
            var Tabla_Patio = new Tabulator("#Tabla_Patio", {
                minHeight:800,
                layout:"fitColumns",
                data:"""+str(Patio)+""",
                rowFormatter:function(row){
                    if(row.getData().Estado == "Not assigned"){
                        $(row.getElement()).find('div').eq(5).addClass('text-danger fw-bold');
                        if(row.getPosition()%2)
                            row.getElement().style.backgroundColor = "#F8D7DA";
                        else
                            row.getElement().style.backgroundColor = "#f7afb5";
                    }
                },
                columns:[
                    {field:"Tiempo","title":"Last Movement",formatter:"html"},
                    /*{field:"UB","title":"UB"},*/
                    {field:"Caja","title":"Container",headerFilter:"input"},
                    {field:"Carrier","title":"Carrier"},
                    {field:"Tipo","title":"Type"},
                    {field:"Estado","title":"Status",formatter:"html"}
                ]
            });
            Tabla_Patio.on("tableBuilt", function(){ 
                setTimeout(() => {
                    Tabla_Patio.clearFilter();
                    Tabla_Patio.redraw();
                }, 100);
            });
        </script>
        <script>
            $( document ).ready(function() {
                setInterval(Actualizar_Hora_Final, 500)
            });
            function Actualizar_Hora_Final()
            {
                $(".tiempo").each(function() {
                    var Limite = moment($(this).attr('tiempo'));
                    var Ahora = moment(new Date()); //todays date
                    //var Faltan = moment.duration(Ahora.diff(Limite));
                    var Faltan = moment.duration(Limite.diff(Ahora));
                    var Dias = Faltan.asDays().toString().split(".")[0];
                    if(Dias < 0)
                        Dias = Dias*-1
                    var Horas = Faltan.hours();
                    if(Horas < 0)
                        Horas = Horas*-1
                    if(Horas.toString().length == 1)
                        Horas = "0"+Horas;
                    var Minutos = Faltan.minutes();
                        if(Minutos < 0)
                        Minutos = Minutos*-1
                    if(Minutos.toString().length == 1)
                        Minutos = "0"+Minutos;
                    var Segundos = Faltan.seconds();
                    if(Segundos < 0)
                        Segundos = Segundos*-1
                    if(Segundos.toString().length == 1)
                        Segundos = "0"+Segundos;
                    if (Dias == 0)
                        $(this).html("<b>" + Horas +":" + Minutos +":"+ Segundos +"</b>")
                    else
                        $(this).html("<b>" + Dias + " Days, " + Horas +":" + Minutos +":"+ Segundos +"</b>")

                });

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

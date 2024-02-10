from flask import request,session,render_template
from cryptography.fernet import Fernet
from datetime import datetime,date,timedelta
import sys
import json
import os
from Componentes import LibDM_2023
Url = ""
fernet = Fernet(LibDM_2023.Compartido().Dame_K2())
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
        Contenido += "<div class='h2 fw-lighter mt-1 mb-1 text-center border-bottom'><i class='mdi mdi-feature-search'></i> Container Search</div>"
        Formulario = {"Col":"12", "Campos": [],"Clase": "Buscar" }
        Formulario["Campos"].append({"tipo":"texto","campo":"Container","titulo":"Container","Requerido":1,"min":1,"max":150,"valor":"","Col":4})
        Formulario["Campos"].append({"tipo":"fecha","campo":"Fecha de Rura","titulo":"In Date","Requerido":0,"Col":4,"valor":"","editable":True})
        Formulario["Campos"].append({"tipo":"seleccion","campo":"Carrier","titulo":"Carrier","Requerido":0,"Tipo_Opciones":"Query","Opciones":"SELECT cca_nombre as Valor, cca_nombre as Texto FROM wtc_slp_test.ccarrier ","valor":"","Col":4})
        
        Contenido += "<div class='container'>"
        Contenido += str(Compartido.Formulario(Formulario))
        Contenido += """
        <div class='w-100 text-center mt-2'><button class='btn btn-primary w-75' onclick='Buscar_Caja()'><i class='mdi mdi-cloud-download'></i> Download</button></div>
        <hr>
        <div id='Res'></div>
        """
        Contenido += """
        </div>
        <script>
            function Buscar_Caja(){
                var Info = Dame_Formulario(".Buscar",true);
                if(Info != null)
                {
                    Mostrar_Ventana_Cargando(false);
                    var parametros = {"Fun":'"""+str(fernet.encrypt("Buscar_Caja".encode()).decode("utf-8"))+"""',"Info":JSON.stringify(Info)};
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
                $.ajax({data:  parametros,url:\""""+str(request.url_root)+"""/ODC/Container_Control\",type:  "post",
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

from flask import request,session,render_template
from cryptography.fernet import Fernet
import sys
import hashlib
import json
from Componentes import LibDM_2023
def Inicio():
    try:
        session.clear
        session.pop("IDu")
        session.pop("K")
    except:
        pass
    Test = ""
    fernet = Fernet(LibDM_2023.Compartido().Dame_K2())
    Cur = ""
    try:
        Compartido = LibDM_2023.Compartido()
        Contenido = """
        <script>
        function Entrar()
        {   
            Mostrar_Ventana_Cargando(false);
             $("#Error").hide();
            if ($("#User").val().trim() == "" || $("#Pwr").val().trim() == "")
            {
                $("#Error").html('Add User,Email / Password.')
                $("#Error").show();
                swal.close();
            }
            $("#Formulario").attr('disabled',true);
            var parametros = {"Fun":'"""+str(fernet.encrypt("Entrar".encode()).decode("utf-8"))+"""', "Usr":$("#User").val().trim(), "Pass":$("#Pwr").val().trim()};
            $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                success:  function (response)
                {
                   alert(response);
                   var Resultado = JSON.parse(response);
                        if(Resultado["Estado"] == 1)
                        {
                            $(location).attr('href','ToDo');
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
                    $("#Error").html(textStatus);
                    $("#Error").show();
                    swal.close();
                }
            });
        }
        </script>
        """
        Cur += render_template("inicio_sesion.html",Contenido=Contenido,Componentes=Compartido.Complementos(None),Test=Test)
    except:
        Cur += str(sys.exc_info())
    return Cur
def Entrar(Datos):
    Cur = ""
    DB = LibDM_2023.DataBase()
    Resultado = {"Estado":0, "Contenido":""}
    try:
        Res = DB.Get_Dato("SELECT * FROM universal_yms.cuser WHERE (UPPER(cususuario) = '"+str(Datos["Usr"]).upper()+"' or UPPER(cuscorreo) = '"+str(Datos["Usr"]).upper()+"') AND cpss_2 = '"+str(hashlib.md5(str(Datos["Pass"]).encode('utf-8')).hexdigest())+"'")
        # if len(Res) > 0:
        #     Resultado["Estado"] = 1
        #     session["IDu"] = str(Res[0]["cusrid"])
        #     session["K"] = str(Fernet.generate_key().decode())
        Resultado["Contenido"] = str(Res)
    except:
        Resultado["Contenido"] = str(sys.exc_info())
    Cur += json.dumps(Resultado)
    return Cur
def Direccionar(Datos):
    try:
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
                return globals()[Funcion](Par)
            else:
                return Inicio()
    except:
        return str(sys.exc_info())

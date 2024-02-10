from flask import request,session,render_template,current_app
from cryptography.fernet import Fernet
import sys
import json
import os
from Componentes import LibDM_2023
Url = ""
#PATH_DIR = str(current_app.root_path).replace("\\","/")
def Inicio():
    # fernet = Fernet(LibDM_2023.Compartido().Dame_K2())
    # if "K" in session.keys():
    #     fernet = Fernet(session["K"])
    Cur = ""
    try:
        Activo = "To Do"
        # Compartido = LibDM_2023.Compartido()
        # Menu = LibDM_2023.Menu().Menu(Activo,request.url_root,session["IDu"])
        # Titulo = LibDM_2023.Menu().Get_Titulo(Activo)
        # Contenido = """
        # <div class='row h-100 me-1'>
        #     <div class='col border Completar p-0' id='ToDo' completo=0></div>
        #     <div class='col-2 border Completar p-0' id='News' style='box-shadow: rgba(14, 30, 37, 0.12) 0px 2px 4px 0px, rgba(14, 30, 37, 0.32) 0px 2px 16px 0px;' completo=1></div>
        # </div>
        # <script>
        #     Mostrar_Ventana_Cargando(true);
        #     function ToDo(){
        #         var parametros = {"Fun":'"""+str(fernet.encrypt("ToDo".encode()).decode("utf-8"))+"""',"Activo":"To Do"};
        #         $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
        #             success:  function (response)
        #             {
        #                 var Resultado = JSON.parse(response);
        #                 $("#ToDo").html(Resultado["Contenido"]).attr('completo',1);
        #             },
        #             error: function (jqXHR, textStatus, errorThrown )
        #             {
        #                 $("#ToDo").html(textStatus).attr('completo',1);
        #             }
        #         });
        #     }
        #     function News(){
        #         var parametros = {"Fun":'"""+str(fernet.encrypt("News".encode()).decode("utf-8"))+"""'};
        #         $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
        #             success:  function (response)
        #             {
        #                 var Resultado = JSON.parse(response);
        #                 $("#News").html(Resultado["Contenido"]).attr('completo',1);
        #             },
        #             error: function (jqXHR, textStatus, errorThrown )
        #             {
        #                 $("#News").html(textStatus).attr('completo',1);
        #             }
        #         });
        #     }

        #     function ToDo_Actualizar(){
        #         Mostrar_Ventana_Cargando(false);
        #         var parametros = {"Fun":'"""+str(fernet.encrypt("ToDo".encode()).decode("utf-8"))+"""',"Activo":"To Do"};
        #         $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
        #             success:  function (response)
        #             {
        #                 var Resultado = JSON.parse(response);
        #                 $("#ToDo").html(Resultado["Contenido"]).attr('completo',1);
        #                 swal.close();
        #             },
        #             error: function (jqXHR, textStatus, errorThrown )
        #             {
        #                 $("#ToDo").html(textStatus).attr('completo',1);
        #                 swal.close();
        #             }
        #         });
        #     }
        # </script>
        # """
        # Cur += render_template("general.html",Contenido=Contenido,Componentes=Compartido.Complementos(None),Menu=Menu,Titulo=Titulo)
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

from flask import request,session,render_template
from cryptography.fernet import Fernet
import sys
import json
import os
from Componentes import LibDM_2023
Url = ""
def Inicio():
    fernet = Fernet(LibDM_2023.Compartido().Dame_K2())
    if "K" in session.keys():
        fernet = Fernet(session["K"])
    Cur = ""
    try:
        Activo = "To Do"
        Compartido = LibDM_2023.Compartido()
        Menu = LibDM_2023.Menu().Menu(Activo,request.url_root,session["IDu"])
        Titulo = LibDM_2023.Menu().Get_Titulo(Activo)
        Contenido = """
        <div class='row h-100 me-1'>
            <div class='col border Completar p-0' id='ToDo' completo=0></div>
            <div class='col-2 border Completar p-0' id='News' style='box-shadow: rgba(14, 30, 37, 0.12) 0px 2px 4px 0px, rgba(14, 30, 37, 0.32) 0px 2px 16px 0px;' completo=1></div>
        </div>
        <script>
            Mostrar_Ventana_Cargando(true);
            function ToDo(){
                var parametros = {"Fun":'"""+str(fernet.encrypt("ToDo".encode()).decode("utf-8"))+"""',"Activo":"To Do"};
                $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                    success:  function (response)
                    {
                        var Resultado = JSON.parse(response);
                        $("#ToDo").html(Resultado["Contenido"]).attr('completo',1);
                    },
                    error: function (jqXHR, textStatus, errorThrown )
                    {
                        $("#ToDo").html(textStatus).attr('completo',1);
                    }
                });
            }
            function News(){
                var parametros = {"Fun":'"""+str(fernet.encrypt("News".encode()).decode("utf-8"))+"""'};
                $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                    success:  function (response)
                    {
                        var Resultado = JSON.parse(response);
                        $("#News").html(Resultado["Contenido"]).attr('completo',1);
                    },
                    error: function (jqXHR, textStatus, errorThrown )
                    {
                        $("#News").html(textStatus).attr('completo',1);
                    }
                });
            }
            ToDo();
            News();

            function ToDo_Actualizar(){
                Mostrar_Ventana_Cargando(false);
                var parametros = {"Fun":'"""+str(fernet.encrypt("ToDo".encode()).decode("utf-8"))+"""',"Activo":"To Do"};
                $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                    success:  function (response)
                    {
                        var Resultado = JSON.parse(response);
                        $("#ToDo").html(Resultado["Contenido"]).attr('completo',1);
                        swal.close();
                    },
                    error: function (jqXHR, textStatus, errorThrown )
                    {
                        $("#ToDo").html(textStatus).attr('completo',1);
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
def ToDo(Datos):
    DB = LibDM_2023.DataBase()
    Resultado = {"Contenido":"","Estado":0}
    Cur = ""
    try:
        Resultado["Contenido"] += """
        <div class='w-100 h-100 position-relative'>
            <div class='row p-5'>
        """
        Resultado["Contenido"] += """
            </div>
        </div>
        <script>
            function Ver_Detalle(Icono,Nombre,Codigo,Aplicar){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi "+Icono+"'></i> " + Nombre);
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm').addClass('modal-xl');
                var parametros = {"Fun":"Ver_Detalle","Codigo":Codigo,"Aplicar":Aplicar };
                $.ajax({data:  parametros,url:\""""+str(os.path.basename(__file__))+"""\",type:  "post",
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
        Resultado["Contenido"] += str(sys.exc_info())
    Cur += json.dumps(Resultado)
    return Cur
def News(Datos):
    DB = LibDM_2023.DataBase()
    Resultado = {"Contenido":"","Estado":0}
    Cur = ""
    try:
        Resultado["Contenido"] += """
        <div style='height:60%;' class='border w-100' style='box-shadow: rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset;'>
        """
        
        Resultado["Contenido"] += """
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
            <script>
                 $(document).ready(function() {
                   $('.carousel_1').carousel();
                 });

                 function Ver_Imagen(Imagen)
                 {
                    $("#Ventana").modal("show").find(".modal-body").html("<img src='"+Imagen+"' class='img-fluid'>").parent().find(".modal-title").html("<i class='mdi mdi-image'></i> News");
                 }
            </script>
        """

        Resultado["Contenido"] += """
        </div>
        <div style='height:20%;' class='border'>
        """
        Resultado["Contenido"] += """
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleDar_2" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleDar_2" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
            <script>
                 $(document).ready(function() {
                   $('.carousel_2').carousel({
                     interval: 3500
                   })
                 });
            </script>
        """

        Resultado["Contenido"] += """
        </div>
        <div style='height:20%;' class='border p-1' >
            <div class="ratio ratio-21x9 h-100 w-100" style='box-shadow: rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset;'>
                <iframe allowfullscreen
                    src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAFX1yVDt3U&#x2F;view?embed">
                </iframe>
            </div>
        """
        Resultado["Contenido"] += """
        </div>
        """

    except:
        Resultado["Contenido"] += str(sys.exc_info())
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

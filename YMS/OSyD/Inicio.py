from flask import request,session,render_template
from cryptography.fernet import Fernet
from datetime import datetime,date,timedelta
import sys
import json
import os
from Componentes import LibDM_2023
Url = ""
BD_Nombre = "public"
Bandera_Dock = "YMS"
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

        Compartido += """<div class='text-end pe-1 pt-1'><small class='link-primary' style='cursor:pointer' onclick='Llamar_Funcion(\""""+str(request.url)+"""\");'>Actualizar <i class='mdi mdi-refresh'></i></small></div>"""
        Compartido += "<div class='h2 fw-lighter mt-1 mb-1 text-center border-bottom'><i class='mdi mdi-alert'></i> OS&D</div>"
        Compartido += """
        <div class='container-fluid'>
             <ul class="nav nav-tabs nav-fill">
                <li class="nav-item">
                    <a id='Tab_Abierto' class="nav-link active bg-primary fw-bold text-light" href="#" onclick='Cargar_Abiertos()'>OS&D Abiertos <span class="badge text-bg-secondary"></span></a>
                </li>
                <li class="nav-item">
                    <a id='Tab_Liberados' class="nav-link" href="#" onclick='Cargar_Liberados()'>OS&D Liberados <span class="badge text-bg-secondary"></span></a>
                </li>
                <li class="nav-item">
                    <a id='Tab_Reporte' class="nav-link" href="#" onclick='Cargar_Menu_Reporte()'>OS&D Reporte</a>
                </li>
            </ul>
            <div id='Res'></div>
        </div>
        <style>
            .tabulator .tabulator-row.tabulator-selectable:hover .tabulator-cell{
                background-color: rgba(255, 221, 221, 1)
            }
            .tabulator-row .tabulator-cell[tabulator-field="Ultimo Comentario"] {
                white-space: pre-wrap;
            }
        </style>
        <script>
            $( document ).ready(function() {
               Cargar_Abiertos();
            });
            function Cargar_Abiertos(){
                Mostrar_Ventana_Cargando(false);
                $(".nav-link").removeClass('active bg-primary fw-bold text-light');
                $("#Tab_Abierto").addClass('active bg-primary fw-bold text-light');
                var parametros = {"Fun":'"""+str(fernet.encrypt("Cargar_Abiertos".encode()).decode("utf-8"))+"""'};
                $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                    success:  function (response)
                    {
                        var Resultado = JSON.parse(response);
                        $("#Res").html(Resultado["Contenido"]);
                        swal.close();
                    },
                    error: function (jqXHR, textStatus, errorThrown ){Mensaje(0,'Process error ['+ jqXHR.status + " | " + textStatus  + " | " + errorThrown +']');}
                });
            }
            function Cargar_Liberados(){
                Mostrar_Ventana_Cargando(false);
                $(".nav-link").removeClass('active bg-primary fw-bold text-light')
                $("#Tab_Liberados").addClass('active bg-primary fw-bold text-light')
                $("#Res").html("Loading...");
                var parametros = {"Fun":'"""+str(fernet.encrypt("Cargar_Liberados".encode()).decode("utf-8"))+"""'};
                $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                    success:  function (response)
                    {
                        var Resultado = JSON.parse(response);
                        $("#Res").html(Resultado["Contenido"]);
                        swal.close();
                    },
                    error: function (jqXHR, textStatus, errorThrown )
                    {
                        Swal.fire({icon: 'error',position: 'top-end',title: 'Process error ['+ jqXHR.status + " | " + textStatus  + " | " + errorThrown +']',showConfirmButton: false,toast: true,background : "#fac9c9",timer: 3500,timerProgressBar: true});
                    }
                });
            }
            function Ver_Detalle(IDMaster){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm').addClass('modal-lg')
                $("#Vent_1").modal("show").find(".modal-body").html("<div class='w-100 text-center'><div class='spinner-grow' role='status'></div><b> Loading...</b></div>").parent().find(".modal-title").html(pad(IDMaster,5));
                var parametros = {"Fun":'"""+str(fernet.encrypt("Ver_Detalle".encode()).decode("utf-8"))+"""',"IDMaster":IDMaster};
                $.ajax({data:  parametros,url:   \""""+str(request.url)+"""\",
                    type:  "post",
                    success:  function (response){ var Resultado = JSON.parse(response); $("#Vent_1").find(".modal-body").html(Resultado["Contenido"]); swal.close();},
                    error: function (jqXHR, textStatus, errorThrown ){Mensaje(0,'Process error ['+ jqXHR.status + " | " + textStatus  + " | " + errorThrown +']');}
                });
            }
            function Generar_Archivo_Ruteo(IDMaster){
                Mostrar_Ventana_Cargando(false);
                var parametros = {"Fun":'"""+str(fernet.encrypt("Generar_Archivo".encode()).decode("utf-8"))+"""',"IDMaster":IDMaster};
                $.ajax({data:  parametros,url:   \""""+str(request.url)+"""\",
                    type:  "post",
                    success:  function (response){ 
                        var Resultado = JSON.parse(response);
                        if(Resultado["Estado"] == 1){
                            swal.close();
                            var win = window.open(Resultado["Archivo"], '_blank');
                            win.focus();
                        }else{
                            Swal.fire({icon: 'error',position: 'top-end',title: 'Process error ['+ Resultado["Contenido"] +']',showConfirmButton: false,toast: true,background : "#fac9c9",timer: 3500,timerProgressBar: true});
                        }
                    },
                   error: function (jqXHR, textStatus, errorThrown ){Mensaje(0,'Process error ['+ jqXHR.status + " | " + textStatus  + " | " + errorThrown +']');}
                });
            }
            function pad(num, size) {
                num = num.toString();
                while (num.length < size) num = "0" + num;
                return num;
            }
            function Ver_Historico(ID,Folio){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm').addClass('modal-lg')
                $("#Vent_1").modal("show").find(".modal-body").html("<div class='w-100 text-center'><div class='spinner-grow' role='status'></div><b> Loading...</b></div>").parent().find(".modal-title").html("<i class='mdi mdi-history'></i> History ["+Folio+"]");
                var parametros = {"Fun":'"""+str(fernet.encrypt("Ver_Historico".encode()).decode("utf-8"))+"""',"ID":ID};
                $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                    type:  "post",
                    success:  function (response){var Resultado = JSON.parse(response); $("#Vent_1").find(".modal-body").html(Resultado["Contenido"]);swal.close();},
                    error: function (jqXHR, textStatus, errorThrown ){Mensaje(0,'Process error ['+ jqXHR.status + " | " + textStatus  + " | " + errorThrown +']');}
                });
            }
            function Cargar_Menu_Reporte(){
                Mostrar_Ventana_Cargando(false);
                $(".nav-link").removeClass('active bg-primary fw-bold text-light')
                $("#Tab_Reporte").addClass('active bg-primary fw-bold text-light')
                $("#Res").html("Loading...");
                var parametros = {"Fun":'"""+str(fernet.encrypt("Cargar_Menu_Reporte".encode()).decode("utf-8"))+"""'};
                $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                    success:  function (response)
                    {
                        var Resultado = JSON.parse(response);
                        $("#Res").html(Resultado["Contenido"]);
                        swal.close();
                    },
                    error: function (jqXHR, textStatus, errorThrown )
                    {
                        Swal.fire({icon: 'error',position: 'top-end',title: 'Process error ['+ jqXHR.status + " | " + textStatus  + " | " + errorThrown +']',showConfirmButton: false,toast: true,background : "#fac9c9",timer: 3500,timerProgressBar: true});
                    }
                });
            }
        </script>
        """

        Cur += render_template("general.html",Contenido=Contenido,Componentes=Compartido.Complementos(None),Menu=Menu,Titulo=Titulo)
    except:
        Cur += str(sys.exc_info())
    return Cur
def Cargar_Abiertos(Datos):
    if "K" in session.keys():
        fernet = Fernet(session["K"])
    DB = LibDM_2023.DataBase()
    Compartido_2023 = LibDM_2023.Compartido()
    Cur = ""
    Resultado = {"Contenido":"","Estado":0}
    try:
        Contador_Abierto = {"valor":0,"clase":"text-bg-secondary"}
        Contador_Liberados = {"valor":0,"clase":"text-bg-secondary"}
        Contador_Pre_Liberados = {"valor":0,"clase":"text-bg-secondary"}
        Resultado["Contenido"] += "<div class='h3 text-center mt-2'>OS&D Abiertos</div>"
        Tabla_Datos_Ruteo = []

        Proveedores = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".cproveedores")
        
        Tabla_Datos_Porduccion = []
        Tabla_Datos_Cerrados = []
        for PakingSplip in DB.Get_Dato("""
        select MASTER.*,PARTES.*,
        (select HIS.cosyd_fecha from """+str(BD_Nombre)+""".cosyd_historico as HIS where HIS.cosyd_master = MASTER.cosyd_id  order by cosyd_fecha desc limit 1) as Fecha_Ultimo,
        (select HIS.cosyd_usuario  from """+str(BD_Nombre)+""".cosyd_historico as HIS where HIS.cosyd_master = MASTER.cosyd_id  order by cosyd_fecha desc limit 1) as Usuario,
        (select HIS.cosyd_movimiento from """+str(BD_Nombre)+""".cosyd_historico as HIS where HIS.cosyd_master = MASTER.cosyd_id  order by cosyd_fecha desc limit 1) as Tipo,
        (select HIS.cosyd_evidencia  from """+str(BD_Nombre)+""".cosyd_historico as HIS where HIS.cosyd_master = MASTER.cosyd_id  order by cosyd_fecha desc limit 1) as Evidencia
        FROM """+str(BD_Nombre)+""".cosyd  MASTER 
        left join """+str(BD_Nombre)+""".cosyd_partes PARTES ON PARTES.cosyd_master = MASTER.cosyd_id
        WHERE MASTER.cosyd_estado IN (1,2,4)
        group by MASTER.cosyd_id
        """):
            if int(PakingSplip["cosyd_estado"]) == 1:
                Contador_Abierto["valor"] += 1
            if int(PakingSplip["cosyd_estado"]) == 2:
                Contador_Liberados["valor"] += 1
            if int(PakingSplip["cosyd_estado"]) == 4:
                Contador_Pre_Liberados["valor"] += 1
            OK = 0
            Numeros = 0
            Problemas = []
            Historico = int(DB.Get_Dato("SELECT COUNT(*) AS Numero FROM "+str(BD_Nombre)+".cosyd_historico WHERE cosyd_master = '"+str(PakingSplip["cosyd_id"])+"'")[0]["Numero"])
            for Partes in DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".cosyd_partes WHERE cosyd_master = '"+str(PakingSplip["cosyd_id"])+"'"):
                if int(Partes["cosyd_p_1_damage"]) == 1 and "1. Damage" not in Problemas:
                    Problemas.append("1. Damage")
                if int(Partes["cosyd_p_2_shortage"]) == 1 and "2. Shortage" not in Problemas:
                    Problemas.append("2. Shortage")
                if int(Partes["cosyd_p_3_surplus"]) == 1 and "3. Surplus" not in Problemas:
                    Problemas.append("3. Surplus")
                if int(Partes["cosyd_p_4_asn_Issue"]) == 1 and "4. ASN Issue" not in Problemas:
                    Problemas.append("4. ASN Issue")
                if int(Partes["cosyd_p_5_missing_doc_in_prisma"]) == 1 and "5. Missing doc in Prisma" not in Problemas:
                    Problemas.append("5. Missing doc in Prisma")
                Numeros += 1
            for K in PakingSplip.keys():
                if PakingSplip[K] is None:
                    PakingSplip[K]  = ""
            Aux_Datos = {}
            Aux_Datos["Estado"] = OK
            Opciones = """
            <div class="btn-group btn-group-sm" role="group">

            <button class='btn btn-warning btn-sm p-0 ps-1 pe-1' onclick='Ver_Historico("""+str(PakingSplip["cosyd_id"])+""",\""""+str(PakingSplip["cosyd_id"]).zfill(5)+"""\");'><i class='mdi mdi-history'></i></button>
            """
            if Numeros == 0:
                Aux_Datos["Estado"] = 2
                Opciones += """
                <button class='btn btn-primary btn-sm p-0 ps-1 pe-1' onclick='Completar_Ruteo("""+str(PakingSplip["cosyd_id"])+""");'><i class='mdi mdi-file-document-edit'></i></button>
                """
                if Historico == 1:
                    Opciones += """<button class='btn btn-danger btn-sm p-0 ps-1 pe-1' onclick='Eliminar_Ruteo("""+str(PakingSplip["cosyd_id"])+""",\""""+str(PakingSplip["cosyd_id"]).zfill(5)+"""\");'><i class='mdi mdi-trash-can'></i></button>"""
            else:
                Opciones += """
                <button class='btn btn-primary btn-sm p-0 ps-1 pe-1' onclick='Modificar_Ruteo("Editar","""+str(PakingSplip["cosyd_id"])+""",\""""+str(PakingSplip["cosyd_id"]).zfill(5)+"""\",\"ABIERTOS\",\""""+str(",".join(Problemas))+"""\");'><i class='mdi mdi-file-document-edit'></i></button>
                <button class='btn btn-dark btn-sm p-0 ps-1 pe-1' onclick='Generar_Archivo_Ruteo("""+str(PakingSplip["cosyd_id"])+""");'><i class='mdi mdi-printer'></i></button>
                """
                if Historico == 1:
                    Opciones += """<button class='btn btn-danger btn-sm p-0 ps-1 pe-1' onclick='Eliminar_Ruteo("""+str(PakingSplip["cosyd_id"])+""",\""""+str(PakingSplip["cosyd_id"]).zfill(5)+"""\");'><i class='mdi mdi-trash-can'></i></button>"""
            Opciones += """
            </div>"""
            Aux_Datos[" "] = str(Opciones)
            
            Lleva = ""
            Diff = datetime.now() - PakingSplip["Fecha_Ultimo"]
            if Diff.days > 0:
                Lleva += str(Diff.days)+" Day(s) "
            segundos = Diff.seconds
            horas, segundos = divmod(segundos, 3600)
            minutos, segundos = divmod(segundos, 60)

            if len(str(horas)) == 1:
                horas = "0"+str(horas)
            if len(str(minutos)) == 1:
                minutos = "0"+str(minutos)
            if len(str(segundos)) == 1:
                segundos = "0"+str(segundos)
            Lleva += str(horas)+":"+str(minutos)+":"+str(segundos)

            Aux_Datos["Ultima modificacion"] = str(Lleva)
            Aux_Datos["Folio"] = str(PakingSplip["cosyd_id"]).zfill(5)

            Aux_Datos["Ruta"] = str(PakingSplip["cosyd_ruta"]) + " ["+str(PakingSplip["cosyd_ruta_fecha_hora"])+"]"
            Aux_Datos["Fecha de Ruta"] = str(PakingSplip["cosyd_ruta_fecha_hora"])

            Aux_Datos["Fecha Alta"] = str(PakingSplip["cosyd_alta"])
            # if PakingSplip["cosyd_fecha_envio"] is not None and PakingSplip["cosyd_fecha_envio"] != "":
            #     Aux_Datos["Fecha de envío del proveedor"] = PakingSplip["cosyd_fecha_envio"].strftime("%y-%m-%d")
            Aux_Datos["Fecha de envío del proveedor"] = ""
            Aux_Datos["Proveedor"] = PakingSplip["cosyd_proveedor"]
            #Aux_Datos["PackingSlip"] = "<a class='link-primary' style='cursor:pointer' onclick='Ver_Detalle("+str(PakingSplip["cosyd_id"])+",\""+str(PakingSplip["cosyd_packingslip"])+"\")'>"+str(PakingSplip["cosyd_packingslip"])+"</a>"
            #Aux_Datos["Packing Slip"] = str(PakingSplip["cosyd_packingslip"])

            Aux_Datos["Problema"] = str(",".join(Problemas))

            if PakingSplip["Fecha_Ultimo"] is None or "Fecha_Ultimo" not in PakingSplip.keys():
                PakingSplip["Fecha_Ultimo"] = datetime.now()
            

            Aux_Datos["Destino"] = PakingSplip["cosyd_p_destino"]
            Aux_Datos["Contenedor"] = PakingSplip["cosyd_caja"]
            Aux_Datos["SCAC"] = PakingSplip["cosyd_scac"]
            Clase_Hora = ""
            if DB.Dame_Hora() <= PakingSplip["Fecha_Ultimo"] + timedelta(minutes=30):
                Clase_Hora = "text-bg-success"
            elif DB.Dame_Hora() <= PakingSplip["Fecha_Ultimo"] + timedelta(minutes=60):
                Clase_Hora = "text-bg-warning"
            elif DB.Dame_Hora() >= PakingSplip["Fecha_Ultimo"] + timedelta(hours=3):
                Clase_Hora = "Pulsa_Texto_Rojo"
            else:
                Clase_Hora = 'text-muted'

            Aux_Datos["Ultimo Comentario"] = "<small><span class='"+str(Clase_Hora)+" ps-1 pe-1 fw-lighter'>"+str(PakingSplip["Fecha_Ultimo"])+"</span> <span class='fw-bold'>"+str(DB.Dame_Nombre_IDUsuario(PakingSplip["Usuario"])) + "</span></small><br>"+str(PakingSplip["cosyd_comentario"])
            Aux_Datos["Numeros"] = "<a class='link-primary' style='cursor:pointer' onclick='Ver_Detalle("+str(PakingSplip["cosyd_id"])+")'>"+str(Numeros)+"</a>" 
            Aux_Datos["Numeros_de_Parte"] = str(Numeros)
            Aux_Datos["Archivos"] = ""
            Aux_Datos["Packing_Slip"] = PakingSplip["cosyd_p_pakingslip"]
            for Archivo in str(PakingSplip["Evidencia"]).split(","):
                if Archivo.strip() != "":
                    if "pdf" in Archivo:
                        Aux_Datos["Archivos"] += "<a href='http://10.4.7.219:8080/Portal_File/"+str(Archivo)+"' target='_blank' class='mdi mdi-file-pdf-box ms-1'></a>"
                    else:
                        Aux_Datos["Archivos"] += "<a href='http://10.4.7.219:8080/Portal_File/"+str(Archivo)+"' target='_blank' class='mdi mdi-image ms-1'></a>"

            
            if str(PakingSplip["cosyd_tipo"]) == "RUTEO" and int(PakingSplip["cosyd_estado"]) == 1:
                Tabla_Datos_Ruteo.append(Aux_Datos)
            if str(PakingSplip["cosyd_tipo"]) == "PRODUCCION" and int(PakingSplip["cosyd_estado"]) == 1:
                Tabla_Datos_Porduccion.append(Aux_Datos)
            if int(PakingSplip["cosyd_estado"]) != 1:
                Aux_Datos[" "] = """<button class='btn btn-warning btn-sm p-0 ps-1 pe-1' onclick='Ver_Historico("""+str(PakingSplip["cosyd_id"])+""",\""""+str(PakingSplip["cosyd_id"]).zfill(5)+"""\");'><i class='mdi mdi-history'></i></button>"""
                Aux_Datos["Cerrado"] = str(PakingSplip["cosyd_baja"])
                Aux_Datos["Tipo"] = str(PakingSplip["cosyd_tipo"])
                if int(PakingSplip["cosyd_estado"]) == 0: 
                    Aux_Datos["Estado"] = 3
                Tabla_Datos_Cerrados.append(Aux_Datos)
        
        if Contador_Abierto["valor"] > 0:
            Contador_Abierto["clase"] = "text-bg-danger"
        if Contador_Liberados["valor"] > 0:
            Contador_Liberados["clase"] = "text-bg-danger"
        if Contador_Pre_Liberados["valor"] > 0:
            Contador_Pre_Liberados["clase"] = "text-bg-danger"
        Resultado["Contenido"] += """
        <div class='row'>
            <div class='col-12'>
                <div class='h3'><i class='mdi mdi-go-kart-track'></i> Ruteo</div>
                <div class='w-100 d-flex justify-content-end'>
                    <button class='btn btn-success mb-1 me-1' onclick='Nueva_Ruteo()'><i class='mdi mdi-plus'></i> Nuevo</button>
                    <button class='btn btn-primary mb-1' id="download-xlsx-ruteo"><i class='mdi mdi-microsoft-excel'></i> Descargar Excel</button>
                </div>
                <div id='Tabla-Ruteo' class='border border-dark bg-dark-subtle'></div>
                <script>
                    delete table_abiertos;
                    var Col = [
                        {title: ' ', field: ' ', formatter: 'html',download: false,width:100,headerSort:false}, 
                        {title: 'Folio', field: 'Folio', headerFilter: 'input',width:65},
                        {title: 'Packing Slip', field: 'Packing_Slip', headerFilter: 'input',width:100},
                        {title: 'Ruta', field: 'Ruta', headerFilter: 'input',width:140}, 
                        {title: 'Fecha Alta', field: 'Fecha Alta', headerFilter: 'input',width:100}, 
                        {title: 'Proveedor', field: 'Proveedor', headerFilter: 'input',width:90}, 
                        {title: 'Destino', field: 'Destino', headerFilter: 'input',width:80}, 
                        {title: 'Numeros de Parte', field: 'Numeros', formatter: 'html',download: false,width:30,hozAlign:"center"},
                        {title: 'Numeros_de_Parte', field: 'Numeros_de_Parte',download: true,visible:false}, 
                        {title: 'Problema', field: 'Problema',width:150},
                        {title: 'Ultimo Comentario', field: 'Ultimo Comentario', headerFilter: 'input',formatter:'html'}, 
                        {title: 'Archivo(s)', field: 'Archivos', formatter: 'html',download: false,headerSort:false,width:90}];
                    var table_abiertos = new Tabulator("#Tabla-Ruteo", {
                        minHeight:500,
                        data:"""+str(Tabla_Datos_Ruteo)+""",
                        initialSort:[
                            {column:"Fecha Alta", dir:"asc"}
                        ],
                        layout:"fitColumns",
                        pagination:"local",
                        rowFormatter:function(row){
                        if(row.getData().Estado == 1){
                                row.getElement().style.backgroundColor = "#5dff67";
                            }
                        },
                        paginationSize:50,  
                        paginationCounter:"rows",
                        columns:Col
                    });
                    document.getElementById("download-xlsx-ruteo").addEventListener("click", function(){
                        table_abiertos.download("xlsx", "Ruteo.xlsx", {sheetName:"My Data"});
                    });
                </script>

            </div>
            <div class='col-12'>
                <hr>
                <div class='h3'><i class='mdi mdi-forklift'></i> Operaciones</div>
                <div class='w-100 d-flex justify-content-end'>
                    <button class='btn btn-success mb-1' id="download-xlsx-produccion"><i class='mdi mdi-microsoft-excel'></i> Descargar Excel</button>
                </div>
                <div id='Tabla-Produccion' class='border border-dark bg-dark-subtle'></div>
                <script>
                    delete table_p;
                    var Col = [
                        {title: ' ', field: ' ', formatter: 'html',download: false,width:100,headerSort:false}, 
                        {title: 'Folio', field: 'Folio', headerFilter: 'input',width:65},
                        {title: 'Packing Slip', field: 'Packing_Slip', headerFilter: 'input',width:100},
                        {title: 'Ruta', field: 'Ruta', headerFilter: 'input',width:140}, 
                        {title: 'Fecha Alta', field: 'Fecha Alta', headerFilter: 'input',width:100}, 
                        {title: 'Proveedor', field: 'Proveedor', headerFilter: 'input',width:90}, 
                        {title: 'Destino', field: 'Destino', headerFilter: 'input',width:80}, 
                        {title: 'Numeros de Parte', field: 'Numeros', formatter: 'html',download: false,width:30,hozAlign:"center"},
                        {title: 'Numeros_de_Parte', field: 'Numeros_de_Parte',download: true,visible:false},
                        {title: 'Problema', field: 'Problema',width:150},
                        {title: 'Ultimo Comentario', field: 'Ultimo Comentario', headerFilter: 'input',formatter:'html'}, 
                        {title: 'Archivo(s)', field: 'Archivos', formatter: 'html',download: false,headerSort:false,width:90}];
                    var table_p = new Tabulator("#Tabla-Produccion", {
                        minHeight:500,
                        data:"""+str(Tabla_Datos_Porduccion)+""",
                        initialSort:[
                            {column:"Fecha Alta", dir:"desc"}
                        ],
                        layout:"fitColumns",
                        pagination:"local",
                        rowFormatter:function(row){
                            if(row.getData().Estado == 1){
                                    row.getElement().style.backgroundColor = "#5dff67";
                                }
                            if(row.getData().Estado == 2){
                                    row.getElement().style.backgroundColor = "#cbe00f";
                                }
                        },
                        paginationSize:50,  
                        paginationCounter:"rows",
                        columns:Col,
                    });
                    document.getElementById("download-xlsx-produccion").addEventListener("click", function(){
                        table_p.download("xlsx", "Produccion.xlsx", {sheetName:"My Data"});
                    });
                </script>
            </div
        </div>
        <script>
            $( document ).ready(function() {
                $('.tabulator-header-contents').addClass('bg-body-secondary').find('.tabulator-col').addClass('bg-body-secondary');
                $("#Tab_Abierto").find('.badge').html("""+str(Contador_Abierto["valor"])+""").removeClass('text-bg-danger text-bg-secondary').addClass('"""+str(Contador_Abierto["clase"])+"""');
                $("#Tab_Liberados").find('.badge').html("""+str(Contador_Liberados["valor"])+""").removeClass('text-bg-danger text-bg-secondary').addClass('"""+str(Contador_Liberados["clase"])+"""');
                $("#Tab_Pre_Liberados").find('.badge').html("""+str(Contador_Pre_Liberados["valor"])+""").removeClass('text-bg-danger text-bg-secondary').addClass('"""+str(Contador_Pre_Liberados["clase"])+"""');
            })
            function Nueva_Ruteo()
            {   
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-plus'></i> Nuevo OS&D de Ruteo");
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm').addClass('modal-xl');
                var parametros = {"Fun":'"""+str(fernet.encrypt("Nueva_Ruteo".encode()).decode("utf-8"))+"""'};
                $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                    success:  function (response)
                    {
                        var Resultado = JSON.parse(response);
                        $("#Vent_1").modal("show").find(".modal-body").html(Resultado["Contenido"]);
                        $("#Vent_1").find(".modal-footer").find("button").attr('onclick',"$('#Vent_1').modal('hide'); delete table; ")
                        swal.close();
                    },
                    error: function (jqXHR, textStatus, errorThrown ){Mensaje(0,'Process error ['+ jqXHR.status + " | " + textStatus  + " | " + errorThrown +']');}
                });
            }
            function Completar_Ruteo(ID){
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm').addClass('modal-lg')
                $("#Vent_1").modal("show").find(".modal-body").html("<div class='w-100 text-center'><div class='spinner-grow' role='status'></div><b> Loading...</b></div>").parent().find(".modal-title").html("<i class='mdi mdi-plus'></i> Nuevo OS&D de Ruteo");
                var parametros = {"Fun":'"""+str(fernet.encrypt("Completar_Ruteo".encode()).decode("utf-8"))+"""',"ID_User":'"""+str(Datos["ID_User"])+"""',"ID":ID};
                $.ajax({
                    data:  parametros,
                    url:   \""""+str(request.url)+"""\",
                    type:  "post",
                    success:  function (response){var Resultado = JSON.parse(response); $("#Vent_1").find(".modal-body").html(Resultado["Contenido"]);},
                    error: function (jqXHR, textStatus, errorThrown){$("#Vent_1").find(".modal-body").html("<span style='color:red;'><b>ERROR</b></span> <hr>"+textStatus);}
                });
            }
            function Modificar_Ruteo(Accion,ID,Folio,De_Donde,Problemas){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm').addClass('modal-lg')
                $("#Vent_1").modal("show").find(".modal-body").html("<div class='w-100 text-center'><div class='spinner-grow' role='status'></div><b> Loading...</b></div>").parent().find(".modal-title").html("<i class='mdi mdi-file-document-edit'></i> Edit ["+Folio+"] "+Problemas);
                var parametros = {"Fun":'"""+str(fernet.encrypt("Modificar_Ruteo".encode()).decode("utf-8"))+"""',"Accion":Accion,"ID":ID,"De_Donde":De_Donde};
                $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                    type:  "post",
                    success:  function (response){var Resultado = JSON.parse(response); $("#Vent_1").find(".modal-body").html(Resultado["Contenido"]);swal.close();},
                    error: function (jqXHR, textStatus, errorThrown){$("#Vent_1").find(".modal-body").html("<span style='color:red;'><b>ERROR</b></span> <hr>"+textStatus);}
                });
            }
            function Eliminar_Ruteo(ID,Folio){
                Swal.fire({
                title: '¿Estás seguro de eliminar el OS&D ['+Folio+']?',
                input: 'text',buttonsStyling: false,showCancelButton: true,confirmButtonText: "<i class='mdi mdi-check'></i> Si",cancelButtonText: "<i class='mdi mdi-close'></i> No",showLoaderOnConfirm: true,
                customClass: {confirmButton: 'btn btn-success ms-1 me-1',cancelButton: 'btn btn-danger ms-1 me-1'},
                preConfirm: (Comentario) => {
                    
                    if(Comentario.trim() == ""){
                        Mensaje(1,"Agrega comentario");
                    }else{
                        Mostrar_Ventana_Cargando(false);
                        var parametros = {"Fun":'"""+str(fernet.encrypt("Eliminar_Ruteo".encode()).decode("utf-8"))+"""',"Comentario":Comentario,"ID":ID};
                        $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                            success:  function (response)
                            {
                                var Resultado = JSON.parse(response);
                                if(Resultado["Estado"] == 1)
                                {
                                    $("#Vent_1").modal("hide");
                                    Mensaje(2);
                                    Cargar_Abiertos();
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
        """

        
    except:
        Resultado["Contenido"] = str(sys.exc_info())
    Cur += json.dumps(Resultado)
    print(Cur)



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

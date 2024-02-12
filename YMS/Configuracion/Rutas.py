from flask import request,session,render_template,current_app
from cryptography.fernet import Fernet
from datetime import datetime,date,timedelta
import sys
import json
import os
import openpyxl
from openpyxl.workbook.protection import WorkbookProtection
from openpyxl.styles.borders import Border, Side
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font
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
        Rutas = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".crutas WHERE cr_tipo != 'Empty'")
        Patio = []
        for Ruta in Rutas:
            Opciones = "<div class='text-center'><div class='btn-group' role='group' aria-label='Basic mixed styles example'>"
            Opciones += "</div></div>"
            Patio.append({"Tipo":str(Ruta["cr_tipo"]),"Opciones":Opciones})


        Contenido += "<div class='container'><div class='h2 fw-lighter mt-1 mb-1 text-center border-bottom'><i class='mdi mdi-card-bulleted'></i> Route Master</div>"
        for Ruta in Rutas:
            Contenido += """
            <div class='w-100 border border-dark bg-body mb-2 p-3'>
                <div class='fs-1 text-center'>"""+str(Ruta["cr_tipo"])+""" <a class='link-primary' onclick='Agregar_Nivel("N1",\""""+str(Ruta["cr_tipo"])+"""\")' style='cursor:pointer'><i class='mdi mdi-plus'></i></a></div>
            """
            if Ruta["cr_niveles"] is not None and str(Ruta["cr_niveles"]) != "":
                Contenido += "<div class='row'>"
                Niveles = json.loads(Ruta["cr_niveles"]) 
                for N1 in Niveles.keys():
                    Tiene = False
                    Contenido += "<div class='col p-1'><div class='border border-dark bg-body-tertiary'>"
                    Contenido += "<div class='text-center fs-2'>"+str(N1)+" <a class='link-warning' style='cursor:pointer' onclick='Agregar_Nivel(\"N2\",\""+str(Ruta["cr_tipo"])+"/"+str(N1)+"\")' ><i class='mdi mdi-pencil'></i></a> <a class='link-danger' style='cursor:pointer' onclick='Eliminar_Nivel(\"N2\",\""+str(Ruta["cr_tipo"])+"/"+str(N1)+"\")'><i class='mdi mdi-trash-can'></i></a></div>"
                    try:
                        Keys = Niveles[N1].keys()
                        Contenido += "<div class='row p-3'>"
                        for N2 in Keys:
                            Contenido += "<div class='col p-1'><div class='border border-dark bg-dark-subtle'>"
                            Contenido += "<div class='text-center fs-3'>"+str(N2)+"</div>"
                            try:
                                Docks = Niveles[N1][N2]["DOCKS"]
                                Contenido += "<div class='row p-3'>"
                                for N3 in Docks:
                                    Contenido += "<div class='col p-1'><div class='border border-dark bg-warning'>"
                                    Contenido += "<div class='text-center fs-4'>"+str(N3)+"</div>"
                                    Contenido += "</div></div>"
                                Contenido += "</div>"
                            except:
                                pass

                            Contenido += "</div></div>"
                        Contenido += "</div>"
                    except:
                        pass
                    Contenido += "</div></div>"
                Contenido += "</div>"
            Contenido += """
            </div>
            """
        Contenido += "</div>"
        Contenido += """
        <script>
            function Agregar_Nivel(Nivel,Direccion){
                Mostrar_Ventana_Cargando(false);
                $("#Vent_1").find(".modal-title").html("<i class='mdi mdi-plus'></i>" + Direccion );
                $("#Vent_1").removeClass('modal-xl modal-lg modal-sm');
                var parametros = {"Fun":'"""+str(fernet.encrypt("Agregar_Nivel".encode()).decode("utf-8"))+"""',"Nivel":Nivel,"Direccion":Direccion};
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
            function Eliminar_Nivel(Nivel,Direccion){
                Swal.fire({
                title: 'Are you sure delete ['+Direccion+']?',
                buttonsStyling: false,showCancelButton: true,confirmButtonText: "<i class='mdi mdi-check'></i> Yes",cancelButtonText: "<i class='mdi mdi-close'></i> No",showLoaderOnConfirm: true,
                customClass: {confirmButton: 'btn btn-success ms-1 me-1',cancelButton: 'btn btn-danger ms-1 me-1'},
                preConfirm: () => {
                
                    Mostrar_Ventana_Cargando(false);
                    var parametros = {"Fun":'"""+str(fernet.encrypt("Eliminar_Nivel".encode()).decode("utf-8"))+"""',"Nivel":Nivel,"Direccion":Direccion};
                    $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                        success:  function (response)
                        {
                            var Resultado = JSON.parse(response);
                            if(Resultado["Estado"] == 1)
                            {
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
        """
        Cur += render_template("general.html",Contenido=Contenido,Componentes=Compartido.Complementos(None),Menu=Menu,Titulo=Titulo)
    except:
        Cur += str(sys.exc_info())
    return Cur
def Agregar_Nivel(Datos):
    if "K" in session.keys():
        fernet = Fernet(session["K"])
    DB = LibDM_2023.DataBase()
    Compartido_2023 = LibDM_2023.Compartido()
    Cur = ""
    Resultado = {"Contenido":"","Estado":0}
    try:
        if str(Datos["Nivel"]) == "N1":
            Formulario = {"Col":"12", "Campos": [],"Clase": "Alta_Ruta" }
            Formulario["Campos"].append({"tipo":"texto","campo":"Nombre","titulo":"Name","Requerido":1,"min":1,"max":30,"valor":""})
            Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
        if str(Datos["Nivel"]) == "N2":
            Resultado["Contenido"] += "<div class='w-100 text-center'><button class='btn btn-primary' onclick='Descargar_Excel(\""+str(Datos["Direccion"])+"\")'><i class='mdi mdi-cloud-download'></i> Download configuration file (Excel)</button></div>"
            Formulario = {"Col":"12", "Campos": [],"Clase": "Alta_Ruta" }
            Formulario["Campos"].append({"tipo":"archivo","campo":"Nueva Rutas","titulo":"New route","Requerido":1,"Col":12,"min":1,"max":1,"tipo_archivo":["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"],"valor":""})
            Resultado["Contenido"] += str(Compartido_2023.Formulario(Formulario))
        Resultado["Contenido"] += """
        <hr>
        <div class='w-100 text-center'><button class='btn btn-success w-75' onclick='Guardar_Nivel(\""""+str(Datos["Nivel"])+"""\",\""""+str(Datos["Direccion"])+"""\")'><i class='mdi mdi-floppy'></i> Save</button></div>
        <script>
            function Guardar_Nivel(Nivel,Direccion){
                var Info = Dame_Formulario(".Alta_Ruta",true);
                if(Info != null)
                {
                    Mostrar_Ventana_Cargando(false);
                    var parametros = {"Fun":'"""+str(fernet.encrypt("Guardar_Nivel".encode()).decode("utf-8"))+"""',"Info":JSON.stringify(Info),"Nivel":Nivel,"Direccion":Direccion};
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
            }
            function Descargar_Excel(Direccion){
                Mostrar_Ventana_Cargando(false);
                var parametros = {"Fun":'"""+str(fernet.encrypt("Descargar_Excel".encode()).decode("utf-8"))+"""',"Direccion":Direccion};
                $.ajax({data:  parametros,url:\""""+str(request.url)+"""\",type:  "post",
                    success:  function (response)
                    {
                        var Resultado = JSON.parse(response);
                        if(Resultado["Estado"] == 1)
                        {
                            if("Archivo" in Resultado)
                            {
                                var win1 = window.open('"""+str(request.url_root)+"""/Portal_File/Gen/'+Resultado["Archivo"], '_blank');
                                win1.focus();
                            }
                            Mensaje(2);
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
        </script>
        """
    except:
        Resultado["Contenido"] = str(sys.exc_info())
    Cur += json.dumps(Resultado)
    return Cur
def Guardar_Nivel(Datos):
    DB = LibDM_2023.DataBase()
    Compartido_2023 = LibDM_2023.Compartido()
    Cur = ""
    Resultado = {"Contenido":"","Estado":0}
    try:
        Error = ""
        Info_Datos = json.loads(str(Datos["Info"]))
        Tipo = str(Datos["Direccion"]).split('/')[0]
        Info_Ahora = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".crutas WHERE cr_tipo = '"+str(Tipo)+"'")[0]
        if Info_Ahora["cr_niveles"] is None or str(Info_Ahora["cr_niveles"]).strip() == "":
            Info_Ruta = {}
        else:
            Info_Ruta = json.loads(str(Info_Ahora["cr_niveles"]))
        if Datos["Nivel"] == "N1":
            Info_Ruta[str(Info_Datos["Nombre"])] = 0
        if Datos["Nivel"] == "N2":
            Tipo_2 = str(Datos["Direccion"]).split('/')[1]
            Info_Ruta[str(Tipo_2)] = {}
            wb_obj = openpyxl.load_workbook(str(current_app.root_path).replace("\\","/")+"/Files/"+str(Info_Datos["Nueva Rutas"][0]))
            
            Dia = ["M","T","W","R","F"]
            Runas_Letras = []
            for N1 in wb_obj.sheetnames:
                for D in Dia:
                    if str(D) in str(N1) and str(N1) not in Runas_Letras:
                        Runas_Letras.append(N1)

            for N1 in wb_obj.sheetnames:
                if str(Tipo_2) == "MilkRun":
                    if str(N1) in Runas_Letras:
                        N2 = {}
                        wb_obj.active = wb_obj[N1]
                        Shell = wb_obj.active
                        N2["NOMBRE"] = Shell["B1"].value
                        N2["ZONA"] = Shell["B2"].value
                        N2["SCAC"] = Shell["B3"].value
                        
                        index = 6
                        N2["DOCKS"] = []
                        A = "."
                        while A is not None and str(A).strip() != "":
                            A = Shell["A"+str(index)].value
                            if A != "" and A is not None:
                                N2["DOCKS"].append(A)
                                index += 1
                        
                        index = 7
                        N2["RUTAS"] = []
                        A = "."
                        while A is not None and str(A).strip() != "":
                            A = Shell["D"+str(index)].value
                            if A != "" and A is not None:
                                DUNS = Shell["D"+str(index)].value

                                INICIO = ""
                                try:
                                    INICIO = Shell["E"+str(index)].value.strftime("%Y-%m-%d %H:%M:%S")
                                except:
                                    INICIO = datetime.strptime(Shell["E"+str(index)].value,"%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                                
                                FIN = ""
                                try:
                                    FIN = Shell["F"+str(index)].value.strftime("%Y-%m-%d %H:%M:%S")
                                except:
                                    FIN = datetime.strptime(Shell["F"+str(index)].value,"%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")

                                R = {"DUNS":DUNS,"INICIA":INICIO,"FIN":FIN}
                                N2["RUTAS"].append(R)
                                index += 1

                        DL = []
                        index = 6
                        A = "."
                        while A is not None and str(A).strip() != "":
                            A = Shell["H"+str(index)].value
                            if A != "" and A is not None:
                                DL.append(A.replace(" ","").replace(";",""))
                                index += 1

                        N2["DL"] = ";".join(DL)


                        # if len(N2.keys()) == 0:
                        #     Info_Ruta[str(Tipo_2)][N1] = 0
                        # else:
                        Info_Ruta[str(Tipo_2)][N1] = N2
                    else:
                        wb_obj.active = wb_obj[N1]
                        Dia = ["M","T","W","R","F"]
                        for D in Dia:
                            if str(N1)+str(D) not in Runas_Letras:
                                N2 = {}
                                Shell = wb_obj.active
                                N2["NOMBRE"] = Shell["B1"].value
                                N2["ZONA"] = Shell["B2"].value
                                N2["SCAC"] = Shell["B3"].value
                                
                                index = 6
                                N2["DOCKS"] = []
                                A = "."
                                while A is not None and str(A).strip() != "":
                                    A = Shell["A"+str(index)].value
                                    if A != "" and A is not None:
                                        N2["DOCKS"].append(A)
                                        index += 1
                                
                                index = 7
                                N2["RUTAS"] = []
                                A = "."
                                while A is not None and str(A).strip() != "":
                                    A = Shell["D"+str(index)].value
                                    if A != "" and A is not None:
                                        DUNS = Shell["D"+str(index)].value

                                        INICIO = ""
                                        try:
                                            INICIO = Shell["E"+str(index)].value.strftime("%Y-%m-%d %H:%M:%S")
                                        except:
                                            INICIO = datetime.strptime(Shell["E"+str(index)].value,"%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                                        
                                        FIN = ""
                                        try:
                                            FIN = Shell["F"+str(index)].value.strftime("%Y-%m-%d %H:%M:%S")
                                        except:
                                            FIN = datetime.strptime(Shell["F"+str(index)].value,"%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")

                                        R = {"DUNS":DUNS,"INICIA":INICIO,"FIN":FIN}
                                        N2["RUTAS"].append(R)
                                        index += 1

                                DL = []
                                index = 6
                                A = "."
                                while A is not None and str(A).strip() != "":
                                    A = Shell["H"+str(index)].value
                                    if A != "" and A is not None:
                                        DL.append(A.replace(" ","").replace(";",""))
                                        index += 1

                                N2["DL"] = ";".join(DL)


                                # if len(N2.keys()) == 0:
                                #     Info_Ruta[str(Tipo_2)][N1] = 0
                                # else:
                                Info_Ruta[str(Tipo_2)][N1+str(D)] = N2
                else:
                    N2 = {}
                    wb_obj.active = wb_obj[N1]
                    Shell = wb_obj.active
                    N2["NOMBRE"] = Shell["B1"].value
                    N2["ZONA"] = Shell["B2"].value
                    N2["SCAC"] = Shell["B3"].value
                    
                    index = 6
                    N2["DOCKS"] = []
                    A = "."
                    while A is not None and str(A).strip() != "":
                        A = Shell["A"+str(index)].value
                        if A != "" and A is not None:
                            N2["DOCKS"].append(A)
                            index += 1
                    
                    index = 7
                    N2["RUTAS"] = []
                    A = "."
                    while A is not None and str(A).strip() != "":
                        A = Shell["D"+str(index)].value
                        if A != "" and A is not None:
                            DUNS = Shell["D"+str(index)].value

                            INICIO = ""
                            try:
                                INICIO = Shell["E"+str(index)].value.strftime("%Y-%m-%d %H:%M:%S")
                            except:
                                INICIO = datetime.strptime(Shell["E"+str(index)].value,"%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                            
                            FIN = ""
                            try:
                                FIN = Shell["F"+str(index)].value.strftime("%Y-%m-%d %H:%M:%S")
                            except:
                                FIN = datetime.strptime(Shell["F"+str(index)].value,"%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")

                            R = {"DUNS":DUNS,"INICIA":INICIO,"FIN":FIN}
                            N2["RUTAS"].append(R)
                            index += 1

                    DL = []
                    index = 6
                    A = "."
                    while A is not None and str(A).strip() != "":
                        A = Shell["H"+str(index)].value
                        if A != "" and A is not None:
                            DL.append(A.replace(" ","").replace(";",""))
                            index += 1

                    N2["DL"] = ";".join(DL)
                    Info_Ruta[str(Tipo_2)][N1] = N2
                

        Error = DB.Instruccion("UPDATE "+str(BD_Nombre)+".crutas SET cr_niveles = '"+str(json.dumps(Info_Ruta))+"' WHERE cr_tipo = '"+str(Tipo)+"'")

        #Error = str(Runas_Letras)
 
        if Error == "":
            Resultado["Estado"] = 1
        else:
            Resultado["Contenido"] += str(Error)
    except:
        Resultado["Contenido"] = str(sys.exc_info())
    Cur += json.dumps(Resultado)
    return Cur
def Descargar_Excel(Datos):
    DB = LibDM_2023.DataBase()
    Compartido_2023 = LibDM_2023.Compartido()
    Cur = ""
    Resultado = {"Contenido":"","Estado":0}
    try:
        Borrar_Primera = False
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "NUEVA RUTA"
        Tipo = str(Datos["Direccion"]).split('/')[0]
        Info_Ahora = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".crutas WHERE cr_tipo = '"+str(Tipo)+"'")[0]
        Info_Ruta = json.loads(str(Info_Ahora["cr_niveles"]))
        if Info_Ruta[str(Datos["Direccion"]).split('/')[1]] == 0 or "NOMBRE" in Info_Ruta[str(Datos["Direccion"]).split('/')[1]].keys():

            ws['A1'] = "NOMBRE"
            ws['B1'].fill = PatternFill("solid", fgColor="fffd00")
            ws['B1'].border = Border(bottom=Side(border_style="thin", color="000000"))
            ws['B1'] = ""

            ws['A2'] = "ZONA"
            ws['B2'].fill = PatternFill("solid", fgColor="fffd00")
            ws['B2'].border = Border(bottom=Side(border_style="thin", color="000000"))
            ws['B2'] = ""

            ws['A3'] = "SCAC"
            ws['B3'].fill = PatternFill("solid", fgColor="fffd00")
            ws['B3'].border = Border(bottom=Side(border_style="thin", color="000000"))
            ws['B3'] = ""
            
            index = 6
            if len(Docks) == 0:
                for r in range(0,10):
                    ws['A'+str(index)].fill = PatternFill("solid", fgColor="fffd00")
                    ws['A'+str(index)].border = Border(bottom=Side(border_style="thin", color="000000"))
                    ws['A'+str(index)] = ""
                    index += 1
            
            ws['D5'] = "RUTA"
            ws['D6'] = "DUNS"
            ws['E6'] = "INICIA"
            ws['F6'] = "FIN"

            index = 7
            for r in range(0,10):
                ws['D'+str(index)].fill = PatternFill("solid", fgColor="fffd00")
                ws['D'+str(index)].border = Border(bottom=Side(border_style="thin", color="000000"))
                ws['D'+str(index)] = ""
                ws['E'+str(index)].fill = PatternFill("solid", fgColor="fffd00")
                ws['E'+str(index)].border = Border(bottom=Side(border_style="thin", color="000000"))
                ws['E'+str(index)] = ""
                ws['F'+str(index)].fill = PatternFill("solid", fgColor="fffd00")
                ws['F'+str(index)].border = Border(bottom=Side(border_style="thin", color="000000"))
                ws['F'+str(index)] = ""
                index += 1
            
            ws['H5'] = "DL"

            index = 6
            for r in range(0,10):
                ws['H'+str(index)].fill = PatternFill("solid", fgColor="fffd00")
                ws['H'+str(index)].border = Border(bottom=Side(border_style="thin", color="000000"))
                ws['H'+str(index)] = ""
                index += 1
        else:
            for N1 in Info_Ruta[str(Datos["Direccion"]).split('/')[1]].keys():
                
                Nombre = ""
                Zona = ""
                SCAC = ""
                Rutas = []
                Docks = []

                if Info_Ruta[str(Datos["Direccion"]).split('/')[1]][N1] == 0:
                    pass
                else:
                    Nombre = Info_Ruta[str(Datos["Direccion"]).split('/')[1]][N1]["NOMBRE"]
                    Zona = Info_Ruta[str(Datos["Direccion"]).split('/')[1]][N1]["ZONA"]
                    SCAC = Info_Ruta[str(Datos["Direccion"]).split('/')[1]][N1]["SCAC"]
                    Rutas = Info_Ruta[str(Datos["Direccion"]).split('/')[1]][N1]["RUTAS"]
                    Docks = Info_Ruta[str(Datos["Direccion"]).split('/')[1]][N1]["DOCKS"]
                    
                    if "DL" in Info_Ruta[str(Datos["Direccion"]).split('/')[1]][N1].keys():
                        DL = str(Info_Ruta[str(Datos["Direccion"]).split('/')[1]][N1]["DL"]).split(";")
                    else:
                        DL = []

               

                Borrar_Primera = True
                ws = wb.create_sheet(str(N1))
                ws['A1'] = "NOMBRE"
                ws['B1'].fill = PatternFill("solid", fgColor="fffd00")
                ws['B1'].border = Border(bottom=Side(border_style="thin", color="000000"))
                ws['B1'] = Nombre

                ws['A2'] = "ZONA"
                ws['B2'].fill = PatternFill("solid", fgColor="fffd00")
                ws['B2'].border = Border(bottom=Side(border_style="thin", color="000000"))
                ws['B2'] = Zona

                ws['A3'] = "SCAC"
                ws['B3'].fill = PatternFill("solid", fgColor="fffd00")
                ws['B3'].border = Border(bottom=Side(border_style="thin", color="000000"))
                ws['B3'] = SCAC



                
                ws['A5'] = "DOCKS"

                index = 6
                if len(Docks) == 0:
                    for r in range(0,10):
                        ws['A'+str(index)].fill = PatternFill("solid", fgColor="fffd00")
                        ws['A'+str(index)].border = Border(bottom=Side(border_style="thin", color="000000"))
                        ws['A'+str(index)] = ""
                        index += 1
                else:
                    for D in Docks:
                        ws['A'+str(index)].fill = PatternFill("solid", fgColor="fffd00")
                        ws['A'+str(index)].border = Border(bottom=Side(border_style="thin", color="000000"))
                        ws['A'+str(index)] = D
                        index += 1

                ws['D5'] = "RUTA"
                ws['D6'] = "DUNS"
                ws['E6'] = "INICIA"
                ws['F6'] = "FIN"

                index = 7
                if len(Rutas) == 0:
                    for r in range(0,10):
                        ws['D'+str(index)].fill = PatternFill("solid", fgColor="fffd00")
                        ws['D'+str(index)].border = Border(bottom=Side(border_style="thin", color="000000"))
                        ws['D'+str(index)] = ""
                        ws['E'+str(index)].fill = PatternFill("solid", fgColor="fffd00")
                        ws['E'+str(index)].border = Border(bottom=Side(border_style="thin", color="000000"))
                        ws['E'+str(index)] = ""
                        ws['F'+str(index)].fill = PatternFill("solid", fgColor="fffd00")
                        ws['F'+str(index)].border = Border(bottom=Side(border_style="thin", color="000000"))
                        ws['F'+str(index)] = ""
                        index += 1
                else:
                    for R in Rutas:
                        ws['D'+str(index)].fill = PatternFill("solid", fgColor="fffd00")
                        ws['D'+str(index)].border = Border(bottom=Side(border_style="thin", color="000000"))
                        ws['D'+str(index)] = R["DUNS"]
                        ws['E'+str(index)].fill = PatternFill("solid", fgColor="fffd00")
                        ws['E'+str(index)].border = Border(bottom=Side(border_style="thin", color="000000"))
                        ws['E'+str(index)] = R["INICIA"]
                        ws['F'+str(index)].fill = PatternFill("solid", fgColor="fffd00")
                        ws['F'+str(index)].border = Border(bottom=Side(border_style="thin", color="000000"))
                        ws['F'+str(index)] = R["FIN"]
                        index += 1

                ws['H5'] = "DL"

                index = 6
                if len(DL) == 0:
                    for r in range(0,10):
                        ws['H'+str(index)].fill = PatternFill("solid", fgColor="fffd00")
                        ws['H'+str(index)].border = Border(bottom=Side(border_style="thin", color="000000"))
                        ws['H'+str(index)] = ""
                        index += 1
                else:
                    for D in DL:
                        ws['H'+str(index)].fill = PatternFill("solid", fgColor="fffd00")
                        ws['H'+str(index)].border = Border(bottom=Side(border_style="thin", color="000000"))
                        ws['H'+str(index)] = str(D).strip()
                        index += 1


                if Info_Ruta[str(Datos["Direccion"]).split('/')[1]][N1] == 0 or "NOMBRE" in Info_Ruta[str(Datos["Direccion"]).split('/')[1]][N1].keys():
                    pass
                else:
                    index = 1
                    for N2 in Info_Ruta[str(Datos["Direccion"]).split('/')[1]][N1].keys():
                        ws['A'+str(index)] = str(N2)
                        index += 1
        if Borrar_Primera:
            wb.remove_sheet(wb.get_sheet_by_name('NUEVA RUTA'))
        
        wb.save(str(current_app.root_path).replace("\\","/")+"/Files/Gen/"+str(Tipo)+'.xlsx')
        Resultado["Contenido"] += str(Info_Ruta)
        Resultado["Archivo"] = str(Tipo)+'.xlsx'
        Resultado["Estado"] = 1
    except:
        Resultado["Contenido"] = str(sys.exc_info())
    Cur += json.dumps(Resultado)
    return Cur
def Eliminar_Nivel(Datos):
    DB = LibDM_2023.DataBase()
    Compartido_2023 = LibDM_2023.Compartido()
    Cur = ""
    Resultado = {"Contenido":"","Estado":0}
    try:
        Tipo = str(Datos["Direccion"]).split('/')[0]
        Info_Ahora = DB.Get_Dato("SELECT * FROM "+str(BD_Nombre)+".crutas WHERE cr_tipo = '"+str(Tipo)+"'")[0]
        Info_Ruta = json.loads(str(Info_Ahora["cr_niveles"]))
        del Info_Ruta[str(Datos["Direccion"]).split('/')[1]]
        Error = DB.Instruccion("UPDATE "+str(BD_Nombre)+".crutas SET cr_niveles = '"+str(json.dumps(Info_Ruta))+"' WHERE cr_tipo = '"+str(Tipo)+"'")
        if Error == "":
            Resultado["Estado"] = 1
        else:
            Resultado["Contenido"] += str(Error)
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

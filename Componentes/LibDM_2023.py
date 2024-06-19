from flask import request,current_app
#import MySQLdb
import psycopg2
import psycopg2.extras
import sys
from datetime import datetime
from datetime import date
from datetime import timedelta
import time
import os
from pathlib import Path
from http import cookies
from cryptography.fernet import Fernet
sys.dont_write_bytecode = True
class DataBase:
    ip_PPS = "192.168.83.50"
    Us_PPS = "root"
    Ps_PPS = "verycool"
    Base_PPS = "produccion"

    ip = "10.4.7.219"
    Us = "root"
    Ps = "verycool"
    Base = "portal"
    def __init__(self):
        return;
    def Instruccion(self,Query):
        try:
            conn = psycopg2.connect("postgres://portal_dz0m_user:E8HYp5RbPqW4afRL9o8xauoiPME5LlbN@dpg-cpplpnuehbks73c52cq0-a/portal_dz0m",database="portal_dz0m", user="portal_dz0m_user", password="E8HYp5RbPqW4afRL9o8xauoiPME5LlbN")
            cursor1=conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
            cursor1.execute(Query)
            conn.commit()
            conn.close()
            # db = MySQLdb.connect(self.ip,self.Us,self.Ps,self.Base, charset='utf8')
            # cursor = db.cursor()
            # Quety2 = "SET SQL_SAFE_UPDATES = 0;"
            # cursor.execute(Quety2)
            # Quety2 = Query
            # cursor.execute(Quety2)
            # db.commit()
            # db.close()
            return ""
        except :
            return "Error : [ " + str(sys.exc_info()) + "]"
    def Instruccion_BITS(self,Query,Bits1,Bits2,Bits3):
        try:
            # db = MySQLdb.connect(self.ip,self.Us,self.Ps,self.Base, charset='utf8')
            # cursor = db.cursor()
            # Quety2 = "SET SQL_SAFE_UPDATES = 0;";
            # cursor.execute(Quety2)
            # Quety2 = Query
            # if Bits1 is None:
            #     cursor.execute(Quety2)
            # else:
            #     if Bits2 is None:
            #         cursor.execute(Quety2,(Bits1,))
            #     else:
            #         if Bits3 is None:
            #             cursor.execute(Quety2,(Bits1,Bits2,))
            #         else:
            #             cursor.execute(Quety2,(Bits1,Bits2,Bits3,))
            # db.commit()
            # db.close()
            return ""
        except :
            return "Error : [ " + str(sys.exc_info()) + "]"
    def Instruccion_2(self,Query):
        try:
            # db = MySQLdb.connect(self.ip,self.Us,self.Ps,self.Base, charset='utf8')
            # cursor = db.cursor()
            # Query = "SET SQL_SAFE_UPDATES = 0;"+Query
            # for Q in Query.split(";"):
            #     if Q.strip() != "":
            #         cursor.execute(Q)
            # db.commit()
            # db.close()
            return ""
        except :
            return "Error : [ " + str(sys.exc_info()) + "]"
    def Get_Dato(self,Query):
        try:
            global ID_User
            ArrRes = []
            conn = psycopg2.connect("postgres://portal_dz0m_user:E8HYp5RbPqW4afRL9o8xauoiPME5LlbN@dpg-cpplpnuehbks73c52cq0-a/portal_dz0m",database="portal_dz0m", user="portal_dz0m_user", password="E8HYp5RbPqW4afRL9o8xauoiPME5LlbN")
            cursor1=conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
            cursor1.execute(Query)
            ArrRes = cursor1.fetchall()
            for A in ArrRes:
                for key,value in A.items():
                    if str(key) != "Foto" and str(key) != "cArtFoto" and str(key) != "cVisIdentificacion" and str(key) != "cVisIDoctoMSS" :
                        if type(A[key]) is bytes:
                            try:
                                #A[key] =  A[key].decode("utf-8")
                                A[key] =  A[key].decode("unicode_escape")
                            except :
                                A[key] =  A[key]
            conn.close()

            # db = MySQLdb.connect(self.ip,self.Us,self.Ps,self.Base, charset='utf8')
            # cursor = db.cursor(MySQLdb.cursors.DictCursor)
            # Quety2 = Query
            # #Quety2 = "#---\n\r/*Usuario:"+str(self.Dame_Nombre(ID_User))+"*/" + str(Quety2);
            # cursor.execute(Quety2)
            # ArrRes = cursor.fetchall()
            # for A in ArrRes:
            #     for key,value in A.items():
            #         if str(key) != "Foto" and str(key) != "cArtFoto" and str(key) != "cVisIdentificacion" and str(key) != "cVisIDoctoMSS" :
            #             if type(A[key]) is bytes:
            #                 try:
            #                     #A[key] =  A[key].decode("utf-8")
            #                     A[key] =  A[key].decode("unicode_escape")
            #                 except :
            #                     A[key] =  A[key]
            # db.close()
            return ArrRes
        except :
            return "Error : [ " + str(sys.exc_info()) + "]"
    def Get_Dato_Crudo(self,Query):
        try:
            global ID_User
            ArrRes = []
            # db = MySQLdb.connect(self.ip,self.Us,self.Ps,self.Base, charset='utf8')
            # cursor = db.cursor(MySQLdb.cursors.DictCursor)
            # Quety2 = Query
            # #Quety2 = "#---\n\r/*Usuario:"+str(self.Dame_Nombre(ID_User))+"*/" + str(Quety2);
            # cursor.execute(Quety2)
            # ArrRes = cursor.fetchall()
            # db.close()
            return ArrRes
        except :
            return "Error : [ " + str(sys.exc_info()) + "]"
    def Get_Dato_70(self,Query):
        try:
            global ID_User
            ArrRes = []
            # db = MySQLdb.connect(self.ip_PPS,self.Us_PPS,self.Ps_PPS,self.Base_PPS, charset='utf8')
            # cursor = db.cursor(MySQLdb.cursors.DictCursor)
            # Quety2 = Query
            # #Quety2 = "#---\n\r/*Usuario:"+str(self.Dame_Nombre(ID_User))+"*/" + str(Quety2);
            # cursor.execute(Quety2)
            # ArrRes = cursor.fetchall()
            # for A in ArrRes:
            #     for key,value in A.items():
            #         if str(key) != "Foto" and str(key) != "cArtFoto":
            #             if type(A[key]) is bytes:
            #                 try:
            #                     A[key] =  A[key].decode("utf-8")
            #                 except :
            #                     A[key] =  A[key]
            # db.close()
            return ArrRes
        except :
            return "Error : [ " + str(sys.exc_info()) + "]"
    def Instruccion_70(self,Query):
        try:
            # db = MySQLdb.connect(self.ip_PPS,self.Us_PPS,self.Ps_PPS,self.Base_PPS, charset='utf8')
            # cursor = db.cursor()
            # Quety2 = "SET SQL_SAFE_UPDATES = 0;";
            # cursor.execute(Quety2)
            # Quety2 = Query
            # cursor.execute(Quety2)
            # db.commit()
            # db.close()
            return ""
        except :
            return "Error : [ " + str(sys.exc_info()) + "]"
    def Dame_Nombre_IDEmpleado(self,idEmpleado):
        Res = "-"
        for Emp in self.Get_Dato("SELECT \"Nombre\" FROM public.cuser where cusrid = '"+str(idEmpleado)+"'"):
            Res = str(Emp["Nombre"])
        return (Res)
    def Dame_Nombre_IDUsuario(self,IDUsuario):
        Res = "-"
        for Emp in self.Get_Dato("SELECT \"Nombre\" FROM public.cuser where cusrid = '"+str(IDUsuario)+"'"):
            Res = str(Emp["Nombre"])
        return (Res)
    def Dame_Hora(self):
        return datetime.now();
        #return datetime.now() - timedelta(hours=1);
class Compartido:
    def __init__(self):
        return;
    def Complementos(self,Adicinal):
        Url_root = request.url_root
        Url = str(request.url_root)+"/recurso"
        Path_Componentes = str(current_app.root_path).replace("\\","/")
        #Normal
        Colores = "#EF2D35,#191919"
        if int(datetime.now().strftime("%m")) == 12:
            #Navidad
            Colores = "#ff0000,#ff0000,#ffffff,#ff0000,#ffffff,#191919"
        if str(datetime.now().strftime("%m-%d")) == "09-16":
            #Mexico
            Colores = "#006545,#ffffff,#C81025,#191919,#191919"
        if str(datetime.now().strftime("%m-%d")) == "07-04":
            #EUA
            Colores = "#38376A,#AC2132,#ffffff,#191919,#191919"
        if str(datetime.now().strftime("%m-%d")) == "07-20":
            Colores = "#F7C700,#002F83,#C20F2C,#191919,#191919"
        if str(datetime.now().strftime("%m-%d")) == "07-01":
            #Canada
            Colores = "#CE2A1D,#ffffff,#CE2A1D,#191919,#191919"
        Colores_Aro = "45deg"
        for n in range(3):
            Colores_Aro += ","+str(Colores)
        Compl = ""
        Compl += "<link rel='icon' href=\""+str(Url)+"/Portal_File/Media/UniversalLogo2.png\" type='image/icon type'>"
        Compl += "<title>Universal YMS</title>"
        contenido = sorted(os.listdir(str(Path_Componentes)+'/static/Default'))
        for Arch in contenido:
            if ".js" in str(Arch):
                Compl += """<script type="text/javascript" src=\""""+str(Url)+"""/Default/"""+str(Arch)+""""></script>"""
            if ".css" in str(Arch):
                Compl += """<link rel="stylesheet" type="text/css" href=\""""+str(Url)+"""/Default/"""+str(Arch)+"""">"""
        Compl += """<link rel="stylesheet" type="text/css" href=\""""+str(Url)+"""/Default/MaterialDesign/css/materialdesignicons.min.css">"""
        if Adicinal is not None:
            Adicional_Dir = sorted(os.listdir(str(Path_Componentes)+'/static/Adicional'))
            for Arch in Adicional_Dir:
                for Add in Adicinal:
                    if Arch[0:2] == Add:
                        if ".js" in str(Arch):
                            Compl += """<script type="text/javascript" src=\""""+str(Url)+"""/Adicional/"""+str(Arch)+""""></script>"""
                        if ".css" in str(Arch):
                            Compl += """<link rel="stylesheet" type="text/css" href=\""""+str(Url)+"""/Adicional/"""+str(Arch)+""""">"""
            if "01" in Adicinal:
                Compl += """<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/v/bs5/dt-1.12.1/datatables.min.css">"""
        
            if "Menu_N" in Adicinal:
                Compl += """
                <div class='fixed-top bg-dark-subtle' style='min-height:43px; box-shadow: rgba(0, 0, 0, 0.19) 0px 10px 20px, rgba(0, 0, 0, 0.23) 0px 6px 6px;' >
                    <div id='Menu_Top' class='row' style='min-height:43px; shadow '>
                        <div class='col-auto me-0 pe-0'>
                            <div class="text-center bg-secondary d-flex justify-content-center align-items-center h-100" style='width:55px;'>
                                <div><img style='width:50px; height:auto;' src='data:image/bmp;base64,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' alt="Linc"></div>
                            </div>
                        </div>
                        <div class='col-auto ms-0'>
                            <div class='h-100 d-flex justify-content-center align-items-center fw-bold' id='Menu_2_Titulo'></div>
                        </div>
                        <div class='col'>
                            <ul class="nav nav-tabs justify-content-center border-0 h-100" id='Menu_2'></ul>
                        </div>
                        <div class='col-auto row me-2 fw-bold' id='Notificaciones'>
                            <div class='col d-flex justify-content-center align-items-center'>
                                <div style='font-size:15px;  cursor:pointer;' class='mdi mdi-alarm-light position-relative' data-bs-toggle="offcanvas" onclick='Ver_Alarmas();' data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">
                                    <span id='Contador_Ala' style='display:none;' class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">1</span>
                                </div>
                            </div>
                            <div class='col d-flex justify-content-center align-items-center'>
                                <div style='font-size:15px; cursor:pointer;' class='mdi mdi-bell position-relative' data-bs-toggle="offcanvas" onclick='Ver_Notificaciones();' data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">
                                    <span id='Contador_Not' style='display:none;' class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-primary"></span>
                                </div>
                            </div>
                            <div class='col-auto d-flex justify-content-center align-items-center'>
                                <div style='font-size:15px; cursor:pointer;' class='mdi mdi-calendar position-relative' data-bs-toggle="offcanvas" onclick='Ver_Notificaciones();' data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">
                                    <span id='Contador_Not' style='display:none;' class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-primary"></span>
                                    """+str(datetime.now().strftime("%d %b, %Y"))+"""
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div id='Item_Menu_Pre' style='display:none;'></div>
                <div id='Menu_Left'  class="fixed-top bg-dark-subtle " style='height: 100%; width: 55px; top:43px; box-shadow: rgba(0, 0, 0, 0.09) 1px 2px 1px, rgba(0, 0, 0, 0.09) 2px 4px 2px, rgba(0, 0, 0, 0.09) 4px 8px 4px, rgba(0, 0, 0, 0.09) 8px 16px 8px, rgba(0, 0, 0, 0.09) 16px 32px 16px; '>
                    <div class="overflow-auto w-100 pb-5" style='height:90%;'>
                        <div class='w-100' id='Menu_1'>
                        </div>
                    </div>

                    <div class='fixed-bottom pb-2 bg-dark-subtle' style='width: 55px;'>
                        <div class="dropdown bg-dark-subtle">
                            <a class="fs-6 nav-link dropdown-toggle badge rounded-pill text-bg-dark text-center ms-1 me-1" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false"><i class='mdi mdi-account'></i></a>
                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="#"><i class="mdi mdi-exit-run"></i> Sign off</a></li>
                                <li><a class="dropdown-item" href="#"><i class="mdi mdi-form-textbox-password"></i> Change password</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                """
        Compl += """
        <script>
            function Enviar_Alerta_Slack(channel,text){
                $.ajax({                   
                    data: {"token": 'xoxb-6219782511137-6220238287665-nvHc8vQnTudY0NuyJN7BMkXz',"channel": channel,"text": text},                      
                    dataType: 'text',type: 'POST',url: "https://slack.com/api/chat.postMessage",error: function(xhr,status,error){},success: function(data) {}
                });
            }
            $(window).on('beforeunload', function(){
                alert("ok");
            });
            $(window).on('resize', function(){
                $("body").css('padding-top',$("#Menu_Top").height());
                $("#Menu_Left").css('top',$("#Menu_Top").height());
            });
            function Mensaje(Tipo,Mensaje=null){
                if(Tipo == 0){
                    if(Mensaje == null || Mensaje.trim() == "")
                        Swal.fire({icon: 'error',position: 'top-end',title: 'Error process!',showConfirmButton: false,toast: true,background : "#ffbfbf",timer: 10000,timerProgressBar: true,customClass: {confirmButton: 'btn btn-danger btn-sm p-0 m-p ps-1 pe-1'},buttonsStyling: false});
                    else
                        Swal.fire({icon: 'error',position: 'top-end',title: 'Error ['+Mensaje+']',toast: true,background : "#ffbfbf",timer: 10000,timerProgressBar: true,customClass: {confirmButton: 'btn btn-danger btn-sm p-0 m-p ps-1 pe-1'},buttonsStyling: false});
                }
                else if(Tipo == 1){
                    if(Mensaje == null || Mensaje.trim() == "")
                        Swal.fire({icon: 'alert',position: 'top-end',title: '<i class="mdi mdi-alert"></i> Alert process!',showConfirmButton: false,toast: true,background : "#ffeb96",timer: 10000,timerProgressBar: true,customClass: {confirmButton: 'btn btn-danger btn-sm p-0 m-p ps-1 pe-1'},buttonsStyling: false});
                    else
                        Swal.fire({icon: 'alert',position: 'top-end',title: Mensaje,showConfirmButton: false,toast: true,background : "#ffeb96",timer: 10000,timerProgressBar: true,customClass: {confirmButton: 'btn btn-danger btn-sm p-0 m-p ps-1 pe-1'},buttonsStyling: false});
                }
                else{
                    if(Mensaje == null || Mensaje.trim() == "")
                        Swal.fire({icon: 'success',position: 'top-end',title: 'Successful process!',showConfirmButton: false,toast: true,background : "#c9fad7",timer: 1500,timerProgressBar: true});
                    else
                        Swal.fire({icon: 'success',position: 'top-end',title: Mensaje,showConfirmButton: false,toast: true,background : "#c9fad7",timer: 1500,timerProgressBar: true});
                }
                
            }
            function Menu_2(Key_Master)
            {

                $(".Item_Menu1").each(function() {
                    $(this).css('background','').css('color','');
                });
                $(".Item_Menu1[Key-Master='"+Key_Master+"']").css('background',$(".Item_Menu1[Key-Master='"+Key_Master+"']").attr('bg')).css('color',$(".Item_Menu1[Key-Master='"+Key_Master+"']").attr('lt'));

                $("#Menu_2").html( $("#Item_Menu_Pre").find(".Menu_2_Pre[KeyMaster='"+Key_Master+"']").html());
                $("#Menu_2_Titulo").html( "<div><i class='"+$("#Item_Menu_Pre").find(".Menu_2_Pre[KeyMaster='"+Key_Master+"']").attr('Icono')+"'></i> "+$("#Item_Menu_Pre").find(".Menu_2_Pre[KeyMaster='"+Key_Master+"']").attr('Titulo')+"</div>");
                
                $("#Notificaciones").css('color',$("#Item_Menu_Pre").find(".Menu_2_Pre[KeyMaster='"+Key_Master+"']").attr('Color_Letra'));
                $("#Menu_2_Titulo").parent().css('background',$("#Item_Menu_Pre").find(".Menu_2_Pre[KeyMaster='"+Key_Master+"']").attr('Color')).css('color',$("#Item_Menu_Pre").find(".Menu_2_Pre[KeyMaster='"+Key_Master+"']").attr('Color_Letra'));
                $("#Menu_2").parent().parent().css('background',$("#Item_Menu_Pre").find(".Menu_2_Pre[KeyMaster='"+Key_Master+"']").attr('Color'))
                $("#Menu_2").css('background',$("#Item_Menu_Pre").find(".Menu_2_Pre[KeyMaster='"+Key_Master+"']").attr('Color_Letra'))
                
                $("body").css('padding-top',$("#Menu_Top").height());
                $("#Menu_Left").css('top',$("#Menu_Top").height());
                swal.close();

               
            }

             $(document).ready(function() {
                const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
                const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
            });
            function Mostrar_Ventana_Cargando(Esperar_Completo){
                delete Swal_Cargar;
                var Swal_Cargar = Swal.fire({html: "<div class='row m-0 p-0'><div class='col m-0 p-0 h-100 d-flex justify-content-center align-items-center'><img class='Logo_Universal' src='data:image/bmp;base64,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' width='125' height='71'></img></div> <div class='col m-0 p-0 d-flex flex-column justify-content-center align-items-center'><div class='spinner-border text-danger' role='status'></div><img src='data:image/bmp;base64,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' class='Logo_Letras' width='155' height='20'></img></div> </div><hr> <div class='row p-0 m-0'><div class='col p-0 m-0 d-flex flex-row'><img class='Bandera_USA' src=' data:image/webp;base64,UklGRsgDAABXRUJQVlA4WAoAAAAgAAAAHwAAEAAASUNDUKACAAAAAAKgbGNtcwQwAABtbnRyUkdCIFhZWiAH5wACAAkADgAOAC1hY3NwTVNGVAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA9tYAAQAAAADTLWxjbXMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1kZXNjAAABIAAAAEBjcHJ0AAABYAAAADZ3dHB0AAABmAAAABRjaGFkAAABrAAAACxyWFlaAAAB2AAAABRiWFlaAAAB7AAAABRnWFlaAAACAAAAABRyVFJDAAACFAAAACBnVFJDAAACFAAAACBiVFJDAAACFAAAACBjaHJtAAACNAAAACRkbW5kAAACWAAAACRkbWRkAAACfAAAACRtbHVjAAAAAAAAAAEAAAAMZW5VUwAAACQAAAAcAEcASQBNAFAAIABiAHUAaQBsAHQALQBpAG4AIABzAFIARwBCbWx1YwAAAAAAAAABAAAADGVuVVMAAAAaAAAAHABQAHUAYgBsAGkAYwAgAEQAbwBtAGEAaQBuAABYWVogAAAAAAAA9tYAAQAAAADTLXNmMzIAAAAAAAEMQgAABd7///MlAAAHkwAA/ZD///uh///9ogAAA9wAAMBuWFlaIAAAAAAAAG+gAAA49QAAA5BYWVogAAAAAAAAJJ8AAA+EAAC2xFhZWiAAAAAAAABilwAAt4cAABjZcGFyYQAAAAAAAwAAAAJmZgAA8qcAAA1ZAAAT0AAACltjaHJtAAAAAAADAAAAAKPXAABUfAAATM0AAJmaAAAmZwAAD1xtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAEcASQBNAFBtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAHMAUgBHAEJWUDggAgEAALAFAJ0BKiAAEQA+MRaJQ6IhIRQEACADBLIPoARRCpbkBaIH4qzyL/AeSz4v6SUJ3yFIo0hgQAD+5sJMiYc1fIe/f4E/j/0zL/CPHrK4hrucvb6xO8oqrvF6B36gy7TWFx7c4f8gsAG7kRhU01RgC/xVsUC5fna9f/NMVf9ZxnBTcNv6z1hk+/rkv+rRv1uo24AX0L/aO5JM6s6L6JSnbCP9nK//lczeY+dZOP6s9OuQ+HuJ/6pO4osE69X1EePlH/c30JA/9syiq+XpTWJNOCxo5LGv6kSuKNJknxlngVys6cEFf8rfUiweK8/WpCneacyim/+n1f+n1f/T6v/TnAAAAA==' width='30px' height='17px'></img><img src='data:image/webp;base64,UklGRowDAABXRUJQVlA4WAoAAAAgAAAAHQAAEAAASUNDUKACAAAAAAKgbGNtcwQwAABtbnRyUkdCIFhZWiAH5wACAAkADgAOAC1hY3NwTVNGVAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA9tYAAQAAAADTLWxjbXMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1kZXNjAAABIAAAAEBjcHJ0AAABYAAAADZ3dHB0AAABmAAAABRjaGFkAAABrAAAACxyWFlaAAAB2AAAABRiWFlaAAAB7AAAABRnWFlaAAACAAAAABRyVFJDAAACFAAAACBnVFJDAAACFAAAACBiVFJDAAACFAAAACBjaHJtAAACNAAAACRkbW5kAAACWAAAACRkbWRkAAACfAAAACRtbHVjAAAAAAAAAAEAAAAMZW5VUwAAACQAAAAcAEcASQBNAFAAIABiAHUAaQBsAHQALQBpAG4AIABzAFIARwBCbWx1YwAAAAAAAAABAAAADGVuVVMAAAAaAAAAHABQAHUAYgBsAGkAYwAgAEQAbwBtAGEAaQBuAABYWVogAAAAAAAA9tYAAQAAAADTLXNmMzIAAAAAAAEMQgAABd7///MlAAAHkwAA/ZD///uh///9ogAAA9wAAMBuWFlaIAAAAAAAAG+gAAA49QAAA5BYWVogAAAAAAAAJJ8AAA+EAAC2xFhZWiAAAAAAAABilwAAt4cAABjZcGFyYQAAAAAAAwAAAAJmZgAA8qcAAA1ZAAAT0AAACltjaHJtAAAAAAADAAAAAKPXAABUfAAATM0AAJmaAAAmZwAAD1xtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAEcASQBNAFBtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAHMAUgBHAEJWUDggxgAAABAFAJ0BKh4AEQA+LRCHQqGhDf6qAAwBYlqALszND9QKLLBBA0HFB1zBQ6XtYkwSMAgA/v1V7f6x//G1d//yMmi6voc0CxeNNLr9BVQ0LTmmHeFAny62kKZ9vEK/f/+4/P/x2f2/Jv/9j/f9n/6//kvoPu1NMqVKfUIFXvRbS9e2Sb7WMIy69IkdVp/i687XzC/Vjd8BzxvA/66D/ygcP+VD/+tg/ut/8oA3/BD/9XPX2n4DBdpMM4KzVzDsvJpuc2HZ3jAAAA==' class='Bandera_MX' width='30px' height='17px'></img><img  class='Bandera_COL' src='data:image/png;base64,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cmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIgogICAgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIKICAgIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIKICAgIHhtbG5zOkdJTVA9Imh0dHA6Ly93d3cuZ2ltcC5vcmcveG1wLyIKICAgIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIgogICAgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIgogICB4bXBNTTpEb2N1bWVudElEPSJnaW1wOmRvY2lkOmdpbXA6N2E5MTFkM2EtNWVhMC00YWYyLTg1MTMtODZlODRjOThhOWRiIgogICB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjQ5MjY2NWEwLWRhNzQtNGE1Yy04NzcwLWEyNGU4NDM1YTdhMCIKICAgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ4bXAuZGlkOjA2NTZhYWIwLTBhYzEtNDRmOS1iY2EwLTE0NmUxNmZjMWRlYyIKICAgZGM6Rm9ybWF0PSJpbWFnZS9wbmciCiAgIEdJTVA6QVBJPSIyLjAiCiAgIEdJTVA6UGxhdGZvcm09IldpbmRvd3MiCiAgIEdJTVA6VGltZVN0YW1wPSIxNjc1OTUyNDU2NDAxMzA5IgogICBHSU1QOlZlcnNpb249IjIuMTAuMzIiCiAgIHRpZmY6T3JpZW50YXRpb249IjEiCiAgIHhtcDpDcmVhdG9yVG9vbD0iR0lNUCAyLjEwIgogICB4bXA6TWV0YWRhdGFEYXRlPSIyMDIzOjAyOjA5VDA4OjIwOjU2LTA2OjAwIgogICB4bXA6TW9kaWZ5RGF0ZT0iMjAyMzowMjowOVQwODoyMDo1Ni0wNjowMCI+CiAgIDx4bXBNTTpIaXN0b3J5PgogICAgPHJkZjpTZXE+CiAgICAgPHJkZjpsaQogICAgICBzdEV2dDphY3Rpb249InNhdmVkIgogICAgICBzdEV2dDpjaGFuZ2VkPSIvIgogICAgICBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjAwOWZjYjJmLWM4MzEtNGZiNy04M2NkLTVkODA3NGE1ZGMxNCIKICAgICAgc3RFdnQ6c29mdHdhcmVBZ2VudD0iR2ltcCAyLjEwIChXaW5kb3dzKSIKICAgICAgc3RFdnQ6d2hlbj0iMjAyMy0wMi0wOVQwODoyMDo1NiIvPgogICAgPC9yZGY6U2VxPgogICA8L3htcE1NOkhpc3Rvcnk+CiAgPC9yZGY6RGVzY3JpcHRpb24+CiA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgCjw/eHBhY2tldCBlbmQ9InciPz5BKqYrAAAADFBMVEX/zQDIEC5kIFoAMIfTZVjAAAAAAWJLR0QAiAUdSAAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+cCCQ4UOMxv37EAAAAbSURBVAjXY2CgEvgPBh8w6FVgsIAhFAwCcNEAcbwikyuS05oAAAAASUVORK5CYII=' width='30px' height='17px'></img></div><div class='col p-0 m-0 text-end fs-6 text-muted'>Portal 2023</div></div>",allowOutsideClick: false,stopKeydownPropagation: false,showConfirmButton: false,backdrop: 'rgba(0, 0, 0, 0.90)',customClass:{popup:'block'}});
                /*LoadImagesAndRender('Logo_Linc',130,73,'Logo_Linc');
                LoadImagesAndRender('Logo_Letras',155,20,'Logo_Letras');
                LoadImagesAndRender('Logo_Universal',125,71,'Logo_Universal');
                LoadImagesAndRender('Bandera_MX',30,17,'Bandera_MX');
                LoadImagesAndRender('Bandera_USA',30,17,'Bandera_USA');
                LoadImagesAndRender('Bandera_COL',30,17,'Bandera_COL');*/
                if(Esperar_Completo == true)
                    Cargando();
            }

            function Cargando()
            {
                var Entra = 0;
                $(".Completar").each(function() {
                    if($(this).attr('completo')*1 == 0)
                    {
                        Entra = 1;
                    }
                });
                if(Entra == 1)
                    setTimeout(Cargando, 300);
                else
                    swal.close();
            }

            function LoadImagesAndRender(ID,W,H,Imagen){
                    var date = new Date().toJSON().replace("-", "").replace(":", "").replace(".", "").replace("-", "").replace(":", "").replace(".", "").replace("Z", "").replace("T", "");
                    date = date.substring(date.length - 2);
                     delete images;
                    if(Imagen == "Logo_Linc")
                        var images = ['data:image/bmp;base64,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'];
                    if(Imagen == "Logo_Universal")
                        var images = ['data:image/bmp;base64,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'+date];
                    if(Imagen == "Logo_Letras")
                        var images = ['data:image/bmp;base64,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'];;
                    if(Imagen == "Bandera_MX")
                        var images = ['data:image/webp;base64,UklGRowDAABXRUJQVlA4WAoAAAAgAAAAHQAAEAAASUNDUKACAAAAAAKgbGNtcwQwAABtbnRyUkdCIFhZWiAH5wACAAkADgAOAC1hY3NwTVNGVAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA9tYAAQAAAADTLWxjbXMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1kZXNjAAABIAAAAEBjcHJ0AAABYAAAADZ3dHB0AAABmAAAABRjaGFkAAABrAAAACxyWFlaAAAB2AAAABRiWFlaAAAB7AAAABRnWFlaAAACAAAAABRyVFJDAAACFAAAACBnVFJDAAACFAAAACBiVFJDAAACFAAAACBjaHJtAAACNAAAACRkbW5kAAACWAAAACRkbWRkAAACfAAAACRtbHVjAAAAAAAAAAEAAAAMZW5VUwAAACQAAAAcAEcASQBNAFAAIABiAHUAaQBsAHQALQBpAG4AIABzAFIARwBCbWx1YwAAAAAAAAABAAAADGVuVVMAAAAaAAAAHABQAHUAYgBsAGkAYwAgAEQAbwBtAGEAaQBuAABYWVogAAAAAAAA9tYAAQAAAADTLXNmMzIAAAAAAAEMQgAABd7///MlAAAHkwAA/ZD///uh///9ogAAA9wAAMBuWFlaIAAAAAAAAG+gAAA49QAAA5BYWVogAAAAAAAAJJ8AAA+EAAC2xFhZWiAAAAAAAABilwAAt4cAABjZcGFyYQAAAAAAAwAAAAJmZgAA8qcAAA1ZAAAT0AAACltjaHJtAAAAAAADAAAAAKPXAABUfAAATM0AAJmaAAAmZwAAD1xtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAEcASQBNAFBtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAHMAUgBHAEJWUDggxgAAABAFAJ0BKh4AEQA+LRCHQqGhDf6qAAwBYlqALszND9QKLLBBA0HFB1zBQ6XtYkwSMAgA/v1V7f6x//G1d//yMmi6voc0CxeNNLr9BVQ0LTmmHeFAny62kKZ9vEK/f/+4/P/x2f2/Jv/9j/f9n/6//kvoPu1NMqVKfUIFXvRbS9e2Sb7WMIy69IkdVp/i687XzC/Vjd8BzxvA/66D/ygcP+VD/+tg/ut/8oA3/BD/9XPX2n4DBdpMM4KzVzDsvJpuc2HZ3jAAAA=='];
                    if(Imagen == "Bandera_USA")
                        var images = [' data:image/webp;base64,UklGRsgDAABXRUJQVlA4WAoAAAAgAAAAHwAAEAAASUNDUKACAAAAAAKgbGNtcwQwAABtbnRyUkdCIFhZWiAH5wACAAkADgAOAC1hY3NwTVNGVAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA9tYAAQAAAADTLWxjbXMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1kZXNjAAABIAAAAEBjcHJ0AAABYAAAADZ3dHB0AAABmAAAABRjaGFkAAABrAAAACxyWFlaAAAB2AAAABRiWFlaAAAB7AAAABRnWFlaAAACAAAAABRyVFJDAAACFAAAACBnVFJDAAACFAAAACBiVFJDAAACFAAAACBjaHJtAAACNAAAACRkbW5kAAACWAAAACRkbWRkAAACfAAAACRtbHVjAAAAAAAAAAEAAAAMZW5VUwAAACQAAAAcAEcASQBNAFAAIABiAHUAaQBsAHQALQBpAG4AIABzAFIARwBCbWx1YwAAAAAAAAABAAAADGVuVVMAAAAaAAAAHABQAHUAYgBsAGkAYwAgAEQAbwBtAGEAaQBuAABYWVogAAAAAAAA9tYAAQAAAADTLXNmMzIAAAAAAAEMQgAABd7///MlAAAHkwAA/ZD///uh///9ogAAA9wAAMBuWFlaIAAAAAAAAG+gAAA49QAAA5BYWVogAAAAAAAAJJ8AAA+EAAC2xFhZWiAAAAAAAABilwAAt4cAABjZcGFyYQAAAAAAAwAAAAJmZgAA8qcAAA1ZAAAT0AAACltjaHJtAAAAAAADAAAAAKPXAABUfAAATM0AAJmaAAAmZwAAD1xtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAEcASQBNAFBtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAHMAUgBHAEJWUDggAgEAALAFAJ0BKiAAEQA+MRaJQ6IhIRQEACADBLIPoARRCpbkBaIH4qzyL/AeSz4v6SUJ3yFIo0hgQAD+5sJMiYc1fIe/f4E/j/0zL/CPHrK4hrucvb6xO8oqrvF6B36gy7TWFx7c4f8gsAG7kRhU01RgC/xVsUC5fna9f/NMVf9ZxnBTcNv6z1hk+/rkv+rRv1uo24AX0L/aO5JM6s6L6JSnbCP9nK//lczeY+dZOP6s9OuQ+HuJ/6pO4osE69X1EePlH/c30JA/9syiq+XpTWJNOCxo5LGv6kSuKNJknxlngVys6cEFf8rfUiweK8/WpCneacyim/+n1f+n1f/T6v/TnAAAAA=='];
                    if(Imagen == "Bandera_COL") 
                        var images = ['data:image/png;base64,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cmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIgogICAgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIKICAgIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIKICAgIHhtbG5zOkdJTVA9Imh0dHA6Ly93d3cuZ2ltcC5vcmcveG1wLyIKICAgIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIgogICAgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIgogICB4bXBNTTpEb2N1bWVudElEPSJnaW1wOmRvY2lkOmdpbXA6N2E5MTFkM2EtNWVhMC00YWYyLTg1MTMtODZlODRjOThhOWRiIgogICB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjQ5MjY2NWEwLWRhNzQtNGE1Yy04NzcwLWEyNGU4NDM1YTdhMCIKICAgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ4bXAuZGlkOjA2NTZhYWIwLTBhYzEtNDRmOS1iY2EwLTE0NmUxNmZjMWRlYyIKICAgZGM6Rm9ybWF0PSJpbWFnZS9wbmciCiAgIEdJTVA6QVBJPSIyLjAiCiAgIEdJTVA6UGxhdGZvcm09IldpbmRvd3MiCiAgIEdJTVA6VGltZVN0YW1wPSIxNjc1OTUyNDU2NDAxMzA5IgogICBHSU1QOlZlcnNpb249IjIuMTAuMzIiCiAgIHRpZmY6T3JpZW50YXRpb249IjEiCiAgIHhtcDpDcmVhdG9yVG9vbD0iR0lNUCAyLjEwIgogICB4bXA6TWV0YWRhdGFEYXRlPSIyMDIzOjAyOjA5VDA4OjIwOjU2LTA2OjAwIgogICB4bXA6TW9kaWZ5RGF0ZT0iMjAyMzowMjowOVQwODoyMDo1Ni0wNjowMCI+CiAgIDx4bXBNTTpIaXN0b3J5PgogICAgPHJkZjpTZXE+CiAgICAgPHJkZjpsaQogICAgICBzdEV2dDphY3Rpb249InNhdmVkIgogICAgICBzdEV2dDpjaGFuZ2VkPSIvIgogICAgICBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjAwOWZjYjJmLWM4MzEtNGZiNy04M2NkLTVkODA3NGE1ZGMxNCIKICAgICAgc3RFdnQ6c29mdHdhcmVBZ2VudD0iR2ltcCAyLjEwIChXaW5kb3dzKSIKICAgICAgc3RFdnQ6d2hlbj0iMjAyMy0wMi0wOVQwODoyMDo1NiIvPgogICAgPC9yZGY6U2VxPgogICA8L3htcE1NOkhpc3Rvcnk+CiAgPC9yZGY6RGVzY3JpcHRpb24+CiA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgCjw/eHBhY2tldCBlbmQ9InciPz5BKqYrAAAADFBMVEX/zQDIEC5kIFoAMIfTZVjAAAAAAWJLR0QAiAUdSAAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+cCCQ4UOMxv37EAAAAbSURBVAjXY2CgEvgPBh8w6FVgsIAhFAwCcNEAcbwikyuS05oAAAAASUVORK5CYII='];
                    var loadedImages=0;
                    for(var i=0;i<images.length;i++){
                        var source=images[i];
                        images[i] = new Image();
                        images[i].src=source;
                        images[i].onload = function(){loadedImages++;if (loadedImages==images.length){Render(ID,W,H,images);}};
                    }
            }
            function Render(ID,W,H,images){
                var canvas = $("."+ID)[0];
                var ctx = canvas.getContext('2d');
                canvas.width=W;
                canvas.height=H;
                ctx.drawImage(images[0],0,0,W,H,0,0,W,H);
            }

            function Cambia_Texto(Control)
            {
                Verificar_Dato(Control);
            }
            function Actualizar_Cambia_Texto()
            {
                $(".formulario-informacion").each(function() {
                    Verificar_Dato(this);
                });
            }
            function Verificar_Dato(Control)
            {
                if( $(Control).attr('tipo') == 'texto' )
                {
                    if( $(Control).val().length > $(Control).attr('Max') || $(Control).val().length < $(Control).attr('Min') ){ $(Control).addClass('is-invalid').attr('valido',false).parent().find('.Lleva').removeClass('bg-success').addClass('bg-danger'); } else { $(Control).removeClass('is-invalid').attr('valido',true).parent().find('.Lleva').removeClass('bg-danger').addClass('bg-success'); }
                    $(Control).parent().find('.Lleva').html( $(Control).val().length );
                }
                if( $(Control).attr('tipo') == 'color' )
                {
                    if($(Control).attr('requerido') == 'true' && $(Control).val().trim() == "") { $(Control).addClass('is-invalid').attr('valido',false); }else{  $(Control).removeClass('is-invalid').attr('valido',true); }
                }
                if( $(Control).attr('tipo') == 'seleccion')
                {
                    if( $(Control).attr('requerido') == 'true' && $(Control).find("option:selected.valio").length == 0)
                        $(Control).addClass('is-invalid').attr('valido',false);
                    else
                        $(Control).removeClass('is-invalid').attr('valido',true);
                }
                if($(Control).attr('tipo') == 'multiseleccion')
                {
                    if( $(Control).attr('requerido') == 'true' && $(Control).find("option:selected.valio").length == 0)
                    {
                        $(Control).addClass('is-invalid').attr('valido',false);
                        $(Control).next().find('.selection > .select2-selection').addClass('border-danger');
                    }
                    else
                    {
                        $(Control).removeClass('is-invalid').attr('valido',true);
                        $(Control).next().find('.selection > .select2-selection').removeClass('border-danger');
                    }

                }
                if( $(Control).attr('tipo') == 'fecha' || $(Control).attr('tipo') == 'hora' || $(Control).attr('tipo') == 'fecha-rango' || $(Control).attr('tipo') == 'fecha-hora' || $(Control).attr('tipo') == 'fecha-multi')
                {
                    if($(Control).attr('requerido') == 'true' && $(Control).val().trim() == "") { $(Control).addClass('is-invalid').attr('valido',false); }else{  $(Control).removeClass('is-invalid').attr('valido',true); }
                }
                if( $(Control).attr('tipo') == 'archivo' )
                {
                    if( $(Control).find(".filepond--data").children().length > $(Control).attr('Max') || $(Control).find(".filepond--data").children().length < $(Control).attr('Min'))
                    {
                        $(Control).attr('valido',false).find('.Lleva').removeClass('bg-success').addClass('bg-danger');
                        $(Control).find(".filepond--root").addClass('border border-danger');
                    }
                    else
                    {
                        $(Control).attr('valido',true).find('.Lleva').removeClass('bg-danger').addClass('bg-success');
                        $(Control).find(".filepond--root").removeClass('border border-danger');
                    }
                    $(Control).find('.Lleva').html( $(Control).find(".filepond--data").children().length );
                }
                if( $(Control).attr('tipo') == 'numero' )
                {
                    var Sintax = /^\d*\.*\d+$|(^$)/;
                    if( $(Control).val().length > $(Control).attr('Max') || $(Control).val().length < $(Control).attr('Min') || !Sintax.test($(Control).val()) ){ $(Control).addClass('is-invalid').attr('valido',false).parent().find('.Lleva').removeClass('bg-success').addClass('bg-danger'); } else { $(Control).removeClass('is-invalid').attr('valido',true).parent().find('.Lleva').removeClass('bg-danger').addClass('bg-success'); }
                    $(Control).parent().find('.Lleva').html( $(Control).val().length );

                }
                if( $(Control).attr('tipo') == 'email' )
                {
                    var Sintax = /(\w+@\w+\.\w+)|(^$)/;
                    if( $(Control).val().length > $(Control).attr('Max') || $(Control).val().length < $(Control).attr('Min') || !Sintax.test($(Control).val()) ){ $(Control).addClass('is-invalid').attr('valido',false).parent().find('.Lleva').removeClass('bg-success').addClass('bg-danger'); } else { $(Control).removeClass('is-invalid').attr('valido',true).parent().find('.Lleva').removeClass('bg-danger').addClass('bg-success'); }
                    $(Control).parent().find('.Lleva').html( $(Control).val().length );
                }
                if( $(Control).attr('tipo') == 'lista' )
                {
                    if( $(Control).find(".list-group").children().length > $(Control).attr('Max') || $(Control).find(".list-group").children().length < $(Control).attr('Min') ){ $(Control).find(".list-group").parent().addClass('border-danger'); $(Control).attr('valido',false).find('.Lleva').removeClass('bg-success').addClass('bg-danger');; } else { $(Control).find(".list-group").parent().removeClass('border-danger'); $(Control).attr('valido',true).find('.Lleva').removeClass('bg-danger').addClass('bg-success'); }
                    $(Control).parent().find('.Lleva').html( $(Control).find(".list-group").children().length );
                }

                if($(Control).attr("tipo") == 'radio')
                {
                    var Seleccinado = false;
                    $(Control).find('input[type="radio"]').each(function() {
                        if($(this).is(":checked"))
                            Seleccinado = true;
                    });

                    if(Seleccinado == true)
                    {
                        $(Control).find('input[type="radio"]').each(function() {
                           $(this).removeClass("is-invalid");
                        });
                         $(Control).attr('valido',true);
                    }
                    else
                    {
                         $(Control).find('input[type="radio"]').each(function() {
                           $(this).addClass("is-invalid");
                        });
                        $(Control).attr('valido',false);
                    }
                }
            

            }

            function Dame_Formulario(Clase_Adicional,Mensaje)
            {
                var Error = 0;
                Info = {};
                $(".formulario-informacion"+Clase_Adicional).each(function() {
                    if( $(this).attr('valido') == 'false')
                        Error = 1;
                });
                if(Error == 1)
                {
                    if(Mensaje == true)
                        Swal.fire({icon: 'warning',position: 'top-end',title: 'Check required fields.',showConfirmButton: false,toast: true,background : "#ffeb96",timer: 1500,timerProgressBar: true});
                    return null;
                }
                var Info = {};
                $(".formulario-informacion"+Clase_Adicional).each(function() {
                    if( $(this).attr("tipo") == 'texto' || $(this).attr("tipo") == 'color' || $(this).attr("tipo") == 'fecha' || $(this).attr("tipo") == 'hora' || $(this).attr("tipo") == 'fecha-hora' || $(this).attr("tipo") == 'numero' || $(this).attr("tipo") == 'email')
                        Info[$(this).attr('campo')] = $(this).val().trim();
                    if( $(this).attr("tipo") == 'fecha-rango')
                    {
                        var Fecha_Inicio = "";
                        var Fecha_Fin = "";
                        if($(this).val().trim().includes("a"))
                        {
                            Info[$(this).attr('campo')] = []
                            Info[$(this).attr('campo')].push( $(this).val().trim().split('a')[0].trim() );
                            Info[$(this).attr('campo')].push( $(this).val().trim().split('a')[1].trim() );
                        }
                        else if($(this).val().trim().includes("to"))
                        {
                            Info[$(this).attr('campo')] = []
                            Info[$(this).attr('campo')].push( $(this).val().trim().split('to')[0].trim() );
                            Info[$(this).attr('campo')].push( $(this).val().trim().split('to')[1].trim() );
                        }
                        else
                        {
                            Info[$(this).attr('campo')] = []
                            Info[$(this).attr('campo')].push( $(this).val().trim() );
                            Info[$(this).attr('campo')].push( $(this).val().trim() );
                        }
                    }
                    if( $(this).attr("tipo") == 'fecha-multi')
                    {
                        var Fechas = []
                        for (var i = 0; i < $(this).val().trim().split(",").length; i++) {
                            Fechas.push( $(this).val().trim().split(",")[i] );
                        }
                        Info[$(this).attr('campo')] = Fechas
                    }
                    if($(this).attr("tipo") == 'seleccion')
                    {
                        Info[$(this).attr('campo')] = $(this).find('option:selected').val().trim()
                    }
                    if($(this).attr("tipo") == 'multiseleccion')
                    {
                        var Valores = []
                        $(this).find('option:selected').each(function() {
                            Valores.push($(this).val().trim());
                        });
                        Info[$(this).attr('campo')] = Valores;
                    }
                    if($(this).attr("tipo") == 'archivo')
                    {
                        var Master = this;
                        var Archivos = [];
                        $(Master).find('.filepond--data').children().each(function() {
                            if($(this).attr("archivo") != null)
                                Archivos.push($(this).attr("archivo"));
                        });
                        Info[$(Master).attr('campo')] = Archivos;
                    }
                    if($(this).attr("tipo") == 'lista')
                    {
                        var Master = this;
                        Info[$(Master).attr('campo')] = [];
                        $(this).find(".list-group").children().each(function() {
                            Info[$(Master).attr('campo')].push($(this).attr('valor'));
                        });
                    }
                    if($(this).attr("tipo") == 'checkbox')
                    {
                        if ($(this).is(':checked'))
                            Info[$(this).attr('campo')] = 1;
                        else
                            Info[$(this).attr('campo')] = 0;
                    }

                    if($(this).attr("tipo") == 'radio')
                    {
                        Info[$(this).attr('campo')] = $(this).find('input[type="radio"]:checked').val()
                    }

                    

                    

                });
                return Info;
            }

            function Limpiar_Formulario(Clase_Adicional)
            {
                $(".formulario-informacion"+Clase_Adicional).each(function() {
                    if( $(this).attr("tipo") == 'texto' || $(this).attr("tipo") == 'color' || $(this).attr("tipo") == 'fecha' ||  $(this).attr("tipo") == 'fecha-hora' || $(this).attr("tipo") == 'numero' || $(this).attr("tipo") == 'email' || $(this).attr("tipo") == 'fecha-rango')
                        $(this).val('');
                    if($(this).attr("tipo") == 'seleccion')
                    {
                        $(this).find('option').removeAttr('selected')
                        $(this).find("option[value='0']").attr("selected","selected");
                        $(this).val('').trigger('change');
                    }
                    if($(this).attr("tipo") == 'archivo')
                        $(this).find('.filepond--data').html("");
                    if($(this).attr("tipo") == 'lista')
                        $(this).find(".list-group").html("");
                    if($(this).attr("tipo") == 'checkbox')
                        $(this).prop( "checked", false );
                });
                Actualizar_Cambia_Texto();
            }

            function Envia_Nombre_Archivo(Nombre,ID)
            {
              if($("input[value='"+ID+"']").length == 0)
                  setTimeout(function(){Envia_Nombre_Archivo(Nombre,ID)},500);
              else
              {
                 $("input[value='"+ID+"']").attr('archivo',Nombre);
                 Cambia_Texto($("input[value='"+ID+"']").parent().parent().parent().get());
              }
            }
            function Quitar_Archivo(Control,ID)
            {
              if($("input[value='"+ID+"']").length == 0)
                Cambia_Texto(Control);
              else
                setTimeout(function(){Quitar_Archivo(Control,ID)},500);
            }
            $.fn.filepond.registerPlugin(FilePondPluginFileValidateType);
            $.fn.filepond.registerPlugin(FilePondPluginImageExifOrientation);
            $.fn.filepond.setDefaults({ maxFileSize: '10MB', credits: false });
            $.fn.filepond.registerPlugin(FilePondPluginGetFile);
            //$.fn.filepond.registerPlugin(FilePondPluginMediaPreview);
            $.fn.filepond.registerPlugin(FilePondPluginImagePreview);

            $.fn.filepond.setOptions({
                labelButtonDownloadItem: 'custom label', // by default 'Download file'
                allowDownloadByUrl: false, // by default downloading by URL disabled
                 server: {
                      process: {
                            url:   '"""+str(Url_root)+"""/ProFiles',
                            method: 'POST',
                            headers: {'x-customheader': 'Processing File'},
                            onload: (response) => { response = JSON.parse(response); Envia_Nombre_Archivo(response.file,response.key); return response.key;},
                            onerror: (response) =>{ response = JSON.parse(response); return response.msg},
                            ondata: (formData) => { window.h = formData; return formData;}
                      },
                      revert: (uniqueFileId, load, error) => {
                            var Control = $("input[value='"+uniqueFileId+"']").parent().parent().parent().get();
                            var parametros = {"Fun":"Eliminar","ID":uniqueFileId,"Archivo": $("input[value='"+uniqueFileId+"']").attr('archivo') };
                            $.ajax({data:parametros,url:'"""+str(Url_root)+"""/ProFiles',type:"post",
                                success:  function (response){ },
                                error: function (jqXHR, textStatus, errorThrown ){}
                            });
                           load();
                           Quitar_Archivo(Control,uniqueFileId);
                      }
                }
            });


        </script>
        <style>
            .swal2-html-container{
                overflow: hidden;
                z-index: 50000;
            }
             .block {
              position: relative;
            }
            .block:before, .block:after {
              content: '';
              position: absolute;
              left: -2px;
              top: -2px;
              background: linear-gradient("""+str(Colores_Aro)+""");
              background-size: 400%;
              width: calc(100% + 4px);
              height: calc(100% + 4px);
              z-index: -1;
              animation: steam 20s linear infinite;
            }

            @keyframes steam {
              0% {
                background-position: 0 0;
              }
              50% {
                background-position: 400% 0;
              }
              100% {
                background-position: 0 0;
              }
            }

            .block:after {
              filter: blur(10px);
            }

           .form-floating .select2-container--bootstrap-5 .select2-selection {
                height: calc(3.5rem + 2px);
                padding: 1rem 0.75rem;
            }

            .form-floating .select2-container--bootstrap-5 .select2-selection>.select2-selection__rendered {
                margin-top: 0.6rem;
                margin-left: 0.25rem;
            }
            .form-floating  > label{
                z-index:1;
            }

            .Firma_En
             {
                animation: Firma_En_pulse 2s infinite;
             }
             @keyframes Firma_En_pulse
             {
                50% { box-shadow:  0 0 3px #ff9100, 0 0 8px #ff9100 ,0 0 20px #ff9100; }
             }
             .select2 {
                width:100%!important;
                }
              .swal2-container {
                z-index: 50000;
                }
            body { padding-right: 0 !important }
           .tabulator-col{
                background:#ebeff1;
            }
            :root{
                --Color_Inbound: #FFB800;
                --Color_Outbound:#0029FF;
                --Color_Empty: #000000;
            }

            .Pulsa_Texto
             {
                animation: Pulsa_Texto_pulse 2s infinite;
             }
             @keyframes Pulsa_Texto_pulse
             {
                50% { text-shadow: 0 0 3px #ff9100, 0 0 8px #ff9100 ,0 0 20px #ff9100; }
             }
             .Pulsa_Div
             {
                animation: Pulsa_Div_pulse 2s infinite;
             }
             @keyframes Pulsa_Div_pulse
             {
                50% { box-shadow:  0 0 3px #ff9100, 0 0 8px #ff9100 ,0 0 20px #ff9100; }
             }

             .Pulsa_Texto_Rojo
             {
                animation: Pulsa_Texto_Rojo_pulse 2s infinite;
             }
             @keyframes Pulsa_Texto_Rojo_pulse
             {
                50% { text-shadow: 0 0 3px #ff0000, 0 0 8px #ff0000 ,0 0 20px #ff0000; color:#000000 }
             }


        </style>
        

        <div class="modal fade" id="Vent_1" data-bs-focus="false" style='background:rgba(0, 0, 0, 0.5)' data-bs-backdrop="static" data-bs-keyboard="false" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header Color_Barra Letra"><h5 class="modal-title">Modal title</h5></div>
                <div class="modal-body"></div>
                <div class="modal-footer"><button type="button" class="btn btn-danger" onclick="$('#Vent_1').modal('hide');"><i class='mdi mdi-close'></i> Close</button></div>
            </div>
            </div>
        </div>

        <div class="modal fade" id="Vent_2" data-bs-focus="false" style='background:rgba(0, 0, 0, 0.5)' data-bs-backdrop="static" data-bs-keyboard="false" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header Color_Barra Letra"><h5 class="modal-title">Modal title</h5></div>
                <div class="modal-body"></div>
                <div class="modal-footer"><button type="button" class="btn btn-danger" onclick="$('#Vent_2').modal('hide');"><i class='mdi mdi-close'></i> Close</button></div>
            </div>
            </div>
        </div>
        
        <div class="modal fade" id="Vent_3" data-bs-focus="false" style='background:rgba(0, 0, 0, 0.5)' data-bs-backdrop="static" data-bs-keyboard="false" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header Color_Barra Letra"><h5 class="modal-title">Modal title</h5></div>
                <div class="modal-body"></div>
                <div class="modal-footer"><button type="button" class="btn btn-danger" onclick="$('#Vent_3').modal('hide');"><i class='mdi mdi-close'></i> Close</button></div>
            </div>
            </div>
        </div>
        """
        return Compl;
    def Formulario(self,Datos,Script=True,Dir_Raiz=""):
        DB = DataBase()
        Cur = "<div class='row'>"
        Configurar_Calendario = ""
        index = 0
        for Campo in Datos["Campos"]:
            if "Separacion" in Campo.keys():
                Cur += "<div class='w-100'></div>"
            else:
                if "Col" in Campo.keys():
                    Cur += "<div class='col-"+str(Campo["Col"])+" m-0 p-0 ps-1'>"
                else:
                    if str(Datos["Col"]) == "":
                        Cur += "<div class='col m-0 p-0 ps-1'>"
                    else:
                        Cur += "<div class='col-"+str(Datos["Col"])+" m-0 p-0 ps-1'>"
                Editable =""
                Valor_Actual = ""
                ID_Actual = ""
                Solo_ID = ""
                Requerido = ""
                Requerido_Att = "false"
                if "valor" in Campo.keys() and Campo["valor"] is not None and str(Campo["valor"]).strip() != "":
                    Valor_Actual = Campo["valor"]
                if "id" in Campo.keys() and Campo["id"] is not None and str(Campo["id"]).strip() != "":
                    ID_Actual = "id='"+str(Campo["id"])+"'"
                    Solo_ID = str(Campo["id"])
                if ("min" in Campo.keys() and int(Campo["min"]) > 0) or  ("Requerido" in Campo.keys() and Campo["Requerido"] == True):
                    Requerido = "(<a class='text-danger'>Requerido</a>)"
                    Requerido_Att = "true"
                if "editable" in Campo.keys() and  Campo["editable"] == False:
                    Editable = "disabled"
                if Campo["tipo"] == "texto":
                    if "mdi" not in str(Campo["titulo"]):
                        Campo["titulo"] = "<i class='mdi mdi-form-textbox'></i> " + Campo["titulo"]
                    Cur += """
                    <div class='border-start ps-1 mt-1'>
                    <label class="form-label">"""+str(Campo["titulo"])+"""</label>
                    <input type='text' class='form-control """+str(Datos["Clase"])+""" formulario-informacion' tipo='texto' campo='"""+str(Campo["campo"])+"""' valido=false value='"""+str(Valor_Actual)+"""' """+str(ID_Actual)+""" """+str(Editable)+""" requerido='"""+str(Requerido_Att)+"""' Min='"""+str(Campo["min"])+"""' Max='"""+str(Campo["max"])+"""' placeholder='' onkeyup='Cambia_Texto(this)'></input>
                    """
                    if Editable != "disabled":
                        Cur += """<div class='text-muted w-100 text-end' style='font-size:12px;'><small class='form-text'><span class='badge bg-success Lleva'>0</span> """+str(Campo["min"])+"""-"""+str(Campo["max"])+""" numero de caracteres """+str(Requerido)+"""</small></div>"""
                    Cur += """</div>"""
                if Campo["tipo"] == "multitexto":
                    if "mdi" not in str(Campo["titulo"]):
                        Campo["titulo"] = "<i class='mdi mdi-form-textarea'></i> " + Campo["titulo"]
                    Cur += """
                    <div class='border-start ps-1 mt-1'>
                    <label class="form-label">"""+str(Campo["titulo"])+"""</label>
                    <textarea rows='3' class='form-control """+str(Datos["Clase"])+""" formulario-informacion' tipo='texto' campo='"""+str(Campo["campo"])+"""' valido=false """+str(ID_Actual)+""" """+str(Editable)+""" requerido='"""+str(Requerido_Att)+"""' Min='"""+str(Campo["min"])+"""' Max='"""+str(Campo["max"])+"""' placeholder='' onkeyup='Cambia_Texto(this)'>"""+str(Valor_Actual)+"""</textarea>
                    """
                    if Editable != "disabled":
                        Cur += """<div class='text-muted w-100 text-end' style='font-size:12px;'><small class='form-text'><span class='badge bg-success Lleva'>0</span> """+str(Campo["min"])+"""-"""+str(Campo["max"])+""" numero de caracteres """+str(Requerido)+"""</small></div>"""
                    Cur += """</div>"""
                if Campo["tipo"] == "color":
                    if "mdi" not in str(Campo["titulo"]):
                        Campo["titulo"] = "<i class='mdi mdi-format-color-fill'></i> " + Campo["titulo"]
                    Cur += """
                    <div class='form-floating mb-1'>
                    <input type='color' class='form-control """+str(Datos["Clase"])+""" formulario-informacion' tipo='color' campo='"""+str(Campo["campo"])+"""' valido=true value='"""+str(Valor_Actual)+"""' """+str(ID_Actual)+""" """+str(Editable)+""" requerido='"+str(Requerido_Att)+""' placeholder='' onkeyup='Cambia_Texto(this)'>
                    <label for='Color'>"""+str(Campo["titulo"])+"""</label>
                    """
                    if Editable != "disabled":
                        Cur += """<div class='text-muted w-100 text-end' style='font-size:12px;'><small class='form-text'>"""+str(Requerido)+"""</small></div>"""
                    Cur += "</div>"
                if Campo["tipo"] == "seleccion":
                    if "mdi" not in str(Campo["titulo"]):
                        Campo["titulo"] = "<i class='mdi mdi-form-select'></i> " + Campo["titulo"]
                    Cur += """
                    <div class='border-start ps-1 mt-1'>
                    <label class='form-label'>"""+str(Campo["titulo"])+"""</label>
                    <select class='form-select """+str(Datos["Clase"])+""" formulario-informacion' tipo='seleccion' campo='"""+str(Campo["campo"])+"""' """+str(ID_Actual)+""" """+str(Editable)+""" requerido='"""+str(Requerido_Att)+"""' valido=true onchange='Cambia_Texto(this)'>
                    """
                    if Valor_Actual == "":
                        Cur += """<option class='' value='-1' selected></option>"""
                    else:
                        Cur += """<option class='' value='-1'></option>"""
                    if Campo["Tipo_Opciones"] == "Query":
                        for Opciones in DB.Get_Dato(Campo["Opciones"]):
                            if str(Valor_Actual) == str(Opciones["valor"]):
                                Cur += " <option class='valio' value='"+str(Opciones["valor"])+"' selected>"+str(Opciones["texto"])+"</option>"
                            else:
                                Cur += " <option class='valio' value='"+str(Opciones["valor"])+"'>"+str(Opciones["texto"])+"</option>"
                    if Campo["Tipo_Opciones"] == "Query_70":
                        for Opciones in DB.Get_Dato_70(Campo["Opciones"]):
                            if str(Valor_Actual) == str(Opciones["valor"]):
                                Cur += " <option class='valio' value='"+str(Opciones["valor"])+"' selected>"+str(Opciones["texto"])+"</option>"
                            else:
                                Cur += " <option class='valio' value='"+str(Opciones["valor"])+"'>"+str(Opciones["texto"])+"</option>"
                    if Campo["Tipo_Opciones"] == "Opciones":
                        for Opciones in Campo["Opciones"]:
                            if str(Valor_Actual) == str(Opciones):
                                Cur += " <option class='valio' value='"+str(Opciones)+"' selected>"+str(Opciones)+"</option>"
                            else:
                                Cur += " <option class='valio' value='"+str(Opciones)+"'>"+str(Opciones)+"</option>"

                    Cur += """
                    </select>
                    """
                    if Editable != "disabled":
                        Cur += """<div class='text-muted w-100 text-end' style='font-size:12px;'><small class='form-text'>"""+str(Requerido)+"""</small></div>"""
                    Cur += "</div>"
                if Campo["tipo"] == "autos_seleccion":
                    if "mdi" not in str(Campo["titulo"]):
                        Campo["titulo"] = "<i class='mdi mdi-form-textbox'></i> " + Campo["titulo"]
                    Cur += """
                    <div class='border-start ps-1 mt-1'>
                    <label class="form-label">"""+str(Campo["titulo"])+"""</label>
                    <input type='text' class='form-control """+str(Datos["Clase"])+""" formulario-informacion' list='autos_seleccion_"""+str(index)+"""' tipo='texto' campo='"""+str(Campo["campo"])+"""' valido=false value='"""+str(Valor_Actual)+"""' """+str(ID_Actual)+""" """+str(Editable)+""" requerido='"""+str(Requerido_Att)+"""' Min='"""+str(Campo["min"])+"""' Max='"""+str(Campo["max"])+"""' placeholder='' onkeyup='Cambia_Texto(this)'></input>
                    """
                    Cur += "<datalist id='autos_seleccion_"+str(index)+"'>"
                    if Campo["Tipo_Opciones"] == "Query":
                        if Campo["Opciones"] != "":
                            for Opciones in DB.Get_Dato(Campo["Opciones"]):
                                if str(Valor_Actual) == str(Opciones["valor"]):
                                    Cur += " <option class='valio' value='"+str(Opciones["valor"])+"' selected>"+str(Opciones["texto"])+"</option>"
                                else:
                                    Cur += " <option class='valio' value='"+str(Opciones["valor"])+"'>"+str(Opciones["texto"])+"</option>"
                    if Campo["Tipo_Opciones"] == "Query_70":
                        if Campo["Opciones"] != "":
                            for Opciones in DB.Get_Dato_70(Campo["Opciones"]):
                                if str(Valor_Actual) == str(Opciones["valor"]):
                                    Cur += " <option class='valio' value='"+str(Opciones["valor"])+"' selected>"+str(Opciones["texto"])+"</option>"
                                else:
                                    Cur += " <option class='valio' value='"+str(Opciones["valor"])+"'>"+str(Opciones["texto"])+"</option>"
                    if Campo["Tipo_Opciones"] == "Opciones":
                        if Campo["Opciones"] != "":
                            for Opciones in Campo["Opciones"]:
                                if str(Valor_Actual) == str(Opciones):
                                    Cur += " <option class='valio' value='"+str(Opciones)+"' selected>"+str(Opciones)+"</option>"
                                else:
                                    Cur += " <option class='valio' value='"+str(Opciones)+"'>"+str(Opciones)+"</option>"
                    Cur += "</datalist>"
                    if Editable != "disabled":
                        Cur += """<div class='text-muted w-100 text-end' style='font-size:12px;'><small class='form-text'><span class='badge bg-success Lleva'>0</span> """+str(Campo["min"])+"""-"""+str(Campo["max"])+""" numero de caracteres """+str(Requerido)+"""</small></div>"""
                    Cur += """</div>"""

                if Campo["tipo"] == "multiseleccion":
                    if "mdi" not in str(Campo["titulo"]):
                        Campo["titulo"] = "<i class='mdi mdi-form-select'></i> " + Campo["titulo"]
                    Cur += """
                    <div class='input-group mb-1'>
                    <div class="input-group-text">"""+str(Campo["titulo"])+"""</div>
                    <select class='form-select seleccion """+str(Datos["Clase"])+""" formulario-informacion' multiple='multiple' tipo='multiseleccion' campo='"""+str(Campo["campo"])+"""' """+str(ID_Actual)+""" """+str(Editable)+""" requerido='"""+str(Requerido_Att)+"""' valido=true onchange='Cambia_Texto(this)'>
                    """
                    if Campo["Tipo_Opciones"] == "Query":
                        if Campo["Opciones"] != "":
                            for Opciones in DB.Get_Dato(Campo["Opciones"]):
                                if str(Valor_Actual) == str(Opciones["valor"]):
                                    Cur += " <option class='valio' value='"+str(Opciones["valor"])+"' selected>"+str(Opciones["texto"])+"</option>"
                                else:
                                    Cur += " <option class='valio' value='"+str(Opciones["valor"])+"'>"+str(Opciones["texto"])+"</option>"
                    if Campo["Tipo_Opciones"] == "Query_70":
                        if Campo["Opciones"] != "":
                            for Opciones in DB.Get_Dato_70(Campo["Opciones"]):
                                if str(Valor_Actual) == str(Opciones["valor"]):
                                    Cur += " <option class='valio' value='"+str(Opciones["valor"])+"' selected>"+str(Opciones["texto"])+"</option>"
                                else:
                                    Cur += " <option class='valio' value='"+str(Opciones["valor"])+"'>"+str(Opciones["texto"])+"</option>"
                    if Campo["Tipo_Opciones"] == "Opciones":
                        if Campo["Opciones"] != "":
                            for Opciones in Campo["Opciones"]:
                                if str(Valor_Actual) == str(Opciones):
                                    Cur += " <option class='valio' value='"+str(Opciones)+"' selected>"+str(Opciones)+"</option>"
                                else:
                                    Cur += " <option class='valio' value='"+str(Opciones)+"'>"+str(Opciones)+"</option>"


                    Cur += "</select>"
                    if Editable != "disabled":
                        Cur += """<div class='text-muted w-100 text-end' style='font-size:12px;'><small class='form-text'>"""+str(Requerido)+"""</small></div>"""
                    Cur += "</div>"
                if Campo["tipo"] == "fecha":
                    if "mdi" not in str(Campo["titulo"]):
                        Campo["titulo"] = "<i class='mdi mdi-calendar'></i> " + Campo["titulo"]
                    if "Configuracion" in Campo.keys():
                        Configurar_Calendario = Campo["Configuracion"]
                    Cur += """
                    <div class='border-start ps-1 mt-1'>
                    <label class="form-label">"""+str(Campo["titulo"])+"""</label>
                    <input type='text' class='form-control """+str(Datos["Clase"])+""" fecha formulario-informacion' tipo='fecha' campo='"""+str(Campo["campo"])+"""' valido=false  value='"""+str(Valor_Actual)+"""' """+str(ID_Actual)+""" """+str(Editable)+""" requerido='"""+str(Requerido_Att)+"""' placeholder='' onchange='Cambia_Texto(this)'>
                    """
                    if Editable != "disabled":
                        Cur += """<div class='text-muted w-100 text-end' style='font-size:12px;'><small class='form-text'>"""+str(Requerido)+"""</small></div>"""
                    Cur += "</div>"
                if Campo["tipo"] == "hora":
                    if "mdi" not in str(Campo["titulo"]):
                        Campo["titulo"] = "<i class='mdi mdi-clock'></i> " + Campo["titulo"]
                    Cur += """
                    <div class='form-floating mb-1'>
                    <input type='text' class='form-control """+str(Datos["Clase"])+""" hora formulario-informacion' tipo='hora' campo='"""+str(Campo["campo"])+"""' valido=false  value='"""+str(Valor_Actual)+"""' """+str(ID_Actual)+""" """+str(Editable)+""" requerido='"""+str(Requerido_Att)+"""' placeholder='' onchange='Cambia_Texto(this)'>
                    <label>"""+str(Campo["titulo"])+"""</label>
                    """
                    if Editable != "disabled":
                        Cur += """<div class='text-muted w-100 text-end' style='font-size:12px;'><small class='form-text'>"""+str(Requerido)+"""</small></div>"""
                    Cur += "</div>"
                if Campo["tipo"] == "fecha-rango":
                    if "mdi" not in str(Campo["titulo"]):
                        Campo["titulo"] = "<i class='mdi mdi-calendar-minus-outline'></i> " + Campo["titulo"]
                    Cur += """
                   <div class='border-start ps-1 mt-1'>
                    <label>"""+str(Campo["titulo"])+"""</label>
                    <input type='text' class='form-control """+str(Datos["Clase"])+""" fecha-rango formulario-informacion' tipo='fecha-rango' campo='"""+str(Campo["campo"])+"""' valido=false  value='"""+str(Valor_Actual)+"""' """+str(ID_Actual)+""" """+str(Editable)+""" requerido='"""+str(Requerido_Att)+"""' placeholder='' onchange='Cambia_Texto(this)'>
                    """
                    if Editable != "disabled":
                        Cur += """<div class='text-muted w-100 text-end' style='font-size:12px;'><small class='form-text'>"""+str(Requerido)+"""</small></div>"""
                    Cur += "</div>"
                if Campo["tipo"] == "fecha-hora":
                    if "mdi" not in str(Campo["titulo"]):
                        Campo["titulo"] = "<i class='mdi mdi-calendar-clock'></i> " + Campo["titulo"]
                    Cur += """
                    <div class='form-floating mb-1'>
                    <input type='text' class='form-control """+str(Datos["Clase"])+""" fecha-hora formulario-informacion' tipo='fecha-hora' campo='"""+str(Campo["campo"])+"""' valido=false  value='"""+str(Valor_Actual)+"""' """+str(ID_Actual)+""" """+str(Editable)+""" requerido='"""+str(Requerido_Att)+"""' placeholder='' onchange='Cambia_Texto(this)'>
                    <label>"""+str(Campo["titulo"])+"""</label>
                    """
                    if Editable != "disabled":
                        Cur += """<div class='text-muted w-100 text-end' style='font-size:12px;'><small class='form-text'>"""+str(Requerido)+"""</small></div>"""
                    Cur += "</div>"
                if Campo["tipo"] == "fecha-multi":
                    if "mdi" not in str(Campo["titulo"]):
                        Campo["titulo"] = "<i class='mdi mdi-calendar-multiselect'></i> " + Campo["titulo"]
                    Cur += """
                    <div class='form-floating mb-1'>
                    <input type='text' class='form-control """+str(Datos["Clase"])+""" fecha-multi formulario-informacion' tipo='fecha-multi' campo='"""+str(Campo["campo"])+"""' valido=false  value='"""+str(Valor_Actual)+"""' """+str(ID_Actual)+""" """+str(Editable)+""" requerido='"""+str(Requerido_Att)+"""' placeholder='' onchange='Cambia_Texto(this)'>
                    <label>"""+str(Campo["titulo"])+"""</label>
                    """
                    if Editable != "disabled":
                        Cur += """<div class='text-muted w-100 text-end' style='font-size:12px;'><small class='form-text'>"""+str(Requerido)+"""</small></div>"""
                    Cur += "</div>"
                if Campo["tipo"] == "archivo":
                    if "mdi" not in str(Campo["titulo"]):
                        Campo["titulo"] = "<i class='mdi mdi-file-cabinet'></i> " + Campo["titulo"]
                    if Valor_Actual != "" and Editable == "disabled":
                        Cur += "<div>"+str(Campo["titulo"])+"</div><div class='row ms-3 me-3 border-top border-bottom mb-1 mt-1'>"
                        if "||" in str(Valor_Actual):
                            for Archivo in Valor_Actual.split("||"):
                                Cur += "<div class='col-12'><a target='_blank' href='"+str(request.url_root)+"/Portal_File/Gen/"+str(Archivo)+"'  class='w-100 btn btn-sm btn-primary'><i class='mdi mdi-file'></i> "+str(Archivo)+"</a></div>"
                        else:
                            for Archivo in Valor_Actual.split(","):
                                Cur += "<div class='col-12'><a target='_blank' href='"+str(request.url_root)+"/Portal_File/Gen/"+str(Archivo)+"'  class='w-100 btn btn-sm btn-primary'><i class='mdi mdi-file'></i> "+str(Archivo)+"</a></div>"
                        Cur += "</div>"
                    else:
                        Multiple = ""
                        if int(Campo["max"]) > 1:
                            Multiple = "multiple='multiple'"
                        Cur += """
                        <div class='"""+str(Datos["Clase"])+""" formulario-informacion' tipo='archivo' campo='"""+str(Campo["campo"])+"""' valido=false """+str(ID_Actual)+""" Min='"""+str(Campo["min"])+"""' Max='"""+str(Campo["max"])+"""' requerido='"""+str(Requerido_Att)+"""'>
                            <div class='fw-bold text-start'>"""+str(Campo["titulo"])+"""</div>
                            <input class='Archivo-"""+str(index)+"""' type='file' id='multiFiles' name='files[]' """+str(Multiple)+""" """+str(Editable)+"""/>
                            <script>
                                $('.Archivo-"""+str(index)+"""').filepond({
                                    acceptedFileTypes: """+str(Campo["tipo_archivo"])+""",
                                    fileValidateTypeDetectType: (source, type) => new Promise((resolve, reject) => { resolve(type);}),
                                    labelIdle : "<div class='h3 link-primary' style='cursor:pointer'><i class='mdi mdi-folder'></i> Examinar</div>"
                                });
                        """
                        if Valor_Actual != "":
                            if "||" in str(Valor_Actual):
                                for Archivo in Valor_Actual.split("||"):
                                    if str(Archivo).strip() != "" and str(Archivo).strip() != "None":
                                        Cur += """
                                        $('.Archivo-"""+str(index)+"""')
                                        .filepond('addFile', '"""+str(request.url_root)+'/Portal_File/Gen/'+str(Archivo)+"""')
                                        .then(function (file) {});
                                        """
                            else:
                                for Archivo in Valor_Actual.split(","):
                                    if str(Archivo).strip() != "" and str(Archivo).strip() != "None":
                                        Cur += """
                                        $('.Archivo-"""+str(index)+"""')
                                        .filepond('addFile', '"""+str(request.url_root)+'/Portal_File/Gen/'+str(Archivo)+"""')
                                        .then(function (file) {});
                                        """

                        Cur += """
                            </script>
                            <div class='text-muted w-100 text-end' style='font-size:12px;'><small class="form-text"><span class="badge bg-success Lleva">0</span> """+str(Campo["min"])+"""-"""+str(Campo["max"])+""" numero de archivos """+str(Requerido)+"""</small></div>
                        </div>
                        """
                if Campo["tipo"] == "numero":
                    if "mdi" not in str(Campo["titulo"]):
                        Campo["titulo"] = "<i class='mdi mdi-form-textbox'></i> " + Campo["titulo"]
                    Cur += """
                    <div class='border-start ps-1 mt-1'>
                    <label class="form-label">"""+str(Campo["titulo"])+"""</label>
                    <input type='number' class='form-control """+str(Datos["Clase"])+""" formulario-informacion' tipo='numero' campo='"""+str(Campo["campo"])+"""' valido=false value='"""+str(Valor_Actual)+"""' """+str(ID_Actual)+""" """+str(Editable)+""" requerido='"""+str(Requerido_Att)+"""' Min='"""+str(Campo["min"])+"""' Max='"""+str(Campo["max"])+"""' placeholder='' onkeyup='Cambia_Texto(this)'>
                    """
                    if Editable != "disabled":
                        Cur += """<div class='text-muted w-100 text-end' style='font-size:12px;'><small class='form-text'><span class='badge bg-success Lleva'>0</span> """+str(Campo["min"])+"""-"""+str(Campo["max"])+""" numero de caracteres """+str(Requerido)+"""</small></div>"""
                    Cur += "</div>"
                if Campo["tipo"] == "email":
                    if "mdi" not in str(Campo["titulo"]):
                        Campo["titulo"] = "<i class='mdi mdi-form-textbox'></i> " + Campo["titulo"]
                    Cur += """
                    <div class='border-start ps-1 mt-1'>
                    <label class="form-label">"""+str(Campo["titulo"])+"""</label>
                    <input type='email' class='form-control """+str(Datos["Clase"])+""" formulario-informacion' tipo='numero' campo='"""+str(Campo["campo"])+"""' valido=false value='"""+str(Valor_Actual)+"""' """+str(ID_Actual)+""" """+str(Editable)+""" requerido='"""+str(Requerido_Att)+"""' Min='"""+str(Campo["min"])+"""' Max='"""+str(Campo["max"])+"""' placeholder='' onkeyup='Cambia_Texto(this)'>
                    
                    """
                    if Editable != "disabled":
                        Cur += """<div class='text-muted w-100 text-end' style='font-size:12px;'><small class='form-text'><span class='badge bg-success Lleva'>0</span> """+str(Campo["min"])+"""-"""+str(Campo["max"])+""" numero de caracteres """+str(Requerido)+"""</small></div>"""
                    Cur += "</div>"
                if Campo["tipo"] == "lista":
                    if "mdi" not in str(Campo["titulo"]):
                        Campo["titulo"] = "<i class='mdi mdi-format-list-bulleted'></i> " + Campo["titulo"]
                    Cur += """
                    <div class='"""+str(Datos["Clase"])+""" formulario-informacion mt-1 mb-1' tipo='lista' campo='"""+str(Campo["campo"])+"""' valido=false """+str(ID_Actual)+""" Min='"""+str(Campo["min"])+"""' Max='"""+str(Campo["max"])+"""' requerido='"""+str(Requerido_Att)+"""'>
                    """
                    if Editable == "disabled":
                        Cur +="""<div class='mb-1'><label>"""+str(Campo["titulo"])+"""</label></div>"""
                    else:
                        Cur +="""<div class='row mb-1'>
                            <div class='col'><label>"""+str(Campo["titulo"])+"""</label></div>
                            <div class='col-auto text-end'><button onclick='Agregar_item_"""+str(index)+"""()' class='btn btn-success btn-sm p-0 ps-1 pe-1'><i class='mdi mdi-plus'></i> Nuevo</button></div>
                        </div>"""
                    Cur += """
                        <div class='border'>
                        <ol class='list-group list-group-numbered'>
                    """
                    for Valor in Valor_Actual:
                        if str(Valor).strip() != "" and str(Valor).strip() != "None":
                            if Editable == "disabled":
                                Cur += """
                                <li class='list-group-item d-flex justify-content-between align-items-start disabled' valor='"""+str(Valor)+"""'>
                                    <div class='ms-2 me-auto'>"""+str(Valor)+"""</div>
                                </li>
                                """
                            else:
                                Cur += """
                                <li class='list-group-item d-flex justify-content-between align-items-start' valor='"""+str(Valor)+"""'>
                                    <div class='ms-2 me-auto'>"""+str(Valor)+"""</div>
                                    <span style='cursor:pointer' onclick='$(this).parent().remove(); Actualizar_Lista_"""+str(index)+"""();' class='badge bg-danger rounded-pill'><i class='mdi mdi-trash-can'></i></span>
                                </li>
                                """
                    Cur += """
                        </ol>
                        </div>
                        <div class='text-muted w-100 text-end' style='font-size:12px;'><small class='form-text'><span class='badge bg-success Lleva'>0</span> """+str(Campo["min"])+"""-"""+str(Campo["max"])+""" item(s) """+str(Requerido)+"""</small></div>
                        <script>
                            function Agregar_item_"""+str(index)+"""()
                            {
                                $.fn.modal.Constructor.prototype._initializeFocusTrap = function () { return { activate: function () { }, deactivate: function () { } } };
                                Swal.fire({
                                title: '"""+str(Campo["titulo_nuevo_item"])+"""',
                                input: '"""+str(Campo["tipo_item"])+"""',
                                showCloseButton: true,
                                showCancelButton: true,
                                focusConfirm: false,
                                confirmButtonText:'<i class="mdi mdi-plus"></i> Agregar',
                                cancelButtonText:'<i class="mdi mdi-close"></i> Cancelar'
                    """
                    Cur += """
                                ,preConfirm: (item) => {
                                    $(".formulario-informacion."""+str(Datos["Clase"])+"""[campo='"""+str(Campo["campo"])+"""']").find(".list-group").children().each(function() {
                                        if($(this).attr('valor').trim().toUpperCase() == item.trim().toUpperCase())
                                        {
                                            Swal.showValidationMessage('Este ítem ya existe');
                                            return false;
                                        }
                                    });
                                    return item.trim().toUpperCase();
                                },
                                allowOutsideClick: () => !Swal.isLoading()
                    """
                    Cur += """
                                }).then((result) => {
                                    if (result.isConfirmed)
                                    {
                                        $(".formulario-informacion."""+str(Datos["Clase"])+"""[campo='"""+str(Campo["campo"])+"""']").find(".list-group").append("<li class='list-group-item d-flex justify-content-between align-items-start' valor='"+result.value+"'><div class='ms-2 me-auto'>"+result.value+"</div><span style='cursor:pointer' onclick='$(this).parent().remove(); Actualizar_Lista_"""+str(index)+"""();' class='badge bg-danger rounded-pill'><i class='mdi mdi-trash-can'></i></span></li>")
                                        Actualizar_Lista_"""+str(index)+"""();
                                    }
                                })

                            }
                            function Actualizar_Lista_"""+str(index)+"""()
                            {
                                Cambia_Texto($(".formulario-informacion."""+str(Datos["Clase"])+"""[campo='"""+str(Campo["campo"])+"""']").get());
                            }
                        </script>
                    </div>
                    """
                if Campo["tipo"] == "checkbox":
                    if "mdi" not in str(Campo["titulo"]):
                        Campo["titulo"] = "<i class='mdi mdi-format-list-checks'></i> " + Campo["titulo"]
                    Solo_ID = "checkbox_"+str(index)
                    Check = ""
                    if Valor_Actual == True:
                        Check = "checked"
                    Cur += """
                    <div class="form-check">
                    <input """+str(Check)+""" class='form-check-input """+str(Datos["Clase"])+""" formulario-informacion' tipo='checkbox' type='checkbox' campo='"""+str(Campo["campo"])+"""' id='"""+str(Solo_ID)+"""' """+str(Editable)+""">
                    <label for='"""+str(Solo_ID)+"""' class='form-check-label'>"""+str(Campo["titulo"])+"""</label>
                    </div>
                    """
                if Campo["tipo"] == "radio":
                    if "mdi" not in str(Campo["titulo"]):
                        Campo["titulo"] = "<i class='mdi mdi-format-list-checks'></i> " + Campo["titulo"]
                    Cur += "<div class='formulario-informacion "+str(Datos["Clase"])+" mb-3' campo='"+str(Campo["campo"])+"' tipo='radio' "+str(ID_Actual)+" valido=false onchange='Cambia_Texto(this)'>"
                    Cur += "<div><label>"+str(Campo["titulo"])+"</label></div>"
                    index_0 = 0
                    if Campo["Tipo_Opciones"] == "Query":
                        for Opciones in DB.Get_Dato(Campo["Opciones"]):
                            Solo_ID = "radio_"+str(index)+"_"+str(index_0)
                            Check = ""
                            if str(Valor_Actual) == str(Opciones["Valor"]):
                                Check = "checked"
                            Cur += """
                            <div class='form-check form-check-inline'>
                                <input """+str(Check)+""" class='form-check-input' tipo='radio' type='radio' value='"""+str(Opciones["Valor"])+"""' name='"""+str(Campo["campo"])+"""' id='"""+str(Solo_ID)+"""'>
                                <label class='form-check-label' for='"""+str(Solo_ID)+"""'>"""+str(Opciones["Texto"])+"""</label>
                            </div>
                            """
                            index_0 += 1
                    if Campo["Tipo_Opciones"] == "Query_70":
                        for Opciones in DB.Get_Dato_70(Campo["Opciones"]):
                            Solo_ID = "radio_"+str(index)+"_"+str(index_0)
                            Check = ""
                            if str(Valor_Actual) == str(Opciones["Valor"]):
                                Check = "checked"
                            Cur += """
                            <div class='form-check form-check-inline'>
                                <input """+str(Check)+""" class='form-check-input' tipo='radio' type='radio' value='"""+str(Opciones["Valor"])+"""' name='"""+str(Campo["campo"])+"""' id='"""+str(Solo_ID)+"""'>
                                <label class='form-check-label' for='"""+str(Solo_ID)+"""'>"""+str(Opciones["Texto"])+"""</label>
                            </div>
                            """
                            index_0 += 1
                    if Campo["Tipo_Opciones"] == "Opciones":
                        for Opciones in Campo["Opciones"]:
                            Solo_ID = "radio_"+str(index)+"_"+str(index_0)
                            Check = ""
                            if str(Valor_Actual) == str(Opciones):
                                Check = "checked"
                            Cur += """
                            <div class='form-check form-check-inline'>
                                <input """+str(Check)+""" class='form-check-input' tipo='radio' type='radio' value='"""+str(Opciones)+"""' name='"""+str(Campo["campo"])+"""' id='"""+str(Solo_ID)+"""'>
                                <label class='form-check-label' for='"""+str(Solo_ID)+"""'>"""+str(Opciones)+"""</label>
                            </div>
                            """
                            index_0 += 1
                    Cur += "</div>"
                Cur += "</div>"
            index += 1
        Cur += """
        </div>
        """
        if Script == True:
            Cur += """
            <script>
                flatpickr.localize(flatpickr.l10ns.es);
                $('.fecha').flatpickr("""+str(Configurar_Calendario)+""");
                $('.hora').flatpickr({enableTime: true,noCalendar: true,dateFormat: 'H:i',time_24hr: true,defaultHour:0,defaultMinute:0});
                $('.fecha-rango').flatpickr({ mode: 'range'});
                $('.fecha-multi').flatpickr({ mode: 'multiple'});
                $('.fecha-hora').flatpickr({ enableTime: true});
                Actualizar_Cambia_Texto()
                $( document ).ready(function() {
                    $.fn.modal.Constructor.prototype._enforceFocus = function () {}
                    $(".flatpickr-calendar").each(function() {
                        if($(this).hasClass("Principal"))
                            $(this).css('z-index',1);
                        else
                            $(this).css('z-index',2000);
                    });
                    
                });
                /*$('.seleccion').select2( {
                    theme: 'bootstrap-5'
                } );*/

            </script>
            """
        return Cur
    def Estado_Firmas(self,Folio):
        Resultado = {}
        DB = DataBase()
        Pasa_Por_Fimas = False
        Firmas_YA =[]
        Pasos_Adicionas = []
        Estado = {"Estado":None,"Color":None,"Icono":None,"Alerta":None}
        Fimas = []
        Str_Firmas = None
        Formato_Dia = False
        Estado_Gen = 0
        if "AT" in str(Folio):
            Info = DB.Get_Dato("SELECT * FROM portal.creque_empleado WHERE cre_id = '"+str(Folio)[2:]+"' ")[0]
            Str_Firmas = Info["cre_firmas"].replace(" ","")
            Estado_Gen = Info["cre_estado"]
        if "ST" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT cst_firmas FROM portal.cst WHERE cst_id = '"+str(Folio)[2:]+"' ")[0]["cst_firmas"].replace(" ","")
        if "TE" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT cte_firmas FROM portal.cte WHERE cte_id = '"+str(Folio)[2:]+"' ")[0]["cte_firmas"].replace(" ","")
        if "VA" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT cva_firmas FROM portal.cva WHERE cva_id = '"+str(Folio)[2:]+"' ")[0]["cva_firmas"].replace(" ","")
        if "AR" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT car_firmas FROM portal.car WHERE car_id = '"+str(Folio)[2:]+"' ")[0]["car_firmas"].replace(" ","")
        if "RE" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT cre_firmas FROM portal.cda WHERE cre_id = '"+str(Folio)[2:]+"' ")[0]["cre_firmas"].replace(" ","")
        if "PT" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT cpt_firmas FROM portal.cpt WHERE cpt_id = '"+str(Folio)[2:]+"' ")[0]["cpt_firmas"].replace(" ","")
        if "DL" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT cdl_firmas FROM portal.cdl WHERE cdl_id = '"+str(Folio)[2:]+"' ")[0]["cdl_firmas"].replace(" ","")
        if "SD" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT csd_firmas FROM portal.csd WHERE csd_id = '"+str(Folio)[2:]+"' ")[0]["csd_firmas"].replace(" ","")
        if "IN" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT cin_firmas FROM portal.cin WHERE cin_id = '"+str(Folio)[2:]+"' ")[0]["cin_firmas"].replace(" ","")
        if "PE" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT cpe_firmas FROM portal.cpe WHERE cpe_id = '"+str(Folio)[2:]+"' ")[0]["cpe_firmas"].replace(" ","")
        if "CP" in str(Folio):
            Info = DB.Get_Dato("SELECT * FROM portal.ccp WHERE ccp_id = '"+str(Folio)[2:]+"' ")[0]
            Str_Firmas = Info["ccp_firmas"].replace(" ","")
            Estado_Gen = Info["ccp_estado"]
        if "CA" in str(Folio):
            Info = DB.Get_Dato("SELECT * FROM portal.cca WHERE cca_id = '"+str(Folio)[2:]+"' ")[0]
            Str_Firmas = Info["cca_firmas"].replace(" ","")
            Estado_Gen = Info["cca_estado"]
        if "CC" in str(Folio):
            Info = DB.Get_Dato("SELECT * FROM portal.ccc WHERE ccc_id = '"+str(Folio)[2:]+"' ")[0]
            Str_Firmas = Info["ccc_firmas"].replace(" ","")
            Estado_Gen = Info["ccc_estado"]
        if "DF" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT cdf_firmas FROM portal.cdf WHERE cdf_id = '"+str(Folio)[2:]+"' ")[0]["cdf_firmas"].replace(" ","")
        if "RD" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT crd_firmas FROM portal.crd WHERE crd_id = '"+str(Folio)[2:]+"' ")[0]["crd_firmas"].replace(" ","")
        if "WC" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT cwc_firmas FROM portal.cwc WHERE cwc_id = '"+str(Folio)[2:]+"' ")[0]["cwc_firmas"].replace(" ","")
        if "WD" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT cwd_firmas FROM portal.cwd WHERE cwd_id = '"+str(Folio)[2:]+"' ")[0]["cwd_firmas"].replace(" ","")
        
        
        if Formato_Dia == True:
            Firmas_YA = DB.Get_Dato("select * from portal.cfirmas FIR where FIR.Folio = '"+str(Folio)[2:]+"'")
            Estado_Gen = DB.Get_Dato("select cfd_estado from portal.cformato_dia where cfd_id = '"+str(Folio)[2:]+"'")[0]["cfd_estado"]
            ToDo = DB.Get_Dato("select * from portal.ctodo ToDo where ToDo.ctd_formato_dia = '"+str(Folio)[2:]+"'")
        else:
            Firmas_YA = DB.Get_Dato("select * from portal.cfirmas FIR where FIR.cffolio = '"+str(Folio)+"'")
            ToDo = DB.Get_Dato("select * from portal.ctodo ToDo where ToDo.ctd_folio = '"+str(Folio)+"'")

        En_AV = DB.Get_Dato("SELECT * FROM portal.cestado_av WHERE cesav_folio = '"+str(Folio)+"'")
        if Str_Firmas is not None and str(Str_Firmas).strip() != "":
            for F in str(Str_Firmas).split("|"):
                Nombre = DB.Get_Dato("SELECT EMP.IDEmpleado,EMP.Nombre FROM portal.cuser USR inner join linc.empleados EMP on EMP.IDEmpleado = USR.cusidempleado WHERE cusrid = '"+str(F)+"' ")
                if len(Nombre) > 0:
                    Nombre = Nombre[0]
                    Ya = None
                    for F_YA in Firmas_YA:
                        if str(F_YA["cFirEmpleado"]) == str(F):
                            Ya = F_YA
                            break
                    if Ya is None:
                        if len(ToDo) > 0 and str(ToDo[0]["ctd_idusuario"]) == str(F):
                            Aux_Fimas = {"Usuario":str(F),"Nombre":Nombre["Nombre"],"IDEmpleado":Nombre["Nombre"],"Aqui":"Todo"}
                        else:
                            Aux_Fimas = {"Usuario":str(F),"Nombre":Nombre["Nombre"],"IDEmpleado":Nombre["Nombre"]}
                    else:
                        if len(ToDo) > 0 and str(ToDo[0]["ctd_idusuario"]) == str(F):
                            Aux_Fimas = {"Usuario":str(F),"Nombre":Nombre["Nombre"],"IDEmpleado":Nombre["Nombre"],"Fecha":Ya["cfir_fecha_hora"],"Tipo":Ya["Tipo"],"Comentario":Ya["Comentario"],"Aqui":"Todo"}
                        else:
                            Aux_Fimas = {"Usuario":str(F),"Nombre":Nombre["Nombre"],"IDEmpleado":Nombre["Nombre"],"Fecha":Ya["cfir_fecha_hora"],"Tipo":Ya["Tipo"],"Comentario":Ya["Comentario"]}
                    Fimas.append(Aux_Fimas)
            Tipo_AV = [
                {"Departamento":"ADT Departament","Texto":"In recruitment process","Tipo_AV":"ADT"},
                {"Departamento":"Nominas Departament","Texto":"In process of application","Tipo_AV":"NOMINA"},
                {"Departamento":"RH Departament","Texto":"In process of application","Tipo_AV":"RH"}
            ]
            for AV in Tipo_AV:
                if AV["Tipo_AV"] in Str_Firmas:
                    Ya = None
                    for F_YA in Firmas_YA:
                        if str(F_YA["cFir_Tipo_AV"]) == AV["Tipo_AV"]:
                            Ya = F_YA
                            break
                    if Ya is None:
                        Pasos_Adicionas.append(AV)
                    else:
                        Nombre = DB.Get_Dato("SELECT EMP.IDEmpleado,EMP.Nombre FROM portal.cuser USR inner join linc.empleados EMP on EMP.IDEmpleado = USR.cusidempleado WHERE cusrid = '"+str(Ya["cFirEmpleado"])+"' ")[0]
                        AV["Usuario"] = Ya["cFirEmpleado"]
                        AV["Nombre"] = Nombre["Nombre"]
                        AV["IDEmpleado"] = Nombre["IDEmpleado"]
                        AV["Fecha"] = Ya["cfir_fecha_hora"]
                        AV["Tipo"] = Ya["Tipo"]
                        AV["Comentario"] = Ya["Comentario"]
                        Pasos_Adicionas.append(AV)

        if Estado_Gen == 1:
            Estado["Estado"] = "In the signing process "
            Estado["Color"] = "bg-warning text-dark"
            Estado["Icono"] = "mdi mdi-alert"
        elif Estado_Gen == 2:
            if len(Pasos_Adicionas) > 0:
                Aqui = None
                for PA in Pasos_Adicionas:
                    if "Usuario" not in PA.keys():
                        Aqui = PA
                        break
                if Aqui is not None:
                    Estado["Estado"] = "Approved ["+str(Aqui["Texto"])+"]"
                    Estado["Color"] = "bg-success-subtle text-dark"
                    Estado["Icono"] = "mdi mdi-check"
                else:
                    Estado["Estado"] = "Approved"
                    Estado["Color"] = "bg-success-subtle text-dark"
                    Estado["Icono"] = "mdi mdi-check"
            else:
                Estado["Estado"] = "Approved"
                Estado["Color"] = "bg-success-subtle text-dark"
                Estado["Icono"] = "mdi mdi-check"
        elif Estado_Gen == 3:
            Estado["Estado"] = "Rejected"
            Estado["Color"] = "bg-danger text-white"
            Estado["Icono"] = "mdi mdi-close"
            Quien = ""
            Comentario = ""
            for F_YA in Firmas_YA:
                if int(F_YA["Tipo"]) == 2:
                    Quien = DB.Get_Dato("SELECT IFNULL(EMP.Nombre,USR.cusnombre) as Nombre FROM portal.cuser USR left join linc.empleados EMP on EMP.IDEmpleado = USR.cusidempleado WHERE cusrid = '"+str(F_YA["cFirEmpleado"])+"' ")[0]["Nombre"]
                    Comentario = F_YA["Comentario"]
            Estado["Quien"] = Quien
            Estado["Comentario"] = Comentario
        elif Estado_Gen >= 4:
            Estado["Estado"] = "Complete"
            Estado["Color"] = "bg-success text-white"
            Estado["Icono"] = "mdi mdi-check-all"

        Estado_Todo = []
        for F in Fimas:
            if "Aqui" in F.keys():
                Estado_Todo.append(F)
        
        if len(Estado_Todo) == 0 and Estado_Gen == 1:
            Estado["Alerta"] = "Error en el flujo de firmas, favor de contactar al departamento de IT [Error: F-001]"
        elif len(Estado_Todo) > 1:
            Estado["Alerta"] = "Error en el flujo de firmas, favor de contactar al departamento de IT [Error: F-002]"
        elif len(Estado_Todo) > 0 and "Aqui" in Estado_Todo[0].keys() and "Fecha" in Estado_Todo[0].keys():
            Estado["Alerta"] = "Error en el flujo de firmas, favor de contactar al departamento de IT [Error: F-002]"

        Resultado["Json_Estado"] = Estado

        if Estado["Alerta"] is None:
            Resultado["Estado"] = """
            <div class='"""+str(Estado["Color"])+""" p-3 fs-6 text-center'>
            <i class='fw-bold """+str(Estado["Icono"])+"""'></i> """+str(Estado["Estado"])
            if Estado_Gen == 3:
                Resultado["Estado"] += "<div class='fw-semibold'><small>"+str(Estado["Quien"])+"</small></div>"
                Resultado["Estado"] += "<div class='fw-lighter'><small>"+str(Estado["Comentario"])+"</small></div>"
            Resultado["Estado"] += """
            </div>
            """
        else:
            Resultado["Estado"] = """
            <div class='bg-danger text-white p-3 fs-6 text-center fw-bold'>
            <i class='mdi mdi-alert-rhombus'></i> """+str(Estado["Alerta"])+"""
            </div>
            """
        Firmas_Totales = []
        for F in Fimas:
            Firmas_Totales.append(F)
        for F in Pasos_Adicionas:
            Firmas_Totales.append(F)
        Resultado["Json_Firmas"] = Firmas_Totales
        Resultado["Firmas"] = ""
        if len(Firmas_Totales) > 0:
            Resultado["Firmas"] += "<div class='mt-1 mb-1 border-bottom'><i class='mdi mdi-signature-freehand'></i> Signatures</div>"
            Resultado["Firmas"] += "<div class='progress progress-stacked' style='height: auto'>"
            for F in Fimas:
                Clase_Campo = "bg-secondary text-dark"
                if "Aqui" in F.keys():
                    Clase_Campo = "progress-bar-striped progress-bar-animated bg-warning text-dark"
                if "Fecha" in F.keys():
                    if int(F["Tipo"]) != 2:
                        Clase_Campo = "bg-success text-white"
                    else:
                        Clase_Campo = "bg-danger text-white"
                Resultado["Firmas"] += """
                <div class="progress h-auto" style="width: """+str(100/len(Firmas_Totales))+"""%;">
                    <div class="progress-bar text-wrap h-100 w-100 fs-6 border """+str(Clase_Campo)+""" ">"""+str(F["Nombre"])+"""</div>
                </div>
                """
            for P in Pasos_Adicionas:
                Usuario = ""
                Clase_Campo = "bg-secondary text-dark"
                Aqui = None
                for A in En_AV:
                    if A["cesav_av"] == P["Tipo_AV"]:
                        Aqui = A
                        break
                if Aqui is not None:
                    Clase_Campo = "progress-bar-striped progress-bar-animated bg-warning text-dark"
                else:
                    if "Fecha" in P.keys():
                        Usuario = "<br><small>"+str(P["Nombre"])+"</small>"
                        if int(P["Tipo"]) != 2:
                            Clase_Campo = "bg-success text-white"
                        else:
                            Clase_Campo = "bg-danger text-white"
                Resultado["Firmas"] += """
                <div class="progress h-auto" style="width: """+str(100/len(Firmas_Totales))+"""%;">
                    <div class="progress-bar text-wrap h-100 w-100 fs-6 border """+str(Clase_Campo)+""" ">"""+str(P["Departamento"])+str(Usuario)+"""</div>
                </div>
                """
            Resultado["Firmas"] += "</div>"
            
            #Comentarios
            Resultado["Firmas"] += "<div class='progress progress-stacked' style='height: auto'>"
            Comentario = ""
            for F in Fimas:
                Clase_Campo = "bg-white text-dark"
                if "Comentario" in F.keys() and F["Comentario"] is not None and str(F["Comentario"]).strip() != "" and int(F["Tipo"]) != 2 :
                    Clase_Campo = "bg-success-subtle text-dark"
                    Comentario = str(F["Comentario"])
                if "Comentario" in F.keys() and F["Comentario"] is not None and str(F["Comentario"]).strip() != "" and int(F["Tipo"]) == 2 :
                    Clase_Campo = "bg-danger-subtle text-dark"
                    Comentario = str(F["Comentario"])
                Resultado["Firmas"] += """
                <div class="progress h-auto" style="width: """+str(100/len(Firmas_Totales))+"""%;">
                    <div class="progress-bar text-wrap h-100 w-100 border """+str(Clase_Campo)+""" "><small>"""+str(Comentario)+"""</small></div>
                </div>
                """
            for P in Pasos_Adicionas:
                Clase_Campo = "bg-white text-dark"
                if "Comentario" in P.keys() and P["Comentario"] is not None and str(P["Comentario"]).strip() != "" and int(P["Tipo"]) != 2 :
                    Clase_Campo = "bg-success-subtle text-dark"
                    Comentario = str(P["Comentario"])
                if "Comentario" in P.keys() and P["Comentario"] is not None and str(P["Comentario"]).strip() != "" and int(P["Tipo"]) == 2 :
                    Clase_Campo = "bg-danger-subtle text-dark"
                    Comentario = str(P["Comentario"])
                Resultado["Firmas"] += """
                <div class="progress h-auto" style="width: """+str(100/len(Firmas_Totales))+"""%;">
                    <div class="progress-bar text-wrap h-100 w-100 border """+str(Clase_Campo)+""" "><small>"""+str(Comentario)+"""</small></div>
                </div>
                """
            Resultado["Firmas"] += "</div>"
        return Resultado
    def Estado_Actual(self,Folio):
        Resultado = {"html":"","Lo_Tiene":"","Estado":""}
        Cur = ""
        DB = DataBase()
        Pasa_Por_Fimas = False
        Firmas_YA = []
        if str(Folio)[:2] in ["AT","CC","CA","CP"]:
            for F in DB.Get_Dato("select cFirEmpleado,cFir_Tipo_AV from portal.cfirmas FIR where FIR.cffolio = '"+str(Folio)+"' ORDER BY cfir_fecha_hora"):
                if F["cFir_Tipo_AV"] is None:
                    Firmas_YA.append(str(F["cFirEmpleado"]))
                else:
                    Firmas_YA.append(str(F["cFir_Tipo_AV"]))
        if str(Folio)[:2] in ["TE","ST","AR","RE","VA","PT","DL","SD","IN","PE"]:
            for F in DB.Get_Dato("select cFirEmpleado,cFir_Tipo_AV from portal.cfirmas FIR where FIR.Folio = '"+str(Folio)[2:]+"' ORDER BY cfir_fecha_hora"):
                if F["cFir_Tipo_AV"] is None:
                    Firmas_YA.append(str(F["cFirEmpleado"]))
                else:
                    Firmas_YA.append(str(F["cFir_Tipo_AV"]))
        Pasos_Adicionas = []
        Estado = {"Estado":"COMPLETE","Color":"success","Color_2":"success","Icono":"mdi-check-decagram"}
        Fimas = []
        if "AT" in str(Folio):
            for F in str(DB.Get_Dato("SELECT * FROM portal.creque_empleado WHERE cre_id = '"+str(Folio)[2:]+"' ")[0]["cre_firmas"]).split(","):
                Fimas.append(str(F))
            ADT = {"Nombre":"ADT Departament","Estado":0,"Estado_Text":"In recruitment process","Color":"secondary","Icono":"mdi-arrow-down-bold","Fecha":"","Comentario":"","Proceso_Aqui":"","Tipo_AV":"ADP"}
            Pasos_Adicionas.append(ADT)
        if "TE" in str(Folio):
            for F in str(DB.Get_Dato("SELECT * FROM portal.cte WHERE cte_id = '"+str(Folio)[2:]+"'")[0]["cte_firmas"]).split("|"):
                Fimas.append(str(F))
        if "ST" in str(Folio):
            for F in str(DB.Get_Dato("SELECT * FROM portal.cst WHERE cst_id = '"+str(Folio)[2:]+"'")[0]["cst_firmas"]).split("|"):
                Fimas.append(str(F))
        if "AR" in str(Folio):
            for F in str(DB.Get_Dato("SELECT * FROM portal.car WHERE car_id = '"+str(Folio)[2:]+"'")[0]["car_firmas"]).split("|"):
                Fimas.append(str(F))
        if "RE" in str(Folio):
            for F in str(DB.Get_Dato("SELECT * FROM portal.cda WHERE cre_id = '"+str(Folio)[2:]+"'")[0]["cre_firmas"]).split("|"):
                Fimas.append(str(F))
        if "VA" in str(Folio):
            for F in str(DB.Get_Dato("SELECT * FROM portal.cva WHERE cva_id = '"+str(Folio)[2:]+"'")[0]["cva_firmas"]).split("|"):
                Fimas.append(str(F))
        if "PT" in str(Folio):
            for F in str(DB.Get_Dato("SELECT * FROM portal.cpt WHERE cpt_id = '"+str(Folio)[2:]+"'")[0]["cpt_firmas"]).split("|"):
                Fimas.append(str(F))
        if "DL" in str(Folio):
            for F in str(DB.Get_Dato("SELECT * FROM portal.cdl WHERE cdl_id = '"+str(Folio)[2:]+"'")[0]["cdl_firmas"]).split("|"):
                Fimas.append(str(F))
        if "SD" in str(Folio):
            for F in str(DB.Get_Dato("SELECT * FROM portal.csd WHERE csd_id = '"+str(Folio)[2:]+"'")[0]["csd_firmas"]).split("|"):
                Fimas.append(str(F))
        if "IN" in str(Folio):
            for F in str(DB.Get_Dato("SELECT * FROM portal.cin WHERE cin_id = '"+str(Folio)[2:]+"'")[0]["cin_firmas"]).split("|"):
                Fimas.append(str(F))
        if "PE" in str(Folio):
            for F in str(DB.Get_Dato("SELECT * FROM portal.cpe WHERE cpe_id = '"+str(Folio)[2:]+"'")[0]["cpe_firmas"]).split("|"):
                Fimas.append(str(F))
        if "CC" in str(Folio):
            for F in str(DB.Get_Dato("SELECT * FROM portal.ccc WHERE ccc_id = '"+str(Folio)[2:]+"'")[0]["ccc_firmas"]).split("|"):
                Fimas.append(str(F))
        if "CA" in str(Folio):
            for F in str(DB.Get_Dato("SELECT * FROM portal.cca WHERE cca_id = '"+str(Folio)[2:]+"'")[0]["cca_firmas"]).split("|"):
                Fimas.append(str(F))
        if "CP" in str(Folio):
            for F in str(DB.Get_Dato("SELECT * FROM portal.ccp WHERE ccp_id = '"+str(Folio)[2:]+"'")[0]["ccp_firmas"]).split("|"):
                Fimas.append(str(F))
        
        
        if "NOMINA" in Fimas:
            NOMINAS = {"Nombre":"Nominas Departament","Estado":0,"Estado_Text":"In process of application","Color":"secondary","Icono":"mdi-arrow-down-bold","Fecha":"","Comentario":"","Proceso_Aqui":"","Tipo_AV":"NOMINA"}
            Pasos_Adicionas.append(NOMINAS)
        if "RH" in Fimas:
            RH = {"Nombre":"RH Departament","Estado":0,"Estado_Text":"In process of application","Color":"secondary","Icono":"mdi-arrow-down-bold","Fecha":"","Comentario":"","Proceso_Aqui":"","Tipo_AV":"RH"}
            Pasos_Adicionas.append(RH)
        if "PDF" in Fimas:
            RH = {"Nombre":"RH Departament (PDF)","Estado":0,"Estado_Text":"In process of application","Color":"secondary","Icono":"mdi-arrow-down-bold","Fecha":"","Comentario":"","Proceso_Aqui":"","Tipo_AV":"PDF"}
            Pasos_Adicionas.append(RH)
        Falta = list(set(Fimas) - set(Firmas_YA))
        Folta_Aux = []
        for F in Fimas:
            if F in Falta:
                Folta_Aux.append(F)
        Falta = Folta_Aux
        if len(Falta) > 0:
            Es_Paso_Adicional = False
            for Paso in Pasos_Adicionas:
                if str(Paso["Tipo_AV"]) == str(Falta[0]):
                    Cur += "<small class='badge rounded-pill text-bg-warning text-wrap'>"+str(Paso["Nombre"])+" AQUI</small>"
                    Resultado["html"] = "<small class='badge rounded-pill text-bg-warning text-wrap'>"+str(Paso["Nombre"])+"</small>"
                    Resultado["Lo_Tiene"] = str(Paso["Nombre"])
                    Resultado["Estado"] = "APPROVED"
                    Resultado["Tipo_AV"] = str(Paso["Tipo_AV"])
                    Es_Paso_Adicional = True
                    break
            if Es_Paso_Adicional == False:
                if len(DB.Get_Dato("SELECT * FROM portal.ctodo WHERE ctd_idusuario = '"+str(Falta[0])+"' AND (ctd_formato_dia = '"+str(Folio[2:])+"' OR ctd_folio = '"+str(Folio)+"') ")) > 0:
                    Resultado["html"] = "<small class='badge rounded-pill text-bg-warning text-wrap'>"+str(self.Dame_Nombre(Falta[0]))+"</small>"
                    Resultado["Lo_Tiene"] = str(self.Dame_Nombre(Falta[0]))
                    Cur += "<small class='badge rounded-pill text-bg-warning text-wrap'>"+str(self.Dame_Nombre(Falta[0]))+"</small>"
                    Resultado["Estado"] = "IN PROCESS"
                # else:
                #     Cur += "<small class='badge rounded-pill bg-danger text-wrap'><i class='mdi mdi-alert'></i> Contact the department of IT Mexico</small>"
        return Resultado
    def Firmas(self,Empleado,Folio,Planta,Masivo=0):
        DB = DataBase()
        Firmas = []
        Configuracion_Firmas = DB.Get_Dato("SELECT * FROM portal.cconf_firmas WHERE ccf_folio_formato = '"+str(Folio)+"' AND ccf_planta = '"+str(Planta)+"'")
        if len(Configuracion_Firmas) > 0:
            Aplica = Configuracion_Firmas[0]["ccf_aplica"]
            if Masivo == 0:
                Configuracion_Firmas = Configuracion_Firmas[0]["ccf_firmas"]
                if Configuracion_Firmas is not None and str(Configuracion_Firmas) != "":
                    for FC in str(Configuracion_Firmas).split("|"):
                        if FC == "*":
                            Supervisor = str(self.Escalera_Reposables(Empleado,'Supervisor',-1))
                            if str(Supervisor) not in Firmas:
                                Firmas.append(str(Supervisor))
                        elif FC == "#":
                            Coordinador = str(self.Escalera_Reposables(Empleado,'Coordinador',-1))
                            if str(Coordinador) not in Firmas:
                                Firmas.append(str(Coordinador))
                        elif FC == "+":
                            Gerente = str(self.Escalera_Reposables(Empleado,'Gerente',-1))
                            if str(Gerente) not in Firmas:
                                Firmas.append(str(Gerente))
                        elif FC == "$":
                            Gerente_Planta = DB.Get_Dato("SELECT PLANTA.IDGteGral,USR.cusrid  FROM linc.plantas PLANTA inner join portal.cuser USR on USR.cusidempleado = PLANTA.IDGteGral WHERE PLANTA.IDplanta = '"+str(Planta)+"'")
                            if len(Gerente_Planta) > 0:
                                Gerente_Planta = Gerente_Planta[0]["cusrid"]
                                if str(Gerente_Planta) not in Firmas:
                                    Firmas.append(str(Gerente_Planta))
                            else:
                                Firmas.append("-1")
                        else:
                            if str(FC) not in Firmas:
                                Firmas.append(str(FC))
            Staff = DB.Get_Dato("SELECT * FROM portal.cstaff WHERE csf_idempleado = '"+str(Empleado)+"'")
            if "DL" in Folio and len(Staff) > 0:
                if "30" not in Firmas:
                    Firmas.append("30")
            if Aplica is not None and str(Aplica) != "":
                if str(Aplica) not in Firmas:
                    Firmas.append(str(Aplica))
        return Firmas
    def Escalera_Reposables(self,Empleado,Puesto,Antes):
        DB = DataBase()
        Buscar = []
        if Puesto == "Supervisor":
            Buscar.append("Supervisor")
            Buscar.append("Coordinador")
            Buscar.append("Gerente")
        elif Puesto == "Coordinador":
            Buscar.append("Coordinador")
            Buscar.append("Gerente")
        else:
            Buscar.append(Puesto)
        Arriba = DB.Get_Dato("""
        select EMP_2.IDEmpleado,Puesto.Puesto2,USR.cusrid  from linc.empleados EMP 
        inner join linc.areasempleados AREA on AREA.IDAreaEmpl = EMP.IDAreaEmpl 
        inner join linc.empleados EMP_2 on EMP_2.Nombre = AREA.Responsable 
        inner join linc.puestos Puesto on Puesto.IDPuesto = EMP_2.IDPuesto 
        inner join portal.cuser USR on USR.cusidempleado = EMP_2.IDEmpleado 
        where EMP.IDEmpleado = '"""+str(Empleado)+"""'
        """)
        if len(Arriba) == 0:
            return -1
        else:
            if Empleado != Antes:
                if str(Arriba[0]["Puesto2"]) in Buscar:
                    return int(Arriba[0]["cusrid"])
                else:
                    return self.Escalera_Reposables(int(Arriba[0]["IDEmpleado"]),Puesto,Empleado)
            else:
                return -1
    def Dame_Nombre(self,ID,Tipo="PORTAL"):
        DB = DataBase()
        ID_Empelado = -1
        if Tipo == "PORTAL":
            ID_Empelado = DB.Get_Dato("SELECT cusidempleado FROM portal.cuser WHERE cusrid = '"+str(ID)+"'")
            if len(ID_Empelado) > 0:
                ID_Empelado = ID_Empelado[0]["cusidempleado"]
        else:
            ID_Empelado = ID
        if ID_Empelado is None:
            return DB.Get_Dato("SELECT cusnombre FROM portal.cuser WHERE cusrid = '"+str(ID)+"'")[0]["cusnombre"]
        else:
            Nombre = DB.Get_Dato("SELECT Nombre FROM linc.empleados WHERE IDEmpleado = '"+str(ID_Empelado)+"'")
            if len(Nombre) > 0:
                return Nombre[0]["Nombre"]
            else:
                return "N/A"
    def Cancelar_Formato(self,Folio,Empleado,ID_User,Comentario):
        Resultado = {"Contenido":"","Estado":0}
        DB = DataBase()
        if "CC" in Folio:
            Resultado["Contenido"] += DB.Instruccion("UPDATE portal.ccc SET ccc_estado = '3' WHERE ccc_id ='"+str(Folio)[2:]+"'")
            if Resultado["Contenido"] == "":
                Resultado["Contenido"] = DB.Instruccion("""
                INSERT INTO portal.cfirmas 
                (cFirEmpleado,Tipo,Comentario,cffolio,Fecha,Hora,cfir_fecha_hora)
                VALUES
                ('"""+str(ID_User)+"""',2,'"""+str(Comentario)+"""','"""+str(Folio)+"""',DATE(NOW()),TIME(NOW()),NOW())
                """)
        elif "CP" in Folio:
            Resultado["Contenido"] += DB.Instruccion("UPDATE portal.ccp SET ccp_estado = '3' WHERE ccp_id ='"+str(Folio)[2:]+"'")
            if Resultado["Contenido"] == "":
                Resultado["Contenido"] = DB.Instruccion("""
                INSERT INTO portal.cfirmas 
                (cFirEmpleado,Tipo,Comentario,cffolio,Fecha,Hora,cfir_fecha_hora)
                VALUES
                ('"""+str(ID_User)+"""',2,'"""+str(Comentario)+"""','"""+str(Folio)+"""',DATE(NOW()),TIME(NOW()),NOW())
                """)
        elif "CA" in Folio:
            Resultado["Contenido"] += DB.Instruccion("UPDATE portal.cca SET cca_estado = '3' WHERE cca_id ='"+str(Folio)[2:]+"'")
            if Resultado["Contenido"] == "":
                Resultado["Contenido"] = DB.Instruccion("""
                INSERT INTO portal.cfirmas 
                (cFirEmpleado,Tipo,Comentario,cffolio,Fecha,Hora,cfir_fecha_hora)
                VALUES
                ('"""+str(ID_User)+"""',2,'"""+str(Comentario)+"""','"""+str(Folio)+"""',DATE(NOW()),TIME(NOW()),NOW())
                """)
        else:
            Resultado["Contenido"] += DB.Instruccion("UPDATE portal.cformato_dia SET cfd_estado = '3' WHERE cfd_id ='"+str(Folio)[2:]+"'")
            if Resultado["Contenido"] == "":
                Resultado["Contenido"] = DB.Instruccion("""
                INSERT INTO portal.cfirmas 
                (cFirEmpleado,Tipo,Comentario,Folio,Fecha,Hora,cfir_fecha_hora)
                VALUES
                ('"""+str(ID_User)+"""',2,'"""+str(Comentario)+"""','"""+str(Folio)[2:]+"""',DATE(NOW()),TIME(NOW()),NOW())
                """)
                if Resultado["Contenido"] == "":
                    if "VA" in str(Folio):
                        Resultado["Contenido"] += DB.Instruccion("UPDATE portal.cvacaciones SET cvaRestantes = cvaRestantes + 1,cvaIDTomadas = cvaIDTomadas - 1 WHERE cvaIDEmpleado = '"+str(Empleado)+"'")
                    if "SD" in str(Folio):
                        Resultado["Contenido"] += DB.Instruccion("UPDATE portal.csickdays SET csda_dias_restantes = csda_dias_restantes + 1,csda_dias_tomados = csda_dias_tomados - 1 WHERE csda_idempleado = '"+str(Empleado)+"'")
        Resultado["Contenido"] += DB.Instruccion("DELETE FROM portal.ctodo WHERE ctd_formato_dia = '"+str(Folio)[2:]+"' OR ctd_folio = '"+str(Folio)+"';")
        Resultado["Contenido"] += DB.Instruccion("DELETE FROM portal.cestado_av WHERE cesav_folio = '"+str(Folio)+"';")
        if Resultado["Contenido"] == "":
            Resultado["Estado"] = 1
        return Resultado
    def Dame_Aniversario(self,Empleado):
        Resultado = {"Contenido":"","Estado":0,"Sig_Aniversario":datetime.now()}
        DB = DataBase()
        Fecha_Ingreso_DB = DB.Get_Dato("""
        select IFNULL(STAFF.csf_fecha_staff,EMP.FechaIngreso) as Fecha_Ingreso  from linc.empleados EMP 
        left join portal.cstaff STAFF on STAFF.csf_idempleado = EMP.IDEmpleado 
        where EMP.IDEmpleado = '"""+str(Empleado)+"""'
        """)[0]["Fecha_Ingreso"]
        Fecha_Ingreso = datetime.strptime(str(Fecha_Ingreso_DB),"%Y-%m-%d")
        Fecha_Ingreso_Aux = Fecha_Ingreso
        if Fecha_Ingreso_Aux.replace(year=datetime.now().year) < datetime.now():
            Resultado["Sig_Aniversario"] = Fecha_Ingreso.replace(year=datetime.now().year) + timedelta(days=365)
        else:
            Resultado["Sig_Aniversario"] = Fecha_Ingreso.replace(year=datetime.now().year)
        return Resultado
    def Generar_Pdf(self,Planta,Tipo,ID,Info):
        Resultado = {"Estado":0,"Contenido":"","Archivo":""}
        try:
            ficheros_viejos = [f for f in Path("C:/inetpub/wwwroot/Portal/Formatos Master/Generar/").iterdir() if self.minutos_desde_modificacion(f)>10]
            for F in ficheros_viejos:
                os.remove(F)
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=letter)
            Alto = 792
            can.setFont('Helvetica-Bold', 12)
            for F in Info:
                if "Alinear" in F.keys():
                    if F["Alinear"] == "Centrado":
                        can.drawCentredString(F["Ancho"], Alto - F["Alto"], F["Texto"])
                    if F["Alinear"] == "Derecha":
                        can.setFont('Helvetica', 9)
                        can.drawRightString(F["Ancho"], Alto - F["Alto"], F["Texto"])
                        can.setFont('Helvetica-Bold', 12)
                else:
                    can.drawString(F["Ancho"], Alto - F["Alto"], F["Texto"])
            can.save()
            packet.seek(0)
            new_pdf = PdfReader(packet)
            existing_pdf = PdfReader(open("C:/inetpub/wwwroot/Portal/Formatos Master/"+str(Tipo)+"-"+str(Planta)+".pdf", "rb"))
            output = PdfWriter()
            page = existing_pdf.pages[0]
            page.merge_page(new_pdf.pages[0])
            output.add_page(page)
            output_stream = open("C:/inetpub/wwwroot/Portal/Formatos Master/Generar/"+str(ID)+".pdf", "wb")
            output.write(output_stream)
            output_stream.close()
            Resultado["Archivo"] = str(ID)+".pdf"
            Resultado["Estado"] = 1
        except :
            Resultado["Contenido"] = str(sys.exc_info())
        return Resultado
    def minutos_desde_modificacion(self,f): 
        return (time.time() - f.stat().st_mtime)/60
    def Dame_Siguiente_Firma(self,Folio):
        Firma_Sig = None
        DB = DataBase()
        Firmas_YA =[]
        Pasos_Adicionas = []
        Fimas = []
        Str_Firmas = None
        Formato_Dia = False
        if "AT" in str(Folio):
            Info = DB.Get_Dato("SELECT * FROM portal.creque_empleado WHERE cre_id = '"+str(Folio)[2:]+"' ")[0]
            Str_Firmas = Info["cre_firmas"].replace(" ","")
        if "ST" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT cst_firmas FROM portal.cst WHERE cst_id = '"+str(Folio)[2:]+"' ")[0]["cst_firmas"].replace(" ","")
        if "TE" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT cte_firmas FROM portal.cte WHERE cte_id = '"+str(Folio)[2:]+"' ")[0]["cte_firmas"].replace(" ","")
        if "VA" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT cva_firmas FROM portal.cva WHERE cva_id = '"+str(Folio)[2:]+"' ")[0]["cva_firmas"].replace(" ","")
        if "AR" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT car_firmas FROM portal.car WHERE car_id = '"+str(Folio)[2:]+"' ")[0]["car_firmas"].replace(" ","")
        if "RE" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT cre_firmas FROM portal.cda WHERE cre_id = '"+str(Folio)[2:]+"' ")[0]["cre_firmas"].replace(" ","")
        if "PT" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT cpt_firmas FROM portal.cpt WHERE cpt_id = '"+str(Folio)[2:]+"' ")[0]["cpt_firmas"].replace(" ","")
        if "DL" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT cdl_firmas FROM portal.cdl WHERE cdl_id = '"+str(Folio)[2:]+"' ")[0]["cdl_firmas"].replace(" ","")
        if "SD" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT csd_firmas FROM portal.csd WHERE csd_id = '"+str(Folio)[2:]+"' ")[0]["csd_firmas"].replace(" ","")
        if "IN" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT cin_firmas FROM portal.cin WHERE cin_id = '"+str(Folio)[2:]+"' ")[0]["cin_firmas"].replace(" ","")
        if "PE" in str(Folio):
            Formato_Dia = True
            Str_Firmas = DB.Get_Dato("SELECT cpe_firmas FROM portal.cpe WHERE cpe_id = '"+str(Folio)[2:]+"' ")[0]["cpe_firmas"].replace(" ","")
        if "CC" in str(Folio):
            Str_Firmas = DB.Get_Dato("SELECT ccp_firmas FROM portal.ccp WHERE ccp_id = '"+str(Folio)[2:]+"' ")[0]["ccp_firmas"].replace(" ","")
        if "CA" in str(Folio):
            Str_Firmas = DB.Get_Dato("SELECT cca_firmas FROM portal.cca WHERE cca_id = '"+str(Folio)[2:]+"' ")[0]["cca_firmas"].replace(" ","")
        if "CC" in str(Folio):
            Str_Firmas = DB.Get_Dato("SELECT ccc_firmas FROM portal.ccc WHERE ccc_id = '"+str(Folio)[2:]+"' ")[0]["ccc_firmas"].replace(" ","")
        if "DF" in str(Folio):
            Str_Firmas = DB.Get_Dato("SELECT cdf_firmas FROM portal.cdf WHERE cdf_id = '"+str(Folio)[2:]+"' ")[0]["cdf_firmas"].replace(" ","")
        if "RD" in str(Folio):
            Str_Firmas = DB.Get_Dato("SELECT crd_firmas FROM portal.crd WHERE crd_id = '"+str(Folio)[2:]+"' ")[0]["crd_firmas"].replace(" ","")
        if "WC" in str(Folio):
            Str_Firmas = DB.Get_Dato("SELECT cwc_firmas FROM portal.cwc WHERE cwc_id = '"+str(Folio)[2:]+"' ")[0]["cwc_firmas"].replace(" ","")
        if "WD" in str(Folio):
            Str_Firmas = DB.Get_Dato("SELECT cwd_firmas FROM portal.cwd WHERE cwd_id = '"+str(Folio)[2:]+"' ")[0]["cwd_firmas"].replace(" ","")

        if Formato_Dia == True:
            Firmas_YA = DB.Get_Dato("select * from portal.cfirmas FIR where FIR.Folio = '"+str(Folio)[2:]+"'")
        else:
            Firmas_YA = DB.Get_Dato("select * from portal.cfirmas FIR where FIR.cffolio = '"+str(Folio)+"'")
        ToDo = DB.Get_Dato("select * from portal.ctodo ToDo where ToDo.ctd_folio = '"+str(Folio)+"'")

        if Str_Firmas is not None:
            for F in str(Str_Firmas).split("|"):
                Nombre = DB.Get_Dato("SELECT EMP.IDEmpleado,EMP.Nombre FROM portal.cuser USR inner join linc.empleados EMP on EMP.IDEmpleado = USR.cusidempleado WHERE cusrid = '"+str(F)+"' ")
                if len(Nombre) > 0:
                    Nombre = Nombre[0]
                    Ya = None
                    for F_YA in Firmas_YA:
                        if str(F_YA["cFirEmpleado"]) == str(F):
                            Ya = F_YA
                            break
                    if Ya is None:
                        if len(ToDo) > 0 and str(ToDo[0]["ctd_idusuario"]) == str(F):
                            Aux_Fimas = {"Usuario":str(F),"Nombre":Nombre["Nombre"],"IDEmpleado":Nombre["Nombre"],"Aqui":"Todo"}
                        else:
                            Aux_Fimas = {"Usuario":str(F),"Nombre":Nombre["Nombre"],"IDEmpleado":Nombre["Nombre"]}
                    else:
                        if len(ToDo) > 0 and str(ToDo[0]["ctd_idusuario"]) == str(F):
                            Aux_Fimas = {"Usuario":str(F),"Nombre":Nombre["Nombre"],"IDEmpleado":Nombre["Nombre"],"Fecha":Ya["cfir_fecha_hora"],"Tipo":Ya["Tipo"],"Comentario":Ya["Comentario"],"Aqui":"Todo"}
                        else:
                            Aux_Fimas = {"Usuario":str(F),"Nombre":Nombre["Nombre"],"IDEmpleado":Nombre["Nombre"],"Fecha":Ya["cfir_fecha_hora"],"Tipo":Ya["Tipo"],"Comentario":Ya["Comentario"]}
                    Fimas.append(Aux_Fimas)
            Tipo_AV = [
                {"Departamento":"ADT Departament","Texto":"In recruitment process","Tipo_AV":"ADT"},
                {"Departamento":"Nominas Departament","Texto":"In process of application","Tipo_AV":"NOMINA"},
                {"Departamento":"RH Departament","Texto":"In process of application","Tipo_AV":"RH"}
            ]
            for AV in Tipo_AV:
                if AV["Tipo_AV"] in Str_Firmas:
                    Ya = None
                    for F_YA in Firmas_YA:
                        if str(F_YA["cFir_Tipo_AV"]) == AV["Tipo_AV"]:
                            Ya = F_YA
                            break
                    if Ya is None:
                        Pasos_Adicionas.append(AV)
                    else:
                        Nombre = DB.Get_Dato("SELECT EMP.IDEmpleado,EMP.Nombre FROM portal.cuser USR inner join linc.empleados EMP on EMP.IDEmpleado = USR.cusidempleado WHERE cusrid = '"+str(Ya["cFirEmpleado"])+"' ")[0]
                        AV["Usuario"] = Ya["cFirEmpleado"]
                        AV["Nombre"] = Nombre["Nombre"]
                        AV["IDEmpleado"] = Nombre["IDEmpleado"]
                        AV["Fecha"] = Ya["cfir_fecha_hora"]
                        AV["Tipo"] = Ya["Tipo"]
                        AV["Comentario"] = Ya["Comentario"]
                        Pasos_Adicionas.append(AV)

        Firmas_Totales = []
        for F in Fimas:
            Firmas_Totales.append(F)
        for F in Pasos_Adicionas:
            Firmas_Totales.append(F)
        
        Next = False
        for T in Firmas_Totales:
            if Next == True:
                if "Fecha" not in T.keys():
                    if "Tipo_AV" in T.keys():
                        Firma_Sig = T["Tipo_AV"]
                    else:
                        Firma_Sig = T["Usuario"]
                    break
                else:
                    Next = False
            if "Fecha" in T.keys():
                Next = True

        return Firma_Sig
    def Dame_AV(self):
        AV = ["NOMINA","ADT","RH","CONTEOS","PDF"]
        return AV
    def Dame_K(self):
        return "HbAHa3PZrpKinCOcJAlWTM-Yj3nx6QFbHW5SG6DLmRI="
    def Dame_K2(self):
        return "Kz2P2Oih49uGkKV4LHrpIr-65WHgy8yFuaBvQ75boLE="
    def Dame_Base_Datos(self,Negocio):
        if Negocio == "YMS":
            return "public"
class Encriptar:
    def __init__(self):
        return;
    def Get_Key(self,ID):
        DB = DataBase()
        fernet = Fernet(DB.Get_Dato("SELECT cportal_key FROM portal.cconf_portal")[0]["cportal_key"])
        Key = fernet.encrypt(str(str(ID)+"-"+str(datetime.now().strftime("%H%M%S"))).encode()).decode("utf-8")
        return Key
    def Update_Key(self,Key):
        DB = DataBase()
        fernet = Fernet(DB.Get_Dato("SELECT cportal_key FROM portal.cconf_portal")[0]["cportal_key"])
        ID = str(fernet.decrypt(Key.encode()).decode()).split("-")[0]
        Key = fernet.encrypt(str(str(ID)+"-"+str(datetime.now().strftime("%H%M%S"))).encode()).decode("utf-8")
        return Key
    def Get_IDUsuario(self,Key):
        DB = DataBase()
        fernet = Fernet(DB.Get_Dato("SELECT cportal_key FROM portal.cconf_portal")[0]["cportal_key"])
        ID = str(fernet.decrypt(Key.encode()).decode()).split("-")[0]
        return ID
    def Get_Encriptar(self,Texto):
        DB = DataBase()
        fernet = Fernet(DB.Get_Dato("SELECT cportal_key FROM portal.cconf_portal")[0]["cportal_key"])
        return fernet.encrypt(str(Texto).encode()).decode("utf-8")
    def Get_Desencriptar(self,Key):
        DB = DataBase()
        fernet = Fernet(DB.Get_Dato("SELECT cportal_key FROM portal.cconf_portal")[0]["cportal_key"])
        return str(fernet.decrypt(Key.encode()).decode())
class Pass:
    def __init__(self):
        return;
    def cifrar(self,plaintext):
        A = list([str(ord(c)*5) for c in plaintext])
        AA = []
        for B in A:
            AA.append(B.zfill(5))
        return "".join(AA)
    def descifrar(self,plaintext):
        Res = ""
        index = 0
        B = ""
        for A in plaintext:
            if index == 5:
                Res += chr(int(int(B)/5))
                index =0
                B = ""
            else:
                B += str(A)
            index += 1
        Res += chr(int(int(plaintext[-5:])/5))
        return Res
class Menu:
    def __init__(self):
        return;
    def Get_Menu(self,Raiz,ID_User=None):
        DB = DataBase()
        Permisos = []
        Info_User = DB.Get_Dato("select * FROM public.cuser USR where USR.cusrid = '"+str(ID_User)+"'")
        # if len(Info_User) > 0:
        #     Permisos = Info_User[0]["cpermisos_temp_portal2"].split(",")
        Menu = {}
        Menu["To Do"] ={
            "Link": str(Raiz)+"ToDo",
            "Icono":"mdi mdi-bullhorn",
            "Color":"#fb3a3a",
            "Letra":"rgba(255, 255, 255, 0.9)",
            "ID":"RH",
            "P":"",
            "Grupo_IDS":[]
        }
        
        # Menu["WTC"] ={
        #             "Link": str(Raiz)+"WTC",
        #             "Items":{
        #                 "Yard":{"Icono":"mdi mdi-script","Link":"/WTC/Yard","P":"Yard","Fun":"Inicio","ID":1504},
        #                 "Dispatch":{"Icono":"mdi mdi-check-decagram","Link":"/WTC/Despacho","P":"Yard","Fun":"Inicio","ID":1508}
        #             },
        #             "Icono":"mdi mdi-domain",
        #             "Color":"#8C68CD",
        #             "Letra":"rgba(255, 255, 255, 0.9)",
        #             "ID":"RH",
        #             "P":"",
        #             "Grupo_IDS":[]
        #         }
        # Menu["ODC"] ={
        #             "Link": str(Raiz)+"ODC",
        #             "Items":{
        #                 "Container Control":{
        #                     "Icono":"mdi mdi-truck-trailer",
        #                     "Items":{
        #                         "Container":{"Icono":"mdi mdi-truck-trailer","Link":"/ODC/Container_Control","P":"Yard","Fun":"Inicio","ID":1501},
        #                         "Container Manager":{"Icono":"mdi mdi-truck-trailer","Link":"/ODC/Container_Manager","P":"Yard","Fun":"Inicio","ID":1502},
        #                     }
        #                 },
        #                 "Outbound Status":{
        #                     "Icono":"mdi mdi-progress-upload",
        #                     "Items":{
        #                         "Outbound Status":{"Icono":"mdi mdi-progress-upload","Link":"/ODC/OutBound/Status","P":"Yard","Fun":"Inicio","ID":1501},
        #                         "Reporte":{"Icono":"mdi mdi-projector-screen","Link":"/ODC/OutBound/Report","P":"Yard","Fun":"Inicio","ID":1501}
        #                     }
        #                 },
        #                 # "MilkRun Status":{
        #                 #     "Icono":"mdi mdi-progress-upload",
        #                 #     "Items":{
        #                 #         "MilkRun Status":{"Icono":"mdi mdi-progress-upload","Link":"./MilkRun/inicio.py","P":"Yard","Fun":"Inicio","ID":1501},
        #                 #         "Reporte":{"Icono":"mdi mdi-projector-screen","Link":"./MilkRun/reporte.py","P":"Yard","Fun":"Inicio","ID":1501}
        #                 #     }
        #                 # },
        #                 # "Empty Rack":{
        #                 #     "Icono":"mdi mdi-dots-square",
        #                 #     "Items":{
        #                 #         "Estado Empty Racks":{"Icono":"mdi mdi-dots-square","Link":"./Equipo_Vacio/manifiestos.py","P":"Yard","Fun":"Inicio","ID":1501},
        #                 #         "Ingreso de Equipo Vacio":{"Icono":"mdi mdi-inbox-arrow-down","Link":"./Equipo_Vacio/ingreso.py","P":"Yard","Fun":"Inicio","ID":1501},
        #                 #         "Reporte":{"Icono":"mdi mdi-view-grid-compact","Link":"./Equipo_Vacio/reporte.py","P":"Yard","Fun":"Inicio","ID":1502}
        #                 #     }
        #                 # },
        #                 "OS&D":{"Icono":"mdi mdi-alert","Link":"/ODC/OSyD","Fun":"Inicio","ID":1508},
        #                 "Reports":{
        #                     "Icono":"mdi mdi-book",
        #                     "Items":{
        #                         "Container Search":{"Icono":"mdi mdi-feature-search","Link":"/ODC/Report/Container","P":"Yard","Fun":"Inicio","ID":1509},
        #                         "Daily":{"Icono":"mdi mdi-book","Link":"/ODC/Report/Daily","P":"Yard","Fun":"Inicio","ID":1510},
        #                         "Carrier":{"Icono":"mdi mdi-book","Link":"/ODC/Report/Carrier","P":"Yard","Fun":"Inicio","ID":1511},
        #                         "Aging Report":{"Icono":"mdi mdi-book","Link":"/ODC/Report/Aging","P":"Yard","Fun":"Inicio","ID":1512}
        #                     }
        #                 },
        #                 "Configuration":{
        #                     "Icono":"mdi mdi-cog",
        #                     "Items":{
        #                         "Suppliers Master":{"Icono":"mdi mdi-card-bulleted","Link":"/ODC/Conf/Suppliers","P":"Yard","Fun":"Inicio","ID":1505},
        #                         "Route Master":{"Icono":"mdi mdi-swap-vertical-variant","Link":"/ODC/Conf/Routes","P":"Yard","Fun":"Inicio","ID":1506},
        #                         "Docks Master":{"Icono":"mdi mdi-sign-caution","Link":"/ODC/Conf/Docks","P":"Yard","Fun":"Inicio","ID":1507},
        #                         "Destinos":{"Icono":"mdi mdi-card-bulleted","Link":"/ODC/Conf/Destination","P":"Yard","Fun":"Inicio","ID":1507}
        #                     }
        #                 },

        #             },
        #             "Icono":"mdi mdi-factory",
        #             "Color":"#3D8BFD",
        #             "Letra":"",
        #             "ID":"RH",
        #             "P":"",
        #             "Grupo_IDS":[1500,1501,1502,1503,1504,1505]
        #         }
        
        Menu["YMS"] ={
                    "Link": str(Raiz)+"YMS",
                    "Items":{
                        "Container Control":{
                            "Icono":"mdi mdi-truck-trailer",
                            "Items":{
                                "Container":{"Icono":"mdi mdi-truck-trailer","Link":"/YMS/Container_Control","P":"Yard","Fun":"Inicio","ID":1501},
                                "Container Manager":{"Icono":"mdi mdi-truck-trailer","Link":"/YMS/Container_Manager","P":"Yard","Fun":"Inicio","ID":1502},
                            }
                        },
                        "Docks":{"Icono":"mdi mdi-sign-caution","Link":"/YMS/Docks","Fun":"Inicio","ID":1508},
                        "Outbound Status":{
                            "Icono":"mdi mdi-progress-upload",
                            "Items":{
                                "Outbound Status":{"Icono":"mdi mdi-progress-upload","Link":"/YMS/OutBound/Status","P":"Yard","Fun":"Inicio","ID":1501},
                                "Reporte":{"Icono":"mdi mdi-projector-screen","Link":"/YMS/OutBound/Report","P":"Yard","Fun":"Inicio","ID":1501}
                            }
                        },
                        "OS&D":{"Icono":"mdi mdi-alert","Link":"/YMS/OSyD","Fun":"Inicio","ID":1508},
                        "Reports":{
                            "Icono":"mdi mdi-book",
                            "Items":{
                                "Container Search":{"Icono":"mdi mdi-feature-search","Link":"/YMS/Report/Container","P":"Yard","Fun":"Inicio","ID":1509},
                                "Daily":{"Icono":"mdi mdi-book","Link":"/YMS/Report/Daily","P":"Yard","Fun":"Inicio","ID":1510},
                                "Carrier":{"Icono":"mdi mdi-book","Link":"/YMS/Report/Carrier","P":"Yard","Fun":"Inicio","ID":1511},
                                "Aging Report":{"Icono":"mdi mdi-book","Link":"/YMS/Report/Aging","P":"Yard","Fun":"Inicio","ID":1512}
                            }
                        },
                        "Configuration":{
                            "Icono":"mdi mdi-cog",
                            "Items":{
                                "Suppliers Master":{"Icono":"mdi mdi-card-bulleted","Link":"/YMS/Conf/Suppliers","P":"Yard","Fun":"Inicio","ID":1505},
                                "Route Master":{"Icono":"mdi mdi-swap-vertical-variant","Link":"/YMS/Conf/Routes","P":"Yard","Fun":"Inicio","ID":1506},
                                "Docks Master":{"Icono":"mdi mdi-sign-caution","Link":"/YMS/Conf/Docks","P":"Yard","Fun":"Inicio","ID":1507},
                                "Destinatio Master":{"Icono":"mdi mdi-card-bulleted","Link":"/YMS/Conf/Destination","P":"Yard","Fun":"Inicio","ID":1507},
                                "Carrier Master":{"Icono":"mdi mdi-card-bulleted","Link":"/YMS/Conf/Carrier","P":"Yard","Fun":"Inicio","ID":1507}
                            }
                        },

                    },
                    "Icono":"mdi mdi-factory",
                    "Color":"#3D8BFD",
                    "Letra":"",
                    "ID":"RH",
                    "P":"",
                    "Grupo_IDS":[1500,1501,1502,1503,1504,1505]
                }
    
        # if ID_User is not None:
        #     if "WTC" not in Permisos:
        #         del Menu["WTC"]
        #     if "ODC" not in Permisos:
        #         del Menu["ODC"]
        #     if "XDOCK NISSAN" not in Permisos:
        #         del Menu["XDOCK NISSAN"]
        #     if "LC" not in Permisos:
        #         del Menu["LC"]
        #     if "RG" not in Permisos:
        #         del Menu["RG"]
        #     if "ILC Saltillo" not in Permisos:
        #         del Menu["ILC Saltillo"]
        #     if "RILC Toluca" not in Permisos:
        #         del Menu["RILC Toluca"]
        #     if "DTNA Saltillo" not in Permisos:
        #         del Menu["DTNA Saltillo"]
        return Menu
    def Menu(self,Activo,Raiz,ID_User):
        DB = DataBase()
        Info_User = DB.Get_Dato("select * FROM public.cuser USR where USR.cusrid = '"+str(ID_User)+"'")[0]
        #Info_User = DB.Get_Dato("select EMP.IDEmpleado,EMP.Nombre,PER.cpu_permisos  FROM portal.cuser USR inner join linc.empleados EMP on USR.cusidempleado = EMP.IDEmpleado inner join portal.cpermisos_usuario PER on PER.cpu_id = USR.cgrupo_permisos where USR.cusrid = '"+str(ID_User)+"'")[0]
        Menu = self.Get_Menu(Raiz,str(ID_User))
        Res = ""
        Res += """
            <style>
                .Color_Barra{
                    background: """+str(Menu[Activo]["Color"])+""";
                }
            </style>
            <nav class="navbar bg-dark bg-body-tertiary  p-0 m-0 shadow " data-bs-theme="dark">
                <div class="container-fluid">
                    <div>
                        <button class="navbar-toggler mt-1 mb-1" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
                            <span class="mdi mdi-menu"></span>
                        </button>
                        <span class='fst-italic  text-nowrap'><i class="mdi mdi-chevron-double-right " style="color:#ED1C24"></i><span class='text-white '>Universal</span> <span style="color:#ED1C24">YMS</span> <i class="mdi mdi-chevron-double-right " style="color:#ED1C24"></i> <span style='color:"""+str(Menu[Activo]["Color"])+"""'> <i class='"""+str(Menu[Activo]["Icono"])+"""'></i> """+str(Activo)+"""</span> </span>
                    </div>
                    <div>
                        <div class='row'>
                            <div class='col text-white '>
                                <i class='mdi mdi-account-box'></i> """+str(Info_User["Nombre"])+"""
                            </div>
                            <div class='col-auto'>
                                <a class='link-danger' style='cursor:pointer' onclick='Cerrar_Sesion();'><i class='mdi mdi-exit-run'></i> Sign Out</a>
                            </div>
                            <div class='col-auto'>
                                <!--<a class='link-primary'><i class='mdi mdi-form-textbox-password'></i> Change Password</a>-->
                            </div>
                        </div>
                        
                    </div>
                    <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
                        <div class="offcanvas-header">
                            <h5 class='fst-italic  text-nowrap'><i class="mdi mdi-chevron-double-right " style="color:#ED1C24"></i><span class='text-white '>Universal</span> <span style="color:#ED1C24">YMS</span></h5>
                            <!--<div class='text-end pe-5'><img class='p-1' style='background:#212529' width='30%' height='auto'  id='Logo_Universal' src=''></img></div>-->
                            <script>$("#Logo_Universal").attr('src',Logo_Univerasl);</script>
                            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                        </div>
                        <div class="offcanvas-body">
                            <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
        """
        for M in Menu.keys():
            Res += """<li class="nav-item fs-5 fst-italic  border-bottom border-opacity-50" onmousemove='animateCSS($(this).find(".flechas").get(), "fadeInLeft")' style='color:"""+str(Menu[M]["Color"])+""";cursor:pointer;' onclick='Ir_Index(\""""+str(Menu[M]["Link"])+"""\")'><a><div style='display: inline-block; color:"""+str(Menu[M]["Color"])+"""' class='flechas mdi mdi-chevron-double-right'></div> <i class='"""+str(Menu[M]["Icono"])+"""'></i> """+str(M)+"""</a></li>"""
        Res += """
                        </ul>
                    </div>
                </div>
            </div>
        </nav>
        """
        if "Items" in Menu[Activo].keys():
            Res += """
            <ul class="nav nav-underline justify-content-center shadow " style='background:"""+str(Menu[Activo]["Color"])+"""'>
            """
            for Sub in Menu[Activo]["Items"].keys():
                if "Items" in Menu[Activo]["Items"][Sub].keys():
                    Res += """
                      <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle text-decoration-none link-dark link-opacity-75 " data-bs-toggle="dropdown" role="button" aria-expanded="false"><i class='"""+str(Menu[Activo]["Items"][Sub]["Icono"])+"""'></i> """+str(Sub)+"""</a>
                            <ul class="dropdown-menu" style='background:"""+str(Menu[Activo]["Color"])+"""'>
                    """
                    for SubSub in Menu[Activo]["Items"][Sub]["Items"].keys():
                        if "Items" in Menu[Activo]["Items"][Sub]["Items"][SubSub].keys():
                             Res += "<div style='color:rgba(0, 0, 0, 0.4)' class='fw-semibold fs-6 text border-top p-0 m-0'> <i class='"+str(Menu[Activo]["Items"][Sub]["Items"][SubSub]["Icono"])+"'></i>"+str(SubSub)+"</div>"
                             for SubSubSub in Menu[Activo]["Items"][Sub]["Items"][SubSub]["Items"].keys():
                                 Res += """<li style='cursor:pointer;' onmousemove='animateCSS($(this).find(".flechas").get(), "fadeInLeft")'><a class='p-0 m-0 p-1 dropdown-item nav-link text-decoration-none link-dark link-opacity-75'><div style='display: inline-block;' class='flechas mdi mdi-chevron-double-right'></div><i class='"""+str(Menu[Activo]["Items"][Sub]["Items"][SubSub]["Items"][SubSubSub]["Icono"])+"""'></i> """+str(SubSubSub)+"""</a></li>"""
                        else:
                            Res += """<li onclick='Llamar_Funcion(\""""+Menu[Activo]["Items"][Sub]["Items"][SubSub]["Link"]+"""\")' style='cursor:pointer;' onmousemove='animateCSS($(this).find(".flechas").get(), "fadeInLeft")'><a class='p-0 m-0 p-1 dropdown-item nav-link text-decoration-none link-dark link-opacity-75'><div style='display: inline-block;' class='flechas mdi mdi-chevron-double-right'></div><i class='"""+str(Menu[Activo]["Items"][Sub]["Items"][SubSub]["Icono"])+"""'></i> """+str(SubSub)+"""</a></li>"""
                    Res += """
                            </ul>
                        </li>
                    """
                else:
                    Res += """<li onclick='Llamar_Funcion(\""""+Menu[Activo]["Items"][Sub]["Link"]+"""\")' style='cursor:pointer;' onmousemove='animateCSS($(this).find(".flechas").get(), "fadeInLeft")' class='nav-item'><a class='nav-link text-decoration-none link-dark link-opacity-75'><div style='display: inline-block;' class='flechas mdi mdi-chevron-double-right'></div><i class='"""+str(Menu[Activo]["Items"][Sub]["Icono"])+"""'></i> """+str(Sub)+"""</a></li>"""
            Res += """
            </ul>
            """

        Res += """
        <script>
            const animateCSS = (element, animation, prefix = 'animate__') =>
            new Promise((resolve, reject) => {
                const animationName = `${prefix}${animation}`;
                const node = $(element)[0];
                node.classList.add(`${prefix}animated`, animationName);
                function handleAnimationEnd(event) {
                event.stopPropagation();
                $(element).removeClass("animate__animated " + animationName);
                node.classList.remove(`${prefix}animated`, animationName);
                resolve('Animation ended');
                }
                node.addEventListener('animationend', handleAnimationEnd, {once: true});
            });

            function Ir_Index(Link){
                Mostrar_Ventana_Cargando(false);
                setTimeout(function(){ window.location.href = Link },500);
               
            }
            function Llamar_Funcion(Direccion,Mensaje=null,P=null){
                Mostrar_Ventana_Cargando(false);
                setTimeout(function(){ window.location.href = Direccion },500);
                /*window.location.href = Direccion;
                var parametros = {"Fun":"Inicio","P":P };
                $.ajax({data:  parametros,url:Direccion,type:  "post",
                    success:  function (response)
                    {
                        alert(response);
                        var Resultado = JSON.parse(response);
                        $("#Pag").html(Resultado["Contenido"]);
                        swal.close();
                        if(Mensaje != null){
                            Mensaje(Mensaje);
                        }
                            
                    },
                    error: function (jqXHR, textStatus, errorThrown )
                    {
                        $("#Pag").html("<div class='text-center fw-bold text-danger'><i class='mdi mdi-alert'></i> "+ textStatus+"</div>");
                        swal.close();
                    }
                });*/
            }
            function Cerrar_Sesion(){
                window.location= '"""+str(request.url_root)+"""';
            }
       </script>
        """
        return Res
    def Get_Titulo(self,Activo):
        Menu = self.Get_Menu("")
        return "<i class='"+str(Menu[Activo]["Icono"])+"'></i> "+str(Activo)
class Menu_Proveedor:
    def __init__(self):
        return;
    def Get_Menu(self,Raiz,ID_User=None):
        DB = DataBase()
        Permisos = []
        Info_User = DB.Get_Dato("select * FROM portal.cuser USR where USR.cusrid = '"+str(ID_User)+"'")
        if len(Info_User) > 0:
            Permisos = Info_User[0]["cpermisos_temp_portal2"].split(",")
        Menu = {}
        Menu["Proveedores"] ={
                "Link": str(Raiz)+"Proveedores/index.py",
                "Items":{
                    #"Yard":{"Icono":"mdi mdi-car-brake-parking","Link":"./yard.py","Fun":"Inicio","ID":1500},
                    # "Container Control":{
                    #     "Icono":"mdi mdi-truck-trailer",
                    #     "Items":{
                    #         "Container":{"Icono":"mdi mdi-truck-trailer","Link":"./Container_Control/Container.py","Fun":"Inicio","ID":1501},
                    #         "Container Manager":{"Icono":"mdi mdi-truck-trailer","Link":"./Container_Control/Container_Manager.py","Fun":"Inicio","ID":1502},
                    #     }
                    # },
                    "Órdenes de compra":{"Icono":"mdi mdi-cards-variant","Link":"./Ordenes.py","Fun":"Inicio","ID":1508},
                    "Información de registro":{"Icono":"mdi mdi-format-align-justify","Link":"./OSyD.py","Fun":"Inicio","ID":1508}
                    # "Reports":{
                    #     "Icono":"mdi mdi-book",
                    #     "Items":{
                    #         "Container Search":{"Icono":"mdi mdi-feature-search","Link":"./Reportes/buscar.py","Fun":"Inicio","ID":1509},
                    #         "Daily":{"Icono":"mdi mdi-book","Link":"./Reportes/daily.py","Fun":"Inicio","ID":1510},
                    #         "Carrier":{"Icono":"mdi mdi-book","Link":"./Reportes/carrier.py","Fun":"Inicio","ID":1511},
                    #         "Aging Report":{"Icono":"mdi mdi-book","Link":"./Reportes/tiempo.py","Fun":"Inicio","ID":1512}
                    #     }
                    # },
                    # "Configuration":{
                    #     "Icono":"mdi mdi-cog",
                    #     "Items":{
                    #         "Suppliers Master":{"Icono":"mdi mdi-card-bulleted","Link":"./Configuracion/Proveedores.py","Fun":"Inicio","ID":1505},
                    #         "Route Master":{"Icono":"mdi mdi-swap-vertical-variant","Link":"./Configuracion/Rutas.py","Fun":"Inicio","ID":1506},
                    #         "Docks Master":{"Icono":"mdi mdi-sign-caution","Link":"./Configuracion/Docks.py","Fun":"Inicio","ID":1507}
                    #     }
                    # },

                },
                "Icono":"mdi mdi-factory",
                "Color":"#07C6B9",
                "Letra":"",
                "ID":"RH",
                "Grupo_IDS":[1500,1501,1502,1503,1504,1505]
            }
        return Menu
        #177
    def Menu(self,Activo,Raiz,Key):
        DB = DataBase()
        Encripta = Encriptar()
        ID_User = Encripta.Get_IDUsuario(Key)
        Info_User = DB.Get_Dato("select EMP.IDEmpleado,EMP.Nombre,PER.cpu_permisos  FROM portal.cuser USR inner join linc.empleados EMP on USR.cusidempleado = EMP.IDEmpleado inner join portal.cpermisos_usuario PER on PER.cpu_id = USR.cgrupo_permisos where USR.cusrid = '"+str(ID_User)+"'")[0]
        Menu = self.Get_Menu(Raiz,str(ID_User))
        Res = ""
        Res += """
            <style>
                .Color_Barra{
                    background: """+str(Menu[Activo]["Color"])+""";
                }
            </style>
            <nav class="navbar bg-dark bg-body-tertiary  p-0 m-0 shadow " data-bs-theme="dark">
                <div class="container-fluid">
                    <div class='mt-1 mb-1'>
                        <!--<button class="navbar-toggler mt-1 mb-1" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
                            <span class="mdi mdi-menu"></span>
                        </button>-->
                        <!--<span class='fst-italic fw-bold text-nowrap'><i class="mdi mdi-chevron-double-right " style="color:#ED1C24"></i><span class='text-white '>Portal</span> <span style="color:#ED1C24">MX</span> <i class="mdi mdi-chevron-double-right " style="color:#ED1C24"></i> <span style='color:"""+str(Menu[Activo]["Color"])+"""'> <i class='"""+str(Menu[Activo]["Icono"])+"""'></i> """+str(Activo)+"""</span> </span>-->
                        <span class='fst-italic fw-bold text-nowrap'><i class="mdi mdi-chevron-double-right " style="color:#ED1C24"></i><span class='text-white '>Portal</span> <span style="color:#ED1C24" class='fw-light'>Proveedores</span> <span style='color:"""+str(Menu[Activo]["Color"])+"""'></span> </span>
                    </div>
                    <div>
                        <div class='row'>
                            <div class='col text-white fw-bold'>
                                <i class='mdi mdi-account-box'></i> """+str(Info_User["Nombre"])+"""
                            </div>
                            <div class='col-auto'>
                                <a class='link-danger' style='cursor:pointer' onclick='Cerrar_Sesion();'><i class='mdi mdi-exit-run'></i> Salir</a>
                            </div>
                            <div class='col-auto'>
                                <!--<a class='link-primary'><i class='mdi mdi-form-textbox-password'></i> Change Password</a>-->
                            </div>
                        </div>
                        
                    </div>
                    <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
                        <div class="offcanvas-header">
                            <h5 class='fst-italic fw-bold text-nowrap'><i class="mdi mdi-chevron-double-right " style="color:#ED1C24"></i><span class='text-white '>Portal</span> <span style="color:#ED1C24">MX</span></h5>
                            <!--<div class='text-end pe-5'><img class='p-1' style='background:#212529' width='30%' height='auto'  id='Logo_Universal' src=''></img></div>--!>
                            <script>$("#Logo_Universal").attr('src',Logo_Univerasl);</script>
                            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                        </div>
                        <div class="offcanvas-body">
                            <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
        """
        for M in Menu.keys():
            Res += """<li class="nav-item fs-5 fst-italic fw-bold border-bottom border-opacity-50" onmousemove='animateCSS($(this).find(".flechas").get(), "fadeInLeft")' style='color:"""+str(Menu[M]["Color"])+""";cursor:pointer;' onclick='Ir_Index(\""""+str(Menu[M]["Link"])+"""\")'><a><div style='display: inline-block; color:"""+str(Menu[M]["Color"])+"""' class='flechas mdi mdi-chevron-double-right'></div> <i class='"""+str(Menu[M]["Icono"])+"""'></i> """+str(M)+"""</a></li>"""
        Res += """
                        </ul>
                    </div>
                </div>
            </div>
        </nav>
        """
        if "Items" in Menu[Activo].keys():
            Res += """
            <ul class="nav nav-underline justify-content-center shadow " style='background:"""+str(Menu[Activo]["Color"])+"""'>
            """
            for Sub in Menu[Activo]["Items"].keys():
                if "Items" in Menu[Activo]["Items"][Sub].keys():
                    Res += """
                      <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle text-decoration-none link-dark link-opacity-75 fw-bold" data-bs-toggle="dropdown" role="button" aria-expanded="false"><i class='"""+str(Menu[Activo]["Items"][Sub]["Icono"])+"""'></i> """+str(Sub)+"""</a>
                            <ul class="dropdown-menu" style='background:"""+str(Menu[Activo]["Color"])+"""'>
                    """
                    for SubSub in Menu[Activo]["Items"][Sub]["Items"].keys():
                        if "Items" in Menu[Activo]["Items"][Sub]["Items"][SubSub].keys():
                             Res += "<div style='color:rgba(0, 0, 0, 0.4)' class='fw-semibold fs-6 text border-top p-0 m-0'> <i class='"+str(Menu[Activo]["Items"][Sub]["Items"][SubSub]["Icono"])+"'></i>"+str(SubSub)+"</div>"
                             for SubSubSub in Menu[Activo]["Items"][Sub]["Items"][SubSub]["Items"].keys():
                                 Res += """<li style='cursor:pointer;' onmousemove='animateCSS($(this).find(".flechas").get(), "fadeInLeft")'><a class='p-0 m-0 p-1 dropdown-item nav-link text-decoration-none link-dark link-opacity-75 fw-bold'><div style='display: inline-block;' class='flechas mdi mdi-chevron-double-right'></div><i class='"""+str(Menu[Activo]["Items"][Sub]["Items"][SubSub]["Items"][SubSubSub]["Icono"])+"""'></i> """+str(SubSubSub)+"""</a></li>"""
                        else:
                            Res += """<li onclick='Llamar_Funcion(\""""+Menu[Activo]["Items"][Sub]["Items"][SubSub]["Link"]+"""\")' style='cursor:pointer;' onmousemove='animateCSS($(this).find(".flechas").get(), "fadeInLeft")'><a class='p-0 m-0 p-1 dropdown-item nav-link text-decoration-none link-dark link-opacity-75 fw-bold'><div style='display: inline-block;' class='flechas mdi mdi-chevron-double-right'></div><i class='"""+str(Menu[Activo]["Items"][Sub]["Items"][SubSub]["Icono"])+"""'></i> """+str(SubSub)+"""</a></li>"""
                    Res += """
                            </ul>
                        </li>
                    """
                else:
                    Res += """<li onclick='Llamar_Funcion(\""""+Menu[Activo]["Items"][Sub]["Link"]+"""\")' style='cursor:pointer;' onmousemove='animateCSS($(this).find(".flechas").get(), "fadeInLeft")' class='nav-item'><a class='nav-link text-decoration-none link-dark link-opacity-75 fw-bold'><div style='display: inline-block;' class='flechas mdi mdi-chevron-double-right'></div><i class='"""+str(Menu[Activo]["Items"][Sub]["Icono"])+"""'></i> """+str(Sub)+"""</a></li>"""
            Res += """
            </ul>
            """

        Res += """
        <script>
            const animateCSS = (element, animation, prefix = 'animate__') =>
            new Promise((resolve, reject) => {
                const animationName = `${prefix}${animation}`;
                const node = $(element)[0];
                node.classList.add(`${prefix}animated`, animationName);
                function handleAnimationEnd(event) {
                event.stopPropagation();
                $(element).removeClass("animate__animated " + animationName);
                node.classList.remove(`${prefix}animated`, animationName);
                resolve('Animation ended');
                }
                node.addEventListener('animationend', handleAnimationEnd, {once: true});
            });

            function Ir_Index(Link){
                Mostrar_Ventana_Cargando(false);
                setTimeout(function(){ window.location.href = Link },500);
               
            }
            function Llamar_Funcion(Direccion,Mensaje=null){
                Mostrar_Ventana_Cargando(false);
                var parametros = {"Fun":"Inicio" };
                $.ajax({data:  parametros,url:Direccion,type:  "post",
                    success:  function (response)
                    {
                        var Resultado = JSON.parse(response);
                        $("#Pag").html(Resultado["Contenido"]);
                        swal.close();
                        if(Mensaje != null){
                            Mensaje(Mensaje);
                        }
                            
                    },
                    error: function (jqXHR, textStatus, errorThrown )
                    {
                        $("#Pag").html("<div class='text-center fw-bold text-danger'><i class='mdi mdi-alert'></i> "+ textStatus+"</div>");
                        swal.close();
                    }
                });
            }
            function Cerrar_Sesion(){
                window.location= "../index.py";
            }
       </script>
        """
        return Res
    def Get_Titulo(self,Activo):
        Menu = self.Get_Menu("")
        return "<i class='"+str(Menu[Activo]["Icono"])+"'></i> "+str(Activo)
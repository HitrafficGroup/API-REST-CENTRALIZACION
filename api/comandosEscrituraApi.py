from subprocess import run
import json
from . import conversionDatos as convertData
from . import comandosLecturaApi as apiRead
comandoBaseWrite="./ejecutable_comandos_api/Windows_winsock.exe "

def hitrafficSetTimeControlador(ip, time_zone,data):
    """ Escribe la hora de la PC en el controlador"""
    try:
        output = run(comandoBaseWrite+str(ip)+ " --sincronizar_hora_fecha "+str(time_zone), capture_output=True, timeout=10).stdout
    except:
        raise Exception('Error ejecutando comando setear hora')
    data = convertData.convertToDictHoraControlador(ip,time_zone)
    context = {
        "data":data,
        "confirmacion" : "yes",
    }
    return context

def hitrafficSetGruposControlador(ip,g1,g2,g3,g4,data):
    """ Escribe la configuracion de los grupos en el controlador """

    try:
        output = run("""{} {} --escribir_grupos {} {} {} {}""".format(comandoBaseWrite,str(ip),g1,g2,g3,g4), capture_output=True, timeout=10).stdout
    except:
        raise Exception('Error ejecutando comando escribir grupos')

    data = { ip:{"G1":g1,"G2":g2,"G3":g3,"G4":g4}}

    context = {
        "data":data,
        "confirmacion" : "yes",
    }

    return context

def hitrafficSetFasesControlador(ip,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16): 
    """ Escribe la configuracion de las fases en el controlador """

    try:
        output = run("""{} {} --escribir_fases {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}""".format(comandoBaseWrite,str(ip),f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16), capture_output=True, timeout=10).stdout
    except:
        raise Exception('Error ejecutando comando escribir fases')

    data = {ip:{"fase1":f1,"fase2":f2,"fase3":f3,"fase4":f4,"fase5":f5,"fase6":f6,"fase7":f7,"fase8":f8,"fase9":f9,"fase10":f10,"fase11":f11,"fase12":f12,"fase13":f13,"fase14":f14,"fase15":f15,"fase16":f16 }}

    context = {
        "data":data,
        "confirmacion" : "yes",
    }
  
    return context






def hitrafficSetPlanesControlador(ip,num_plan,fase1,tiempo1,fase2,tiempo2,fase3,tiempo3,fase4,tiempo4,fase5,tiempo5,fase6,tiempo6,fase7,tiempo7,fase8,tiempo8,fase9,tiempo9,fase10,tiempo10,fase11,tiempo11,fase12,tiempo12):
    """ Escribe la configuracion de los planes en el controlador, pero solo del plan seleccionado en la interfaz """

    try:
        output = run("""{} {} --escribir_plan {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}""".format(comandoBaseWrite,str(ip),num_plan,fase1,tiempo1,fase2,tiempo2,fase3,tiempo3,fase4,tiempo4,fase5,tiempo5,fase6,tiempo6,fase7,tiempo7,fase8,tiempo8,fase9,tiempo9,fase10,tiempo10,fase11,tiempo11,fase12,tiempo12), capture_output=True, timeout=30).stdout
    except:
        raise Exception('Error ejecutando comando escribir planes')

    #Conversion de los datos
    data = convertData.convertToDictPlanes(ip,num_plan,fase1,tiempo1,fase2,tiempo2,fase3,tiempo3,fase4,tiempo4,fase5,tiempo5,fase6,tiempo6,fase7,tiempo7,fase8,tiempo8,fase9,tiempo9,fase10,tiempo10,fase11,tiempo11,fase12,tiempo12)
    context = {
        "data":data,
        "confirmacion" : "yes",
    }

    return context

def hitrafficSetOtrosParamControlador(ip,time_destello_on,time_red_on,time_destello_green_p,time_destello_green_v,time_yellow_v,time_all_red,time_min_green,sincro_value):
    """ Escribe la congiguracion de parametros opertivos en el controlador """

    try:
        output = run("""{} {} --escribir_otros_parametros {} {} {} {} {} {} {} {}""".format(comandoBaseWrite,str(ip),time_destello_on,time_red_on,time_destello_green_p,time_destello_green_v,time_yellow_v,time_all_red,time_min_green,sincro_value), capture_output=True, timeout=10).stdout
    except:
        raise Exception('Error ejecutando comando escribir otros parametros')

    
    data = convertData.convertToDictOtrosParametros(ip,time_destello_on,time_red_on,time_destello_green_p,time_destello_green_v,time_yellow_v,time_all_red,time_min_green,sincro_value)

    context = {
        "data": data,
        "confirmacion" : "yes",
    }

  
    return context


def hitrafficSetHorariosControlador(ip,num_horario,hora1,minuto1,mod1,desfase1,hora2,minuto2,mod2,desfase2,hora3,minuto3,mod3,desfase3,hora4,minuto4,mod4,desfase4,hora5,minuto5,mod5,desfase5,hora6,minuto6,mod6,desfase6,hora7,minuto7,mod7,desfase7,hora8,minuto8,mod8,desfase8,hora9,minuto9,mod9,desfase9,hora10,minuto10,mod10,desfase10,hora11,minuto11,mod11,desfase11,hora12,minuto12,mod12,desfase12,hora13,minuto13,mod13,desfase13,hora14,minuto14,mod14,desfase14,hora15,minuto15,mod15,desfase15,hora16,minuto16,mod16,desfase16):
    """ Escribe la configuracion de los horarios en el controlador """
    
    try:
        output = run("""{} {} --escribir_horario {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}""".format(comandoBaseWrite,str(ip),num_horario,hora1,minuto1,mod1,desfase1,hora2,minuto2,mod2,desfase2,hora3,minuto3,mod3,desfase3,hora4,minuto4,mod4,desfase4,hora5,minuto5,mod5,desfase5,hora6,minuto6,mod6,desfase6,hora7,minuto7,mod7,desfase7,hora8,minuto8,mod8,desfase8,hora9,minuto9,mod9,desfase9,hora10,minuto10,mod10,desfase10,hora11,minuto11,mod11,desfase11,hora12,minuto12,mod12,desfase12,hora13,minuto13,mod13,desfase13,hora14,minuto14,mod14,desfase14,hora15,minuto15,mod15,desfase15,hora16,minuto16,mod16,desfase16), capture_output=True, timeout=10).stdout
    except:
        raise Exception('Error ejecutando comando escribir horarios')


    #cacheBd.procesarEscrituraHorario(ip,mac,json_data)
    data = convertData.convertToDictHorarios(ip,num_horario,hora1,minuto1,mod1,desfase1,hora2,minuto2,mod2,desfase2,hora3,minuto3,mod3,desfase3,hora4,minuto4,mod4,desfase4,hora5,minuto5,mod5,desfase5,hora6,minuto6,mod6,desfase6,hora7,minuto7,mod7,desfase7,hora8,minuto8,mod8,desfase8,hora9,minuto9,mod9,desfase9,hora10,minuto10,mod10,desfase10,hora11,minuto11,mod11,desfase11,hora12,minuto12,mod12,desfase12,hora13,minuto13,mod13,desfase13,hora14,minuto14,mod14,desfase14,hora15,minuto15,mod15,desfase15,hora16,minuto16,mod16,desfase16)
    context = {
        "data": data,
        "confirmacion" : "yes",
    }

 

    return context

def hitrafficSetDiasEspecialesControlador(ip, mac, mes1, dia1, mod1, mes2, dia2, mod2, mes3, dia3, mod3, mes4, dia4, mod4, mes5, dia5, mod5, mes6, dia6, mod6, mes7, dia7, mod7, mes8, dia8, mod8, mes9, dia9, mod9, mes10, dia10, mod10, mes11, dia11, mod11, mes12, dia12, mod12, mes13, dia13, mod13, mes14, dia14, mod14, mes15, dia15, mod15, mes16, dia16, mod16, fines_semana):
    """ Escribe la configuracion de los dias especiales en el controlador """

    try:
        output = run("""{} {} --escribir_dias_especiales {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}""".format(comandoBaseWrite,str(ip),mes1, dia1, mod1, mes2, dia2, mod2, mes3, dia3, mod3, mes4, dia4, mod4, mes5, dia5, mod5, mes6, dia6, mod6, mes7, dia7, mod7, mes8, dia8, mod8, mes9, dia9, mod9, mes10, dia10, mod10, mes11, dia11, mod11, mes12, dia12, mod12, mes13, dia13, mod13, mes14, dia14, mod14, mes15, dia15, mod15, mes16, dia16, mod16, fines_semana), capture_output=True, timeout=10).stdout
    except:
        raise Exception('Error ejecutando comando escribir dias especiales')
    
    
    data = convertData.convertToDictDiasEspeciales(ip, mes1, dia1, mod1, mes2, dia2, mod2, mes3, dia3, mod3, mes4, dia4, mod4, mes5, dia5, mod5, mes6, dia6, mod6, mes7, dia7, mod7, mes8, dia8, mod8, mes9, dia9, mod9, mes10, dia10, mod10, mes11, dia11, mod11, mes12, dia12, mod12, mes13, dia13, mod13, mes14, dia14, mod14, mes15, dia15, mod15, mes16, dia16, mod16, fines_semana)
    
    context = {
        "data": data,
        "confirmacion" : "yes",
    }


    return context


def hitrafficSetConflictoVerdesControlador(ip,fila1,fila2,fila3,check1,check2,check3):
    """ Escribe la configuracion de los conflictos en verde en el controlador """

    try:
        output = run("""{} {} --escribir_conflicto_verdes {} {} {} {} {} {}""".format(comandoBaseWrite,str(ip),fila1,fila2,fila3,check1,check2,check3), capture_output=True, timeout=10).stdout
    except:
        raise Exception('Error ejecutando comando escribir conflictos en verde')
    
    data = convertData.convertToDictConflictoVerdes(ip,fila1,fila2,fila3,check1,check2,check3)

    context = {
        "data":data,
        "confirmacion" : "yes",
    }
    return context

def hitrafficSetEntradasControlador(ip,mac,box1,fase1,tiempo1,box2,fase2,tiempo2,box3,fase3,tiempo3,box4,fase4,tiempo4):
    """ Escribe la configuracion de las entradas en el controlador """

    try:
        output = run("""{} {} --escribir_entradas {} {} {} {} {} {} {} {} {} {} {} {}""".format(comandoBaseWrite,str(ip),box1,fase1,tiempo1,box2,fase2,tiempo2,box3,fase3,tiempo3,box4,fase4,tiempo4), capture_output=True, timeout=10).stdout
    except:
        raise Exception('Error ejecutando comando escribir entradas')
    
    data = convertData.convertToDictEntradas(ip,box1,fase1,tiempo1,box2,fase2,tiempo2,box3,fase3,tiempo3,box4,fase4,tiempo4)

    context = {
        "data":data,
        "confirmacion" : "yes",
    }


    return context

def hitrafficSetRegistrosControlador(ip,observacion='undefined'):
    """ Borra todos los registros del controlador """

    try:
        output = run("""{} {} --borrar_registros""".format(comandoBaseWrite,str(ip)), capture_output=True, timeout=10).stdout
    except:
        raise Exception('Error ejecutando comando borrar registros')
    
    context = {
        "confirmacion" : "yes",
    }

    return context

def hitrafficSetBorrarErrorControlador(ip,observacion='undefined'):
    """ Elimina el error sucitado en el controlador, cumple la funcion de reset en caso de fallo presentado en el controlador """

    try:
        output = run("""{} {} --eliminar_error""".format(comandoBaseWrite,str(ip)), capture_output=True, timeout=10).stdout
    except:
        raise Exception('Error ejecutando comando eliminar error')
    
    context = {
        "confirmacion" : "yes",
    }

    return context


def hitrafficSetCambiarIpControlador(ip, nueva_ip,mac,observacion='undefined'):
    """ Realiza un cambio de IP al controlador actualmente seleccionado """

    try:
        output = run("""{} {} --cambiar_ip {} {}""".format(comandoBaseWrite,str(ip), str(nueva_ip), str(mac)), capture_output=True, timeout=20).stdout
    except:
        raise Exception('Error ejecutando comando cambiar ip')
    
    context = {
        "confirmacion" : "yes",
    }

    return context




def checkParamIsClonable(element):
    collection: iter=["grupos","fases","planes","otros_parametros","horarios","dias_especiales","conflicto_verdes","entradas","hora_controlador"]
    return element in collection   

def hitrafficClonarConfigControlador(ipSrc,macSrc,listaMacIPDestino):
    """ Realiza un cambio de IP al controlador actualmente seleccionado """

    # observacion="cloned from ",ipSrc," ",macSrc
    # observacionLecturaFromBD="leyendo parametro desde ",macSrc," para clonarlo"

    #listaMacIPDestino: [ {"ip":valor, "mac":valor},{...},{...} ]
    #--------------------------------------------------------------
    #clonar grupos
    #--------------------------------------------------------------
    ''' 
    if (checkParamIsClonable("grupos")) :
        try:
            print("----------------- clonando grupos -------------------")
            jsonValueFromBD=cacheBd.leerParametro(mac=macSrc,parametroId='grupos',observacion=observacionLecturaFromBD)
            print(jsonValueFromBD)
            #logica para mandar al controlador el parametro
            ObjGrupos = json.loads(jsonValueFromBD)
            print(ObjGrupos)
            for element in listaMacIPDestino:
                #se manda a leer para que se valide si no existe en la bd se cree 
                print(element)
                apiRead.hitrafficGetGruposControlador(element["ip"],element["mac"],observacion)
                hitrafficSetGruposControlador(element["ip"],ObjGrupos[macSrc]["G1"],ObjGrupos[macSrc]["G2"],ObjGrupos[macSrc]["G3"],ObjGrupos[macSrc]["G4"],element["mac"],observacion) 

        except Exception as e:
            print (e)
            raise Exception('Error ejecutando clonacion de grupos', e)
'''
    #--------------------------------------------------------------
    #clonar fases
    #--------------------------------------------------------------
    # if (checkParamIsClonable("fases")) :
    #     try:
    #         print("----------------- clonando fases -------------------")

    #         ObjFases = json.loads(jsonValueFromBD)
    #         print(ObjFases)
    #         for element in listaMacIPDestino:
    #             #se manda a leer para que se valide si no existe en la bd se cree 
    #             print(element)
    #             apiRead.hitrafficGetFasesControlador(element["ip"],element["mac"],observacion)
    #             hitrafficSetFasesControlador(element["ip"],ObjFases[macSrc]["fase1"],ObjFases[macSrc]["fase2"],ObjFases[macSrc]["fase3"],ObjFases[macSrc]["fase4"],ObjFases[macSrc]["fase5"],ObjFases[macSrc]["fase6"],ObjFases[macSrc]["fase7"],ObjFases[macSrc]["fase8"],ObjFases[macSrc]["fase9"],ObjFases[macSrc]["fase10"],ObjFases[macSrc]["fase11"],ObjFases[macSrc]["fase12"],ObjFases[macSrc]["fase13"],ObjFases[macSrc]["fase14"],ObjFases[macSrc]["fase15"],ObjFases[macSrc]["fase16"],element["mac"],observacion)
    #         #logica para mandar al controlador el parametro


    #     except:
    #         raise Exception('Error ejecutando clonacion de fases')


    #--------------------------------------------------------------
    #clonar planes
    #--------------------------------------------------------------
    ''' 
    if (checkParamIsClonable("planes")) :
        try:
            jsonValueFromBD=cacheBd.leerParametro(mac=macSrc,parametroId='planes',observacion=observacionLecturaFromBD)
            ObjPlanes = convertData.InvertConversionPlanes(jsonValueFromBD, macSrc)
            for element in listaMacIPDestino:
                #se manda a leer para que se valide si no existe en la bd se cree 
                apiRead.hitrafficGetPlanesControlador(element["ip"],element["mac"],observacion)
                for idx,key in enumerate(ObjPlanes):
                    #print("llave: ",key)
                    print("LLAVE: ", key)
                    hitrafficSetPlanesControlador(element["ip"],str(idx+1),ObjPlanes[key]["fase1"],ObjPlanes[key]["tiempo1"],ObjPlanes[key]["fase2"],ObjPlanes[key]["tiempo2"],ObjPlanes[key]["fase3"],ObjPlanes[key]["tiempo3"],ObjPlanes[key]["fase4"],ObjPlanes[key]["tiempo4"],ObjPlanes[key]["fase5"],ObjPlanes[key]["tiempo5"],ObjPlanes[key]["fase6"],ObjPlanes[key]["tiempo6"],ObjPlanes[key]["fase7"],ObjPlanes[key]["tiempo7"],ObjPlanes[key]["fase8"],ObjPlanes[key]["tiempo8"],ObjPlanes[key]["fase9"],ObjPlanes[key]["tiempo9"],ObjPlanes[key]["fase10"],ObjPlanes[key]["tiempo10"],ObjPlanes[key]["fase11"],ObjPlanes[key]["tiempo11"],ObjPlanes[key]["fase12"],ObjPlanes[key]["tiempo12"],element["mac"],observacion)
            #logica para mandar al controlador el parametro

        except:
            raise Exception('Error ejecutando clonacion de planes')


    #--------------------------------------------------------------
    #clonar otros parametros
    #--------------------------------------------------------------
    if (checkParamIsClonable("otros_parametros")) :
        try:
            jsonValueFromBD=cacheBd.leerParametro(mac=macSrc,parametroId='otros_parametros',observacion=observacionLecturaFromBD)
            ObjOtrosParametros = convertData.InvertConversionOtrosParametros(jsonValueFromBD,macSrc)
            for element in listaMacIPDestino:
                #se manda a leer para que se valide si no existe en la bd se cree 
                apiRead.hitrafficGetOtrosParamControlador(element["ip"],element["mac"],observacion)
                hitrafficSetOtrosParamControlador(element["ip"],element["mac"],ObjOtrosParametros["time_destello_on"],ObjOtrosParametros["time_red_on"],ObjOtrosParametros["time_destello_green_p"],ObjOtrosParametros["time_destello_green_v"],ObjOtrosParametros["time_yellow_v"],ObjOtrosParametros["time_all_red"],ObjOtrosParametros["time_min_green"],ObjOtrosParametros["sincro_value"],observacion)
        except:
            raise Exception('Error ejecutando clonacion de otros parametros')

    #--------------------------------------------------------------
    #clonar horarios
    #--------------------------------------------------------------
    if (checkParamIsClonable("horarios")) :
        try:
            jsonValueFromBD=cacheBd.leerParametro(mac=macSrc,parametroId='horarios',observacion=observacionLecturaFromBD)
            ObjHorarios = convertData.InvertConversionHorarios(jsonValueFromBD, macSrc)
            for element in listaMacIPDestino:
                #se manda a leer para que se valide si no existe en la bd se cree 
                apiRead.hitrafficGetHorariosControlador(element["ip"],element["mac"],('red ',observacion))
                for idx,key in enumerate(ObjHorarios):
                    hitrafficSetHorariosControlador(element["mac"],element["ip"],str(idx),ObjHorarios[key]["hora1"],ObjHorarios[key]["minuto1"],ObjHorarios[key]["mod1"],ObjHorarios[key]["desfase1"],ObjHorarios[key]["hora2"],ObjHorarios[key]["minuto2"],ObjHorarios[key]["mod2"],ObjHorarios[key]["desfase2"],ObjHorarios[key]["hora3"],ObjHorarios[key]["minuto3"],ObjHorarios[key]["mod3"],ObjHorarios[key]["desfase3"],ObjHorarios[key]["hora4"],ObjHorarios[key]["minuto4"],ObjHorarios[key]["mod4"],ObjHorarios[key]["desfase4"],ObjHorarios[key]["hora5"],ObjHorarios[key]["minuto5"],ObjHorarios[key]["mod5"],ObjHorarios[key]["desfase5"],ObjHorarios[key]["hora6"],ObjHorarios[key]["minuto6"],ObjHorarios[key]["mod6"],ObjHorarios[key]["desfase6"],ObjHorarios[key]["hora7"],ObjHorarios[key]["minuto7"],ObjHorarios[key]["mod7"],ObjHorarios[key]["desfase7"],ObjHorarios[key]["hora8"],ObjHorarios[key]["minuto8"],ObjHorarios[key]["mod8"],ObjHorarios[key]["desfase8"],ObjHorarios[key]["hora9"],ObjHorarios[key]["minuto9"],ObjHorarios[key]["mod9"],ObjHorarios[key]["desfase9"],ObjHorarios[key]["hora10"],ObjHorarios[key]["minuto10"],ObjHorarios[key]["mod10"],ObjHorarios[key]["desfase10"],ObjHorarios[key]["hora11"],ObjHorarios[key]["minuto11"],ObjHorarios[key]["mod11"],ObjHorarios[key]["desfase11"],ObjHorarios[key]["hora12"],ObjHorarios[key]["minuto12"],ObjHorarios[key]["mod12"],ObjHorarios[key]["desfase12"],ObjHorarios[key]["hora13"],ObjHorarios[key]["minuto13"],ObjHorarios[key]["mod13"],ObjHorarios[key]["desfase13"],ObjHorarios[key]["hora14"],ObjHorarios[key]["minuto14"],ObjHorarios[key]["mod14"],ObjHorarios[key]["desfase14"],ObjHorarios[key]["hora15"],ObjHorarios[key]["minuto15"],ObjHorarios[key]["mod15"],ObjHorarios[key]["desfase15"],ObjHorarios[key]["hora16"],ObjHorarios[key]["minuto16"],ObjHorarios[key]["mod16"],ObjHorarios[key]["desfase16"],observacion)
            #logica para mandar al controlador el parametro

        except:
            raise Exception('Error ejecutando clonacion de horarios')


    #--------------------------------------------------------------
    #clonar dias especiales
    #--------------------------------------------------------------
    if (checkParamIsClonable("dias_especiales")) :
        try:
            jsonValueFromBD=cacheBd.leerParametro(mac=macSrc,parametroId='dias_especiales',observacion=observacionLecturaFromBD)
            ObjDiasEspeciales = convertData.InvertConversionDiasEspeciales(jsonValueFromBD,macSrc)
            #print(ObjDiasEspeciales)
            for element in listaMacIPDestino:
                #se manda a leer para que se valide si no existe en la bd se cree 
                apiRead.hitrafficGetDiasEspecialesControlador(element["ip"],element["mac"],observacion)
                hitrafficSetDiasEspecialesControlador(element["ip"], element["mac"], ObjDiasEspeciales["dias_festivos"]["mes1"], ObjDiasEspeciales["dias_festivos"]["dia1"], ObjDiasEspeciales["dias_festivos"]["mod1"], ObjDiasEspeciales["dias_festivos"]["mes2"], ObjDiasEspeciales["dias_festivos"]["dia2"], ObjDiasEspeciales["dias_festivos"]["mod2"], ObjDiasEspeciales["dias_festivos"]["mes3"], ObjDiasEspeciales["dias_festivos"]["dia3"], ObjDiasEspeciales["dias_festivos"]["mod3"], ObjDiasEspeciales["dias_festivos"]["mes4"], ObjDiasEspeciales["dias_festivos"]["dia4"], ObjDiasEspeciales["dias_festivos"]["mod4"], ObjDiasEspeciales["dias_festivos"]["mes5"], ObjDiasEspeciales["dias_festivos"]["dia5"], ObjDiasEspeciales["dias_festivos"]["mod5"], ObjDiasEspeciales["dias_festivos"]["mes6"], ObjDiasEspeciales["dias_festivos"]["dia6"], ObjDiasEspeciales["dias_festivos"]["mod6"], ObjDiasEspeciales["dias_festivos"]["mes7"], ObjDiasEspeciales["dias_festivos"]["dia7"], ObjDiasEspeciales["dias_festivos"]["mod7"], ObjDiasEspeciales["dias_festivos"]["mes8"], ObjDiasEspeciales["dias_festivos"]["dia8"], ObjDiasEspeciales["dias_festivos"]["mod8"], ObjDiasEspeciales["dias_festivos"]["mes9"], ObjDiasEspeciales["dias_festivos"]["dia9"], ObjDiasEspeciales["dias_festivos"]["mod9"], ObjDiasEspeciales["dias_festivos"]["mes10"], ObjDiasEspeciales["dias_festivos"]["dia10"], ObjDiasEspeciales["dias_festivos"]["mod10"], ObjDiasEspeciales["dias_festivos"]["mes11"], ObjDiasEspeciales["dias_festivos"]["dia11"], ObjDiasEspeciales["dias_festivos"]["mod11"], ObjDiasEspeciales["dias_festivos"]["mes12"], ObjDiasEspeciales["dias_festivos"]["dia12"], ObjDiasEspeciales["dias_festivos"]["mod12"], ObjDiasEspeciales["dias_festivos"]["mes13"], ObjDiasEspeciales["dias_festivos"]["dia13"], ObjDiasEspeciales["dias_festivos"]["mod13"], ObjDiasEspeciales["dias_festivos"]["mes14"], ObjDiasEspeciales["dias_festivos"]["dia14"], ObjDiasEspeciales["dias_festivos"]["mod14"], ObjDiasEspeciales["dias_festivos"]["mes15"], ObjDiasEspeciales["dias_festivos"]["dia15"], ObjDiasEspeciales["dias_festivos"]["mod15"], ObjDiasEspeciales["dias_festivos"]["mes16"], ObjDiasEspeciales["dias_festivos"]["dia16"], ObjDiasEspeciales["dias_festivos"]["mod16"], ObjDiasEspeciales["fines_semana"],observacion)

        except:
            raise Exception('Error ejecutando clonacion de dias especiales')  

    
    #--------------------------------------------------------------
    #clonar conflictos en verde
    #--------------------------------------------------------------

    if (checkParamIsClonable("conflicto_verdes")) :
        try:
            jsonValueFromBD=cacheBd.leerParametro(mac=macSrc,parametroId='conflicto_verdes',observacion=observacionLecturaFromBD)
            ObjConflictosVerde = convertData.InvertConversionConflictoVerdes(jsonValueFromBD,macSrc)
            for element in listaMacIPDestino:
                #se manda a leer para que se valide si no existe en la bd se cree 
                apiRead.hitrafficGetConflictoVerdesControlador(element["ip"],element["mac"],observacion)
                hitrafficSetConflictoVerdesControlador(element["ip"],element["mac"],ObjConflictosVerde["fila1"],ObjConflictosVerde["fila2"],ObjConflictosVerde["fila3"],ObjConflictosVerde["check1"],ObjConflictosVerde["check2"],ObjConflictosVerde["check3"],observacion)


        except:
            raise Exception('Error ejecutando clonacion de conflicto verdes')  


    #--------------------------------------------------------------
    #clonar sincronizacion tiempo
    #--------------------------------------------------------------
    if (checkParamIsClonable("hora_controlador")) :
        try:
            
            jsonValueFromBD=cacheBd.leerParametro(mac=macSrc,parametroId='hora_controlador',observacion=observacionLecturaFromBD)
            diccionario_hora = json.loads(jsonValueFromBD)
            for element in listaMacIPDestino:
                #se manda a leer para que se valide si no existe en la bd se cree 
                apiRead.hitrafficGetTimeControlador(element["ip"],element["mac"],observacion)
                hitrafficSetTimeControlador(element["ip"], diccionario_hora[macSrc]["time_zone"] ,element["mac"],observacion)
        except:
            raise Exception('Error ejecutando clonacion de sincronizacion tiempo')  

    
    #--------------------------------------------------------------
    #clonar entradas
    #--------------------------------------------------------------
    if (checkParamIsClonable("entradas")) :
        try:
            
            jsonValueFromBD=cacheBd.leerParametro(mac=macSrc,parametroId='entradas',observacion=observacionLecturaFromBD)
            diccionario_entradas = json.loads(jsonValueFromBD)
            for element in listaMacIPDestino:
                #se manda a leer para que se valide si no existe en la bd se cree 
                apiRead.hitrafficGetEntradasControlador(element["ip"],element["mac"],observacion)
                hitrafficSetEntradasControlador(element["ip"],element["mac"],diccionario_entradas[macSrc]["entrada1"]["checkbox"],diccionario_entradas[macSrc]["entrada1"]["fase"],diccionario_entradas[macSrc]["entrada1"]["tiempo"],diccionario_entradas[macSrc]["entrada2"]["checkbox"],diccionario_entradas[macSrc]["entrada2"]["fase"],diccionario_entradas[macSrc]["entrada2"]["tiempo"],diccionario_entradas[macSrc]["entrada3"]["checkbox"],diccionario_entradas[macSrc]["entrada3"]["fase"],diccionario_entradas[macSrc]["entrada3"]["tiempo"],diccionario_entradas[macSrc]["entrada4"]["checkbox"],diccionario_entradas[macSrc]["entrada4"]["fase"],diccionario_entradas[macSrc]["entrada4"]["tiempo"],observacion)

        except:
            raise Exception('Error ejecutando clonacion de entradas')
'''

    context = {
        "confirmacion" : "yes",
    }
    
    return context
 

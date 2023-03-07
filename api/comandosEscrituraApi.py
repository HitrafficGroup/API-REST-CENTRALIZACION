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

def hitrafficSetFasesControlador(ip,_data): 
    """ Escribe la configuracion de las fases en el controlador """

    try:
        output = run("""{} {} --escribir_fases {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}""".format(comandoBaseWrite,str(ip),_data['fase1'],_data['fase2'],_data['fase3'],_data['fase4'],_data['fase5'],_data['fase6'],_data['fase7'],_data['fase8'],_data['fase9'],_data['fase10'],_data['fase11'],_data['fase12'],_data['fase13'],_data['fase14'],_data['fase15'],_data['fase16']), capture_output=True, timeout=10).stdout
    except:
        raise Exception('Error ejecutando comando escribir fases')

    data = {ip:{"fase1":_data['fase1'],"fase2":_data['fase2'],"fase3":_data['fase3'],"fase4":_data['fase4'],"fase5":_data['fase5'],"fase6":_data['fase6'],"fase7":_data['fase7'],"fase8":_data['fase8'],"fase9":_data['fase9'],"fase10":_data['fase10'],"fase11":_data['fase11'],"fase12":_data['fase12'],"fase13":_data['fase13'],"fase14":_data['fase14'],"fase15":_data['fase15'],"fase16":_data['fase16'] }}

    context = {
        "data":data,
        "confirmacion" : "yes",
    }
  
    return context






def hitrafficSetPlanesControlador(ip,_data):
    """ Escribe la configuracion de los planes en el controlador, pero solo del plan seleccionado en la interfaz """

    try:
        output = run("""{} {} --escribir_plan {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}""".format(comandoBaseWrite,str(ip),_data['num_plan'],_data['data0'],_data['data1'],_data['data2'],_data['data3'],_data['data4'],_data['data5'],_data['data6'],_data['data7'],_data['data8'],_data['data9'],_data['data10'],_data['data11'],_data['data12'],_data['data13'],_data['data14'],_data['data15'],_data['data16'],_data['data17'],_data['data18'],_data['data19'],_data['data20'],_data['data21'],_data['data22'],_data['data23']), capture_output=True, timeout=30).stdout
    except:
        raise Exception('Error ejecutando comando escribir planes')

    data = convertData.convertToDictPlanes(ip,_data['num_plan'],_data['data0'],_data['data1'],_data['data2'],_data['data3'],_data['data4'],_data['data5'],_data['data6'],_data['data7'],_data['data8'],_data['data9'],_data['data10'],_data['data11'],_data['data12'],_data['data13'],_data['data14'],_data['data15'],_data['data16'],_data['data17'],_data['data18'],_data['data19'],_data['data20'],_data['data21'],_data['data22'],_data['data23'])
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


def hitrafficSetHorariosControlador(ip,_data):
    """ Escribe la configuracion de los horarios en el controlador """
    
    try:
        output = run("""{} {} --escribir_horario {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}""".format(comandoBaseWrite,str(ip),_data['num_horario'],_data['hora1'],_data['minuto1'],_data['mod_plan1'],_data['desfase1'],_data['hora2'],_data['minuto2'],_data['mod_plan2'],_data['desfase2'],_data['hora3'],_data['minuto3'],_data['mod_plan3'],_data['desfase3'],_data['hora4'],['minuto4'],_data['mod_plan4'],_data['desfase4'],_data['hora5'],_data['minuto5'],_data['mod_plan5'],_data['desfase5'],_data['hora6'],_data['minuto6'],_data['mod_plan6'],_data['desfase6'],_data['hora7'],_data['minuto7'],_data['mod_plan7'],_data['desfase7'],_data['hora8'],_data['minuto8'],_data['mod_plan8'],_data['desfase8'],_data['hora9'],_data['minuto9'],_data['mod_plan9'],_data['desfase9'],_data['hora10'],_data['minuto10'],_data['mod_plan10'],_data['desfase10'],_data['hora11'],_data['minuto11'],_data['mod_plan11'],_data['desfase11'],_data['hora12'],_data['minuto12'],_data['mod_plan12'],_data['desfase12'],_data['hora13'],_data['minuto13'],_data['mod_plan13'],_data['desfase13'],_data['hora14'],_data['minuto14'],_data['mod_plan14'],_data['desfase14'],_data['hora15'],_data['minuto15'],_data['mod_plan15'],_data['desfase15'],_data['hora16'],_data['minuto16'],_data['mod_plan16'],_data['desfase16']), capture_output=True, timeout=10).stdout
    except:
        raise Exception('Error ejecutando comando escribir horarios')

    data = convertData.convertToDictHorarios(ip,_data['num_horario'],_data['hora1'],_data['minuto1'],_data['mod_plan1'],_data['desfase1'],_data['hora2'],_data['minuto2'],_data['mod_plan2'],_data['desfase2'],_data['hora3'],_data['minuto3'],_data['mod_plan3'],_data['desfase3'],_data['hora4'],['minuto4'],_data['mod_plan4'],_data['desfase4'],_data['hora5'],_data['minuto5'],_data['mod_plan5'],_data['desfase5'],_data['hora6'],_data['minuto6'],_data['mod_plan6'],_data['desfase6'],_data['hora7'],_data['minuto7'],_data['mod_plan7'],_data['desfase7'],_data['hora8'],_data['minuto8'],_data['mod_plan8'],_data['desfase8'],_data['hora9'],_data['minuto9'],_data['mod_plan9'],_data['desfase9'],_data['hora10'],_data['minuto10'],_data['mod_plan10'],_data['desfase10'],_data['hora11'],_data['minuto11'],_data['mod_plan11'],_data['desfase11'],_data['hora12'],_data['minuto12'],_data['mod_plan12'],_data['desfase12'],_data['hora13'],_data['minuto13'],_data['mod_plan13'],_data['desfase13'],_data['hora14'],_data['minuto14'],_data['mod_plan14'],_data['desfase14'],_data['hora15'],_data['minuto15'],_data['mod_plan15'],_data['desfase15'],_data['hora16'],_data['minuto16'],_data['mod_plan16'],_data['desfase16'])
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

def hitrafficClonarConfigControlador(ipSrc,macSrc,listaMacIPDestino,planSrc,horarioSrc,faseSrc):
    """ Realiza la clonacion de planes horarios """
    ##print(planSrc)
    # for x in planSrc:
    #     print(x)
    #     print('\n')
    for i in listaMacIPDestino:
        ip_target = i['ip']
        print(ip_target)
        # operacion de grabado de fases

        for key,value in horarioSrc.items():
            print(key)
            if key == 'dia_ordinario':
                value['num_horario'] = "0"
                value['ip'] = ip_target
            elif key =='dia_festivo':
                value['num_horario'] = "2"
                value['ip'] = ip_target
            else:
                value['num_horario'] = "1"
                value['ip'] = ip_target
            print(value)
            print('\n')
            hitrafficSetHorariosControlador(ip_target,value);
        for x in planSrc:
            x['ip'] = ip_target
            if x['clonable']:
                print(x)
                print('\n')
                hitrafficSetPlanesControlador(ip_target,x)

    

    context = {
        "confirmacion" : "yes",
    }
    
    return context
 

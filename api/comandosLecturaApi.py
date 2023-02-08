
from subprocess import run
import json


comandoBaseRead="./ejecutable_comandos_api/Windows_winsock.exe "
def hitrafficListarIps():
    """ Lista todas las ips disponibles para la conexion """
    try:
        output = run(comandoBaseRead+"--buscar_ip .", capture_output=True, timeout=20).stdout
        #print(output)
    except Exception as error:
        raise Exception('Error ejecutando comando buscar ip'+str(error))

    try:
        ips_disponibles = json.loads(output)
        #print(ips_disponibles)

    except Exception as error:
        raise Exception('Error cargando ips a json: '+str(error))
    return ips_disponibles



def hitrafficGetTimeControlador(ip,mac):
    """ Obtiene la hora del controlador """
    try:
        output = run(comandoBaseRead+str(ip)+ " --leer_hora_controlador", capture_output=True, timeout=20).stdout
    except:
        raise Exception('Error ejecutando comando leer hora controlador')

    try:
        jsonResponse = json.loads(output)
    except:
        raise Exception('Error cargando todo a json')

    context = {
        getJsonId(ip,mac) : hitrafficPrepareResponseJsonSingleRead(ip,mac, jsonResponse) 
    }


    return context

def hitrafficGetGruposControlador(ip,mac):
    """ Obtiene la configuracion de los grupos del controlador """
    try:
        output = run(comandoBaseRead+str(ip)+ " --leer_grupos", capture_output=True, timeout=10).stdout
    except Exception as e:
        raise Exception('Error ejecutando comando leer grupos de ip',ip,' ',e)

    try:
        jsonResponse = json.loads(output)
    except:
        raise Exception('Error cargando todo a json')

    context = {
        getJsonId(ip,mac) : hitrafficPrepareResponseJsonSingleRead(ip,mac, jsonResponse) 
    }
    return context


def hitrafficGetFasesControlador(ip,mac):
    """ Obtiene la configuracion de las fases del controlador """
    try:
        output = run(comandoBaseRead+str(ip)+" --leer_fases", capture_output=True, timeout=10).stdout
    except:
        raise Exception('Error ejecutando comando leer grupos')

    try:
        jsonResponse = json.loads(output)
    except:
        raise Exception('Error cargando todo a json')

    context = {
        getJsonId(ip,mac) : hitrafficPrepareResponseJsonSingleRead(ip,mac, jsonResponse) 
    }
    print("no se ejecuta de aqui abajo")
  

    return context

def hitrafficGetPlanesControlador(ip,mac):

    """ Obtiene la configuracion de todos los 16 planes del controlador, independientemente del valor del selector """
    try:
        output = run(comandoBaseRead+str(ip)+" --leer_planes", capture_output=True, timeout=120).stdout
    except:
        raise Exception('Error ejecutando comando leer planes')

    try:
        jsonResponse = json.loads(output)
    except:
        raise Exception('Error cargando todo a json')

    context = {
        getJsonId(ip,mac) : hitrafficPrepareResponseJsonSingleRead(ip,mac, jsonResponse) 
    }

   

    return context

def hitrafficGetOtrosParamControlador(ip,mac):

    """ Obtiene la configuracion de todos los parametros operativos del controlador"""
    try:
        output = run(comandoBaseRead+str(ip)+" --leer_otros_parametros", capture_output=True, timeout=10).stdout
    except:
        raise Exception('Error ejecutando comando leer otros parametros')

    try:
        jsonResponse = json.loads(output)
    except:
        raise Exception('Error cargando todo a json')

    context = {
        getJsonId(ip,mac) : hitrafficPrepareResponseJsonSingleRead(ip,mac, jsonResponse) 
    }

    return context


def hitrafficGetHorariosControlador(ip,mac):
    """ Obtiene la configuracion de los horarios del controlador"""

    try:
        output = run(comandoBaseRead+str(ip)+" --leer_horarios", capture_output=True, timeout=25).stdout
    except:
        raise Exception('Error ejecutando comando leer horarios')

    try:
        jsonResponse = json.loads(output)
    except:
        raise Exception('Error cargando todo a json')

    context = {
        getJsonId(ip,mac) : hitrafficPrepareResponseJsonSingleRead(ip,mac, jsonResponse) 
    }


    return context

def hitrafficGetDiasEspecialesControlador(ip,mac):
    """ Obtiene la definicion de fin de semana del controlador y los dias especiales programados """

    try:
        output = run(comandoBaseRead+str(ip)+" --leer_dias_especiales", capture_output=True, timeout=15).stdout
    except:
        raise Exception('Error ejecutando comando leer dias especiales')

    try:
        jsonResponse = json.loads(output)
    except:
        raise Exception('Error cargando todo a json')

    context = {
        getJsonId(ip,mac) : hitrafficPrepareResponseJsonSingleRead(ip,mac, jsonResponse) 
    }

    return context

def hitrafficGetConflictoVerdesControlador(ip,mac):
    """ Obtiene la configuracion de conflicto en verdes del controlador """

    try:
        output = run(comandoBaseRead+str(ip)+" --leer_conflicto_verdes", capture_output=True, timeout=15).stdout
    except:
        raise Exception('Error ejecutando comando leer conflicto verdes')

    try:
        jsonResponse = json.loads(output)
    except:
        raise Exception('Error cargando todo a json')

    context = {
        getJsonId(ip,mac) : hitrafficPrepareResponseJsonSingleRead(ip,mac, jsonResponse) 
    }

    return context

def hitrafficGetEntradasControlador(ip,mac):
    """ Obtiene la configuracion de las entradas digitales del controlador """

    try:
        output = run(comandoBaseRead+str(ip)+" --leer_entradas", capture_output=True, timeout=10).stdout
    except:
        raise Exception('Error ejecutando comando leer entradas')

    try:
        jsonResponse = json.loads(output)
    except:
        raise Exception('Error cargando todo a json')

    context = {
        getJsonId(ip,mac) :hitrafficPrepareResponseJsonSingleRead(ip,mac, jsonResponse) 
        ,"srcDatos":"controller"
    }

    return context


def hitrafficGetRegistrosControlador(ip,mac, pagina):
    """ Obtiene los registros de errores del controlador """

    try:
        output = run(comandoBaseRead+str(ip)+" --leer_registro_errores " +str(pagina), capture_output=True, timeout=10).stdout
        
    except:
        raise Exception('Error ejecutando comando leer registro errores')

    try:
        jsonResponse = json.loads(output)
    except:
        raise Exception('Error cargando todo a json')
        
    context = {
        getJsonId(ip,mac) : hitrafficPrepareResponseJsonSingleRead(ip,mac, jsonResponse) 
    }

    return context

def hitrafficGetVersionFirmware(ip,mac):
    """ Obtiene la version Firmware del controlador """

    try:
        output = run(comandoBaseRead+str(ip)+" --leer_version", capture_output=True, timeout=10).stdout
    except:
        raise Exception('Error ejecutando comando leer version')

    try:
        jsonResponse = json.loads(output)
    except:
        raise Exception('Error cargando todo a json')

    context = {
        getJsonId(ip,mac) : hitrafficPrepareResponseJsonSingleRead(ip,mac, jsonResponse) 
    }

    
        
    return context
    

def getJsonId(ip,mac):
    return mac

def hitrafficPrepareResponseJsonSingleRead(ip,mac, json):
    json= json[ip]
    
    return json

def hitrafficPrepareResponseJsonAllRead(ip,mac, json):

    json=json[ip]
    #si el id es la ip pasa directamente
    if getJsonId(ip,mac)==ip:
        return json

    #se reemplazan los campos q contienen la ip por la mac
    camposACambiar = ["hora_controlador", "fases","grupos","planes","otros_parametros","conflicto_verdes","dias_especiales","entradas","version","runtime","horarios"]
    for f in camposACambiar:
        aux1= json [f][ip] 
        del json [f][ip]
        json [f][mac]=aux1


    return json





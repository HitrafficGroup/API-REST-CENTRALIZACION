from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .comandosLecturaApi import *
from .comandosEscrituraApi import *
from django.http import JsonResponse


''' Operaciones de lectura de los controladores ,
estas funciones netamente van a leer los datos y 
los enviara a nuestra aplicacion cliente'''

class ListarIpsControlador(APIView):
    ''' Funcion encargada de listar todos mis controladores que esten en red'''
    def get(self, request, *args, **kwargs):
        result = hitrafficListarIps()
        print(result)
        return Response(result,status=status.HTTP_200_OK)


class restGetTimeControlador(APIView):
    def get(self, request, *args, **kwargs):
        mac=request.GET.get('mac')
        ip=request.GET.get('ip')
        result = hitrafficGetTimeControlador(ip,mac)
    
        return Response(result,status=status.HTTP_200_OK)

class restGetGruposControlador(APIView):
    def get(self, request, *args, **kwargs):
        mac=request.GET.get('mac')
        ip=request.GET.get('ip')
        result = hitrafficGetGruposControlador(ip,mac)
        return Response(result,status=status.HTTP_200_OK)

class restGetFasesControlador(APIView):
    def get(self, request, *args, **kwargs):
        mac=request.GET.get('mac')
        ip=request.GET.get('ip')
        result = hitrafficGetFasesControlador(ip,mac)
        return Response(result,status=status.HTTP_200_OK)


class restGetPlanesControlador(APIView):
    def get(self, request, *args, **kwargs):
        mac=request.GET.get('mac')
        ip=request.GET.get('ip')
        result =  hitrafficGetPlanesControlador(ip,mac)
        return Response(result,status=status.HTTP_200_OK)


class restGetOtrosParamControlador(APIView):
    def get(self, request, *args, **kwargs):
        mac=request.GET.get('mac')
        ip=request.GET.get('ip')
        result = hitrafficGetOtrosParamControlador(ip,mac)
        return Response(result,status=status.HTTP_200_OK)

class restGetHorariosControlador(APIView):
    def get(self, request, *args, **kwargs):
        mac=request.GET.get('mac')
        ip=request.GET.get('ip')
        result =  hitrafficGetHorariosControlador(ip,mac)
        return Response(result,status=status.HTTP_200_OK)

class restGetDiasEspecialesControlador(APIView):
    def get(self, request, *args, **kwargs):
        mac=request.GET.get('mac')
        ip=request.GET.get('ip')
        result = hitrafficGetDiasEspecialesControlador(ip,mac)
        return Response(result,status=status.HTTP_200_OK)

class restGetConflictoVerdesControlador(APIView):
    def get(self, request, *args, **kwargs):
        mac=request.GET.get('mac')
        ip=request.GET.get('ip')
        result = hitrafficGetConflictoVerdesControlador(ip,mac)
        return Response(result,status=status.HTTP_200_OK)

class restGetEntradasControlador(APIView):
    def get(self, request, *args, **kwargs):
        mac=request.GET.get('mac')
        ip=request.GET.get('ip')
        result = hitrafficGetEntradasControlador(ip,mac)
        return Response(result,status=status.HTTP_200_OK)

class  restGetRegistrosControlador(APIView):
    def get(self, request, *args, **kwargs):
        mac=request.GET.get('mac')
        ip=request.GET.get('ip')
        pagina=request.GET.get('pg')
        result =  hitrafficGetRegistrosControlador(ip,mac, pagina)
        return Response(result,status=status.HTTP_200_OK)

class  restGetVersionFirmware(APIView):
    def get(self, request, *args, **kwargs):
        mac=request.GET.get('mac')
        ip=request.GET.get('ip')
        result = hitrafficGetVersionFirmware(ip,mac)
        return Response(result,status=status.HTTP_200_OK)


''' Operaciones de Escritura de los controladores ,
estas funciones netamente van a leer los datos y 
los enviara a nuestra aplicacion cliente'''


class restSetTimeControlador(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip') 
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        time_zone = json_data["time_zone"]
        result = hitrafficSetTimeControlador(ip,time_zone,json_data)
        return Response(result,status=status.HTTP_200_OK)


class restSetGruposControlador(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        g1 = json_data["g1"]
        g2 = json_data["g2"]
        g3 = json_data["g3"]
        g4 = json_data["g4"]
        
    
        result = hitrafficSetGruposControlador(ip,g1,g2,g3,g4,json_data)
        return Response(result,status=status.HTTP_200_OK)

class restSetConflictoVerdesControlador(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        fila1 = json_data["fila1"]
        fila2 = json_data["fila2"]
        fila3 = json_data["fila3"]
        check1 = json_data["check1"]
        check2 = json_data["check2"]
        check3 = json_data["check3"]

        result = hitrafficSetConflictoVerdesControlador(ip,fila1,fila2,fila3,check1,check2,check3)
        return Response(result,status=status.HTTP_200_OK)

class restSetFasesControlador(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        result = hitrafficSetFasesControlador(ip,json_data)
        return Response(result,status=status.HTTP_200_OK)

class  restSetPlanesControlador(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
   
      
        result = hitrafficSetPlanesControlador(ip,json_data)
        
        return Response(result,status=status.HTTP_200_OK)

class  restSetOtrosParamControlador(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        time_destello_on = json_data["tiempo_destello_prender"]
        time_red_on = json_data["tiempo_rojo_prender"]
        time_destello_green_p = json_data["destellar_verde_peatonal"]
        time_destello_green_v = json_data["destellar_verde_vehicular"]
        time_yellow_v = json_data["tiempo_amarillo_vehicular"]
        time_all_red = json_data["tiempo_todo_rojo"]
        time_min_green = json_data["time_min_green"]
        sincro_value = json_data["valor_sincronizacion"]

        result = hitrafficSetOtrosParamControlador(ip,time_destello_on,time_red_on,time_destello_green_p,time_destello_green_v,time_yellow_v,time_all_red,time_min_green,sincro_value)
        return Response(result,status=status.HTTP_200_OK)

class  restSetHorariosControlador(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
     
        result = hitrafficSetHorariosControlador(ip,json_data)
        return Response(result,status=status.HTTP_200_OK)


class  restSetDiasEspecialesControlador(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        print(json_data)
        ip = json_data["ip"]
        fines_semana = json_data["fines_semana"]
        mac = json_data["mac"]
        mes1 = json_data["mes1"]
        dia1 = json_data["dia1"]
        mod1 = json_data["mod1"]
        mes2 = json_data["mes2"]
        dia2 = json_data["dia2"]
        mod2 = json_data["mod2"]
        mes3 = json_data["mes3"]
        dia3 = json_data["dia3"]
        mod3 = json_data["mod3"]
        mes4 = json_data["mes4"]
        dia4 = json_data["dia4"]
        mod4 = json_data["mod4"]
        mes5 = json_data["mes5"]
        dia5 = json_data["dia5"]
        mod5 = json_data["mod5"]
        mes6 = json_data["mes6"]
        dia6 = json_data["dia6"]
        mod6 = json_data["mod6"]
        mes7 = json_data["mes7"]
        dia7 = json_data["dia7"]
        mod7 = json_data["mod7"]
        mes8 = json_data["mes8"]
        dia8 = json_data["dia8"]
        mod8 = json_data["mod8"]
        mes9 = json_data["mes9"]
        dia9 = json_data["dia9"]
        mod9 = json_data["mod9"]
        mes10 = json_data["mes10"]
        dia10 = json_data["dia10"]
        mod10 = json_data["mod10"]
        mes11 = json_data["mes11"]
        dia11 = json_data["dia11"]
        mod11 = json_data["mod11"]
        mes12 = json_data["mes12"]
        dia12 = json_data["dia12"]
        mod12 = json_data["mod12"]
        mes13 = json_data["mes13"]
        dia13 = json_data["dia13"]
        mod13 = json_data["mod13"]
        mes14 = json_data["mes14"]
        dia14 = json_data["dia14"]
        mod14 = json_data["mod14"]
        mes15 = json_data["mes15"]
        dia15 = json_data["dia15"]
        mod15 = json_data["mod15"]
        mes16 = json_data["mes16"]
        dia16 = json_data["dia16"]
        mod16 = json_data["mod16"]
        result = hitrafficSetDiasEspecialesControlador(ip, mac, mes1, dia1, mod1, mes2, dia2, mod2, mes3, dia3, mod3, mes4, dia4, mod4, mes5, dia5, mod5, mes6, dia6, mod6, mes7, dia7, mod7, mes8, dia8, mod8, mes9, dia9, mod9, mes10, dia10, mod10, mes11, dia11, mod11, mes12, dia12, mod12, mes13, dia13, mod13, mes14, dia14, mod14, mes15, dia15, mod15, mes16, dia16, mod16, fines_semana)
        return Response(result,status=status.HTTP_200_OK)

class  restSetEntradasControlador(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        mac = json_data["mac"]
        box1 = json_data["box1"]
        fase1 = json_data["fase1"]
        tiempo1 = json_data["tiempo1"]
        box2 = json_data["box2"]
        fase2 = json_data["fase2"]
        tiempo2 = json_data["tiempo2"]
        box3 = json_data["box3"]
        fase3 = json_data["fase3"]
        tiempo3 = json_data["tiempo3"]
        box4 = json_data["box4"]
        fase4 = json_data["fase4"]
        tiempo4 = json_data["tiempo4"]
        result = hitrafficSetEntradasControlador(ip,mac,box1,fase1,tiempo1,box2,fase2,tiempo2,box3,fase3,tiempo3,box4,fase4,tiempo4)
        return Response(result,status=status.HTTP_200_OK)

class  restSetEntradasControlador(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        mac = json_data["mac"]
        box1 = json_data["box1"]
        fase1 = json_data["fase1"]
        tiempo1 = json_data["tiempo1"]
        box2 = json_data["box2"]
        fase2 = json_data["fase2"]
        tiempo2 = json_data["tiempo2"]
        box3 = json_data["box3"]
        fase3 = json_data["fase3"]
        tiempo3 = json_data["tiempo3"]
        box4 = json_data["box4"]
        fase4 = json_data["fase4"]
        tiempo4 = json_data["tiempo4"]
        result = hitrafficSetEntradasControlador(ip,mac,box1,fase1,tiempo1,box2,fase2,tiempo2,box3,fase3,tiempo3,box4,fase4,tiempo4)
        return Response(result,status=status.HTTP_200_OK)

class  restSetRegistrosControlador(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        result = hitrafficSetRegistrosControlador(ip)
        return Response(result,status=status.HTTP_200_OK)

class  restClonarConfiguracionEnLote(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos')
        json_data = json.loads(request.body)
        ipControladorSrc = json_data["ip"]
        macControladorSrc = json_data["mac"]
        listaMacIpTarget = json_data["lista_controladores"]
        horarios =  json_data["horarios"]
        fases = json_data["fases"]
        planes = json_data["planes"]
        result = hitrafficClonarConfigControlador(ipControladorSrc, macControladorSrc, listaMacIpTarget,planes,horarios,fases)
        return Response(result,status=status.HTTP_200_OK)

class  restSetBorrarErrorControlador(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        result =  hitrafficSetBorrarErrorControlador(ip)
        return Response(result,status=status.HTTP_200_OK)

class  restSetCambioIpControlador(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        nueva_ip = json_data["nueva_ip"]
        mac = json_data["mac"]
        result =  hitrafficSetCambiarIpControlador(ip, nueva_ip, mac)
        return Response(result,status=status.HTTP_200_OK)



data_test= {"peticion":"se envia correctamente"}
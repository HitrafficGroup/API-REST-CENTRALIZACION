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
        return Response(result,status=status.HTTP_200_OK)


class restGetTimeControlador(APIView):
    def get(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            print("esta mal pasa la ip")
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        mac= request.GET.get('mac')
        result = hitrafficGetTimeControlador(ip,mac)
    
        return Response(result,status=status.HTTP_200_OK)

class restGetGruposControlador(APIView):
    def get(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        mac=request.GET.get('mac')
        result = hitrafficGetGruposControlador(ip,mac)
        print(result)
        return Response(result,status=status.HTTP_200_OK)

class restGetFasesControlador(APIView):
    def get(self, request, *args, **kwargs):
        print(request)
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
            
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        mac=request.GET.get('mac')
        result = hitrafficGetFasesControlador(ip,mac)
        return Response(result,status=status.HTTP_200_OK)


class restGetPlanesControlador(APIView):
    def get(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        mac=request.GET.get('mac')
        result =  hitrafficGetPlanesControlador(ip,mac)
        return Response(result,status=status.HTTP_200_OK)


class restGetOtrosParamControlador(APIView):
    def get(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        mac=request.GET.get('mac')
        result = hitrafficGetOtrosParamControlador(ip,mac)
        return Response(result,status=status.HTTP_200_OK)

class restGetHorariosControlador(APIView):
    def get(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        mac=request.GET.get('mac')
        result =  hitrafficGetHorariosControlador(ip,mac)
        return Response(result,status=status.HTTP_200_OK)

class restGetDiasEspecialesControlador(APIView):
    def get(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        mac=request.GET.get('mac')
        result = hitrafficGetDiasEspecialesControlador(ip,mac)
        return Response(result,status=status.HTTP_200_OK)

class restGetConflictoVerdesControlador(APIView):
    def get(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        mac=request.GET.get('mac')
        result = hitrafficGetConflictoVerdesControlador(ip,mac)
        return Response(result,status=status.HTTP_200_OK)

class restGetEntradasControlador(APIView):
    def get(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        mac=request.GET.get('mac')
        result = hitrafficGetEntradasControlador(ip,mac)
        return Response(result,status=status.HTTP_200_OK)

class  restGetRegistrosControlador(APIView):
    def get(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        mac= request.GET.get('mac')
        pagina = json_data["pagina"]
        result =  hitrafficGetRegistrosControlador(ip,mac, pagina)
        return Response(result,status=status.HTTP_200_OK)

class  restGetVersionFirmware(APIView):
    def get(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        mac=request.GET.get('mac')
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
        f1 = json_data["fase1"]
        f2 = json_data["fase2"]
        f3 = json_data["fase3"]
        f4 = json_data["fase4"]
        f5 = json_data["fase5"]
        f6 = json_data["fase6"]
        f7 = json_data["fase7"]
        f8 = json_data["fase8"]
        f9 = json_data["fase9"]
        f10 = json_data["fase10"]
        f11 = json_data["fase11"]
        f12 = json_data["fase12"]
        f13 = json_data["fase13"]
        f14 = json_data["fase14"]
        f15 = json_data["fase15"]
        f16 = json_data["fase16"]

        result = hitrafficSetFasesControlador(ip,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16)
        return Response(result,status=status.HTTP_200_OK)

class  restSetPlanesControlador(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        ip = json_data["ip"]
        num_plan = json_data["num_plan"]
        fase1 =  json_data["data0"]
        tiempo1 = json_data["data1"]
        fase2 = json_data["data2"]
        tiempo2 = json_data["data3"]
        fase3 = json_data["data4"]
        tiempo3 = json_data["data5"]
        fase4 = json_data["data6"]
        tiempo4 = json_data["data7"]
        fase5 = json_data["data8"]
        tiempo5 = json_data["data9"]
        fase6 = json_data["data10"]
        tiempo6 =  json_data["data11"]
        fase7 = json_data["data12"]
        tiempo7 = json_data["data13"]
        fase8 = json_data["data14"]
        tiempo8 = json_data["data15"]
        fase9 = json_data["data16"]
        tiempo9 = json_data["data17"]
        fase10 = json_data["data18"]
        tiempo10 = json_data["data19"]
        fase11 = json_data["data20"]
        tiempo11 = json_data["data21"]
        fase12  = json_data["data22"]
        tiempo12 = json_data["data23"]
        result = hitrafficSetPlanesControlador(ip,num_plan,fase1,tiempo1,fase2,tiempo2,fase3,tiempo3,fase4,tiempo4,fase5,tiempo5,fase6,tiempo6,fase7,tiempo7,fase8,tiempo8,fase9,tiempo9,fase10,tiempo10,fase11,tiempo11,fase12,tiempo12)
        
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
        num_horario = json_data["num_horario"]
        hora1 = json_data["hora1"]
        minuto1 = json_data["minuto1"]
        mod1 = json_data["mod_plan1"]
        desfase1 = json_data["desfase1"]
        hora2 = json_data["hora2"]
        minuto2 = json_data["minuto2"]
        mod2 = json_data["mod_plan2"]
        desfase2 = json_data["desfase2"]
        hora3 = json_data["hora3"]
        minuto3 = json_data["minuto3"]
        mod3 = json_data["mod_plan3"]
        desfase3 = json_data["desfase3"]
        hora4 = json_data["hora4"]
        minuto4 = json_data["minuto4"]
        mod4 = json_data["mod_plan4"]
        desfase4 = json_data["desfase4"]
        hora5 = json_data["hora5"]
        minuto5 = json_data["minuto5"]
        mod5 = json_data["mod_plan5"]
        desfase5 = json_data["desfase5"]
        hora6 = json_data["hora6"]
        minuto6 = json_data["minuto6"]
        mod6 = json_data["mod_plan6"]
        desfase6 = json_data["desfase6"]
        hora7 = json_data["hora7"]
        minuto7 = json_data["minuto7"]
        mod7 = json_data["mod_plan7"]
        desfase7 = json_data["desfase7"]
        hora8 = json_data["hora8"]
        minuto8 = json_data["minuto8"]
        mod8 = json_data["mod_plan8"]
        desfase8 = json_data["desfase8"]
        hora9 = json_data["hora9"]
        minuto9 = json_data["minuto9"]
        mod9 = json_data["mod_plan9"]
        desfase9 = json_data["desfase9"]
        hora10 = json_data["hora10"]
        minuto10 = json_data["minuto10"]
        mod10 = json_data["mod_plan10"]
        desfase10 = json_data["desfase10"]
        hora11 = json_data["hora11"]
        minuto11 = json_data["minuto11"]
        mod11 = json_data["mod_plan11"]
        desfase11 = json_data["desfase11"]
        hora12 = json_data["hora12"]
        minuto12 = json_data["minuto12"]
        mod12 = json_data["mod_plan12"]
        desfase12 = json_data["desfase12"]
        hora13 = json_data["hora13"]
        minuto13 = json_data["minuto13"]
        mod13 = json_data["mod_plan13"]
        desfase13 = json_data["desfase13"]
        hora14 = json_data["hora14"]
        minuto14 = json_data["minuto14"]
        mod14 = json_data["mod_plan14"]
        desfase14 = json_data["desfase14"]
        hora15 = json_data["hora15"]
        minuto15 = json_data["minuto15"]
        mod15 = json_data["mod_plan15"]
        desfase15 = json_data["desfase15"]
        hora16 = json_data["hora16"]
        minuto16 = json_data["minuto16"]
        mod16 = json_data["mod_plan16"]
        desfase16 = json_data["desfase16"]
        result = hitrafficSetHorariosControlador(ip,num_horario,hora1,minuto1,mod1,desfase1,hora2,minuto2,mod2,desfase2,hora3,minuto3,mod3,desfase3,hora4,minuto4,mod4,desfase4,hora5,minuto5,mod5,desfase5,hora6,minuto6,mod6,desfase6,hora7,minuto7,mod7,desfase7,hora8,minuto8,mod8,desfase8,hora9,minuto9,mod9,desfase9,hora10,minuto10,mod10,desfase10,hora11,minuto11,mod11,desfase11,hora12,minuto12,mod12,desfase12,hora13,minuto13,mod13,desfase13,hora14,minuto14,mod14,desfase14,hora15,minuto15,mod15,desfase15,hora16,minuto16,mod16,desfase16)
        return Response(result,status=status.HTTP_200_OK)


# class  restSetDiasEspecialesControlador(APIView):
#     def post(self, request, *args, **kwargs):
#         if len(request.body) == 0 :
#             raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
#         json_data = json.loads(request.body)
#         print(json_data)
#         ip = json_data["ip"]
#         fines_semana = json_data["fines_semana"]
#         mes1 = json_data["mes1"]
#         dia1 = json_data["dia1"]
#         mod1 = json_data["mod1"]
#         mes2 = json_data["mes2"]
#         dia2 = json_data["dia2"]
#         mod2 = json_data["mod2"]
#         mes3 = json_data["mes3"]
#         dia3 = json_data["dia3"]
#         mod3 = json_data["mod3"]
#         mes4 = json_data["mes4"]
#         dia4 = json_data["dia4"]
#         mod4 = json_data["mod4"]
#         mes5 = json_data["mes5"]
#         dia5 = json_data["dia5"]
#         mod5 = json_data["mod5"]
#         mes6 = json_data["mes6"]
#         dia6 = json_data["dia6"]
#         mod6 = json_data["mod6"]
#         mes7 = json_data["mes7"]
#         dia7 = json_data["dia7"]
#         mod7 = json_data["mod7"]
#         mes8 = json_data["mes8"]
#         dia8 = json_data["dia8"]
#         mod8 = json_data["mod8"]
#         mes9 = json_data["mes9"]
#         dia9 = json_data["dia9"]
#         mod9 = json_data["mod9"]
#         mes10 = json_data["mes10"]
#         dia10 = json_data["dia10"]
#         mod10 = json_data["mod10"]
#         mes11 = json_data["mes11"]
#         dia11 = json_data["dia11"]
#         mod11 = json_data["mod11"]
#         mes12 = json_data["mes12"]
#         dia12 = json_data["dia12"]
#         mod12 = json_data["mod12"]
#         mes13 = json_data["mes13"]
#         dia13 = json_data["dia13"]
#         mod13 = json_data["mod13"]
#         mes14 = json_data["mes14"]
#         dia14 = json_data["dia14"]
#         mod14 = json_data["mod14"]
#         mes15 = json_data["mes15"]
#         dia15 = json_data["dia15"]
#         mod15 = json_data["mod15"]
#         mes16 = json_data["mes16"]
#         dia16 = json_data["dia16"]
#         mod16 = json_data["mod16"]
#         result = hitrafficSetDiasEspecialesControlador(ip,mes1,dia1,mod1, mes2, dia2, mod2, mes3, dia3, mod3, mes4, dia4, mod4, mes5, dia5, mod5, mes6, dia6, mod6, mes7, dia7, mod7, mes8, dia8, mod8, mes9, dia9, mod9, mes10, dia10, mod10, mes11, dia11, mod11, mes12, dia12, mod12, mes13, dia13, mod13, mes14, dia14, mod14, mes15, dia15, mod15, mes16, dia16, mod16, fines_semana)
#         return Response(result,status=status.HTTP_200_OK)


data_test= {"peticion":"se envia correctamente"}
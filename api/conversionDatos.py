import json
from datetime import datetime

def convertFromStringToList(tupla_string):
    dato_delimitado = str(tupla_string[1:-2])
    dato_lst = dato_delimitado.split(",")
    return dato_lst


def convertToDictHoraControlador(ip, time_zone):
    hora = datetime.now()
    diccionario_tiempo = {ip:{"year":str(hora.year), "mes":str(hora.month), "dia":str(hora.day), "horas":str(hora.hour), "minutos": str(hora.minute), "segundos":str(hora.second), "indice_dia":str(hora.weekday()+1), "time_zone":time_zone}}
    return diccionario_tiempo


def convertToDictPlanes(ip,num_plan,fase1,tiempo1,fase2,tiempo2,fase3,tiempo3,fase4,tiempo4,fase5,tiempo5,fase6,tiempo6,fase7,tiempo7,fase8,tiempo8,fase9,tiempo9,fase10,tiempo10,fase11,tiempo11,fase12,tiempo12):
    stringPlanes = "("+str(fase1)+","+str(tiempo1)+","+str(fase2)+","+str(tiempo2)+","+str(fase3)+","+str(tiempo3)+","+str(fase4)+","+str(tiempo4)+","+str(fase5)+","+str(tiempo5)+","+str(fase6)+","+str(tiempo6)+","+str(fase7)+","+str(tiempo7)+","+str(fase8)+","+str(tiempo8)+","+str(fase9)+","+str(tiempo9)+","+str(fase10)+","+str(tiempo10)+","+str(fase11)+","+str(tiempo11)+","+str(fase12)+","+str(tiempo12)+","+")"
    diccionario_planes = {ip:{"plan"+str(num_plan):stringPlanes}}
    return diccionario_planes


def InvertConversionPlanes(string_dict_planes,mac):
    diccionario_planes = json.loads(string_dict_planes)
    diccionario_salida = {}
    print(diccionario_planes)
    for idx,key in enumerate(diccionario_planes[mac]):
        plan_lst = convertFromStringToList(diccionario_planes[mac][key])
        print(plan_lst)
        diccionario_salida[key] = {"fase1":plan_lst[0], "tiempo1":plan_lst[1], "fase2":plan_lst[2], "tiempo2": plan_lst[3], "fase3":plan_lst[4], "tiempo3": plan_lst[5], "fase4":plan_lst[6], "tiempo4": plan_lst[7], "fase5":plan_lst[8], "tiempo5": plan_lst[9], "fase6":plan_lst[10], "tiempo6": plan_lst[11], "fase7":plan_lst[12], "tiempo7": plan_lst[13], "fase8":plan_lst[14], "tiempo8": plan_lst[15], "fase9":plan_lst[16], "tiempo9": plan_lst[17], "fase10":plan_lst[18], "tiempo10": plan_lst[19], "fase11":plan_lst[20], "tiempo11": plan_lst[21], "fase12":plan_lst[22], "tiempo12": plan_lst[23]}
    
    return diccionario_salida 


def convertToDictHorarios(ip,num_horario,hora1,minuto1,mod1,desfase1,hora2,minuto2,mod2,desfase2,hora3,minuto3,mod3,desfase3,hora4,minuto4,mod4,desfase4,hora5,minuto5,mod5,desfase5,hora6,minuto6,mod6,desfase6,hora7,minuto7,mod7,desfase7,hora8,minuto8,mod8,desfase8,hora9,minuto9,mod9,desfase9,hora10,minuto10,mod10,desfase10,hora11,minuto11,mod11,desfase11,hora12,minuto12,mod12,desfase12,hora13,minuto13,mod13,desfase13,hora14,minuto14,mod14,desfase14,hora15,minuto15,mod15,desfase15,hora16,minuto16,mod16,desfase16):
    lst_tipos_horario = ["dia_ordinario","fin_semana","dia_festivo"]
    stringHorarios = "("+str(hora1)+","+str(minuto1)+","+str(mod1)+","+str(desfase1)+","+str(hora2)+","+str(minuto2)+","+str(mod2)+","+str(desfase2)+","+str(hora3)+","+str(minuto3)+","+str(mod3)+","+str(desfase3)+","+str(hora4)+","+str(minuto4)+","+str(mod4)+","+str(desfase4)+","+str(hora5)+","+str(minuto5)+","+str(mod5)+","+str(desfase5)+","+str(hora6)+","+str(minuto6)+","+str(mod6)+","+str(desfase6)+","+str(hora7)+","+str(minuto7)+","+str(mod7)+","+str(desfase7)+","+str(hora8)+","+str(minuto8)+","+str(mod8)+","+str(desfase8)+","+str(hora9)+","+str(minuto9)+","+str(mod9)+","+str(desfase9)+","+str(hora10)+","+str(minuto10)+","+str(mod10)+","+str(desfase10)+","+str(hora11)+","+str(minuto11)+","+str(mod11)+","+str(desfase11)+","+str(hora12)+","+str(minuto12)+","+str(mod12)+","+str(desfase12)+","+str(hora13)+","+str(minuto13)+","+str(mod13)+","+str(desfase13)+","+str(hora14)+","+str(minuto14)+","+str(mod14)+","+str(desfase14)+","+str(hora15)+","+str(minuto15)+","+str(mod15)+","+str(desfase15)+","+str(hora16)+","+str(minuto16)+","+str(mod16)+","+str(desfase16)+",)"
    diccionario_horarios = {ip:{lst_tipos_horario[int(num_horario)]:stringHorarios}}
    return diccionario_horarios

def InvertConversionHorarios(string_dict_horarios, mac):
    diccionario_horarios = json.loads(string_dict_horarios)
    diccionario_salida = {}
    for key in diccionario_horarios[mac]:
        horario_lst = convertFromStringToList(diccionario_horarios[mac][key])
        diccionario_salida[key] = {"hora1":horario_lst[0],"minuto1":horario_lst[1],"mod1":horario_lst[2],"desfase1":horario_lst[3],"hora2":horario_lst[4],"minuto2":horario_lst[5],"mod2":horario_lst[6],"desfase2":horario_lst[7],"hora3":horario_lst[8],"minuto3":horario_lst[9],"mod3":horario_lst[10],"desfase3":horario_lst[11],"hora4":horario_lst[12],"minuto4":horario_lst[13],"mod4":horario_lst[14],"desfase4":horario_lst[15],"hora5":horario_lst[16],"minuto5":horario_lst[17],"mod5":horario_lst[18],"desfase5":horario_lst[19],"hora6":horario_lst[20],"minuto6":horario_lst[21],"mod6":horario_lst[22],"desfase6":horario_lst[23],"hora7":horario_lst[24],"minuto7":horario_lst[25],"mod7":horario_lst[26],"desfase7":horario_lst[27],"hora8":horario_lst[28],"minuto8":horario_lst[29],"mod8":horario_lst[30],"desfase8":horario_lst[31],"hora9":horario_lst[32],"minuto9":horario_lst[33],"mod9":horario_lst[34],"desfase9":horario_lst[35],"hora10":horario_lst[36],"minuto10":horario_lst[37],"mod10":horario_lst[38],"desfase10":horario_lst[39],"hora11":horario_lst[40],"minuto11":horario_lst[41],"mod11":horario_lst[42],"desfase11":horario_lst[43],"hora12":horario_lst[44],"minuto12":horario_lst[45],"mod12":horario_lst[46],"desfase12":horario_lst[47],"hora13":horario_lst[48],"minuto13":horario_lst[49],"mod13":horario_lst[50],"desfase13":horario_lst[51],"hora14":horario_lst[52],"minuto14":horario_lst[53],"mod14":horario_lst[54],"desfase14":horario_lst[55],"hora15":horario_lst[56],"minuto15":horario_lst[57],"mod15":horario_lst[58],"desfase15":horario_lst[59],"hora16":horario_lst[60],"minuto16":horario_lst[61],"mod16":horario_lst[62],"desfase16":horario_lst[63]}

    return diccionario_salida


def convertToDictDiasEspeciales(ip,mes1, dia1, mod1, mes2, dia2, mod2, mes3, dia3, mod3, mes4, dia4, mod4, mes5, dia5, mod5, mes6, dia6, mod6, mes7, dia7, mod7, mes8, dia8, mod8, mes9, dia9, mod9, mes10, dia10, mod10, mes11, dia11, mod11, mes12, dia12, mod12, mes13, dia13, mod13, mes14, dia14, mod14, mes15, dia15, mod15, mes16, dia16, mod16, fines_semana):
    stringDiasEspeciales = "("+mes1+","+str(dia1)+","+str(mod1)+","+str(mes2)+","+str(dia2)+","+str(mod2)+","+str(mes3)+","+str(dia3)+","+str(mod3)+","+str(mes4)+","+str(dia4)+","+str(mod4)+","+str(mes5)+","+str(dia5)+","+str(mod5)+","+str(mes6)+","+str(dia6)+","+str(mod6)+","+str(mes7)+","+str(dia7)+","+str(mod7)+","+str(mes8)+","+str(dia8)+","+str(mod8)+","+str(mes9)+","+str(dia9)+","+str(mod9)+","+str(mes10)+","+str(dia10)+","+str(mod10)+","+str(mes11)+","+str(dia11)+","+str(mod11)+","+str(mes12)+","+str(dia12)+","+str(mod12)+","+str(mes13)+","+str(dia13)+","+str(mod13)+","+str(mes14)+","+str(dia14)+","+str(mod14)+","+str(mes15)+","+str(dia15)+","+str(mod15)+","+str(mes16)+","+str(dia16)+","+str(mod16)+",)"
    diccionario_diasEspeciales = {ip:{"dias_festivos":stringDiasEspeciales,"fines_semana":str(fines_semana)}}
    return diccionario_diasEspeciales


def InvertConversionDiasEspeciales(string_diccionario_diasEspeciales,mac):
    diccionario_diasEspeciales = json.loads(string_diccionario_diasEspeciales)
    diccionario_salida = {}

    for key in diccionario_diasEspeciales[mac]:
        if key == "dias_festivos":
            diasEspeciales_lst = convertFromStringToList(diccionario_diasEspeciales[mac][key])
            diccionario_salida[key] = {"mes1": diasEspeciales_lst[0],"dia1":diasEspeciales_lst[1],"mod1":diasEspeciales_lst[2],"mes2":diasEspeciales_lst[3],"dia2":diasEspeciales_lst[4],"mod2":diasEspeciales_lst[5],"mes3":diasEspeciales_lst[6],"dia3":diasEspeciales_lst[7],"mod3":diasEspeciales_lst[8],"mes4":diasEspeciales_lst[9],"dia4":diasEspeciales_lst[10],"mod4":diasEspeciales_lst[11],"mes5":diasEspeciales_lst[12],"dia5":diasEspeciales_lst[13],"mod5":diasEspeciales_lst[14],"mes6":diasEspeciales_lst[15],"dia6":diasEspeciales_lst[16],"mod6":diasEspeciales_lst[17],"mes7":diasEspeciales_lst[18],"dia7":diasEspeciales_lst[19],"mod7":diasEspeciales_lst[20],"mes8":diasEspeciales_lst[21],"dia8":diasEspeciales_lst[22],"mod8":diasEspeciales_lst[23],"mes9":diasEspeciales_lst[24],"dia9":diasEspeciales_lst[25],"mod9":diasEspeciales_lst[26],"mes10":diasEspeciales_lst[27],"dia10":diasEspeciales_lst[28],"mod10":diasEspeciales_lst[29],"mes11":diasEspeciales_lst[30],"dia11":diasEspeciales_lst[31],"mod11":diasEspeciales_lst[32],"mes12":diasEspeciales_lst[33],"dia12":diasEspeciales_lst[34],"mod12":diasEspeciales_lst[35],"mes13":diasEspeciales_lst[36],"dia13":diasEspeciales_lst[37],"mod13":diasEspeciales_lst[38],"mes14":diasEspeciales_lst[39],"dia14":diasEspeciales_lst[40],"mod14":diasEspeciales_lst[41],"mes15":diasEspeciales_lst[42],"dia15":diasEspeciales_lst[43],"mod15":diasEspeciales_lst[44],"mes16":diasEspeciales_lst[45],"dia16":diasEspeciales_lst[46],"mod16":diasEspeciales_lst[47]}
        elif key=="fines_semana":
            diccionario_salida[key] = diccionario_diasEspeciales[mac][key]

    return diccionario_salida


def convertToDictOtrosParametros(ip,time_destello_on,time_red_on,time_destello_green_p,time_destello_green_v,time_yellow_v,time_all_red,time_min_green,sincro_value):
    binary_tiempo_minimo_verde = bin(int(time_min_green))
    binary_tiempo_minimo_verde = binary_tiempo_minimo_verde[2:]
    bits_faltantes = 16 - len(binary_tiempo_minimo_verde)
    for i in range(0,bits_faltantes):
        binary_tiempo_minimo_verde = "0" + binary_tiempo_minimo_verde

    tiempo_minimo_verde_2 = int(binary_tiempo_minimo_verde[0:8],2)
    tiempo_minimo_verde_1 = int(binary_tiempo_minimo_verde[8:],2)

    diccionario_otrosParametros = {ip:{"tiempo_destello_prender": time_destello_on, "tiempo_rojo_prender":time_red_on, "destellar_verde_peatonal":time_destello_green_p, "destellar_verde_vehicular":time_destello_green_v, "tiempo_amarillo_vehicular":time_yellow_v, "tiempo_todo_rojo": time_all_red, "tiempo_minimo_verde_1": str(tiempo_minimo_verde_1), "tiempo_minimo_verde_2": str(tiempo_minimo_verde_2), "valor_sincronizacion": sincro_value}}
    return diccionario_otrosParametros


def InvertConversionOtrosParametros(string_diccionario_otros_parametros,mac):
    diccionario_otros_parametros = json.loads(string_diccionario_otros_parametros)
    
    tiempo_minimo_verde_1 = diccionario_otros_parametros[mac]["tiempo_minimo_verde_1"]
    tiempo_minimo_verde_2 = diccionario_otros_parametros[mac]["tiempo_minimo_verde_2"]

    binario_1 = bin(int(tiempo_minimo_verde_1))
    binario_1 = binario_1[2:]
    binario_2 = bin(int(tiempo_minimo_verde_2))
    binario_2 = binario_2[2:]
    lst_binarios = [binario_1, binario_2]

    for idx,element in enumerate(lst_binarios):
        bits_falta = 8 - len(element)
        for bit in range(0,bits_falta):
            lst_binarios[idx] = "0" + lst_binarios[idx] 

    binario_final = binario_2 + binario_1
    tiempoMinVerde = int(binario_final,2)

    diccionario_salida = {
        "time_destello_on": diccionario_otros_parametros[mac]["tiempo_destello_prender"],
        "time_red_on": diccionario_otros_parametros[mac]["tiempo_rojo_prender"],
        "time_destello_green_p": diccionario_otros_parametros[mac]["destellar_verde_peatonal"],
        "time_destello_green_v": diccionario_otros_parametros[mac]["destellar_verde_vehicular"],
        "time_yellow_v": diccionario_otros_parametros[mac]["tiempo_amarillo_vehicular"],
        "time_all_red": diccionario_otros_parametros[mac]["tiempo_todo_rojo"],
        "time_min_green": str(tiempoMinVerde),
        "sincro_value": diccionario_otros_parametros[mac]["valor_sincronizacion"],
    }

    return diccionario_salida



def convertToDictConflictoVerdes(ip,fila1,fila2,fila3,check1,check2,check3):
    bin_fila1 = bin(int(fila1))
    bin_fila1 = bin_fila1[2:]
    bin_fila2 = bin(int(fila2))
    bin_fila2 = bin_fila2[2:]
    bin_fila3 = bin(int(fila3))
    bin_fila3 = bin_fila3[2:]
    filas = [bin_fila1, bin_fila2, bin_fila3]

    for idx,element in enumerate(filas):
        bits_faltantes = 4 - len(element)
        for i in range(0,bits_faltantes):
            element = "0" + element
        filas[idx] = element

    #print(filas)        

    diccionario_conflictoVerdes = {ip: {"fila1":filas[0], "fila2":filas[1], "fila3":filas[2], "check1":check1, "check2":check2, "check3":check3 }}
    return diccionario_conflictoVerdes


def InvertConversionConflictoVerdes(string_dict_conflictoVerdes,mac):
    diccionario_conflictoVerdes = json.loads(string_dict_conflictoVerdes)
    print("diccionario de verdes: ",diccionario_conflictoVerdes)
    int_fila1 = int(diccionario_conflictoVerdes[mac]["fila1"],2)
    int_fila2 = int(diccionario_conflictoVerdes[mac]["fila2"],2)
    int_fila3 = int(diccionario_conflictoVerdes[mac]["fila3"],2)

    diccionario_salida = {"fila1":str(int_fila1), "fila2":str(int_fila2), "fila3":str(int_fila3), "check1":diccionario_conflictoVerdes[mac]["check1"], "check2":diccionario_conflictoVerdes[mac]["check2"], "check3":diccionario_conflictoVerdes[mac]["check3"] }

    return diccionario_salida

def convertToDictEntradas(ip,box1,fase1,tiempo1,box2,fase2,tiempo2,box3,fase3,tiempo3,box4,fase4,tiempo4):
    diccionario_entradas = {ip:
        {
            "entrada1":{
                "checkbox":box1, 
                "fase":fase1, 
                "tiempo":tiempo1
            },
            "entrada2":{
            "checkbox":box2, 
            "fase":fase2, 
            "tiempo":tiempo2
            },
            "entrada3":{
            "checkbox":box3, 
            "fase":fase3, 
            "tiempo":tiempo3
            },
            "entrada4":{
            "checkbox":box4, 
            "fase":fase4, 
            "tiempo":tiempo4
            }
        }
    }
    
    return diccionario_entradas
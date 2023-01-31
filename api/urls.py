from django.urls import path, include
from .views import *

urlpatterns = [
    #Operaciones de lectura
    path('listarIps', ListarIpsControlador.as_view()),
    path('restGetTimeControlador',restGetTimeControlador.as_view()),
    path('restGetGruposControlador',restGetGruposControlador.as_view()),
    path('restGetFasesControlador',restGetFasesControlador.as_view()),
    path('restGetPlanesControlador',restGetPlanesControlador.as_view()),
    path('restGetOtrosParamControlador',restGetOtrosParamControlador.as_view()),
    path('restGetHorariosControlador',restGetHorariosControlador.as_view()),
    path('restGetDiasEspecialesControlador',restGetDiasEspecialesControlador.as_view()),
    path('restGetConflictoVerdesControlador',restGetConflictoVerdesControlador.as_view()),
    path('restGetEntradasControlador',restGetEntradasControlador.as_view()),
    path('restGetRegistrosControlador',restGetRegistrosControlador.as_view()),
    path('restGetVersionFirmware',restGetVersionFirmware.as_view()),
    #Operaciones de Escritura
    path('restSetTimeControlador',restSetTimeControlador.as_view()),
    path('restSetGruposControlador',restSetGruposControlador.as_view()),
    path('restSetConflictoVerdesControlador',restSetConflictoVerdesControlador.as_view()),
    path('restSetFasesControlador',restSetFasesControlador.as_view()),
    path('restSetPlanesControlador',restSetPlanesControlador.as_view()),
    path('restSetOtrosParamControlador',restSetOtrosParamControlador.as_view()),
    path('restSetHorariosControlador',restSetHorariosControlador.as_view()),
    path('restSetDiasEspecialesControlador',restSetDiasEspecialesControlador.as_view()),
    path('restSetEntradasControlador',restSetEntradasControlador.as_view()),
    path('restSetRegistrosControlador',restSetRegistrosControlador.as_view()),
    path('restClonarConfiguracionEnLote',restClonarConfiguracionEnLote.as_view()),
    path('restSetBorrarErrorControlador',restSetBorrarErrorControlador.as_view()),
    path('restSetCambioIpControlador',restSetCambioIpControlador.as_view()),
]      
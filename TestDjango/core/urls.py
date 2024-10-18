from django.urls import path
from .views import home, donacion, solicitudes, resumen, foro, register,  crear_tema, catalogo, detallepro, pago, lista_solicitudes

urlpatterns = [
    path('', home,name="home"),
    path('donacion/', donacion,name='donacion'),
    path('solicitudes/', solicitudes,name='solicitudes'),
    path('resumen/', resumen,name='resumen'),
    #path('resumen/<int:donacion_id>/', resumen, name='resumen'),
    path('foro/', foro,name='foro'),
    path('crear_tema/', crear_tema,name='crear_tema'),
    path('register/', register,name='register'),
    path('catalogo/', catalogo,name='catalogo'),
    path('detallepro/', detallepro,name='detallepro'),
    path('pago/', pago,name='pago'),
    path('lista_solicitudes/', lista_solicitudes,name='lista_solicitudes'),
    #path('foro/<int:pk>/', temadetailView.as_view(), name='tema'),

]





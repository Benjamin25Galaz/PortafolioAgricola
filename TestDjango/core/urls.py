from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, donacion,acceder,bienvenido,mostrar_carrito, resumen,pago_exitoso, resumen_donacion, logout, solicitudes, foro, register, detalle_producto,formulario_producto, sumar_producto, limpiar_carrito, agregar_producto, eliminar_producto, restar_producto,  crear_tema, catalogo,listar_productos,  pago, lista_solicitudes,tema_detail

urlpatterns = [
    path('', home,name="home"),
    path('donacion/', donacion,name='donacion'),
    path('solicitudes/', solicitudes,name='solicitudes'),
    path('foro/', foro,name='foro'),
    path('resumen/<int:donacion_id>/', resumen_donacion, name='resumen_donacion'),
    path('resumen/', resumen,name='resumen'),
    path('resumen/<int:donacion_id>/', resumen, name='resumen'),
    path('bienvenido/', bienvenido, name='bienvenido'),
    path('crear_tema/', crear_tema,name='crear_tema'),
    path('register/', register,name='register'),
    path('catalogo/', catalogo,name='catalogo'),
    path('pago/', pago,name='pago'),
        path('pago_exitoso/', pago_exitoso, name='pago_exitoso'),
    path('lista_solicitudes/', lista_solicitudes,name='lista_solicitudes'),
    path('foro/<int:tema_id>/', tema_detail, name='tema_detail'),
    path('acceder/', acceder,name='acceder'),
    path('logout/', logout, name='logout'),
    path('productos/', listar_productos, name='listar_productos'),
    path('producto/<int:pk>/', detalle_producto, name='detalle_producto'),
    path('producto/nuevo/', formulario_producto, name='formulario_producto'),



    #---------------MODULO DE VENTAS------------------------
    path('carrito/', mostrar_carrito, name='morstrar_carrito'),
    path('listar_productos', listar_productos, name='listar_productos'),  # Ruta principal para listar productos
    path('agregar/<int:producto_id>/', agregar_producto, name='Add'),  # Agregar un producto al carrito
    path('eliminar/<int:producto_id>/', eliminar_producto, name='Del'),  # Eliminar un producto del carrito
    path('restar/<int:producto_id>/', restar_producto, name='Sub'),  # Restar uno al carrito
    path('sumar/<int:producto_id>/', sumar_producto, name='Sum'),  # Restar uno al carrito
    path('limpiar/', limpiar_carrito, name='CLS'), 
     # Limpiar el carrito

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





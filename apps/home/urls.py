from django.urls import path, re_path
from apps.home import views
from django.contrib.auth.views import login_required
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    ##########################        DEPARTAMENTO         ########################
    #Crear DEPARTAMENTO
    path('dep_addone', views.ADDONE_DEPARTAMENTO.as_view(), name='dep_addone'),
    #Listar DEPARTAMENTOS
    path('dep_listall', views.DEPARTAMENTO_LISTALL.as_view(), name='dep_listall'),
    #Modificar DEPARTAMENTO
    path('dep_update/<int:pk>', views.DEPARTAMENTO_UPDATE.as_view(), name='dep_update'),
    #Eliminar DEPARTAMENTO
    path('eliminar_departamento/<id>/', views.ELIMINAR_DEPARTAMENTO, name="eliminar_departamento"),


    ##########################       INVENTARIO        #############################
   
    path('inventarios', views.verDeptos, name='inventarios'),
    
    path('verDetallesInventario/<int:id>/', views.verDetallesInventario, name='verDetallesInventario'),



    ###########################         TOUR          #############################
    #Crear TOUR
    path('tou_addone', views.TOUR_ADDONE.as_view(), name='tou_addone'),
    #Listar TOUR
    path('tou_listall', views.TOUR_LISTALL.as_view(), name='tou_listall'),
    #Actualizar TOUR
    path('tou_update/<int:pk>', views.TOUR_UPDATE.as_view(), name='tou_update'),
    #Eliminar TOUR
    path('eliminar_tour/<id>/', views.ELIMINAR_TOUR, name='eliminar_tour'),


    ########################         TRANSPORTE          ##########################
    #Crear TRANSPORTE
    path('tra_addone', views.TRANSPORTE_ADDONE.as_view(), name='tra_addone'),
    #Listar TRANSPORTES
    path('tra_listall', views.TRANSPORTE_LISTALL.as_view(), name='tra_listall'),
    #Editar TRANSPORTE
    path('tra_update/<int:pk>', views.TRANPORTE_UPDATE.as_view(), name='tra_update'),
    #Eliminar TRANSPORTE
    path('eliminar_transporte/<id>/', views.TRANSPORTE_DELETE, name='eliminar_transporte'),


    #########################       HOME_PRINCIPAL         ########################

    #Listar DEPARTAMENTOS
    path('departamentos/', views.DepartamentoListView.as_view(),name='DepartamentoList'),

    #Detalle  DEPARTAMENTO
    path('detalleDepartamento/<DEP_ID>', views.DepartamentoDetailView.as_view(), name='DepartamentoDetailView'),

    #Listar RESERVAS
    path('reservas/', views.ReservaListView.as_view(), name='ReservaList'),

    #Detalle RESERVA
    path('detalleReserva/<int:pk>', views.ReservaDetailView.as_view(), name='detalleReserva'),

    #Cancelar RESERVA
    path('cancelarReserva/<id>/', views.CANCELAR_RESERVA, name='cancelarReserva'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
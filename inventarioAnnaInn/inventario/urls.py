from django.urls import path 

from . import views

app_name = 'inventario'

urlpatterns = [
    
    path('', views.home, name = 'home'),
    
    #-----------------------COCINA----------------------------------------------------
    path('cocina/list/', views.CocinaListView.as_view(), name='cocina_list'),
    path('cocina/new/', views.CocinaCreateView.as_view(), name = 'cocina_new'),
    path('cocina/update/<int:pk>/', views.CocinaUpdateView.as_view(), name='cocina_update'),
    path('cocina/delete/<int:pk>/', views.CocinaDeleteView.as_view(), name='cocina_delete'),
    
    #-----------------------BLANCOS----------------------------------------------------
    path('blancos/list/', views.BlancosListView.as_view(), name='blancos_list'),
    path('blancos/new/', views.BlancosCreateView.as_view(), name = 'blancos_new'),
    path('blancos/update/<int:pk>/', views.BlancosUpdateView.as_view(), name='blancos_update'),
    path('blancos/delete/<int:pk>/', views.BlancosDeleteView.as_view(), name='blancos_delete'),
    
    #-----------------------INSUMOS----------------------------------------------------
    path('insumos/list/', views.InsumosListView.as_view(), name='insumo_list'),
    path('insumos/new/', views.InsumosCreateView.as_view(), name = 'insumos_new'),
    path('insumos/update/<int:pk>/', views.InsumosUpdateView.as_view(), name='insumos_update'),
    path('insumos/delete/<int:pk>/', views.InsumosDeleteView.as_view(), name='insumos_delete'),

]

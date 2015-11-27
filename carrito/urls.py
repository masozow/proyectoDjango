from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$',views.ver_producto),
     url(r'^producto/(?P<pk>[0-9]+)/$', views.detalle_producto),
     url(r'^producto/nuevo/$', views.producto_nuevo, name='producto_nuevo'),
     url(r'^proucto/(?P<pk>[0-9]+)/editar/$', views.editar_producto, name='editar_producto'),


     url(r'^compra/$',views.ver_compra),
      url(r'^compra/compras/(?P<pk>[0-9]+)/$', views.detalle_compra),
      url(r'^compra/compras/nueva/$', views.compra_nueva, name='compra_nueva'),
      url(r'^compra/compras/(?P<pk>[0-9]+)/editar/$', views.editar_compra, name='editar_compra'),
]

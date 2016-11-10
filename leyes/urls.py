from django.conf.urls import url
from .views import index, iniciativa_view,iniciativa_list,iniciativa_update

urlpatterns = (
   url(r'^leyes/$',index,name='index'),
   url(r'^leyes/nuevo/$',iniciativa_view, name="iniciativa_crear"),
   url(r'^leyes/listar/$',iniciativa_list, name="iniciativa_listar"),
   url(r'^leyes/actualizar/$',iniciativa_update, name="iniciativa_actualizar"),
    #url(r'^leyes/editar/(?P<pk>\d+)$', IniciativaUpdate.as_view(), name="iniciativa_update"),
    #url(r'^leyes/borrar/(?P<pk>\d+)$', IniciativaDelete.as_view(), name="iniciativa_delete"),
)



from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import(
	CreateView,
	UpdateView,
	DeleteView

)

from .models import Diputado


class DiputadoList(ListView):
	model = Diputado
	#context_object_name = 'diputados'

class DiputadoDetail(DetailView):
	model =  Diputado

class DiputadoCreation(CreateView):
	model = Diputado
	success_url = reverse_lazy('diputados:list')
	fields = ['nombre', 'ciudad', 'pais', 'email', 'fechaNacimiento', 'suplente']


class DiputadoUpdate(UpdateView):
	model = Diputado
	success_url = reverse_lazy('diputados:list')
	fields = ['nombre', 'ciudad', 'pais', 'email', 'fechaNacimiento', 'suplente']

class DiputadoDelete(DeleteView):
	model = Diputado
	success_url = reverse_lazy('diputado:list')

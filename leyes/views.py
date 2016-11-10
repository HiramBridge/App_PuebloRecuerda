from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.http import HttpResponse
#from django.views.generic import View
#from django.views.generic.detail import DetailView
#from django.views.generic.edit import(
#	CreateView,
from .models import Iniciativa
from .forms import IniciativaForm

def index(request):
    return render(request,'leyes/index.html')

def iniciativa_view(request):
	if request.method == 'POST':
		form=IniciativaForm(request.POST)
		if form.is_valid():
				form.save()
		return redirect('leyes:index')
	else:
		form=IniciativaForm()

	return render(request,'leyes/iniciativa_form.html',{'form':form})


def iniciativa_list(request):
	iniciativa = Iniciativa.objects.all().order_by('id')
	contexto = {'iniciativas':iniciativa}
	return render(request, 'leyes/iniciativa_list.html', contexto)

def iniciativa_update(request):
	iniciativa = Iniciativa.objects.all().order_by('id')
	contexto = {'iniciativas':iniciativa}
	return render(request, 'leyes/iniciativa_list.html', contexto)







"""class IniciativaList(ListView):
	model = Iniciativa
	success_url = reverse_lazy('leyes:iniciativa_list')
	#context_object_name = 'leyes'

class IniciativaDetail(DetailView):
	model =  Iniciativa
	success_url = reverse_lazy('leyes:iniciativa_detail')

class IniciativaCreation(CreateView):
	model = Iniciativa
	success_url = reverse_lazy('leyes:iniciativa_create')
	fields = ['num', 'nombre', 'turno', 'comision', 'resolutivos', 'enlace','diputado']


class IniciativaUpdate(UpdateView):
	model = Iniciativa
	success_url = reverse_lazy('leyes:iniciativa_update')
	fields = ['num', 'nombre', 'turno', 'comision', 'resolutivos', 'enlace','diputado']

class IniciativaDelete(DeleteView):
	model = Iniciativa
	success_url = reverse_lazy('leyes:delete')"""
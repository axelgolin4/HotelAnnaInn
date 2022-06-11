from re import template
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from .forms import  CocinaForm, InsumosForm, BlancosForm
from .models import Insumos, Cocina, Blancos

@login_required
def home(request):
    return render(request, 'main.html')


#----------------------------VISTAS COCINA-----------------------------------------
class CocinaListView(ListView):
    model = Cocina
    template_name = 'inventario-cocina.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Cocina'
        return context


class CocinaCreateView(CreateView):
    model = Cocina
    form_class = CocinaForm
    template_name = 'cocina/crear.html'
    success_url = reverse_lazy('inventario:cocina_list')

class CocinaUpdateView(UpdateView):
    model = Cocina
    form_class = CocinaForm
    template_name = 'cocina/crear.html'
    success_url = reverse_lazy('inventario:cocina_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición una Categoria'
        context['action'] = 'edit'
        return context

class CocinaDeleteView(DeleteView):
    model = Cocina
    template_name = 'cocina/delete.html'
    success_url = reverse_lazy('inventario:cocina_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Categoria'
        return context
   


#----------------------------VISTAS INSUMOS-----------------------------------------
class InsumosListView(ListView):
    model = Insumos
    template_name = 'inventario-insumos.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Insumos'
        return context

class InsumosCreateView(CreateView):
    model = Insumos
    form_class = InsumosForm
    template_name = 'insumos/crear.html'
    success_url = reverse_lazy('inventario:insumos_list')

class InsumosUpdateView(UpdateView):
    model = Insumos
    form_class = InsumosForm
    template_name = 'insumos/crear.html'
    success_url = reverse_lazy('inventario:insumos_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición una Categoria'
        context['action'] = 'edit'
        return context

class InsumosDeleteView(DeleteView):
    model = Insumos
    template_name = 'insumos/delete.html'
    success_url = reverse_lazy('inventario:insumos_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Categoria'
        return context





#----------------------------VISTAS BLANCOS-----------------------------------------
class BlancosListView(ListView):
    model = Blancos
    template_name = 'inventario-blancos.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Blancos'
        return context

class BlancosCreateView(CreateView):
    model = Blancos
    form_class = BlancosForm
    template_name = 'blancos/crear.html'
    success_url = reverse_lazy('inventario:blancos_list')


class BlancosUpdateView(UpdateView):
    model = Blancos
    form_class = BlancosForm
    template_name = 'blancos/crear.html'
    success_url = reverse_lazy('inventario:blancos_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición una Categoria'
        context['action'] = 'edit'
        return context

class BlancosDeleteView(DeleteView):
    model = Blancos
    template_name = 'blancos/delete.html'
    success_url = reverse_lazy('inventario:blancos_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Categoria'
        return context







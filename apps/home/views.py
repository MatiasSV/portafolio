from email import message
from lib2to3.pygram import pattern_symbols
from typing import List
from django.shortcuts import get_object_or_404, render, redirect
from django import template
from django import forms
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView, View, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from datetime import datetime
from .models import *
from .forms import *
from .functions import comprobar_disponibilidad

# Create your views here.

######################## VISTAS CRUD DEPARTAMENTO ############################

class ADDONE_DEPARTAMENTO(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    try:
        model = DEPARTAMENTO
        form_class = formDEPARTAMENTO
        template_name = 'home/admin/dep_addone.html'
        success_url = reverse_lazy('dep_listall')
        success_message = "Departamento agregado correctamente"

    except Exception as e:
        message=f"Error al agregar departamento"

class DEPARTAMENTO_LISTALL(LoginRequiredMixin, ListView):
    model = DEPARTAMENTO
    template_name = 'home/admin/dep_listall.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DEPARTAMENTO_UPDATE(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = DEPARTAMENTO
    form_class = formDEPARTAMENTO
    template_name = 'home/admin/dep_addone.html'
    success_url = reverse_lazy('dep_listall')
    success_message = "Información de departamento actualizada correctamente"

def ELIMINAR_DEPARTAMENTO(request, id):
    depto = get_object_or_404(DEPARTAMENTO, DEP_ID=id)

    if depto.EST_ID.EST_NOMBRE == 'Reservado':
        messages.error(request, 'No se puede eliminar un departamento reservado.')

    else:
        depto.delete()
        messages.success(request, "Departamento eliminado correctamente")

    return redirect(to="dep_listall")


###########################  VISTAS INVENTARIO DEPTO  #############################

def verDeptos(request):
    mostrarDeptos =DEPARTAMENTO.objects.all()
    return render(request, 'home/admin/inv_inventarios.html', {'data':mostrarDeptos})

def verDetallesInventario(request, id):
    depto = DEPARTAMENTO.objects.all()
    inventarioInfo = DEPARTAMENTO.objects.get(DEP_ID=id)

    # if request.method=="GET":
    #         return render(request,'home/admin/inv_addone.html', {'data':depto})

    if request.method=="POST":
        try:
            microondas = request.POST.get('microondas',False)
            if microondas =='on':
                microondas=True
            horno = request.POST.get('horno',False)
            if horno == 'on':
                horno=True
            INVENTARIO(INV_DEPARTAMENTO_id=id,INV_MICROONDAS=microondas,INV_HORNOELECTRICO=horno).save()
            messages.success(request, "Inventario agregado correctamente")
            return redirect(to="inventarios")

        except Exception as e:
            messages.success(request,'Inventario para departamento "'+request.POST['DEP_ID']+ '" ya existe')

    return render(request, 'home/admin/inv_inventarios.html', {'data':depto, 'verInventario':inventarioInfo})


# class INVENTARIO_UPDATE(UpdateView):
#     model = INVENTARIO
#     form_class = formINVENTARIO
#     template_name = 'home/admin/inv_addone.html'
#     success_url = reverse_lazy('dep_listall')
#     success_message = "Inventario añadido correctamente"





######################## VISTAS CRUD TOUR ############################

class TOUR_ADDONE(SuccessMessageMixin, CreateView):
    model = TOUR
    form_class = formTOUR
    template_name = 'home/admin/tou_addone.html'
    success_url = reverse_lazy('tou_listall')
    success_message = "Tour agregado correctamente"

class TOUR_LISTALL(ListView):
    model = TOUR
    template_name = 'home/admin/tou_listall.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TOUR_UPDATE(SuccessMessageMixin, UpdateView):
    model = TOUR
    form_class = formTOUR
    template_name = 'home/admin/tou_addone.html'
    success_url = reverse_lazy('tou_listall')
    success_message = "Información de tour actualizada correctamente" 

def ELIMINAR_TOUR(request, id):
    tour = get_object_or_404(TOUR, TOU_ID=id)
    tour.delete()
    messages.success(request, "Tour eliminado correctamente")
    return redirect(to="tou_listall")


######################## VISTAS CRUD TRANSPORTE ############################

class TRANSPORTE_ADDONE(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = TRANSPORTE
    form_class = formTRANSPORTE
    template_name = 'home/admin/tra_addone.html'
    success_url = reverse_lazy('tra_listall')
    success_message = "Transporte agregado correctamente"

class TRANSPORTE_LISTALL(ListView):
    model = TRANSPORTE
    template_name = 'home/admin/tra_listall.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TRANPORTE_UPDATE(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TRANSPORTE
    form_class = formTRANSPORTE
    template_name = 'home/admin/tra_addone.html'
    success_url = reverse_lazy('tra_listall')
    success_message = "Transporte actualizado correctamente"

def TRANSPORTE_DELETE(request, id):
    transporte = get_object_or_404(TRANSPORTE, TRA_ID=id)
    transporte.delete()
    messages.success(request, "Transporte eliminado correctamente")
    return redirect(to="tra_listall")



######################## vistas HOME_PRINCIPAL ########################

#Listado de DEPARTAMENTOS cliente
class DepartamentoListView(ListView):
    model = DEPARTAMENTO
    template_name = 'home/cliente/dep_list.html'

#Detalle de DEPARTAMENTO + Crear RESERVA
class DepartamentoDetailView(View):
    def get(self,request,*args, **kwargs):
        id = self.kwargs.get('DEP_ID', None)
        form = formRESERVA()
        depto_list = DEPARTAMENTO.objects.filter(DEP_ID=id)

        if len(depto_list)>0:
            depto = depto_list[0]
            context = {
                'depto_id': depto,
                'form':form,
            }
            return render(request,'home/cliente/dep_detail.html', context)

        else:
            messages.error(request, "ERROR. El departamento ingresado no existe.")
            return redirect(to='DepartamentoList')

    def post(self,request,*args, **kwargs):
        id = self.kwargs.get('DEP_ID', None)
        depto_list = DEPARTAMENTO.objects.filter(DEP_ID=id)
        form = formRESERVA(request.POST)

        if form.is_valid():
            data = form.cleaned_data

        dias_reserva = data['fecha_salida']-data['fecha_ingreso']

        disponibilidad_deptos =[]

        for departamento in depto_list:
            if comprobar_disponibilidad(departamento, data['fecha_ingreso'], data['fecha_salida']):
                disponibilidad_deptos.append(departamento)
            
        if len(disponibilidad_deptos)>0:
            departamento = disponibilidad_deptos[0]
            reserva = RESERVA.objects.create(
                RES_USER = self.request.user,
                RES_DEPARTAMENTO = departamento,
                RES_FECHA_INGRESO = data['fecha_ingreso'],
                RES_FECHA_SALIDA = data['fecha_salida'],
                RES_CANTIDAD_DIAS = dias_reserva.days,
                RES_ASISTENTES = data['asistentes'],
                RES_VALOR_RESERVA = (departamento.DEP_VALOR_DIA*dias_reserva.days)
            )
            reserva.save()
            messages.success(request, "Reserva realizada correctamente")
            return redirect(to='ReservaList')

        else:
            messages.error(request, "ERROR. El departamento se encuentra reservado para esa fecha. Por favor pruebe con otra.")
            return redirect('DepartamentoDetailView', DEP_ID=id)

#Listado de RESERVAS (Cliente/Funcionario)
class ReservaListView(ListView):
    model = RESERVA
    template_name = 'home/funcionario/res_list.html'

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            reserva_list = RESERVA.objects.all()
            return reserva_list

        else:
            reserva_list = RESERVA.objects.filter(RES_USER=self.request.user)
            return reserva_list

#Detalle de RESERVA
class ReservaDetailView(DetailView):
    model = RESERVA
    template_name = 'home/cliente/res_detail.html'

#Cancelar/eliminar RESERVA
def CANCELAR_RESERVA(request, id):
    reserva = get_object_or_404(RESERVA, RES_ID=id)
    reserva.delete()
    messages.success(request, "Reserva cancelada.")
    return redirect(to='ReservaList')



###############        vistas FUNCIONARIO            ####################


# class CHECKLIST_ADDONE(CreateView):

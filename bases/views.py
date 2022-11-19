from django.shortcuts import render
from django.views import generic
from django.shortcuts import render,redirect
import json
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin


class MixinFormInvalid:
    def form_invalid(self,form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

class Transferir(LoginRequiredMixin, generic.TemplateView):
    login_url = "bases:login"
    template_name="bases/transferir.html"

class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    login_url = "bases:login"
    template_name="bases/sin_privilegios.html"


class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin, MixinFormInvalid):
    login_url = 'bases:login'
    raise_exception=False
    redirect_field_name="redirecto_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url='bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    contexto = {}
    login_url='bases:login'

@login_required(login_url='/login/')
@permission_required('bases.add_avisos', login_url='bases:sin_privilegios')
def avisos_list(request):
    template_name="base/base.html"
    contexto = {}


    return render(request,template_name,contexto)


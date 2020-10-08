from .forms import FormularioUsuario
from django import forms
from django.views.generic import CreateView 
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Usuario
from django.shortcuts import render, redirect, HttpResponse, Http404



class SignUpView(CreateView):
    form_class = FormularioUsuario
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'   

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # Modificar en tiempo real
        return form
        
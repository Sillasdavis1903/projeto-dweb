from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *

class Home(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'solicitacao/index.html')

class AddMotorista(CreateView):
    model = Motorista
    template_name = 'solicitacao/solicitacoes/add-solicitacao.html'
    success_url = reverse_lazy('solicitacao:home')
    form_class = AddMotoristaForm

    def form_valid(self, form):
    	obj = form.save(commit=False)
    	obj.user = self.request.user
    	obj.save()
    	return super(AddMotorista, self).form_valid(form)

class AddCozinheiro(CreateView):
    model = Cozinheiro
    template_name = 'solicitacao/solicitacoes/add-solicitacao.html'
    success_url = reverse_lazy('solicitacao:home')
    form_class = AddCozinheiroForm

    def form_valid(self, form):
    	obj = form.save(commit=False)
    	obj.user = self.request.user
    	obj.save()
    	return super(AddCozinheiro, self).form_valid(form)

class AddProfessor(CreateView):
    model = Professor
    template_name = 'solicitacao/solicitacoes/add-solicitacao.html'
    success_url = reverse_lazy('solicitacao:home')
    form_class = AddProfessorForm

    def form_valid(self, form):
    	obj = form.save(commit=False)
    	obj.user = self.request.user
    	obj.save()
    	return super(AddProfessor, self).form_valid(form)

class AddPedreiro(CreateView):
    model = Pedreiro
    template_name = 'solicitacao/solicitacoes/add-solicitacao.html'
    success_url = reverse_lazy('solicitacao:home')
    form_class = AddPedreiroForm

    def form_valid(self, form):
    	obj = form.save(commit=False)
    	obj.user = self.request.user
    	obj.save()
    	return super(AddPedreiro, self).form_valid(form)

class AdmMotorista(ListView):
    model = Motorista
    template_name = 'solicitacao/solicitacoes/listagem.html'
    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Motorista.objects.all().order_by('-solicitacao')
        return super(AdmMotorista, self).get_context_data(**kwargs)

class AdmProfessor(ListView):
    model = Professor
    template_name = 'solicitacao/solicitacoes/listagem.html'
    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Professor.objects.all().order_by('-solicitacao')
        return super(AdmProfessor, self).get_context_data(**kwargs)

class AdmPedreiro(ListView):
    model = Pedreiro
    template_name = 'solicitacao/solicitacoes/listagem.html'
    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Pedreiro.objects.all().order_by('-solicitacao')
        return super(AdmPedreiro, self).get_context_data(**kwargs)

class AdmCozinheiro(ListView):
    model = Cozinheiro
    template_name = 'solicitacao/solicitacoes/listagem.html'
    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Cozinheiro.objects.all().order_by('-solicitacao')
        return super(AdmCozinheiro, self).get_context_data(**kwargs)

class UserMotorista(ListView):
    model = Motorista
    template_name = 'solicitacao/solicitacoes/listagem.html'
    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Motorista.objects.filter(user = self.request.user).order_by('-solicitacao')
        return super(UserMotorista, self).get_context_data(**kwargs)

class UserProfessor(ListView):
    model = Professor
    template_name = 'solicitacao/solicitacoes/listagem.html'
    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Professor.objects.filter(user = self.request.user).order_by('-solicitacao')
        return super(UserProfessor, self).get_context_data(**kwargs)

class UserPedreiro(ListView):
    model = Pedreiro
    template_name = 'solicitacao/solicitacoes/listagem.html'
    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Pedreiro.objects.filter(user = self.request.user).order_by('-solicitacao')
        return super(UserPedreiro, self).get_context_data(**kwargs)

class UserCozinheiro(ListView):
    model = Cozinheiro
    template_name = 'solicitacao/solicitacoes/listagem.html'
    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Cozinheiro.objects.filter(user = self.request.user).order_by('-solicitacao')
        return super(UserCozinheiro, self).get_context_data(**kwargs)

class Visualizar(View):
    def get(self, request, pk):
        cozinha = Cozinheiro.objects.filter(id = pk).first()
        pedreiro = Pedreiro.objects.filter(id = pk).first()
        motorista = Motorista.objects.filter(id = pk).first()
        professor = Professor.objects.filter(id = pk).first()
        if cozinha != None:
            return render(request, 'solicitacao/solicitacoes/visualizar.html', {'object': cozinha})
        elif pedreiro != None:
            return render(request, 'solicitacao/solicitacoes/visualizar.html', {'object': pedreiro})
        elif motorista != None:
            return render(request, 'solicitacao/solicitacoes/visualizar.html', {'object': motorista})
        else:
            return render(request, 'solicitacao/solicitacoes/visualizar.html', {'object': professor})
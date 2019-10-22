from django import forms

from .models import *

class AddMotoristaForm(forms.ModelForm):
  
  class Meta:
    model = Motorista
    fields = ('endereco', 'data', 'hora')
    labels = {
    	'endereco': 'Endereço',
    	'data': 'Data',
    	'hora': 'Hora',
    }
    widgets = {
      'data': forms.DateInput(),
      'hora': forms.TimeInput(),
      'endereco': forms.TextInput(),
    }

class AddPedreiroForm(forms.ModelForm):
  
  class Meta:
    model = Pedreiro
    fields = ('descricao',)
    labels = {
    	'descricao': 'Descrição',
    }
    widgets = {
      'descricao': forms.TextInput(),
    }

class AddProfessorForm(forms.ModelForm):
  
  class Meta:
    model = Professor
    fields = ('materia', 'descricao')
    labels = {
    	'materia': 'Matéria',
    	'descricao': 'Descrição',
    }
    widgets = {
      'descricao': forms.TextInput(),
    }

class AddCozinheiroForm(forms.ModelForm):
  
  class Meta:
    model = Cozinheiro
    fields = ('descricao',)
    labels = {
    	'descricao': 'Descrição',
    }
    widgets = {
      'descricao': forms.TextInput(),
    }
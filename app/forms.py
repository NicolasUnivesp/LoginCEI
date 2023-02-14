from django.forms import ModelForm
from app.models import Livros


class LivrosForm(ModelForm):
    class Meta:
        model = Livros
        fields = ['titulo', 'autor', 'ano', 'quantidade', 'disponivel']

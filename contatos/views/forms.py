from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from contatos.models import Contato
from django.contrib.auth.forms import UserCreationForm

class ContatoForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para seu usuário',
    )

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Aqui veio do init',
        # })

    class Meta:
        model = Contato
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'categoria', 'picture',)
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui',
        #         }
        #     )
        # }
    
    def clean(self):
        fisrt_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if fisrt_name == last_name:
            self.add_error(
                'last_name',
                ValidationError('Nome não pode ser igual ao primeiro nome', 
                                code='invalid')
            )
        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        #print(first_name)
        if first_name == 'abc' or first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError('Erro', code='invalid')
            )

        return first_name


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 
                  'username', 'password1', 'password2',)
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este e-mail já está em uso.")
        return email
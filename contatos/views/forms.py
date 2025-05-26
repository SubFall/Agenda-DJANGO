from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from contatos.models import Contato
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation

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
    

class RegisterUpdateForm(forms.ModelForm):

    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required',
        error_messages={
            'min_length': 'please, add more than 2 letters.'
        }
    )

    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required',
    )

    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
        )

    password2 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
        )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 
                  'username',)
        
    def clean_email(self):
        email = self.cleaned_data.get('email')

        qs = User.objects.filter(email=email)

        # Se estamos editando um usuário existente, excluímos ele mesmo da verificação
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        # Se restou algum usuário com esse email, lançamos erro
        if qs.exists():
            raise ValidationError("Este e-mail já está em uso.")

        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as e:
                self.add_error('password1', e)
        return password1
    
    def clean(self):


        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')

        if p1 and p2 and p1 != p2:
            self.add_error('password2', 
                           ValidationError('Senhas não batem')
                            )
            
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password1')

        if password:
            user.set_password(password)
        
        if commit:
            user.save()
        
        return user

        
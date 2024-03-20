from django import forms
from .models import MyUser, User1, User2

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SignupForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    group_choices = (
        ('group1', 'Проктор'),
        ('group2', 'Ученик'),
    )
    group = forms.ChoiceField(choices=group_choices, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2', 'group']

    def save(self, commit=True):
        user = super().save(commit=False)
        group = self.cleaned_data['group']
        if group == 'group1':
            user.groups.add(User1.objects.get(name='Проктор'))
        elif group == 'group2':
            user.groups.add(User2.objects.get(name='Ученик'))
        if commit:
            user.save()
        return user

class LogoutForm(forms.Form):
    pass


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'password')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user



class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
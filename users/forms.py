from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import  UserCreationForm, UserChangeForm
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError


class RegisterUserForm(forms.ModelForm):
    """ Ррегистрация пользователя """

    password1 = forms.CharField(label='Введите пароль', widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Введите пароль (повторно)', widget=forms.PasswordInput,
                                help_text='Введите тот же пароль еще раз для проверки')
    
    def clean_password(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
    
    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                "Введенные пароли не совпадают", code='password_mismatch')}
            raise ValidationError(errors)
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_activated = True
        if commit:
            user.save()
        
        return user
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
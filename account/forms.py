from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class Login(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs = {'placeholder': "Ім'я користувача"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {'placeholder': 'Пароль'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.check_password(password):
                raise forms.ValidationError('Error in Login or Password!')
        else:
            raise forms.ValidationError('Error in Login or Password!')
        return super().clean()



class Register(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', )

    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data['password2']
        raise forms.ValidationError('Error in passwords!')

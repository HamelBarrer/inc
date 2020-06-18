from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import (
    User,
)


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email', 'role'
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
            'role': 'Rol'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.dispatch import receiver
from django.db.models.signals import post_save


class User(AbstractUser):
    ROLE_CHOICES = {
        ('client', 'Cliente'),
        ('employee', 'Empleado'),
        ('provider', 'Proveedor'),
    }

    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    REQUIRED_FIELDS = ['email', 'role']

    def get_role(self):
        return getattr(self, self.role, None)


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Provider(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def set_user_rol(sender, instance, **kwargs):
    if kwargs.get('created', False):
        user = instance
        if instance.role == 'client':
            Client.objects.create(user=instance)
            group = Group.objects.get(name='cliente')
            user.groups.add(group)
        elif instance.role == 'employee':
            Employee.objects.cruate(user=instance)
            group = Group.objects.get(name='empleado')
            user.groups.add(group)
        else:
            Provider.objects.create(user=instance)
            group = Group.objects.get(name='proveedor')
            user.groups.add(group)

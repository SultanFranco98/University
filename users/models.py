from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    # exclude = ('',)

    def create_user(self, username, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not username:
            raise ValueError('Должно быть введено имя пользователя.')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, blank=False, unique=True, default='',
                                verbose_name='Имя пользователя')
    password = models.CharField(max_length=255, blank=False, null=False, verbose_name='Пароль')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    is_student = models.BooleanField(default=False, verbose_name='Студент')
    is_teacher = models.BooleanField(default=False, verbose_name='Деканат')
    is_staff = models.BooleanField(default=False, verbose_name='Админ')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-date_joined']

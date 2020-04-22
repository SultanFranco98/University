# Generated by Django 2.2.3 on 2020-04-22 16:51

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, default='', max_length=255, unique=True, verbose_name='Имя пользователя')),
                ('password', models.CharField(max_length=255, verbose_name='Пароль')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('is_student', models.BooleanField(default=False, verbose_name='Студент')),
                ('is_teacher', models.BooleanField(default=False, verbose_name='Деканат')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Админ')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['-date_joined'],
            },
            managers=[
                ('objects', users.models.CustomUserManager()),
            ],
        ),
    ]

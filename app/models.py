from django.db import models
from django.conf import settings


class Facultys(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='Факультет')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'


class Specialitys(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='Кафедра')
    faculty = models.ForeignKey(Facultys, on_delete=models.SET_NULL, null=True, verbose_name='Факультет')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'


class Groups(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='Группа')
    speciality = models.ForeignKey(Specialitys, on_delete=models.SET_NULL, null=True, verbose_name='Кафедра')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Students(models.Model):
    select_gender = (
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский')
    )

    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    dateOfBirth = models.DateField(verbose_name='Дата рождения')
    email = models.EmailField(verbose_name='email')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    faculty = models.ForeignKey(Facultys, on_delete=models.SET_NULL, null=True, verbose_name='Факультет')
    speciality = models.ForeignKey(Specialitys, on_delete=models.SET_NULL, null=True, verbose_name='Кафедра')
    group = models.ForeignKey(Groups, on_delete=models.SET_NULL, null=True, verbose_name='Группа')
    gender = models.CharField(max_length=8, choices=select_gender, verbose_name='Пол')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                             verbose_name='Пользователь')

    def get_student_info(self):
        return "ФИО:\t{}\n\nФакультет:\t {}\n\n Кафедра:\t {}\n\nГруппа:\t{}\n\nДата рождения:\t{}\n\nПол:\t{}\n\nemail:\t{}\n\nТелефон:\t{}".format(
            self.full_name, self.faculty, self.speciality, self.group, self.dateOfBirth, self.gender, self.email,
            self.phone)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

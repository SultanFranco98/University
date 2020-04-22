from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegisterForm
from app.forms import StudentsForm
from .models import Users


# Create your views here.

class UsersLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm


class UsersLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'users/logout.html'

def register(request):
    errors = []
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        student_form = StudentsForm(request.POST)

        for user in Users.objects.all():
            if user.username == request.POST['username']:
                errors.append('Такой логин уже существует!')
        if request.POST['password1'] != request.POST['password2']:
            errors.append('Ваши пароли не совпадают!')

        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            student = student_form.save()
            user.is_student = True
            student.user = user
            user.save()
            student.save()
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        student_form = StudentsForm()
    return render(request, 'users/register.html',
                  {'user_form': user_form, 'student_form': student_form, 'errors': errors})
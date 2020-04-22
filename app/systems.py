from django.views import View
from django.shortcuts import render
from .models import Specialitys, Groups


class Home(View):
    def get(self, request):
        return render(request, 'app/base.html')


def load_specialitys(request):
    faculty_id = request.GET.get('faculty')
    specialitys = Specialitys.objects.filter(faculty_id=faculty_id).order_by('title')
    print(specialitys)
    return render(request, 'references/dropdown.html', {'specialitys': specialitys})


def load_groups(request):
    speciality_id = request.GET.get('speciality')
    groups = Groups.objects.filter(speciality_id=speciality_id).order_by('title')
    print(groups)
    return render(request, 'references/dropdown-group.html', {'groups': groups})

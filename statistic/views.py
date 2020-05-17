from django.shortcuts import render,redirect
from home.models import Profile
from django.contrib import auth
from django.contrib import messages

from car.models import Car
from django.db.models import Count, Q
# Create your views here.

def statistic(req):
    cur_user = req.user

    if cur_user.is_authenticated:
        user = Profile.objects.get(user=auth.get_user(req))

        return render(req, "statistic_Service.html",{'user':user})
    else:
        messages.info(req, '로그인 후 이용가능합니다.')
        return redirect('home:index')

def stat(req):
    cur_user = req.user

    if cur_user.is_authenticated:
        user = Profile.objects.get(user=auth.get_user(req))


        cctv = req.POST['cctv']

        dataset = Car.objects.values('brand').annotate(car_count=Count('brand'))

        context = {
            'cctv': cctv,
            'user': user,
            'dataset': dataset
        }
        return render(req, "statistic_Service.html", context)

    else:
        messages.info(req, '로그인 후 이용가능합니다.')
        return redirect('home:index')

from django.shortcuts import render
import datetime

from social.models import Swiped
from user.lib.http import render_json
from user.models import Profile


def get_recommendation(request):
    ...
    # uid = request.user.id
    # profile = Profile.objects.get(id=uid)
    # # 获取筛选条件
    # cond = get_screening_cond(profile)




def match(request):
    pass


def like(request, op_sid):

    swiped = Swiped()
    swiped.uid = request.user.id
    swiped.sid = request.POST.get('sid')
    swiped.mark = '喜欢'
    swiped.save()
    return render_json(swiped)


def super_like(request):
    pass


def dont_like(request):
    pass


def goback(request):
    pass


def get_liked(request):
    pass



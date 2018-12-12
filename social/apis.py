from django.shortcuts import render

from user.models import Profile


def get_recommendation(request):
    uid = request.user.id
    profile = Profile.objects.get(id=uid)
    # 获取筛选条件
    cond = get_screening_cond(profile)




def match(request):
    pass


def like(request):
    pass


def super_like(request):
    pass


def dont_like(request):
    pass


def goback(request):
    pass


def get_liked(request):
    pass



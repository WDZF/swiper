from django.core.cache import cache
from django.shortcuts import render

from user.common.errors import OK, Fail
from user.lib.sms import get_code, check_vcode
from user.lib.sms import send_msg
from user.lib.http import render_json
from user.models import User


def get_vcode(request):
    '''获取验证码'''
    phonenum = request.GET.get('phonenum')
    vcode = get_code(6)
    res = send_msg(phonenum, vcode)
    data = {
        "msg":"数据发送成功"
    }
    cache.set('Vcode-%s' % phonenum, vcode, timeout=3600)
    return render_json(data, OK)


def login(request):
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    if check_vcode(phonenum, vcode):
        user, created = User.objects.get_or_create(phonenum=phonenum)
        print(user.phonenum, created)
        request.session['uid'] = user.id
        return render_json(user.to_dict(), OK)
    else:
        return render_json(None, Fail)


def register(request):
    return render()


def profile_show(request):
    return render()


def profile_modify(request):
    return render()


def profile_upload(request):
    return render()



from django.utils.deprecation import MiddlewareMixin

from user.common import errors
from user.models import User
from user.lib.http import render_json


class AuthMiddleware(MiddlewareMixin):
    white_list = [
        'user/vcode',
        'user/login'
    ]

    def process_request(self, request):
        if request.path in self.white_list:
            return
        uid = request.session.get('uid', None)
        if not uid:
            return render_json(None, errors.LOGIN_REQUIRE)
        else:
            try:
                user = User.objects.get(pk=uid)
            except User.DoesNotExist:
                return render_json(None, errors.VCODE_ERROR)
            else:
                request.user = user


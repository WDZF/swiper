from django.db import models

from user.models import BaseModel


class Swiped(BaseModel):
    '''滑动记录表'''
    like_type = (
        ("喜欢", "喜欢"),
        ("不喜欢", "不喜欢"),
        ("超级喜欢", "超级喜欢"),
    )
    uid = models.IntegerField(null=False)
    sid = models.IntegerField(null=False)
    mark = models.CharField(choices=like_type, max_length=16)
    time = models.DateTimeField(auto_now=True)


class Friend(BaseModel):
    '''互相喜欢表'''
    uid1 = models.IntegerField(null=False)
    uid2 = models.IntegerField(null=False)



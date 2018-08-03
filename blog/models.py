import re
from django.db import models
from django.forms import ValidationError


# Create your models here.
def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    # title = models.CharField(max_length=100)
    # title = models.CharField(max_length=100,
    #     choices = (
    #         ('제목1', '제목1 레이블'),
    #         ('제목2', '제목2 레이블'),
    #         ('제목3', '제목3 레이블'),
    #     ))
    title = models.CharField(max_length=100, verbose_name='제목',help_text='포스팅 제목을 입력해주세요. 100자 내외')
    content = models.TextField(verbose_name='내용')
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
        validators=[lnglat_validator],
        help_text='위도,경도 포멧으로 받겠습니다.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
import re
from django.db import models
from django.forms import ValidationError
from django.conf import settings
from django.urls import reverse


# Create your models here.
def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )

    # title = models.CharField(max_length=100)
    # title = models.CharField(max_length=100,
    #     choices = (
    #         ('제목1', '제목1 레이블'),
    #         ('제목2', '제목2 레이블'),
    #         ('제목3', '제목3 레이블'),
    #     ))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.DO_NOTHING, related_name='blog_post_set')
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name='제목',help_text='포스팅 제목을 입력해주세요. 100자 내외')
    content = models.TextField(verbose_name='내용')
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
        validators=[lnglat_validator],
        help_text='위도,경도 포멧으로 받겠습니다.')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])
    # reserve_url함수를 더 유용하게 해준다고함...(아직 잘 이해 안됨)

    def __str__(self):
        return self.title
    # 그냥 object라고 뜨는 걸 제목으로 띄어줌




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.DO_NOTHING,)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



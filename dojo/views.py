from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.
def mysum(request, numbers):
    # result = sum(map(int, numbers.split("/")))
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name,age))


def post_list1(request):
    name = '상현'
    return  HttpResponse('''
    <h1>AskDjango</h1>
    <p>{name}</p>
    <p>여러분은 파이썬&장고 마스터입니다!</p>
    '''.format(name=name))


def post_list2(request):
    name = '상현'
    return render(request, 'dojo/post_list.html', {'name': name})


def post_list3(request):
    return JsonResponse({
        'message': '안녕 파이썬&장고',
        'items': ['파이썬', '장고', 'Celery', 'Azu'],
        }, json_dumps_params={'ensure_ascii': False}
    )
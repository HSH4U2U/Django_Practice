from django.http import HttpResponse
from django.views.generic import View, TemplateView

class PostListView1(View):
    def get(self, request):
        name = '상현'
        html = '''
            <h1>AskDjango</h1>
            <p>{name}</p>
            <p>여러분은 파이썬&장고 마스터입니다!</p>
        '''.format(name=name)
        return HttpResponse(html)

post_list1 = PostListView1.as_view()


class PostListVeiw2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '공유'
        return context


post_list2 = PostListVeiw2.as_view()


# class PostListView3(object):
#     pass
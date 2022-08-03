from django_micro import configure, route, run
from django.http import HttpResponse

DEBUG = True
html = '''
<div style='color:skyblue;font-size:100px'>Hello Django</div>
'''
configure(locals())

@route('', name='home')
def homepage(request):
    return HttpResponse(html)


application = run()

# 通过命令 python DjangeNote.py runserver 运行

from django.http import HttpResponse
from django.template import Context, loader


def home(request):
    t = loader.get_template('index.html')
    return HttpResponse(t.render(Context({})))

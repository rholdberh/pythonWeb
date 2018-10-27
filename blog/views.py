from django.shortcuts import render_to_response
from blog.utils import MailUtils


def index(requet):
    prepMessage = MailUtils.getBodyMesage("2018-12-11")
    content = {
        'body': prepMessage
    }
    return render_to_response('index.html', content)


def request_page(request):
    return render_to_response('done.html')

from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from blog.utils import MailUtils



def index(requet):
    prepMessage = MailUtils.getBodyMesage("2018-12-11")
    content = {
        'body': prepMessage
    }
    return render_to_response('index.html', content)


def request_page(request):
    return render_to_response('done.html')

@csrf_exempt
def save_value(request):
    firstName = request.POST['fname']
    print("BLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print(firstName)
    return render_to_response('done.html')


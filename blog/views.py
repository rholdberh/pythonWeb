from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from blog.utils import MailUtils
from .forms import CredentialsForm


def index(requet):
    prepMessage = MailUtils.getBodyMesage("2018-12-11")
    emails = MailUtils.getListOfRecepients()
    credForm = CredentialsForm()

    content = {
        'body': prepMessage,
        'emails': emails,
        'form': credForm
    }
    return render_to_response('index.html', content)


def request_page(request):
    return render_to_response('done.html')


@csrf_exempt
def getCredentials(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CredentialsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            firstName = form.cleaned_data['firstName']
            content = {
                'user': firstName,
            }
            return render_to_response('done.html', content)
        else:
            return render_to_response('error.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CredentialsForm()

    return render(request, 'error.html', {'form': form})

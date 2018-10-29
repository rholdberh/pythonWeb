from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from blog.utils import MailUtils
from .forms import CredentialsForm, UserCheckbox


def index(requet):
    prepMessage = MailUtils.getBodyMesage("2018-12-11")
    emails = MailUtils.getListOfRecepients()
    credForm = CredentialsForm()

    checkBoxes = UserCheckbox()

    content = {
        'body': prepMessage,
        'credentialsForm': credForm,
        'emails': emails,
        'userCheckBoxes': checkBoxes,
    }
    return render_to_response('index.html', content)


def request_page(request):
    return render_to_response('done.html')


@csrf_exempt
def getCredentials(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        credentialsForm = CredentialsForm(request.POST)
        # check whether it's valid:
        if credentialsForm.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            firstName = credentialsForm.cleaned_data['firstName']


            emails = request.POST.getlist('email')

            emails2 = request.POST.getlist('emailChoses')

            print("BLAAAAAAAAAAAAAAAAAAAAA")
            print(emails2)
            content = {
                'user': emails2,
            }
            return render_to_response('done.html', content)
        else:
            return render_to_response('error.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        credentialsForm = CredentialsForm()

    return render(request, 'error.html', {'form': credentialsForm})

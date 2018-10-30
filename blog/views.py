from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from .forms import CredentialsForm, UserCheckbox, EmailForm


def index(requet):
    credForm = CredentialsForm()
    emailTextArea = EmailForm()
    checkBoxes = UserCheckbox()

    content = {
        'credentialsForm': credForm,
        'userCheckBoxes': checkBoxes,
        'emailTextArea': emailTextArea,
    }
    return render_to_response('index.html', content)


def request_page(request):
    return render_to_response('done.html')


@csrf_exempt
def submitMail(request):
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

            emails = request.POST.getlist('emailChoses')

            content = {
                'user': emails,
            }
            return render_to_response('done.html', content)
        else:
            return render_to_response('error.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        credentialsForm = CredentialsForm()

    return render(request, 'error.html', {'form': credentialsForm})

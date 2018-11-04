from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import MailForm, UploadFileForm
from webProject.settings import BASE_DIR
import os


def index(request):
    mail_form = MailForm()
    upload_form = UploadFileForm()
    content = {
        'mail_form': mail_form,
        'upload_form': upload_form,
    }
    return render(request, 'index.html', content)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('index')

    return render_to_response('error.html')


def done(request):
    return render(request, 'done.html')


def submitMail(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        mail_form = MailForm(request.POST)

        if mail_form.is_valid():
            emails = mail_form.cleaned_data['emailChoses']
            message_body = mail_form.cleaned_data['email']
            subject = mail_form.cleaned_data['subject']
            # obj_mail = Mail()
            # obj_mail.send_mail(message_body, subject, emails)

            request.session['user'] = emails
            request.session['mail_body'] = message_body
            return redirect('done-page')
        else:
            return render_to_response('error.html')

    else:
        return render(request, 'error.html')


def handle_uploaded_file(f):
    with open(os.path.join(BASE_DIR, 'resources/reportMail.txt'), 'wb+') as destination:
        for chunk in f.chunks():
            print('CHUNK')
            print(chunk)
            destination.write(chunk)
    print('FILE UPDATED')
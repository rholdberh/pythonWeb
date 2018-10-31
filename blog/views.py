from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from blog.utils.Mail import Mail
from .forms import MailForm


def index(requet):
    mail_form = MailForm()
    content = {
        'mail_form': mail_form,
    }
    return render_to_response('index.html', content)


def request_page(request):
    return render_to_response('done.html')


@csrf_exempt
def submitMail(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        mail_form = MailForm(request.POST)

        if mail_form.is_valid():
            emails = mail_form.cleaned_data['emailChoses']
            message_body = mail_form.cleaned_data['email']

            # obj_mail = Mail()
            # obj_mail.send_mail(message_body, 'bla', emails)

            content = {
                'user': emails,
                'mail_body': message_body,
            }
            return render_to_response('done.html', content)
        else:
            return render_to_response('error.html')

    else:
        return render(request, 'error.html')

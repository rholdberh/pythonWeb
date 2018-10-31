from django import forms

from blog.utils import MailUtils


class MailForm(forms.Form):
    prep_subject = 'BLA'
    emails = MailUtils.getListOfRecepients()
    userChoices = [(v, v) for v in emails]
    emailChoses = forms.MultipleChoiceField(
        choices=userChoices,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkmark'}),
        label=False)

    subject = forms.CharField(label='Subject', initial=prep_subject)
    prepMessage = MailUtils.getBodyMesage()
    email = forms.CharField(
        widget=forms.Textarea(),
        label='Mail',
        initial=prepMessage)

from django import forms

from blog.utils import MailUtils


class UserCheckbox(forms.Form):
    emails = MailUtils.getListOfRecepients()
    userChoices = [(v, v) for v in emails]
    emailChoses = forms.MultipleChoiceField(choices=userChoices, widget=forms.CheckboxSelectMultiple)


class CredentialsForm(forms.Form):
    firstName = forms.CharField(label='firstName', max_length=5)
    lastName = forms.CharField(label='lastName', max_length=5)

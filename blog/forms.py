from django import forms

from blog.utils import MailUtils


class UserCheckbox(forms.Form):
    emails = MailUtils.getListOfRecepients()
    userChoices = [(v, v) for v in emails]
    emailChoses = forms.MultipleChoiceField(
        choices=userChoices,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkmark'}),
        label=False)


class CredentialsForm(forms.Form):
    firstName = forms.CharField(label='Name', max_length=10)
    lastName = forms.CharField(label='Surname', max_length=10)


class EmailForm(forms.Form):
    prepMessage = MailUtils.getBodyMesage()
    email = forms.CharField(
        widget=forms.Textarea(),
        label='Mail',
        initial=prepMessage)


class MailForm(forms.Form):
    emails = MailUtils.getListOfRecepients()
    userChoices = [(v, v) for v in emails]
    emailChoses = forms.MultipleChoiceField(
        choices=userChoices,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkmark'}),
        label=False)

    userName = forms.CharField(label='User', max_length=10)
    prepMessage = MailUtils.getBodyMesage()
    email = forms.CharField(
        widget=forms.Textarea(),
        label='Mail',
        initial=prepMessage)

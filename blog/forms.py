from django import forms

from blog.utils.Utils import Utils


class MailForm(forms.Form):
    utils = Utils()
    prep_subject = 'BLA'
    emails = utils.getListOfRecepients()
    userChoices = [(v, v) for v in emails]
    emailChoses = forms.MultipleChoiceField(
        choices=userChoices,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkmark'}),
        label=False)

    subject = forms.CharField(label='Subject', initial=prep_subject)
    prepMessage = utils.getBodyMesage()
    email = forms.CharField(
        widget=forms.Textarea(),
        label='Mail',
        initial=prepMessage)

class UploadFileForm(forms.Form):
    file = forms.FileField()


from .models import Document
class UploadFileForm2(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', )
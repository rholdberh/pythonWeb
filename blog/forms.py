from django import forms


class UserlistForm(forms.Form):
    users = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                      label="Notify and subscribe users to this post:")


class CredentialsForm(forms.Form):
    firstName = forms.CharField(label='firstName', max_length=5)
    lastName = forms.CharField(label='lastName', max_length=5)

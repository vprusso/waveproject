from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Please upload a comma separated file:'
    )

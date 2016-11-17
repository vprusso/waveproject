from django import forms


def validate_file_extension(value):
        if not value.name.endswith('.csv'):
            raise forms.ValidationError("Only CSV file is accepted")

class UploadFileForm(forms.Form):
    docfile = forms.FileField(
        label='Select a CSV file to import:',
        validators=[validate_file_extension]
    )
    

    

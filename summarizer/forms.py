from django import forms
from .models import SpreadSheetFile
from django.core.exceptions import ValidationError


class CSVForm(forms.ModelForm):
    class Meta:
        model = SpreadSheetFile
        fields = ('file', )

    def clean(self):
        file = self.cleaned_data.get('file')
        file_extension = file.name.split('.')[-1]
        if file_extension not in self.Meta.model.FILE_EXTENSIONS:
            raise ValidationError(
                f'Not a valid file, allowed files are {", ".join(self.Meta.model.FILE_EXTENSIONS)}'
            )
        
    def save(self, request):
        model = self.Meta.model
        csv_instance = model.objects.create(
            uploader=request.user, 
            **self.cleaned_data
        )
        return csv_instance
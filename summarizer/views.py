from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from .summarizer_functions import SpreadSheetSummarizer

from .forms import (
    CSVForm
)

from .models import (
    SpreadSheetFile
)


class HomeView(LoginRequiredMixin ,TemplateView):
    template_name = 'home.html'


class UploadCSVView(LoginRequiredMixin, FormView):
    form_class = CSVForm
    template_name = 'upload_csv.html'
    success_url = reverse_lazy('summarizer:success_upload')

    def form_valid(self, form):
        file_instance = form.save(request=self.request)
        summarizer_obj = SpreadSheetSummarizer(file_instance=file_instance)
        if summarizer_obj.validate_columns():
            cleaned_data = summarizer_obj.summarize_spreadsheet_data()
            print(cleaned_data)

            return super().form_valid(form=form)
        file_instance.delete()
        form.add_error(
            'file',
            f'Invalid columns, the file should have {", ".join(self.form_class.Meta.model.REQUIRED_COLUMNS)}'
        )
        return super().form_invalid(form=form)


# class SuccessUploadView(LoginRequiredMixin, View):
#     def get(self, *args, **kwargs):
#         #file_uuid = self.request.session.get('file_instance_uuid')
#         #file_instance = SpreadSheetFile.objects.get_object_or_none(uuid=file_uuid)
#         file_instance = self.request.summarizer_obj.file_instance
#         return render(
#             self.request, 
#             'csv_summarizer.html', 
#             context={
#                 'file_name': file_instance.file.name.split('/')[-1]
#             }
#         )


# class ViewSpreadSheetDataView(LoginRequiredMixin):pass



# class SummarizeCSVView(LoginRequiredMixin, View):
#     def get(self, *args, **kwargs):
#         cleaned_data = self.request.summarizer_obj.clean_data()


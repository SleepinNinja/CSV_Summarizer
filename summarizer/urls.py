from django.urls import path
from .views import HomeView, UploadCSVView
# SummarizeCSVView, SuccessUploadView


app_name = 'summarizer'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload_file/', UploadCSVView.as_view(), name='upload_file'),
    # path('success_upload', SuccessUploadView.as_view(), name='success_upload'),
    # path('summarize/', SummarizeCSVView.as_view(), name='summarize')
]
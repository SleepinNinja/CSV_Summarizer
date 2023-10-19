from django.db import models
from .model_manager import SpreadSheetFileManager
from authentication.models import CustomUser
from django.conf import settings
import uuid
import datetime
import os

def file_upload_location(instance, file_name:str)->str:
    """Returns csv file being uploaded by user by creating folder structure like
    /media/username/csv_files/date/file_name.csv

    Args:
        instance (CSVFile): Object of CSVFile model
        file_name (str): Name of the csv file being uploaded.

    Returns:
        str: Folder path where csv file will be uploaded.
    """
    todays_date = datetime.datetime.now()
    formatted_date = todays_date.strftime('%d-%m-%yy')
    file_path = [
        'csv_files',
        instance.uploader.username,
        formatted_date,
        file_name
    ]
    return os.path.join(*file_path)


class SpreadSheetFile(models.Model):
    FILE_EXTENSIONS = ["xlsx","csv"]
    REQUIRED_COLUMNS = sorted(['id', 'date', 'present value', 'previous value', 'remarks'])
    
    uploader = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    file = models.FileField(upload_to=file_upload_location)

    objects = SpreadSheetFileManager()

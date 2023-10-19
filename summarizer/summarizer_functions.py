import pandas as pd
from .models import SpreadSheetFile
from datetime import datetime


class SpreadSheetSummarizer:
    def __init__(self, file_instance):
        self.file_instance = file_instance
        self.data_frame = self.create_data_frame(file_instance=self.file_instance)

    def create_data_frame(self, file_instance:SpreadSheetFile=None):
        # todo: need to convert filenames from space to _ eg: previous value to previous_vaue
        #f = df.rename(columns={'OldColumnName': 'NewColumnName'})
        file_path = file_instance.file.path
        file_extension = file_path.split('.')[-1]
        data_frame = pd.read_csv(file_path) if file_extension == 'csv' else pd.read_excel(file_path)
        return data_frame

    def validate_columns(self)->bool:
        if sorted(list(map(str.lower, self.data_frame.columns))) != SpreadSheetFile.REQUIRED_COLUMNS:
            return False
        return True

    def clean_spreadsheet_data(self)->dict:
        spreadsheet_data = self.data_frame.to_dict()
        dates = spreadsheet_data.get('date')
        present_value = spreadsheet_data.get('present value')
        previous_value = spreadsheet_data.get('previous value')

        for row in dates.keys():
            date_time_obj = datetime.strptime(dates[row], '%Y-%m-%d %H:%M:%S')
            time_stamp = date_time_obj.timestamp()
            dates[row] = time_stamp
            previous_value[row] = round(previous_value[row], 6)
            previous_value[row] = round(previous_value[row], 6)

        return spreadsheet_data

    def summarize_spreadsheet_data(self)->bool:
        spreadsheet_cleaned_data = self.clean_spreadsheet_data()
        previous_values = spreadsheet_cleaned_data.get('previous value')
        present_values = spreadsheet_cleaned_data.get('present value')
        difference = [present_values[row] - previous_values[row] for row in previous_values.keys()]
        self.data_frame['difference'] = difference
        match_percentage = [round(100 - difference[row]) for row in len(difference)]
        self.data_frame['match_percentage'] = match_percentage
        match = [True if int(match_percentage) == 100 else False]
        self.data_frame['match'] = match





# file_instance = SpreadSheetFile.objects.first()

# ss = SpreadSheetSummarizer(file_instance=file_instance)
# ss.summarize_spreadsheet_data()
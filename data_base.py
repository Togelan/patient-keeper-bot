import pandas as pd
import os
from datetime import datetime
from data_processing import DataProcessing


class DataBase:
    def __init__(self, name_doctor: str, chat_id: int):
        self.file_name = 'data/' + name_doctor + "_" + str(chat_id) + ".csv"
        self.data_processing = DataProcessing()

    def check_file_existence(self) -> bool:
        if os.path.isfile(self.file_name):
            return True
        else:
            self.create_file()
            return False

    def create_file(self) -> None:
        df = pd.DataFrame(columns=['FIO', 'Birthdate', 'Visiting time'])
        df.to_csv(self.file_name, index=False, encoding='utf-8')

    def record_patient(self, patient_fio: str, patient_birthdate: str, visiting_time: str) -> None:
        df = pd.read_csv(self.file_name)

        new_record = pd.DataFrame(
            {'FIO': [patient_fio], 'Birthdate': [patient_birthdate], 'Visiting time': [visiting_time]})
        df = pd.concat([df, new_record], ignore_index=True)

        df.to_csv(self.file_name, index=False, encoding='utf-8')

    def get_today_patients(self) -> tuple:
        df = pd.read_csv(self.file_name)
        df['Visiting time'] = df['Visiting time'].apply(lambda x: datetime.strptime(x, "%d.%m.%Y %H.%M.%S").date())

        today = datetime.now().date().strftime("%Y-%m-%d")

        today_patients = df[df['Visiting time'].astype(str) == today]
        today_patients_list = today_patients['FIO'].to_numpy().tolist()
        special_string_view_patients = self.data_processing.create_specific_string(today_patients_list)

        return str(len(today_patients_list)), special_string_view_patients

    def get_need_day_patients(self, need_date: str) -> str:
        df = pd.read_csv(self.file_name)
        df['Visiting time'] = df['Visiting time'].apply(lambda x: datetime.strptime(x, "%d.%m.%Y %H.%M.%S").date())

        need_date_datetime_obj = datetime.strptime(need_date, '%d.%m.%Y')
        formatted_need_date = need_date_datetime_obj.strftime('%Y-%m-%d')

        need_date_patients = df[df['Visiting time'].astype(str) == str(formatted_need_date)]

        need_date_patients_list = need_date_patients['FIO'].to_numpy().tolist()
        special_string_view_patients = self.data_processing.create_specific_string(need_date_patients_list)

        return special_string_view_patients

    def get_week_patients(self) -> list:
        pass

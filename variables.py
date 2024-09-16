import telebot
from validate_data import ValidationData
from data_processing import DataProcessing


class Variables:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Variables, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_bot'):
            self._bot = telebot.TeleBot('7439522328:AAHg588AAQ2j5ohyQrCkA1nn6a_ryEozlYA')
            self._input_text_flag = None
            self._reaction_buttons_flag = None
            self._obj_data_base = None
            self._obj_data_processing = DataProcessing()
            self._fio = ''
            self._birthdate = ''

    @property
    def input_text_flag(self) -> None | str:
        return self._input_text_flag

    @input_text_flag.setter
    def input_text_flag(self, value: str) -> None:
        self._input_text_flag = value

    @property
    def reaction_buttons_flag(self) -> None | str:
        return self._reaction_buttons_flag

    @reaction_buttons_flag.setter
    def reaction_buttons_flag(self, value: str) -> None:
        self._reaction_buttons_flag = value

    @property
    def obj_data_base(self):
        return self._obj_data_base

    @obj_data_base.setter
    def obj_data_base(self, value: str) -> None:
        self._obj_data_base = value

    @property
    def fio(self) -> str:
        return self._fio

    @fio.setter
    def fio(self, value: str) -> None:
        self._fio = value

    @property
    def birthdate(self) -> str:
        return self._birthdate

    @birthdate.setter
    def birthdate(self, value: str) -> None:
        self._birthdate = value

    def get_bot(self):
        return self._bot

    @staticmethod
    def validate_fio(fio: str) -> bool:
        return ValidationData().validate_fio(fio)

    @staticmethod
    def validate_birthdate(birth: str) -> bool:
        return ValidationData().validate_birthdate(birth)

    def get_obj_data_processing(self):
        return self._obj_data_processing

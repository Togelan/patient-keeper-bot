from telebot.types import CallbackQuery
from variables import Variables
from abc import ABC, abstractmethod


class CallbackTemplate(ABC):
    def __init__(self, callback: CallbackQuery):
        self.callback = callback
        self.bot = Variables().get_bot()

    @abstractmethod
    def execute_callback(self):
        pass
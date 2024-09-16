from .callback_template import CallbackTemplate
from telebot.types import CallbackQuery
from bot_components.variables import Variables


class CleanFileCallback(CallbackTemplate):
    def __init__(self, callback: CallbackQuery):
        super().__init__(callback)

    def execute_callback(self):
        if self.callback.data == 'clean_file':
            Variables().obj_data_base.create_file()
            self.bot.send_message(self.callback.message.chat.id, 'Данные файла были удалены')
            Variables().reaction_buttons_flag = None
        elif self.callback.data == 'use_old_data':
            self.bot.send_message(self.callback.message.chat.id, 'Данные файла не были изменены')
            Variables().reaction_buttons_flag = None


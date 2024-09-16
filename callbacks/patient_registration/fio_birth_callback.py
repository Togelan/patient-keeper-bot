from callbacks.callback_template import CallbackTemplate
from telebot.types import CallbackQuery
from variables import Variables


class FioBirthCallback(CallbackTemplate):
    def __init__(self, callback: CallbackQuery):
        super().__init__(callback)

    def execute_callback(self):
        if self.callback.data == 'input_fullname':
            self.bot.send_message(self.callback.message.chat.id,
                                  f'Укажите ФИО пациента.\n(Пример: Петрович Иван Васильевич)')
            Variables().input_text_flag = 'input_fullname'
            Variables().reaction_buttons_flag = 'only_input_fio'
        elif self.callback.data == 'input_birthdate':
            self.bot.send_message(self.callback.message.chat.id, f'Укажите дату рождения пациента.\n(Пример: 24.04.2002)')
            Variables().input_text_flag = 'input_birthdate'
            Variables().reaction_buttons_flag = 'only_input_birthdate'


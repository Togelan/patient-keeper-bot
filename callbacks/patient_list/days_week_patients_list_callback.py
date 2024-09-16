from callbacks.callback_template import CallbackTemplate
from telebot.types import CallbackQuery
from variables import Variables


class DayPatientListCallback(CallbackTemplate):
    def __init__(self, callback: CallbackQuery):
        super().__init__(callback)

    def execute_callback(self):
        need_patients = Variables().obj_data_base.get_need_day_patients(self.callback.data)
        if len(need_patients) == 0:
            self.bot.send_message(self.callback.message.chat.id, f'{self.callback.data} пациентов не было')
        else:
            self.bot.send_message(self.callback.message.chat.id,
                                  f'Пациенты, пришедшие за {self.callback.data}:\n\n{need_patients}')
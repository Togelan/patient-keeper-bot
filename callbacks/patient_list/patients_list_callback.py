from callbacks.callback_template import CallbackTemplate
from callbacks.patient_list.days_week_patients_list_callback import DayPatientListCallback
from telebot.types import CallbackQuery
from variables import Variables
from commands.commands_patients_list.command_days_week_buttons import DaysWeekCommand



class PatientListCallback(CallbackTemplate):
    def __init__(self, callback: CallbackQuery):
        super().__init__(callback)

    def execute_callback(self):
        if self.callback.data == "today's patients list":
            tuple_amount_list_patients = Variables().obj_data_base.get_today_patients()
            amount_patients = tuple_amount_list_patients[0]
            list_patients = tuple_amount_list_patients[1]
            self.bot.send_message(self.callback.message.chat.id,
                                  f'За сегоднящний день пришло {amount_patients} пациента(ов):\n\n{list_patients}')
        elif self.callback.data == 'day of week patients list':
            DaysWeekCommand(self.callback.message).execute()
        elif self.callback.data in Variables().get_obj_data_processing().get_week_dates():
            DayPatientListCallback(self.callback).execute_callback()
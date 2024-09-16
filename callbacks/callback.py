from telebot.types import CallbackQuery
from .callback_template import CallbackTemplate
from callbacks.clean_file_callback import CleanFileCallback
from callbacks.patient_list.patients_list_callback import PatientListCallback
from callbacks.patient_registration.fio_birth_callback import FioBirthCallback
from callbacks.patient_registration.record_edit_callback import RecordEditCallback
from bot_components.variables import Variables


class Callback(CallbackTemplate):
    def __init__(self, callback: CallbackQuery):
        super().__init__(callback)

    def execute_callback(self):
        if Variables().obj_data_base is None:
            self.bot.send_message(self.callback.message.chat.id,
                                  'Вызови для начала команду /start')
        else:
            if Variables().reaction_buttons_flag == 'only_file_status_selection_buttons':
                CleanFileCallback(self.callback).execute_callback()
            elif Variables().reaction_buttons_flag == 'only_patients_list':
                PatientListCallback(self.callback).execute_callback()
            elif Variables().reaction_buttons_flag == 'only_input_info_patient_buttons':
                FioBirthCallback(self.callback).execute_callback()
            elif Variables().reaction_buttons_flag == 'only_record_patient_buttons':
                RecordEditCallback(self.callback).execute_callback()

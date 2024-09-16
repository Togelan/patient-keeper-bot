from callbacks.callback_template import CallbackTemplate
from telebot.types import CallbackQuery
from variables import Variables
from datetime import datetime
from commands.commands_pationts_registration.command_fio_birth import PatientRegistrationCommand

class RecordEditCallback(CallbackTemplate):
    def __init__(self, callback: CallbackQuery):
        super().__init__(callback)

    def execute_callback(self):
        if self.callback.data == 'record patient':
            Variables().obj_data_base.record_patient(Variables().fio, str(Variables().birthdate),
                                                     str(datetime.now().strftime("%d.%m.%Y %H.%M.%S")))
            self.bot.send_message(self.callback.message.chat.id, 'Пациент занесён в базу')
            Variables().reaction_buttons_flag = None
        elif self.callback.data == 'edit patient':
            PatientRegistrationCommand(self.callback.message).execute()

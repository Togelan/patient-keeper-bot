from variables import Variables
from commands.start_command import StartCommand
from commands.commands_patients_list.command_patients_list import PatientsListCommand
from commands.commands_pationts_registration.command_fio_birth import PatientRegistrationCommand
from callbacks.callback import Callback
from text_processing.text_processing import TextProcessing


class PatientBot:
    def __init__(self):
        self._bot = Variables().get_bot()
        self._setup_handlers()

    def _setup_handlers(self):
        @self._bot.message_handler(commands=['start'])
        def start(message) -> None:
            StartCommand(message).execute()

        @self._bot.message_handler(commands=['get_patients_list'])
        def patients_list_buttons(message) -> None:
            PatientsListCommand(message).execute()

        @self._bot.message_handler(commands=['patient_registration'])
        def input_info_patient_buttons(message) -> None:
            PatientRegistrationCommand(message).execute()

        @self._bot.callback_query_handler(func=lambda callback: True)
        def get_callback_buttons(callback) -> None:
            Callback(callback).execute_callback()

        @self._bot.message_handler()
        def text_processing(message) -> None:
            TextProcessing(message).execute_text_processing()

    def run(self):
        self._bot.polling(none_stop=True)

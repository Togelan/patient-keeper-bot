from telebot.types import Message
from bot_components.variables import Variables
from commands.commands_pationts_registration.record_info import RecordInfoCommand


class TextProcessing:
    def __init__(self, message: Message):
        self.message = message
        self.bot = Variables().get_bot()

    def execute_text_processing(self):
        if Variables().obj_data_base is None:
            self.bot.send_message(self.message.chat.id, 'Вызови для начала команду /start')
        else:
            self.check_text_flags()

    def check_text_flags(self):
        if Variables().input_text_flag == 'input_fullname' and Variables().reaction_buttons_flag == 'only_input_fio':
            self.fio_processing_handler()
        elif Variables().input_text_flag == 'input_birthdate' and Variables().reaction_buttons_flag == 'only_input_birthdate':
            self.birthdate_processing_handler()
        else:
            self.bot.send_message(self.message.chat.id, 'Пожалуйста работайте с ботом при помощи команд и кнопок')

    def fio_processing_handler(self) -> None:
        flag_correct_fio = Variables.validate_fio(self.message.text)
        if flag_correct_fio:
            Variables().fio = self.message.text
            Variables().input_text_flag = None

            if Variables().birthdate != '':
                RecordInfoCommand(self.message).execute()
            else:
                self.bot.send_message(self.message.chat.id,
                                      'ФИО введено корректно, нажмите на кнопку "Ввести дату рождения"')
                Variables().reaction_buttons_flag = 'only_input_info_patient_buttons'
        else:
            self.bot.send_message(self.message.chat.id, 'ФИО введено некорректно, обратите внимание на пример!')
            self.bot.send_message(self.message.chat.id, f'Укажите ФИО пациента.\n(Пример: Петрович Иван Васильевич)')

    def birthdate_processing_handler(self) -> None:
        flag_correct_birthdate = Variables.validate_birthdate(self.message.text)
        if flag_correct_birthdate:
            Variables().birthdate = self.message.text
            Variables().input_text_flag = None

            if Variables().fio != '':
                RecordInfoCommand(self.message).execute()
            else:
                self.bot.send_message(self.message.chat.id,
                                      'Дата рождения введена корректно, нажмите на кнопку "Ввести ФИО"')
                Variables().reaction_buttons_flag = 'only_input_info_patient_buttons'
        else:
            self.bot.send_message(self.message.chat.id,
                                  'Дата рождения введена некорректно, обратите внимание на пример! '
                                  'Также надо учитывать, что возраст пациента не должен превышать 100 лет')
            self.bot.send_message(self.message.chat.id, f'Укажите дату рождения пациента.\n(Пример: 24.04.2002)')

from telebot.types import Message
import telebot
from commands.command_template import CommandTemplate
from bot_components.variables import Variables


class PatientRegistrationCommand(CommandTemplate):
    def __init__(self, message: Message):
        self.message = message
        self.bot = Variables().get_bot()

    def execute(self) -> None:
        if Variables().obj_data_base is None:
            self.bot.send_message(self.message.chat.id, 'Вызови для начала команду /start')
        else:
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton('Ввести ФИО', callback_data='input_fullname'))
            markup.add(telebot.types.InlineKeyboardButton('Ввести дату рождения', callback_data='input_birthdate'))

            self.bot.send_message(self.message.chat.id,
                                  'Давайте заполним информацию о пациенте, вводите данные поочередно, нажимая на кнопки:',
                                  reply_markup=markup)

        Variables().reaction_buttons_flag = 'only_input_info_patient_buttons'
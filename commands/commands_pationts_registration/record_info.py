from telebot.types import Message
import telebot
from commands.command_template import CommandTemplate
from bot_components.variables import Variables


class RecordInfoCommand(CommandTemplate):
    def __init__(self, message: Message):
        self.message = message
        self.bot = Variables().get_bot()

    def execute(self) -> None:
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(
            telebot.types.InlineKeyboardButton('Занести данные о пациенте в базу', callback_data='record patient'))
        markup.add(telebot.types.InlineKeyboardButton('Исправить данные о пациенте', callback_data='edit patient'))

        self.bot.send_message(self.message.chat.id, 'Данные о пациенте введены корректно', reply_markup=markup)

        Variables().reaction_buttons_flag = 'only_record_patient_buttons'

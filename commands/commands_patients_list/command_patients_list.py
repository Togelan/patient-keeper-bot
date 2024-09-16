from telebot.types import Message
import telebot
from commands.command_template import CommandTemplate
from variables import Variables


class PatientsListCommand(CommandTemplate):
    def __init__(self, message: Message):
        self.message = message
        self.bot = Variables().get_bot()

    def execute(self) -> None:
        if Variables().obj_data_base is None:
            self.bot.send_message(self.message.chat.id, 'Привет!\nВызови для начала команду /start')
        else:
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton('пациентов,\nпришедших за сегодняшний день',
                                                          callback_data="today's patients list"))
            markup.add(telebot.types.InlineKeyboardButton('пациентов за определенный день недели',
                                                          callback_data='day of week patients list'))

            self.bot.send_message(self.message.chat.id,
                                  f'Получить список...',
                                  reply_markup=markup)

            Variables().reaction_buttons_flag = 'only_patients_list'
from telebot.types import Message
import telebot
from .command_template import CommandTemplate
from data_base import DataBase
from variables import Variables


class StartCommand(CommandTemplate):
    def __init__(self, message: Message):
        self.message = message
        self.bot = Variables().get_bot()

    def execute(self) -> None:
        name = self.message.from_user.first_name

        Variables().obj_data_base = DataBase(name_doctor=name, chat_id=self.message.chat.id)

        self.bot.send_message(self.message.chat.id, f'Привет, {name}!\nЯ бот для учета пациентов медучреждения.'
                                                    f' Работай со мной при помощи команд и кнопок')

        existence_of_file = Variables().obj_data_base.check_file_existence()

        if existence_of_file:
            Variables().reaction_buttons_flag = 'only_file_status_selection_buttons'
            self.clean_edit_file_buttons_handler(self.message, name)
        else:
            self.bot.send_message(self.message.chat.id,
                                  f'Я создал файл под названием "{name}_{self.message.chat.id}.csv", в который ты '
                                  f'сможешь заносить данные своих пациентов')
            Variables().obj_data_base.create_file()

    def clean_edit_file_buttons_handler(self, message, name) -> None:
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton('Очистить файл', callback_data='clean_file'))
        markup.add(telebot.types.InlineKeyboardButton('Не стирать старые данные', callback_data='use_old_data'))

        self.bot.send_message(message.chat.id,
                              f'Файл под названием "{name}_{message.chat.id}.csv" для записи пациентов уже '
                              f'существует, видимо, ты уже работал со мной.'
                              f'\n\nОчистить файл от старых данных?',
                              reply_markup=markup)

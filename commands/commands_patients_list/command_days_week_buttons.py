from telebot.types import Message
import telebot
from commands.command_template import CommandTemplate
from variables import Variables


class DaysWeekCommand(CommandTemplate):
    def __init__(self, message: Message):
        self.message = message
        self.bot = Variables().get_bot()

    def execute(self) -> None:
        week_dates = Variables().get_obj_data_processing().get_week_dates()

        markup = telebot.types.InlineKeyboardMarkup()
        for date in week_dates:
            markup.add(telebot.types.InlineKeyboardButton(date,
                                                          callback_data=date))
        self.bot.send_message(self.message.chat.id, 'Выберите дату:', reply_markup=markup)

        Variables().reaction_buttons_flag = 'only_patients_list'
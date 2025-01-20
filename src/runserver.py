import telebot
import os
from func.withdrawal import binance_withdraw
from func.ip import get_ip

API_TOKEN = os.getenv('TELEGRAMKEY')

bot = telebot.TeleBot(API_TOKEN)

withdraw_request_data={}

buttons = {
    "withdraw_button" : telebot.types.KeyboardButton(text="/withdraw")
}

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message,text="welcome")
@bot.message_handler(commands=['getip'])
def send_ip(message):
    bot.reply_to(message,text=f"{get_ip()}")



@bot.message_handler(commands=['recipient'])
def set_recipient(message:telebot.types.Message):
    command_text = message.text[len('/withdraw '):].strip()
    bot.send_message(message.chat.id,f"trying to set command with {command_text}")

@bot.message_handler(commands=['withdraw'])
def withdrawal_request(message:telebot.types.Message):
    bot.send_message(message.chat.id,"input the tron address")

    bot.register_next_step_handler(message,ask_receiver_address)

def ask_receiver_address(message):
    withdraw_request_data["address"] = message.text
    bot.reply_to(message,"add the tron amount")
    bot.register_next_step_handler(message,ask_withdrawal_amount)

def ask_withdrawal_amount(message):
    withdraw_request_data["amount"] = message.text
    print(withdraw_request_data)
    bot.reply_to(message=message,text=f"would you like to wihdraw to \n address : {withdraw_request_data["address"]}\namount: {withdraw_request_data["amount"]}TRX\nyes/no")

    bot.register_next_step_handler(message,ask_withdrawal_approuval)

def ask_withdrawal_approuval(message):
    if "yes" in message.text.lower():
        binance_withdraw(amount=withdraw_request_data["amount"],
                         address=withdraw_request_data["address"])
    bot.register_next_step_handler(message,send_welcome)

    


bot.infinity_polling()
import telebot
import link_maker

bot = telebot.TeleBot('926781036:AAEwd13njCMyqA0frhlUlHC4KqKjwv2frtE')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет! Меня зовут Эмили. Просто отправь мне ссылку на приложение из Google Play!")
    else:
        link = link_maker.create_link(message.text)
        bot.send_message(message.from_user.id, link)

bot.polling(none_stop=True, interval=0)

import logging
import openai
import telegram
from telegram.ext import Updater, MessageHandler, filters

openai.api_key = "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"

bot = telegram.Bot(token="6254843237:AAGQ2PzWCtaYdQsjgRw6s-iyzUTm2d_euhQ")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('bot.log')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

context_ = ''
count = 0
def respond(update, context):
    message = update.message.text
    global context_
    global count
    if(message == 'clear context'):
        context_ = ''
        bot.send_message(chat_id=update.effective_chat.id,
                         text="Я всё забыл, как после крепкого рома. О чём ещё тебе может поведать морской волк?")
        message = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "assistant", "content": message + " Ответь коротко и как пират." + "\n" + context_}],
        max_tokens=500,
        n=1,
        temperature=0.5,

    )

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=response.choices[0].message["content"])
    context_ += "\n" + message + '\n' + "You previously told me that " + response.choices[0].message["content"] + '\n\n'
    count += response.usage["completion_tokens"]
    logger.info(f'Received message: {message}')
    logger.info(f'Sent response: {response.choices[0].message["content"]}')
    logger.info(f'tokens total: {count}')
    logger.info(f'cash total: {count * 0.002 // 1000}')
    logger.info(f'----------------------\n')




updater = telegram.ext.Updater(token="6254843237:AAGQ2PzWCtaYdQsjgRw6s-iyzUTm2d_euhQ", use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, respond))

updater.start_polling()

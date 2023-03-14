from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random 
import googletrans
from googletrans import Translator

translator = Translator()

bot = Bot(token='1134641552:AAEzUBP40GyWNfOLa3GzH8Z5iidUo2-xWu4')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id,"Ассалам алейкум!\nНапиши мне что-нибудь!\nКоманда /help чтобы узнать мои возможности")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id,"/gm для пожелания Доброго утра на случайном языке\n/gn для пожелания Спокойной ночи на случайном языке\nТак же для перевода любой фразы на английский язык просто напиши это в чат!")

@dp.message_handler(commands=['gm'])
async def good_morning_command(message: types.Message):
	d = dict(googletrans.LANGUAGES)
	key, value = random.choice(list(d.items()))
	g_m = translator.translate('Good Morning', dest=key)
	await bot.send_message(message.from_user.id,g_m.text)
	g_m_lang = translator.translate(value, dest="ru")
	await bot.send_message(message.from_user.id,"Это 'Доброе утро' на языке '{}'".format(g_m_lang.text))

@dp.message_handler(commands=['gn'])
async def good_night_command(message: types.Message):
	d = dict(googletrans.LANGUAGES)
	key, value = random.choice(list(d.items()))
	g_n = translator.translate('Good Night', dest=key)
	await bot.send_message(message.from_user.id,g_n.text)
	g_n_lang = translator.translate(value, dest="ru")
	await bot.send_message(message.from_user.id,"Это 'Спокойной ночи' на языке '{}'".format(g_n_lang.text))

@dp.message_handler()
async def echo_message(msg: types.Message):
	res = translator.translate(msg.text)
	await bot.send_message(msg.from_user.id, res.text)



if __name__=='__main__':
	executor.start_polling(dp, skip_updates=True)

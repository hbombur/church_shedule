from config.config import TOKEN
from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
	print('Бот запущен')

ikb_city_area = InlineKeyboardMarkup()
ib_area = {}
ib_area['1'] = InlineKeyboardButton(text='Внуково', callback_data="1")
ib_area['2'] = InlineKeyboardButton(text='Проспект Вернадского', callback_data='2')
ib_area['3'] = InlineKeyboardButton(text='Дорогомилово', callback_data='3')
ib_area['4'] = InlineKeyboardButton(text='Раменки', callback_data='4')
ib_area['5'] = InlineKeyboardButton(text='Крылатское', callback_data='5')
ib_area['6'] = InlineKeyboardButton(text='Тропарево-Никулино', callback_data='6')
ib_area['7'] = InlineKeyboardButton(text='Кунцево', callback_data='7')
ib_area['8'] = InlineKeyboardButton(text='Солнцево', callback_data='8')
ib_area['9'] = InlineKeyboardButton(text='Можайский', callback_data='9')
ib_area['10'] = InlineKeyboardButton(text='Филевский парк', callback_data='10')
ib_area['11'] = InlineKeyboardButton(text='Ново-Переделкино',callback_data='11')
ib_area['12'] = InlineKeyboardButton(text='Фили-Давыдково', callback_data='12')
ib_area['13'] = InlineKeyboardButton(text='Очаково-Матвеевское', callback_data='13')

for area in ib_area:
	ikb_city_area.insert(ib_area.get(area))


ikb_adm_dist = InlineKeyboardMarkup()
ib_list = {}
ib_list['ib_dist1'] = InlineKeyboardButton(text='Центральный АО', callback_data='1')
ib_list['ib_dist2'] = InlineKeyboardButton(text='Северный АО', callback_data='2')
ib_list['ib_dist3'] = InlineKeyboardButton(text='Северо-Восточный АО', callback_data='3')
ib_list['ib_dist4'] = InlineKeyboardButton(text='Восточный АО', callback_data='4')
ib_list['ib_dist5'] = InlineKeyboardButton(text='Юго-Восточный АО', callback_data='5')
ib_list['ib_dist6'] = InlineKeyboardButton(text='Южный АО', callback_data='6')
ib_list['ib_dist7'] = InlineKeyboardButton(text='Юго-Западный АО', callback_data='7')
ib_list['ib_dist8'] = InlineKeyboardButton(text='Западный АО', callback_data='8')
ib_list['ib_dist9'] = InlineKeyboardButton(text='Северо-Западный АО', callback_data='9')
ib_list['ib_dist10'] = InlineKeyboardButton(text='Зеленоградский АО', callback_data='10')
ib_list['ib_dist11'] = InlineKeyboardButton(text='Новомосковский АО', callback_data='11')
ib_list['ib_dist12'] = InlineKeyboardButton(text='Троицкий АО', callback_data='12')

for dist in ib_list:
	ikb_adm_dist.insert(ib_list.get(dist))


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
	await message.answer(text='Выберите храм для отображения его расписания', reply_markup=ikb_adm_dist)


if __name__ == '__main__':
	executor.start_polling(dispatcher=dp,
							on_startup=on_startup,
							skip_updates=True)

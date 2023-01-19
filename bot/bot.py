from config.config import TOKEN
from aiogram import Dispatcher, Bot, executor, types
from keyboard.inline_keyboard import ikb_adm_dist, dist_dict

bot = Bot(TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот запущен')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Выберите округ Москвы',
                         reply_markup=ikb_adm_dist)


@dp.callback_query_handler()
async def callback_district(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Выберите район')
    await callback.message.edit_reply_markup(dist_dict[callback.data])

@dp.callback_query_handler()
async def callback_area(callback: types.CallbackQuery):
    pass


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)

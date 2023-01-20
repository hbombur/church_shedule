from config.config import TOKEN
from aiogram import Dispatcher, Bot, executor, types

from keyboard.inline_keyboard import ikb_adm_dist, dist_dict, area_dict

bot = Bot(TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот запущен')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer_photo(photo='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Coat_of_Arms_of_Moscow.'
                                     'svg/1008px-Coat_of_Arms_of_Moscow.svg.png',
                               caption='Выберите округ Москвы',
                               reply_markup=ikb_adm_dist)
    await message.delete()


@dp.callback_query_handler()
async def callback_district(callback: types.CallbackQuery):
    # result = callback.data.split('_')
    if callback.data[3:7] == 'dist':
        await callback.message.edit_caption(caption='Выберите район')
        await callback.message.edit_media(types.InputMedia(media='https://static.tildacdn.com/tild6332-6239-4134-'
                                                                 'a633-663133663837/zao_mos_coa_Abaliru_.png'),
                                          reply_markup=dist_dict[callback.data])
    elif callback.data[3:7] == 'area':
        await callback.message.edit_caption(caption='Выберите Храм')
        await callback.message.edit_media(types.InputMedia(media='https://sun6-23.userapi.com/s/v1/ig2/'
                                                                 'JZEfXBTa8wh27q4EAZ77Mu1HJr1Jpubff4AkL'
                                                                 'C1OrW6Yc4o6CCTis3-2iNVpKgoWqvlAkTD7mx'
                                                                 'RDpmNns_qg9dwJ.jpg?size=671x671&quali'
                                                                 'ty=95&crop=94,325,671,671&ava=1'),
                                          reply_markup=area_dict[callback.data])
    elif callback.data[3:7] == 'chur':
        await callback.message.answer(text='Храм Спиридона святителя Тримифунтского\n'
                                           'Сайт храма: https://svt-spiridon.ru',
                                      reply_markup=ikb_adm_dist)
        await callback.message.delete()


# @dp.callback_query_handler()
# async def callback_area(callback: types.CallbackQuery):
#     a


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)

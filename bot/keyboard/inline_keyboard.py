from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .dictrict_named_dict import DistDict

dist_dict = DistDict
area_dict = DistDict

ikb_vikary_church = InlineKeyboardMarkup()
ib_church = {'ib_church1': InlineKeyboardButton(text='Храм святителя Спиридона епископа Тримифунтского',
                                                callback_data='ib_church1'),
             'ib_church2': InlineKeyboardButton(text='Храм Покрова Пресвятой Богородицы в Филях',
                                                callback_data='ib_church2'),
             'ib_church3': InlineKeyboardButton(text='Храм Всех Святых на Филевской Пойме',
                                                callback_data='ib_church3')}

for adm in ib_church:
    ikb_vikary_church.insert(ib_church.get(adm))


ikb_city_west_area = InlineKeyboardMarkup()
ib_area = {'ib_area1': InlineKeyboardButton(text='Внуково', callback_data="ib_area1"),
           'ib_area2': InlineKeyboardButton(text='Проспект Вернадского', callback_data='ib_area2'),
           'ib_area3': InlineKeyboardButton(text='Дорогомилово', callback_data='ib_area3'),
           'ib_area4': InlineKeyboardButton(text='Раменки', callback_data='ib_area4'),
           'ib_area5': InlineKeyboardButton(text='Крылатское', callback_data='ib_area5'),
           'ib_area6': InlineKeyboardButton(text='Тропарево-Никулино', callback_data='ib_area6'),
           'ib_area7': InlineKeyboardButton(text='Кунцево', callback_data='ib_area7'),
           'ib_area8': InlineKeyboardButton(text='Солнцево', callback_data='ib_area8'),
           'ib_area9': InlineKeyboardButton(text='Можайский', callback_data='ib_area9'),
           'ib_area10': InlineKeyboardButton(text='Филевский парк', callback_data='ib_area10'),
           'ib_area11': InlineKeyboardButton(text='Ново-Переделкино', callback_data='ib_area11'),
           'ib_area12': InlineKeyboardButton(text='Фили-Давыдково', callback_data='ib_area12'),
           'ib_area13': InlineKeyboardButton(text='Очаково-Матвеевское', callback_data='ib_area13')}

for area in ib_area:
    ikb_city_west_area.insert(ib_area.get(area))

ikb_adm_dist = InlineKeyboardMarkup()
ib_dist_list = {'ib_dist1': InlineKeyboardButton(text='Центральный АО', callback_data='ib_dist1'),
                'ib_dist2': InlineKeyboardButton(text='Северный АО', callback_data='ib_dist2'),
                'ib_dist3': InlineKeyboardButton(text='Северо-Восточный АО', callback_data='ib_dist3'),
                'ib_dist4': InlineKeyboardButton(text='Восточный АО', callback_data='ib_dist4'),
                'ib_dist5': InlineKeyboardButton(text='Юго-Восточный АО', callback_data='ib_dist5'),
                'ib_dist6': InlineKeyboardButton(text='Южный АО', callback_data='ib_dist6'),
                'ib_dist7': InlineKeyboardButton(text='Юго-Западный АО', callback_data='ib_dist7'),
                'ib_dist8': InlineKeyboardButton(text='Западный АО', callback_data='ib_dist8'),
                'ib_dist9': InlineKeyboardButton(text='Северо-Западный АО', callback_data='ib_dist9'),
                'ib_dist10': InlineKeyboardButton(text='Зеленоградский АО', callback_data='ib_dist10'),
                'ib_dist11': InlineKeyboardButton(text='Новомосковский АО', callback_data='ib_dist11'),
                'ib_dist12': InlineKeyboardButton(text='Троицкий АО', callback_data='ib_dist12')}

for dist in ib_dist_list:
    ikb_adm_dist.insert(ib_dist_list.get(dist))

dist_dict = {'ib_dist8': ikb_city_west_area,
             'ib_dist1': ikb_city_west_area}

area_dict = {'ib_area10': ikb_vikary_church}


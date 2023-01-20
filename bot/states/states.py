from aiogram.dispatcher.filters.state import  StatesGroup, State


class ChoiseChurch(StatesGroup):
    choose_district = State()
    choose_area = State()
    choose_church = State()

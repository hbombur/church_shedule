from typing import TypedDict
from aiogram.types import InlineKeyboardMarkup


class DistDict(TypedDict):
    ib_dist: InlineKeyboardMarkup


class VicariateDict(TypedDict):
    ib_dist: str

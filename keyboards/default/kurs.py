from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menukurs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="USD"),
            KeyboardButton(text="EUR"),

        ],
        [
            KeyboardButton(text="UAE Dirham"),
            KeyboardButton(text="India Rupee"),
            KeyboardButton(text="Japan Yen"),

        ],
        [
            KeyboardButton(text="Tenge"),
            KeyboardButton(text="Turkish Lira"),

        ],
        [
            KeyboardButton(text="Log Out"),
        ],
    ],
    resize_keyboard=True
)

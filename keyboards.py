from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "🎧 Мои артисты",
                callback_data="artists"
            ),
            InlineKeyboardButton(
                "➕ Добавить артиста",
                callback_data="add"
            ),
            InlineKeyboardButton(
                "❌ Удалить артиста",
                callback_data="delete"
            )
        ],
        [
            InlineKeyboardButton(
                "🔥 Новые релизы",
                callback_data="releases"
            ),
            InlineKeyboardButton(
                "⚙️ Настройки",
                callback_data="settings"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


def back_button():
    keyboard = [
        [
            InlineKeyboardButton(
                "⬅️ Назад",
                callback_data="back"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
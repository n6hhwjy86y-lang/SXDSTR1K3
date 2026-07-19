from telegram import Update
from telegram.ext import ContextTypes

from keyboards import main_menu, back_button
from database import save_data, load_data


users_artists = load_data()
waiting_for_artists = {}
waiting_for_delete = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🖤 SXDSTR1K3\n\n"
        "Добро пожаловать.\n\n"
        "Следи только за той музыкой,\n"
        "которая тебе действительно нравится 🎧",
        reply_markup=main_menu()
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    if query.data == "artists":

        artists = users_artists.get(user_id, [])

        if artists:

            text = "🎧 Твои артисты:\n\n"

            for artist in artists:
                text += f"• {artist}\n"

        else:

            text = (
                "🎧 Твои артисты:\n\n"
                "Пока список пуст."
            )

        await query.message.reply_text(
            text,
            reply_markup=back_button()
        )

    elif query.data == "add":

        waiting_for_artists[user_id] = True

        await query.message.reply_text(
            "➕ Напиши имя артиста 🎧",
            reply_markup=back_button()
        )

    elif query.data == "delete":

        artists = users_artists.get(user_id, [])

        if not artists:

            await query.message.reply_text(
                "❌ У тебя нет артистов для удаления.",
                reply_markup=main_menu()
            )

        else:

            waiting_for_delete[user_id] = True

            text = "❌ Напиши имя артиста для удаления:\n\n"

            for artist in artists:
                text += f"• {artist}\n"

            await query.message.reply_text(
                text,
                reply_markup=back_button()
            )

    elif query.data == "releases":

        await query.message.reply_text(
            "🔥 Новых релизов пока нет.",
            reply_markup=back_button()
        )

    elif query.data == "settings":

        await query.message.reply_text(
            "⚙️ Настройки скоро появятся.",
            reply_markup=back_button()
        )

    elif query.data == "back":

        await query.message.reply_text(
            "🖤 Главное меню",
            reply_markup=main_menu()
        )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.message.from_user.id
    text = update.message.text

    if user_id in waiting_for_delete:

        artists = users_artists.get(user_id, [])

        if text in artists:

            artists.remove(text)

            save_data(users_artists)

            await update.message.reply_text(
                f"🗑️ {text} удалён из списка",
                reply_markup=main_menu()
            )

        else:

            await update.message.reply_text(
                "⚠️ Такого артиста нет в списке",
                reply_markup=main_menu()
            )

        del waiting_for_delete[user_id]
        return

    if user_id in waiting_for_artists:

        if user_id not in users_artists:
            users_artists[user_id] = []

        if text not in users_artists[user_id]:

            users_artists[user_id].append(text)

            save_data(users_artists)

            await update.message.reply_text(
                f"✅ {text} добавлен",
                reply_markup=main_menu()
            )

        else:

            await update.message.reply_text(
                "⚠️ Этот артист уже есть",
                reply_markup=main_menu()
            )

        del waiting_for_artists[user_id]
print("ФАЙЛ ЗАПУСТИЛСЯ")

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters
)

from config import TOKEN
from handlers import (
    start,
    button_handler,
    message_handler
)


app = Application.builder().token(TOKEN).build()


app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(
    CallbackQueryHandler(button_handler)
)

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        message_handler
    )
)


print("🖤 SXDSTR1K3 запущен")

app.run_polling()
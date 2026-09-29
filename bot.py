import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOOKS = {
    "کورد": "📚 مێژووی کورد",
    "ئیسلام": "📚 مێژووی ئیسلام",
    "میسر": "📚 مێژووی میسری کۆن",
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"بەخێربێیت {update.effective_user.first_name}!\n\n"
        "بۆ گەڕان بنووسە:\n"
        "/search کورد\n\n"
        "بۆ بینینی هەموو بابەتەکان:\n"
        "/list"
    )


async def list_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "\n".join(BOOKS.values())
    await update.message.reply_text(text)


async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    word = " ".join(context.args).strip()
    if not word:
        await update.message.reply_text("تکایە وشەیەک بنووسە، وەک: /search کورد")
        return
    results = [v for k, v in BOOKS.items() if word in k]
    if results:
        await update.message.reply_text("\n".join(results))
    else:
        await update.message.reply_text("هیچ ئەنجامێک نەدۆزرایەوە")


app = ApplicationBuilder().token(os.environ["TOKEN"]).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("list", list_all))
app.add_handler(CommandHandler("search", search))
app.run_polling()

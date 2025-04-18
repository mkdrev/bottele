from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Ambil token dari environment variable
TOKEN = os.environ.get("BOT_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://i.pinimg.com/736x/99/9b/b8/999bb8d77251045efa7364b96c170509.jpg",  # Ganti sesuai kebutuhan
        caption="Halo Bosku, selamat datang di *TELKOM4D!*\n\n"
                "Pilih menu di bawah untuk mulai bermain atau cek fitur lainnya.",
        parse_mode="Markdown"
    )

    keyboard = [
        [InlineKeyboardButton("🎮 PLAY", url="https://telkom4dnaga.com/?ref=sewakw12")],
        [InlineKeyboardButton("🎰 RTP GACOR", url="https://telkom4dnaga.com/?ref=sewakw12")],
        [InlineKeyboardButton("🎁 PROMOTION", url="https://telkom4dnaga.com/?ref=sewakw12")],
        [InlineKeyboardButton("📲 SOCIAL MEDIA", url="https://telkom4dnaga.com/?ref=sewakw12")],
        [InlineKeyboardButton("💬 LIVECHAT", url="https://telkom4dnaga.com/?ref=sewakw12")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id=chat_id,
        text="Pilih salah satu opsi berikut:",
        reply_markup=reply_markup
    )

if __name__ == '__main__':
    app.add_handler(CommandHandler("start", start))
    print("[✅] Bot TELKOM4D is running...")
    app.run_polling()

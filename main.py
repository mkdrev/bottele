from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# === KEEP ALIVE ===
app = Flask('')

@app.route('/')
def home():
    return "Bot TELKOM4D Aktif!"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()

# === SETUP BOT ===
TOKEN = os.environ.get("TOKEN")  # Ambil token dari Environment Render

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://i.pinimg.com/736x/99/9b/b8/999bb8d77251045efa7364b96c170509.jpg",
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

    await context.bot.send_message(chat_id=chat_id, text="Pilih salah satu opsi berikut:", reply_markup=reply_markup)

# === JALANKAN BOT ===
if __name__ == '__main__':
    bot = ApplicationBuilder().token(TOKEN).build()
    bot.add_handler(CommandHandler("start", start))
    print("[✅] Bot TELKOM4D aktif!")
    bot.run_polling()

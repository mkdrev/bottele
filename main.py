from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os
import logging

# === SETUP LOGGING ===
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# === KEEP ALIVE ===
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot TELKOM4D Aktif dan Berjalan!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

flask_thread = Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

# === BOT CONFIGURATION ===
TOKEN = os.environ.get("TOKEN")  # Get token from environment variable
BASE_URL = "https://telkom4dnaga.com/?ref=sewakw12"

# === BOT HANDLERS ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user = update.effective_user
    
    try:
        # Send welcome photo with caption
        await context.bot.send_photo(
            chat_id=chat_id,
            photo="https://i.pinimg.com/736x/99/9b/b8/999bb8d77251045efa7364b96c170509.jpg",
            caption=f"Halo {user.first_name}! Selamat datang di *TELKOM4D*!\n\n"
                    "Pilih menu di bawah untuk mulai bermain atau cek fitur lainnya.",
            parse_mode="Markdown"
        )

        # Create inline keyboard
        keyboard = [
            [InlineKeyboardButton("🎮 PLAY", url=BASE_URL)],
            [InlineKeyboardButton("🎰 RTP GACOR", url=BASE_URL)],
            [InlineKeyboardButton("🎁 PROMOTION", url=BASE_URL)],
            [InlineKeyboardButton("📲 SOCIAL MEDIA", url=BASE_URL)],
            [InlineKeyboardButton("💬 LIVECHAT", url=BASE_URL)],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send menu options
        await context.bot.send_message(
            chat_id=chat_id,
            text="Silakan pilih opsi berikut:",
            reply_markup=reply_markup
        )
        
    except Exception as e:
        logger.error(f"Error in start command: {e}")
        await context.bot.send_message(
            chat_id=chat_id,
            text="Maaf, terjadi kesalahan. Silakan coba lagi nanti."
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Gunakan /start untuk memulai bot dan melihat menu utama.\n"
        "Hubungi admin jika Anda membutuhkan bantuan lebih lanjut."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    
    if any(word in text for word in ['hai', 'hello', 'hi', 'halo']):
        await update.message.reply_text(f"Halo {update.effective_user.first_name}! Ketik /start untuk melihat menu.")
    else:
        await update.message.reply_text("Maaf, saya tidak mengerti. Ketik /start untuk melihat menu.")

# === MAIN FUNCTION ===
def main():
    try:
        # Create bot application
        application = ApplicationBuilder().token(TOKEN).build()
        
        # Add handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        logger.info("Bot TELKOM4D starting...")
        print("[✅] Bot TELKOM4D aktif dan siap melayani!")
        
        # Run bot
        application.run_polling(drop_pending_updates=True)
        
    except Exception as e:
        logger.error(f"Bot error: {e}")
        print(f"[❌] Bot error: {e}")

if __name__ == '__main__':
    main()

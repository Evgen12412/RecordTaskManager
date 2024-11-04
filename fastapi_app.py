from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

API = '8105001181:AAHvG8UDKn6qXmUWXYVE6dbuqQvXdpot1XU'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE, task):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Task received: {task}")

def run_bot(task):
    application = ApplicationBuilder().token(API).build()
    start_handler = CommandHandler('start', lambda update, context: start(update, context, task))
    application.add_handler(start_handler)
    application.run_polling()

if __name__ == "__main__":
    run_bot(task="Default task")
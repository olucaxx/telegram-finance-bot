from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from utils.token import TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Envie uma mensagem e eu vou registrar.")
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Minha função é registrar seues gastos e te ajudar a enteder pra onde ta indo todo seu dinheiro.")
    
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Entendido! Encerrando .")


def handle_response(text: str) -> str:
    text += text.lower()
    if 'hello' in text:
        return "Hi!"
    
    if 'goodbye' in text:
        return "See you later!"
    
    return "I didn't understand you..."

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    print(f'User ({update.message.chat.id}): {text}')
    
    await update.message.reply_text(handle_response(text))
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("cancel", cancel))
    
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    app.add_error_handler(error)

    print("BOT IS READY!")
    app.run_polling()

if __name__ == "__main__":
    main()
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes import os

ADMIN_IDS = [1074804932]  # Replace with actual admin user IDs button_text = "Click me" cgpa_message = "Your CGPA is 0.0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): keyboard = [[InlineKeyboardButton(button_text, callback_data="button_click")]] reply_markup = InlineKeyboardMarkup(keyboard) await update.message.reply_text("Press the button:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE): query = update.callback_query await query.answer() await query.message.reply_text("Button clicked!")

async def set_button(update: Update, context: ContextTypes.DEFAULT_TYPE): global button_text user_id = update.message.from_user.id

if user_id not in ADMIN_IDS:
    await update.message.reply_text("You are not authorized to set the button text.")
    return

if context.args:
    button_text = ' '.join(context.args)
    await update.message.reply_text(f"Button text set to: {button_text}")
else:
    await update.message.reply_text("Please provide text for the button.")

async def set_cgpa(update: Update, context: ContextTypes.DEFAULT_TYPE): global cgpa_message user_id = update.message.from_user.id

if user_id not in ADMIN_IDS:
    await update.message.reply_text("You are not authorized to set the CGPA message.")
    return

if context.args:
    cgpa_message = ' '.join(context.args)
    await update.message.reply_text(f"CGPA message set to: {cgpa_message}")
else:
    await update.message.reply_text("Please provide a CGPA message.")

async def get_cgpa(update: Update, context: ContextTypes.DEFAULT_TYPE): await update.message.reply_text(cgpa_message)

def main(): app = ApplicationBuilder().token(os.getenv("7841123141:AAEE-zU5yU5q5Kp2RGH-zWhU2-QLM5_ZrgQ")).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("setbutton", set_button))
app.add_handler(CommandHandler("setcgpa", set_cgpa))
app.add_handler(CommandHandler("getcgpa", get_cgpa))
app.add_handler(CallbackQueryHandler(button_handler, pattern="button_click"))

print("Welcome To Vel Tech CGPA Calculator Bot...")
app.run_polling()

if name == "main": main()


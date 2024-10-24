from telegram.ext import (
    Updater,
    MessageHandler,
    Filters,
    CommandHandler,
    ConversationHandler,
)
import os


def unknown(update, context):
    update.message.reply_text("Sorry, I don't understand that. Try something else!")


def invalid(update, context):
    update.message.reply_text("Invalid!")
    return ConversationHandler.END


def about(update, context):
    update.message.reply_text(
        """CTF - http://ctf.hackusati.tech"""
    )


def text2voice(update, context):
    update.message.reply_text("Okay, send me the text.")
    return 0


def send_voice_msg(update, context):
    text = update.message.text
    fs = open(f"/home/ctf/{update.message.from_user.id}", "w")
    fs.write(f"echo '{text}'")
    fs.close()
    os.system(
        f"su ctf -c 'sh /home/ctf/{update.message.from_user.id} | espeak -w /home/ctf/{update.message.from_user.id}.wav --stdin'"
    )
    update.message.reply_audio(
        open(f"/home/ctf/{update.message.from_user.id}.wav", "rb")
    )
    os.system(
        f"rm /home/ctf/{update.message.from_user.id}; rm /home/ctf/{update.message.from_user.id}.wav"
    )
    return ConversationHandler.END


def start(update, context):
    update.message.reply_text("Welcome to our first misc challenge :D")
    update.message.reply_text(
        """Available Commands:
/start
/help
/text2voice
/about"""
    )


unknown_handler = MessageHandler(Filters.all, unknown)
about_handler = CommandHandler("about", about)
start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", start)
text2voice_states = {0: [MessageHandler(Filters.text, send_voice_msg)]}
text2voice_handler = ConversationHandler(
    entry_points=[CommandHandler("text2voice", text2voice)],
    states=text2voice_states,
    fallbacks=[MessageHandler(Filters.all, invalid)],
)
token = "5320222715:AAFKT7ec9IR50q3-uVs7vhX4c4Vw7Wka05w"
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(about_handler)
dispatcher.add_handler(text2voice_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(unknown_handler)
updater.start_polling()
updater.idle()

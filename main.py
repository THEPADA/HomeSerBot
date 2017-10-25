from telegram.ext import Updater, CommandHandler
import serial
import logging

ser = serial.Serial('/dev/ttyUSB1')
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level=logging.INFO)


def start(bot, update):
    update.message.reply_text('Hello World!')

def socket(bot, update, args):
    update.message.reply_text("proc run")

    Command = args[0]+ " "+args[1]
    ser.write(Command.encode('ascii', 'replace'))
    update.message.reply_text(Command + " was sent")

updater = Updater('468485599:AAHGXLC7FD2etZFb4TDajATuHnLQh7yehFM')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('socket', socket ,pass_args=True))

updater.start_polling()
updater.idle()

import os
from pytesseract import pytesseract
from PIL import Image
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

class OCR:
    def __init__(self):
        # Path for Tesseract in Docker environment
        self.path = '/usr/bin/tesseract'

    def extract(self, filename):
        try:
            pytesseract.tesseract_cmd = self.path
            img = Image.open(filename)
            text = pytesseract.image_to_string(img)
            return text
        except Exception as e:
            print(e)
            return "Error"

ocr = OCR()

async def handle_image(update: Update, context):
    file = await update.message.photo[-1].get_file()
    file_path = f'{file.file_id}.jpg'
    await file.download_to_drive(file_path)
    text = ocr.extract(file_path)
    await update.message.reply_text(f"{text}")
    os.remove(file_path)


async def start(update: Update, context):
    await update.message.reply_text("Send me an image and I'll extract the text!")

if __name__ == '__main__':
    # BOT_TOKEN = '7525646911:AAEPXkuCj34tA2HsGqbDUnGia8hQjoBCVsw'
    BOT_TOKEN = os.getenv('BOT_TOKEN')


    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(MessageHandler(filters.PHOTO, handle_image))

    app.run_polling()
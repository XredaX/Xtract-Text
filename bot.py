import os
from pytesseract import pytesseract
from PIL import Image
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

import logging

logging.basicConfig(level=logging.INFO)  # Configure logging level

# Set the TESSDATA_PREFIX environment variable
os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/5/tessdata'

class OCR:
    def __init__(self):
        self.path = '/usr/bin/tesseract'

    def extract(self, filename):
        try:
            pytesseract.tesseract_cmd = self.path
            img = Image.open(filename)
            text = pytesseract.image_to_string(img)
            return text
        except Exception as e:
            logging.error(f"Error in extract method: {e}")
            return "Error"


async def handle_image(update: Update, context):
    file = await update.message.photo[-1].get_file()
    file_path = f'{file.file_id}.jpg'
    try:
        await file.download_to_drive(file_path)
        if os.path.exists(file_path):
            logging.info(f"File {file_path} downloaded successfully.")
            text = ocr.extract(file_path)
            await update.message.reply_text(f"{text}")
        else:
            logging.error(f"File {file_path} not found.")
            await update.message.reply_text("File download failed.")
    except Exception as e:
        logging.error(f"Error handling image: {e}")
        await update.message.reply_text("An error occurred while processing the image.")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


ocr = OCR()

async def start(update: Update, context):
    await update.message.reply_text("Send me an image and I'll extract the text!")

if __name__ == '__main__':
    # BOT_TOKEN = '7525646911:AAEPXkuCj34tA2HsGqbDUnGia8hQjoBCVsw'
    BOT_TOKEN = os.getenv('BOT_TOKEN')


    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(MessageHandler(filters.PHOTO, handle_image))

    app.run_polling()
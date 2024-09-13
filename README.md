# 📸 Telegram Image-to-Text OCR Bot

This is a **Telegram Bot** that extracts text from images using **pytesseract** (Tesseract OCR) and the **Python Telegram API**. Users can send an image to the bot, and it will respond with the extracted text from the image.

## ✨ Features
- **Image-to-text conversion**: Use `pytesseract` to convert images into text.
- **Error handling**: Catches and logs errors during image processing.
- **Instant response**: Quickly processes images and returns extracted text via Telegram.

## 🚀 Getting Started

Follow these steps to set up and run the bot locally.

### 1. Clone the repository
```bash
git clone https://github.com/XredaX/Xtract-Text
cd Xtract-Text
```

### 2. Install dependencies
Make sure you have Python and the necessary libraries installed. Run:
```bash
pip install -r requirements.txt
```

### 3. Install Tesseract
Ensure that Tesseract is installed on your machine. You can install it via:

**Linux:**
```bash
sudo apt update
sudo apt install tesseract-ocr
```

Make sure to set the `TESSDATA_PREFIX` to point to your Tesseract data files (typically for language support).

### 4. Set environment variables
You need to set two environment variables for the bot to work:

- `BOT_TOKEN`: Your Telegram bot token.
- `TESSDATA_PREFIX`: Path to the Tesseract data directory.

You can set these in your terminal or use a `.env` file.

For terminal:
```bash
export BOT_TOKEN="your_telegram_bot_token"
export TESSDATA_PREFIX="/usr/share/tesseract-ocr/5/tessdata"
```

For `.env` file (create this in the root directory):
```
BOT_TOKEN=your_telegram_bot_token
TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata
```

### 5. Run the bot
After setting the environment variables, you can run the bot:
```bash
python bot.py
```

The bot will now be up and running. Send an image to the bot in Telegram, and it will reply with the extracted text.

### Example Commands
- `/start`: Starts the bot and welcomes the user.
- Send an image: The bot will reply with the extracted text from the image.

## 🤝 Contributing
Feel free to open issues or submit pull requests for improvements!

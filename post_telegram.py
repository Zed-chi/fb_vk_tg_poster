import telegram
import os
import utils
from dotenv import load_dotenv


TOKEN = os.getenv("tg_token")
CHAT_ID = os.getenv("tg_chat_id")


def check_bot(bot):
    return bot.get_me()


def post(text_path=None, image_path=None):
    if not text_path or not image_path:
        return None
    text = utils.get_file_content(text_path)
    bot = telegram.Bot(TOKEN)
    if len(text) < 100:
        caption = text
    else:
        caption = None
        bot.send_message(chat_id=CHAT_ID, text=text)
    bot.send_photo(
        chat_id=CHAT_ID,
        photo=open(image_path, "rb"),
        caption=caption
    )


if __name__ == "__main__":
    load_dotenv()
    args = utils.get_args()
    text_path = args["path_to_text"] or exit()
    image_path = args["path_to_image"] or exit()
    post(text_path=text_path, image_path=image_path)

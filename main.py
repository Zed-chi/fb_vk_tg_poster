from post_facebook import post as fb_post
from post_telegram import post as tg_post
from post_vkontakte import post as vk_post
from dotenv import load_dotenv
import utils


if __name__ == "__main__":
	load_dotenv()
    args = utils.get_args()
    text = args["path_to_text"] or exit("Empty path to text")
    image = args["path_to_image"] or exit("Empty path to image")
    fb_post(text_path=text, image_path=image)
    tg_post(text_path=text, image_path=image)
    vk_post(text_path=text, image_path=image)
    print("Done!")

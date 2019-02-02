import os
import requests
from dotenv import load_dotenv
import utils


FB_API = "https://graph.facebook.com/"
FB_GROUP_ID = os.getenv("fb_group_id")
TOKEN = os.getenv("fb_token")


def post_message_to_group(message=None, group_id=None):
    if not group_id or not message:
        return None
    params = {
        "access_token": TOKEN,
        "message": message,
    }
    url = "{}{}{}".format(FB_API, FB_GROUP_ID, "/feed")
    res = requests.post(url, params=params)
    return res.ok


def post_image_to_group(message=None, id=None):
    if not id or not message:
        return None
    url = "{}{}{}".format(FB_API, FB_GROUP_ID, "/feed")
    params = {
        "access_token": TOKEN,
        "message": message,
        "attached_media[0]": str({
            "media_fbid": id
        }),
    }
    res = requests.post(url, params=params)
    return res


def upload_image(image_content):
    url = "{}{}{}".format(FB_API, FB_GROUP_ID, "/photos")
    files = {"file": image_content}
    params = {
        "caption": "test",
        "access_token": TOKEN,
        "published": False,
    }
    res = requests.post(url, params=params, files=files)
    return res


def post(text_path=None, image_path=None):
    image_file = utils.get_file_content(image_path, file_type="image")
    text = utils.get_file_content(text_path)
    upload = upload_image(image_file)
    if upload.ok:
        id = upload.json()["id"]
        post_image_to_group(message=text, id=id)
    else:
        print(upload.status_code)


if __name__ == "__main__":
    load_dotenv()
    args = utils.get_args()
    text_path = args["path_to_text"] or exit()
    image_path = args["path_to_image"] or exit()
    post(text_path=text_path, image_path=image_path)

import vk_api
import os
from dotenv import load_dotenv
import utils


TOKEN = os.getenv("vk_token")
LOGIN = os.getenv("vk_login")
ALB_ID = os.getenv("vk_album_id")
GROUP_ID = os.getenv("vk_group_id")


def post(text_path=None, image_path=None):
    vk_session = vk_api.VkApi(login=LOGIN, token=TOKEN)
    vk = vk_session.get_api()
    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo(
        image_path,
        album_id=ALB_ID,
        group_id=GROUP_ID,
    )
    attachment = "{}{}_{}".format(
        "photo",
        photo[0]['owner_id'],
        photo[0]['id'],
    )
    text = utils.get_file_content(text_path)
    vk.wall.post(
        owner_id=int("-{}".format(GROUP_ID)),
        message=text,
        from_group=1,
        attachments=attachment
    )


if __name__ == "__main__":
    load_dotenv()
    args = utils.get_args()
    text_path = args["path_to_text"] or exit()
    image_path = args["path_to_image"] or exit()
    post(text_path=text_path, image_path=image_path)

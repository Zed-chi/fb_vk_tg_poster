import os
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "path_to_text", help="path to txt file")
    parser.add_argument("-i", "path_to_image", help="path to image file")
    return parser.parse_args()


def get_file_content(path, file_type="text"):
    if not os.path.exists(path):
        return None
    if file_type is "text":
        with open(path, "r") as text_file:
            return text_file.read()
    else:
        with open(path, "rb") as image_file:
            return image_file.read()

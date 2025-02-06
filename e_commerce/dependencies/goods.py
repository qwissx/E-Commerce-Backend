import os


def remove_image(good_id):
    file_name = str(good_id) + ".webp"
    image_path = os.path.join("e_commerce/static/images", file_name)
    if os.path.exists(image_path):
        os.remove(image_path) 
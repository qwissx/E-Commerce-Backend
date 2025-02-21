import os

from e_commerce.dependencies import cache as cD


def remove_image(good_id):
    file_name = str(good_id) + ".webp"
    image_path = os.path.join("e_commerce/static/images", file_name)
    if os.path.exists(image_path):
        os.remove(image_path) 


async def get_goods_from_cache(offset, limit):
    await cD.check_cache()
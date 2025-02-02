import uuid as ui
import shutil as sh

from fastapi import APIRouter, UploadFile, status

images_router = APIRouter(prefix="/images", tags=["Images"])


@images_router.post(path="/goods", status_code=status.HTTP_201_CREATED)
async def save_image(
    good_id: ui.UUID,
    file: UploadFile,
) -> dict[str, str]:
    with open(f"e_commerce/static/images/{good_id}.webp", "wb+") as file_object:
        sh.copyfileobj(file.file, file_object)
    return {"message": "image saved successfully"}

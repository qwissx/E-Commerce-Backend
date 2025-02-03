from fastapi import status
from fastapi.exceptions import HTTPException


class Exc:
    boxes_exceptions = {
        "add": HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cannot find user or good by id"),
        "get": HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cannot find any goods in your box"),
        "rem": HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cannot delete your box"),
    }

    users_exceptions = {
        "add": HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cannot add user, check user data"),
        "get": HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cannot find your profile"),
        "rem": HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cannot delete your profile"),
    }

    goods_exceptions = {
        "add": HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cannot add good, check good data"),
        "get": HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cannot find good"),
        "rem": HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cannot delete good"),
        "get_all": HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cannot find all goods"),
    }


    @classmethod
    def raise_exception(
        cls,
        model,
        exception,
    ):
        if model == "Boxes":
            raise cls.boxes_exceptions.get(exception)
        elif model == "Users":
            raise cls.users_exceptions.get(exception)
        elif model == "Goods":
            raise cls.goods_exceptions.get(exception)

from fastapi import status
from fastapi.exceptions import HTTPException


class SQLExc:
    CannotFindUserOrGood = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cannot find user or good by id")
    CannotFindGoods = HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Cannot find any goods in your box")
    CannotFindBox = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cannot delete your box")

    CannotAddUser = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cannot add user, check user data")
    CannotFindUser = HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Cannot find your profile")
    CannotDeleteUser = HTTPException(status_code=status.HTTP_404_NOT_FOUND  , detail="Cannot delete your profile")

    CannotAddGood = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cannot add good, check good data")
    CannotFindGood = HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Cannot find good")
    CannotDeleteGood = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cannot delete good")
    CannotFindAnyGood = HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Cannot find all goods")

    CannotAddUserInfo = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cannot add user info")
    CannotFindUserInfo = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cannot find your data")
    CannotDeleteUserInfo = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cannot delete your data")


class AuthExc:
    UserExist = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User is already exist")
    UserDoesNotExist = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not exist")
    UserNotAuthorized = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")

    InfoExist = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Info is already exist")

    NotValidPass = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Password is not valid")

    TokenTimeNotValid = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token time is not valid")
    TokenIdNotValid = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token id is not valid")
    TokenUsernameNotValid = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token username is not valid")

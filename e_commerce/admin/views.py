from sqladmin import ModelView

from e_commerce.models.usersModel import Users
from e_commerce.models.usersInfoModel import UsersInfo
from e_commerce.models.goodsModel import Goods


class UsersAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.username]
    column_details_exclude_list = [Users.password]
    can_delete = False
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"


class GoodsAdmin(ModelView, model=Goods):
    column_list = [Goods.name, Goods.type]
    column_details_exclude_list = [Goods.id]
    can_delete = False
    name = "Good"
    name_plural = "Goods"
    icon = "fa-solid fa-cart-shopping" 


class UsersInfoAdmin(ModelView, model=UsersInfo):
    column_list = [UsersInfo.user, UsersInfo.phone_number, UsersInfo.email]
    column_details_exclude_list = [UsersInfo.id]
    can_delete = False
    name = "UserInfo"
    name_plural = "UsersInfo"
    icon = "fa-solid fa-user"

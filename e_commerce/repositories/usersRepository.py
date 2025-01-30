from e_commerce.models import usersModel as uM
from e_commerce.repositories import mixinRepository as mR


class UsersRepository(mR.MixinRepository):
    model_name = uM.Users

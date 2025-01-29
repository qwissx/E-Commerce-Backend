from e_commerce.models import goodsModel as gM
from e_commerce.repositories import mixinRepository as mR


class GoodsRepository(mR.MixinRepository):
    model_name = gM.Goods
    
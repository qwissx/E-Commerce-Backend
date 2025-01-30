from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from e_commerce.routers import goodsRouter as gR


pages_router = APIRouter(prefix="/pages", tags=["Frotend"])

templates = Jinja2Templates(directory="e_commerce/templates")

@pages_router.get(path="/goods")
async def get_goods_page(
    request: Request,
    goods=Depends(gR.get_all_goods)
):
    return templates.TemplateResponse(name="goods.html", context={"request": request})
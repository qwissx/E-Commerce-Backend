from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from e_commerce.routers import goodsRouter as gR
from e_commerce.routers import usersRouter as uR
from e_commerce.routers import boxesRouter as bR

pages_router = APIRouter(prefix="/pages", tags=["Frotend"])

templates = Jinja2Templates(directory="e_commerce/templates")


@pages_router.get(path="/goods", response_class=HTMLResponse)
async def get_goods_page(
    request: Request,
    goods=Depends(gR.get_pagination_goods)
):
    return templates.TemplateResponse(
        name="goods.html", 
        context={"request": request, "goods": goods},
    )


@pages_router.get(path="/user", response_class=HTMLResponse)
async def get_user_page(
    request: Request,
    user=Depends(uR.get_user),
):
    return templates.TemplateResponse(
        name="user.html",
        context={"request": request, "user": user},
    )


@pages_router.get(path="/user_box")
async def get_user_box_page(
    request: Request,
    user=Depends(uR.get_user),
    user_box=Depends(bR.get_box),
):
    return templates.TemplateResponse(
        name="user_box.html",
        context={"request": request, "user_box": user_box, "user": user}
    )


@pages_router.get(path="/register")
async def get_user_register(
    request: Request,
):
    return templates.TemplateResponse(
        name="register.html",
        context={"request": request}
    )
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from e_commerce.routers import usersRouter as uR
from e_commerce.routers import boxesRouter as bR
from e_commerce.routers import goodsRouter as gR
from e_commerce.routers import pagesRouter as pR
from e_commerce.routers import imagesRouter as iR


api = FastAPI(docs_url="/")

api.mount("/static", StaticFiles(directory="e_commerce/static"), "static")

api.include_router(uR.users_router)
api.include_router(bR.boxes_router)
api.include_router(gR.goods_router)
api.include_router(pR.pages_router)
api.include_router(iR.images_router)

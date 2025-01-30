from fastapi import FastAPI

from e_commerce.routers import usersRouter as uR
from e_commerce.routers import boxesRouter as bR
from e_commerce.routers import goodsRouter as gR
from e_commerce.routers import pagesRouter as pR


api = FastAPI(docs_url="/")

api.include_router(uR.users_router)
api.include_router(bR.boxes_router)
api.include_router(gR.goods_router)
api.include_router(pR.pages_router)

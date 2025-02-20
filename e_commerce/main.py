import time

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from e_commerce.routers import usersRouter as uR
from e_commerce.routers import boxesRouter as bR
from e_commerce.routers import goodsRouter as gR
from e_commerce.routers import pagesRouter as pR
from e_commerce.routers import imagesRouter as iR
from e_commerce.routers import authRouter as aR
from e_commerce.routers import userInfoRouter as uiR
from e_commerce.logger import logger
from e_commerce.connections import lifespan


api = FastAPI(docs_url="/", lifespan=lifespan)


api.mount("/static", StaticFiles(directory="e_commerce/static"), "static")


api.include_router(aR.reg_router)
api.include_router(uR.users_router)
api.include_router(bR.boxes_router)
api.include_router(gR.goods_router)
api.include_router(uiR.users_info_router)
api.include_router(pR.pages_router)
api.include_router(iR.images_router)


@api.middleware("http")
async def add_process_time_heade(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info("Request execution time", extra={
        "process_time": round(process_time, 4)
    })
    return response

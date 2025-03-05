import time

from sqladmin import Admin
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from e_commerce.admin.views import (
    UsersAdmin,
    GoodsAdmin,
    UsersInfoAdmin,
)
from e_commerce.admin.auth import authentication_backend
from e_commerce.connections import engine
from e_commerce.routers import usersRouter as uR
from e_commerce.routers import boxesRouter as bR
from e_commerce.routers import goodsRouter as gR
from e_commerce.routers import pagesRouter as pR
from e_commerce.routers import imagesRouter as iR
from e_commerce.routers import authRouter as aR
from e_commerce.routers import userInfoRouter as uiR
from e_commerce.logger import logger
from fastapi.openapi.docs import (
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)


api = FastAPI(docs_url=None)


admin = Admin(api, engine, authentication_backend=authentication_backend)

admin.add_view(UsersAdmin)
admin.add_view(GoodsAdmin)
admin.add_view(UsersInfoAdmin)


api.mount("/static", StaticFiles(directory="e_commerce/static"), "static")


api.include_router(aR.reg_router)
api.include_router(uR.users_router)
api.include_router(bR.boxes_router)
api.include_router(gR.goods_router)
api.include_router(uiR.users_info_router)
api.include_router(pR.pages_router)
api.include_router(iR.images_router)


@api.get("/", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=api.openapi_url,
        title=api.title + " - Swagger UI",
        oauth2_redirect_url=api.swagger_ui_oauth2_redirect_url,
        swagger_js_url=f"https://unpkg.com/swagger-ui-dist@5.18.2/swagger-ui-bundle.js",
        swagger_css_url=f"https://unpkg.com/swagger-ui-dist@5.18.2/swagger-ui.css",
    )


# @api.middleware("http")
# async def add_process_time_heade(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     logger.info("Request execution time", extra={
#         "process_time": round(process_time, 4)
#     })
#     return response

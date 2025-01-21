from fastapi import FastAPI

from e_commerce.routers import usersRouter as uR

api = FastAPI(docs_url="/")

api.include_router(uR.users_router)
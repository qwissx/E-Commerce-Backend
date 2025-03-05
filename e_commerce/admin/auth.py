from sqladmin import Admin
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse

from e_commerce.connections import async_session_maker
from e_commerce.dependencies import auth as aD, users as uD
from e_commerce import settings as st


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        connection = async_session_maker()

        form = await request.form()
        username, password = form["username"], form["password"]

        user = await aD.authenticate_user(connection, username, password)

        access_token = aD.create_access_token({"sub": str(user.id), "username": username})

        request.session.update({"token": access_token})
        return True


    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True


    async def authenticate(self, request: Request) -> bool:
        connection = async_session_maker()

        token = request.session.get("token")

        if not token:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)
        user = await uD.get_current_user(connection, token)
        return True


authentication_backend = AdminAuth(secret_key=st.secret)

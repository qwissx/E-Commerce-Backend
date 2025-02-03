from functools import wraps

from sqlalchemy.exc import SQLAlchemyError

from e_commerce.logger import logger
from e_commerce.exceptions import Exc
from e_commerce.models.boxesModel import Boxes


def SQLErrorHandrel(func):
    @wraps(func)
    async def wrapper(cls, *f_args, **f_kwargs):
        try:
            result = await func(cls, *f_args, **f_kwargs)
            if not result:
                raise Exception
            return result
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = "Database Exc"
            else:
                msg = "Uknown Exc"
            msg += f": cannot do {func.__name__} with {cls.model_name}."
            logger.error(msg, extra=f_kwargs)
            Exc.raise_exception(cls.model_name.__name__, func.__name__)
    return wrapper

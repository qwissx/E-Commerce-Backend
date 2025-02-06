from e_commerce.logger import logger


def logger_add_info(rout_name, **data):
    msg = f"Database Exc: cannot do '{rout_name}'"
    logger.error(msg, extra=data)
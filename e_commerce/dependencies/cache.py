from e_commerce.database import redisDB


async def check_cache(obj_type, key):
    val_key = f"{obj_type}:{key}"
    value = await redisDB.hgetall(val_key)

    return {key.decode(): val.decode() for key, val in value.items()}


async def add_cache(obj_type, key, ex=60, **args):
    val_key = f"{obj_type}:{key}"
    await redisDB.hset(val_key, mapping=args)
    await redisDB.expire(val_key, ex)

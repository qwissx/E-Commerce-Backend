from e_commerce.connections import redisDB


async def check_cache(obj_type, key):
    val_key = f"{obj_type}:{key}"
    value = await redisDB.hgetall(val_key)

    await redisDB.expire(val_key, 60)

    return {key.decode(): val.decode() for key, val in value.items()}


async def add_cache(obj_type, key, **args):
    val_key = f"{obj_type}:{key}"
    await redisDB.hset(val_key, mapping=args)
    await redisDB.expire(val_key, 60)

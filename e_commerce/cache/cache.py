import json

from e_commerce.connections import redis


async def check_cache(val_key):
    value = await redis.get(val_key)
    if not value:
        return None

    await redis.expire(val_key, 60)

    return json.loads(value.decode())


async def add_cache(val_key, exp=60, **kwargs):
    serialized_data = json.dumps(kwargs)

    await redis.set(val_key, serialized_data)
    await redis.expire(val_key, exp)


async def check_cache_list(val_key, offset, limit):
    values = await redis.lrange(val_key, offset, offset+limit)
    if not values:
        return None

    serialized_values = []
    for value in values:
        serialized_values.append(json.loads(value.decode()))

    return serialized_values


async def add_cache_list(val_key, values: list, exp=60):
    for value in values:
        serialized_value = json.dumps(value)
        await redis.rpush(val_key, serialized_value)

        await redis.expire(val_key, exp)


async def remove_cache(val_key):
    await redis.delete(val_key)

import json

from e_commerce.connections import redis


async def check_cache(obj_type, key):
    val_key = f"{obj_type}:{key}"
    value = await redis.get(val_key)
    if not value:
        return None

    await redis.expire(val_key, 60)

    return json.loads(value.decode())


async def add_cache(obj_type, key, exp=60, **kwargs):
    val_key = f"{obj_type}:{key}"

    serialized_data = json.dumps(kwargs)

    await redis.set(val_key, serialized_data)
    await redis.expire(val_key, exp)


async def check_cache_list(obj_type, cur_count, limit):
    val_key = f"{obj_type}:pagination"
    values = await redis.lrange(val_key, cur_count, cur_count+limit)
    if not values:
        return None

    serialized_values = []
    for value in values:
        serialized_values.append(json.loads(value.decode()))

    return serialized_values


async def add_cache_list(obj_type, exp=60, **kwargs):
    val_key = f"{obj_type}:pagination"

    serialized_value = json.dumps(kwargs)
    await redis_client.rpush(val_key, serialized_user)

    await redis.expire(val_key, exp)

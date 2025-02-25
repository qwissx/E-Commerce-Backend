from sqlalchemy.ext.asyncio import AsyncSession

from e_commerce.cache import cache as cD
from e_commerce.models.usersModel import Users


class Cache:
    
    @classmethod
    async def get(
        cls, 
        model: str, 
        key: str, 
        repository, 
        connection: AsyncSession, 
        offset=0, 
        limit=0,
        **filter_by,
    ):
        val_key = f"{model}:{key}"
        if key == "pagination":
            values = await cls._get_cache_or_from_rep_pag(
                val_key=val_key, 
                offset=offset, 
                limit=limit, 
                repository=repository, 
                connection=connection,
            )
            return values
        else:
            value = await cls._get_cache_or_from_rep_one(
                val_key=val_key,
                repository=repository,
                connection=connection,
                **filter_by,
            )
            return value

    @classmethod
    async def add(cls, model, key, **kwargs):
        val_key = f"{model}:{key}"
        await cD.add_cache(val_key, **kwargs)

    @classmethod
    async def rem(cls, model, key):
        val_key = f"{model}:{key}"
        if await cD.check_cache(val_key):
            await cD.remove_cache(val_key)

    @classmethod
    async def _get_cache_or_from_rep_one(
        cls, 
        val_key, 
        repository, 
        connection: AsyncSession,
        **filter_by,
    ):
        value = await cD.check_cache(val_key)

        if value is None:
            value = await repository.get(
                connection=connection,
                **filter_by,
            )

            if value is None:
                return None

            value_dict = value.__dict__
            value_dict.pop("_sa_instance_state", None)
            value_dict["id"] = str(value_dict["id"])

            await cD.add_cache(val_key, **value_dict)

        return value

    @classmethod
    async def _get_cache_or_from_rep_pag(
        cls, 
        val_key, 
        offset, 
        limit, 
        repository, 
        connection: AsyncSession,
    ):
        values = await cD.check_cache_list(val_key, offset, limit)

        if values is None:
            values = await repository.get_pagination(
                connection=connection, 
                offset=offset, 
                limit=limit,
            )
            values_dict = []
            for value in values:
                value = value.__dict__
                value.pop("_sa_instance_state", None)
                value["id"] = str(value["id"])

                values_dict.append(value)

            await cD.add_cache_list(val_key, *values_dict)

        return values
    
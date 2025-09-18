from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
        self,
        command,
        *args,
        fetch: bool = False,
        fetchval: bool = False,
        fetchrow: bool = False,
        execute: bool = False,
    ):
        
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_user(self, name, username, chat_id, phone):
        sql = "INSERT INTO users(name, username, chat_id, phone) VALUES($1, $2, $3, $4) returning *"
        return await self.execute(sql, name, username, chat_id, phone, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM users"
        return await self.execute(sql, fetch=True)
    
    async def get_one_user(self, chat_id):
        sql = "SELECT * FROM users WHERE chat_id = $1"
        return await self.execute(sql, chat_id, fetch=True)

    async def select_user(self, chat_id, **kwargs):
        sql = "SELECT * FROM users where chat_id = $1"
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, chat_id, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM users"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE users", execute=True)
    
    
    async def add_yer_data(self, user_id, photos, captions, message_id):
        sql = "INSERT INTO yer(user_id, photos, captions, message_id) VALUES($1, $2, $3, $4) returning *"
        return await self.execute(sql, user_id, photos, captions, message_id, fetchrow=True)

    async def yer_get_one_user_data(self, message_id: int):
        sql = "SELECT * FROM yer WHERE message_id = $1"
        return await self.execute(sql, message_id, fetchrow=True)

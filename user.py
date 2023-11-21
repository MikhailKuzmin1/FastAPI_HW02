from fastapi import APIRouter
from model import User, UserIn
from db import users, database
from typing import List

router=APIRouter()

@router.get('/')
async def root():
    return 'Hello'

@router.get('/users/', response_model=List[User])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)

@router.get('/users/{user_id}', response_model= User | None)
async def one_user(user_id: int):
    query = users.select().where(users.c.id==user_id)
    return await database.fetch_one(query)

@router.post('/users/', response_model=str)
async def creat_user(user: UserIn):
    query = users.insert().values(name=user.name, email=user.email, surname=user.surname, password=user.password)
    await database.execute(query)
    return f'Пользователь добавлен'

@router.put('/users/{user_id}', response_model=str)
async def edit_user(user_id:int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(name=new_user.name, email=new_user.email, password=new_user.password)
    await database.execute(query)
    return f'Пользователь изменен'

@router.delete('/users/{user_id}', response_model=str)
async def del_user(user_id: int):
    query = users.delete().where(users.c.id==user_id)
    await database.execute(query)
    return f'Пользователь удален'

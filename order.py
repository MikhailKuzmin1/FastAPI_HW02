from fastapi import APIRouter
from model import Order, OrderIn
from db import orders, database
from typing import List

router=APIRouter()


@router.get('/orders/', response_model=List[Order])
async def get_order():
    query = orders.select()
    return await database.fetch_all(query)

@router.get('/orders/{order_id}', response_model= Order | None)
async def one_order(order_id: int):
    query = orders.select().where(orders.c.id==order_id)
    return await database.fetch_one(query)

@router.post('/orders/', response_model=str)
async def creat_order(order: OrderIn):
    query = orders.insert().values(user_id=order.user_id, product_id=order.product_id, date=order.date, status=order.status)
    await database.execute(query)
    return f'Заказ добавлен'

@router.put('/orders/{order_id}', response_model=str)
async def edit_order(order_id:int, new_order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(
        user_id=new_order.user_id,
        product_id=new_order.product_id, 
        date=new_order.date, 
        status=new_order.status
        )
    await database.execute(query)
    return f'Заказ изменен'

@router.delete('/orders/{order_id}', response_model=str)
async def del_order(order_id: int):
    query = orders.delete().where(orders.c.id==order_id)
    await database.execute(query)
    return f'Заказ удален'

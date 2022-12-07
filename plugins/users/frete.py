from typing import Union
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import BadRequest
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ForceReply,
    Message,
)

from database import cur, save
from utils import create_mention, get_info_wallet, dobrosaldo, get_price
from config import BOT_LINK
from config import BOT_LINK_SUPORTE
from config import ADMIN_CHAT



@Client.on_message(filters.command(["frete", "fretes"]))
@Client.on_callback_query(filters.regex("^frete$"))
async def frete(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    #precos abaixo
    preco1 = "5"
    preco2 = "6"
    preco3 = "9"
    preco4 = "11"
    preco5 = "98"
    preco6 = "7"
    preco7 = "1"
    preco8 = "3"
    preco9 = "10"
    preco10 = "2"
    

    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("AC", callback_data=f"frete_1 {preco1} Acre"),
                InlineKeyboardButton("AL", callback_data=f"frete_2 {preco10} Alagoas"),
            ],
            
            [
                InlineKeyboardButton("AP", callback_data=f"frete_3 {preco2} Amapá"),
                InlineKeyboardButton("AM", callback_data=f"cardapio_3 {preco3} SKYWALKER"),
                
            ],
            [
            InlineKeyboardButton("BA", callback_data=f"cardapio_4 {preco4} SKYWALKER"),
            InlineKeyboardButton("CE", callback_data=f"cardapio_5 {preco5} SKYWALKER"),
            ],
            
             [
            InlineKeyboardButton("DF", callback_data=f"cardapio_6 {preco6} SKYWALKER"),
                InlineKeyboardButton("ES", callback_data=f"cardapio_7 {preco7} SKYWALKER"),
            ],
             [
            InlineKeyboardButton("GO", callback_data=f"cardapio_8 {preco8} SKYWALKER"),
                InlineKeyboardButton("MA", callback_data=f"cardapio_9 {preco9} SKYWALKER"),
            ],
            
            [
                InlineKeyboardButton("MT", callback_data=f"cardapio_1 {preco1} SKYWALKER"),
                InlineKeyboardButton("MS", callback_data=f"cardapio_10 {preco10} SKYWALKER"),
            ],
            
            [
                InlineKeyboardButton("MG", callback_data=f"cardapio_2 {preco2} SKYWALKER"),
                InlineKeyboardButton("PA", callback_data=f"cardapio_3 {preco3} SKYWALKER"),
                
            ],
            [
            InlineKeyboardButton("PB", callback_data=f"cardapio_4 {preco4} SKYWALKER"),
            InlineKeyboardButton("PR", callback_data=f"cardapio_5 {preco5} SKYWALKER"),
            ],
            
             [
            InlineKeyboardButton("PE", callback_data=f"cardapio_6 {preco6} SKYWALKER"),
                InlineKeyboardButton("PI", callback_data=f"cardapio_7 {preco7} SKYWALKER"),
            ],
             [
            InlineKeyboardButton("RJ", callback_data=f"cardapio_8 {preco8} SKYWALKER"),
                InlineKeyboardButton("RN", callback_data=f"cardapio_9 {preco9} SKYWALKER"),
            ],
            
            [
                InlineKeyboardButton("RS", callback_data=f"cardapio_1 {preco1} SKYWALKER"),
                InlineKeyboardButton("RO", callback_data=f"cardapio_10 {preco10} SKYWALKER"),
            ],
            
            [
                InlineKeyboardButton("RR", callback_data=f"cardapio_2 {preco2} SKYWALKER"),
                InlineKeyboardButton("SP", callback_data=f"cardapio_3 {preco3} SKYWALKER"),
                
            ],
            [
            InlineKeyboardButton("SC", callback_data=f"cardapio_4 {preco4} SKYWALKER"),
            InlineKeyboardButton("SE", callback_data=f"cardapio_5 {preco5} SKYWALKER"),
            ],
            
             [
            InlineKeyboardButton("TO", callback_data=f"cardapio_6 {preco6} SKYWALKER"),
            ],
            [
            InlineKeyboardButton("Voltar", callback_data=f"start"),
            ],
            
        ]
    )

    bot_logo, news_channel, support_user = cur.execute(
        "SELECT main_img, channel_user, support_user FROM bot_config WHERE ROWID = 0"
    ).fetchone()

    start_message = f"""Escolha o que deseja comprar e prossiga para o pedido, após concluído, sua comida chegará em sua casa! 😋
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
    
    
    

@Client.on_callback_query(filters.regex("^frete_1 (?P<value>\w+) (?P<id>.+)"))
async def frete_1(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    cardapio_1 = m.matches[0]["value"]
    id = m.matches[0]["id"]

    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZoaHxOwGpEn4RStB0P7SNastIq-tWkuksZg&usqp=CAU"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
Hambúrguer Big Mada
<b>Preco:</b> {cardapio_1}


Dois deliciosos hambúrgueres artesanais de 80g cada carne, pão de 70g, alface americano, fatias de queijo cheddar derretido, cebola roxa, picles e molho especial.

Serve muito bem uma pessoa!

#bigmada #hamburguerartesanal
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)

    
@Client.on_callback_query(filters.regex("^frete_2 (?P<value>\w+) (?P<id>.+)"))
async def frete_2(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    cardapio_1 = m.matches[0]["value"]
    id = m.matches[0]["id"]

    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWaPD9899XYJ03-x6yBCCt3BBorz3s0yMHrw&usqp=CAU"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
Hambúrguer Mada Bacon Duplo - o Matador de Fome!
<b>Preco:</b> {cardapio_1}


Dois deliciosos hambúrgueres artesanais Gigante de 160g cada carne,pão tipo brioche 70g, fatias de queijo cheddar derretido, tiras de bacon em Dobro e nossa Divina maionese artesanal feita com ervas finas.

Esse é o Matador de Fome, experimente já! Grandes Fomes!

#Duplobacon #Madaburguer
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
 
@Client.on_callback_query(filters.regex("^frete_3 (?P<value>\w+) (?P<id>.+)"))
async def frete_3(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    cardapio_1 = m.matches[0]["value"]
    id = m.matches[0]["id"]

    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1H4xCfgi0W5GFJUwfHbvnE4AjBZJpr-DS7g&usqp=CAU"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
Dam cheese
<b>Preco:</b> {cardapio_1}


Suculento blend de angus 180g, cheddar artesanal e pão brioche
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)    
    

    
@Client.on_callback_query(filters.regex("^frete_4 (?P<value>\w+) (?P<id>.+)"))
async def frete_4(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    cardapio_1 = m.matches[0]["value"]
    id = m.matches[0]["id"]

    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://instadelivery-public.nyc3.cdn.digitaloceanspaces.com/itens/4o7lxKyJyydrvMiN23DyJrIUOKJPOKrDOF5veEjd.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
Dam Monster cheddar
<b>Preco:</b> {cardapio_1}


Pão brioche, duas carnes de hambúrguer blend angus 180gr, uma fatia de queijo cheddar 15gr em cada carne + uma calda de cheddar cremoso que acompanha o lanche.
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
                
                            
@Client.on_callback_query(filters.regex("^frete_5 (?P<value>\w+) (?P<id>.+)"))
async def frete_5(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    cardapio_1 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkJSRrVC1b76sTxerVCew75CPex_E4DvqZ2w&usqp=CAU"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
Anéis de cebola empanados
<b>Preco:</b> {cardapio_1}


Porção de anéis de cebola empanada e sequinha com tempero especial. Acompanha maionese verde artesanal.
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
                                           
                                                                                  
@Client.on_callback_query(filters.regex("^frete_6 (?P<value>\w+) (?P<id>.+)"))
async def frete_6(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    cardapio_1 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZoaHxOwGpEn4RStB0P7SNastIq-tWkuksZg&usqp=CAU"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
Hambúrguer Big Mada
<b>Preco:</b> {cardapio_1}


Dois deliciosos hambúrgueres artesanais de 80g cada carne, pão de 70g, alface americano, fatias de queijo cheddar derretido, cebola roxa, picles e molho especial.

Serve muito bem uma pessoa!

#bigmada #hamburguerartesanal
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)                                                                                                                         
                                                                                                                                                                  
  
@Client.on_callback_query(filters.regex("^frete_7 (?P<value>\w+) (?P<id>.+)"))
async def frete_7(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    cardapio_1 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZoaHxOwGpEn4RStB0P7SNastIq-tWkuksZg&usqp=CAU"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
Hambúrguer Big Mada
<b>Preco:</b> {cardapio_1}


Dois deliciosos hambúrgueres artesanais de 80g cada carne, pão de 70g, alface americano, fatias de queijo cheddar derretido, cebola roxa, picles e molho especial.

Serve muito bem uma pessoa!

#bigmada #hamburguerartesanal
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)  
  

  
@Client.on_callback_query(filters.regex("^frete_8 (?P<value>\w+) (?P<id>.+)"))
async def frete_8(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    cardapio_1 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZoaHxOwGpEn4RStB0P7SNastIq-tWkuksZg&usqp=CAU"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
Hambúrguer Big Mada
<b>Preco:</b> {cardapio_1}


Dois deliciosos hambúrgueres artesanais de 80g cada carne, pão de 70g, alface americano, fatias de queijo cheddar derretido, cebola roxa, picles e molho especial.

Serve muito bem uma pessoa!

#bigmada #hamburguerartesanal
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)    

        
                
@Client.on_callback_query(filters.regex("^frete_9 (?P<value>\w+) (?P<id>.+)"))
async def frete_9(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    cardapio_1 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZoaHxOwGpEn4RStB0P7SNastIq-tWkuksZg&usqp=CAU"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
Hambúrguer Big Mada
<b>Preco:</b> {cardapio_1}


Dois deliciosos hambúrgueres artesanais de 80g cada carne, pão de 70g, alface americano, fatias de queijo cheddar derretido, cebola roxa, picles e molho especial.

Serve muito bem uma pessoa!

#bigmada #hamburguerartesanal
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)                        

                                        
@Client.on_callback_query(filters.regex("^frete_10 (?P<value>\w+) (?P<id>.+)"))
async def frete_10(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    cardapio_1 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZoaHxOwGpEn4RStB0P7SNastIq-tWkuksZg&usqp=CAU"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
Hambúrguer Big Mada
<b>Preco:</b> {cardapio_1}


Dois deliciosos hambúrgueres artesanais de 80g cada carne, pão de 70g, alface americano, fatias de queijo cheddar derretido, cebola roxa, picles e molho especial.

Serve muito bem uma pessoa!

#bigmada #hamburguerartesanal
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)                                                                                
                                                                                                                                                                
#@Client.on_callback_query(filters.regex(r"^buyfrete (?P<value>\w+) (?P<id>.+)"))
#async def buyfrete_food(c: Client, m: CallbackQuery):
#	await m.message.delete()
#	user_id = m.from_user.id
#	qry = m.matches[0]["value"]
#	id = m.matches[0]["id"]
#	start_message = f"SEU PEDIIDO FOI FEITO, ID: {id}"




#if None in (dados[0], dados[2]) and select_pay == "mercado pago":
#        name = await m.message.ask("Informe o cep", reply_markup=ForceReply())
#else:
	
#@Client.on_callback_query(
#    filters.regex(r"buyfrete (?P<value>.+) (?P<id>.+)")
#)
#async def buyfrete(c: Client, m: CallbackQuery):
#    await m.message.delete()
#    dados = cur.execute("SELECT cpf, name, email FROM users  WHERE id =?", [m.from_user.id]).fetchone()
#    qry = m.matches[0]["value"]
#    id = qry = m.matches[0]["value"]
#    buyfrete = "buyfrete"
#    
#if None in (dados[0], dados[2]) and buyfrete == "buyfrete":
#    name = await m.message.ask("Informe o nome do cep", reply_markup=ForceReply())
#   # isExist = os.path.exists(name.text)
#else:
#	await m.edit_message_text(f"""<b>Seu pedido foi efetuado com sucesso</b>
#Valor: {qry}
#Pedido: {id}

#Observações: podemos entrar em contato com você caso algo aconteça com seu pedido🍟

#Endereço de entrega: """,)
@Client.on_callback_query(
    filters.regex(r"buyfrete (?P<value>.+) (?P<id>.+)")
)
async def buyfrete_frete(c: Client, m: CallbackQuery):

    qry = m.matches[0]["value"]
    id = m.matches[0]["id"]
    dados = cur.execute(
        "SELECT cpf, name, email FROM users  WHERE id = ?", [m.from_user.id]
    ).fetchone()
    user_id = m.from_user.id
    balance: int = cur.execute("SELECT balance FROM users WHERE id = ?", [user_id]).fetchone()[0]
    price = int(qry)

    if balance < price:
        return await m.answer(
            "Você não possui saldo para realizar esta compra. Por favor, adicione saldo no menu principal.",
            show_alert=True,
        )
        
#    await m.message.delete()
#    name = await m.message.ask("""Informe o endereco completo de entrega\n
#NOME:
#CPF;
#ENDEREÇO:
#N⁰:
#COMPLEMENTO: 
#BAIRRO:
#CIDADE:
#ESTADO:
#CEP:""", reply_markup=ForceReply())
    


    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(f"ID: #{id}", callback_data=f"{id}")],
        ]
    )


    await m.message.reply_text(
        f"""<b>Seu pedido foi efetuado com sucesso</b>
Valor: {qry}
Pedido: {id}

Observações: seu pedido estará em breve em sua casa!🍟""", reply_markup=kb
    )	
    new_balance = balance - price
    diamonds = 0
    cur.execute(
        "UPDATE users SET balance = ?, balance_diamonds = round(balance_diamonds + ?, 2) WHERE id = ?",
        [new_balance, diamonds, user_id],
    )
    mention = create_mention(m.from_user)
    await m.message.reply_text(
        f"""<b>Foram descontados {qry} da sua carteira, seu pedido estará em breve em sua casa!

Observações: em caso de problemas entraremos em contato</b>
""", )
    adm_msg = f"""Usuário: {mention} comprou um: {id}
Valor: {qry}

Status: Pago com sucesso"""	  
    await c.send_message(ADMIN_CHAT, adm_msg)i
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



@Client.on_message(filters.command(["cardapio", "cardapio"]))
@Client.on_callback_query(filters.regex("^cardapio$"))
async def cardapio(c: Client, m: Union[Message, CallbackQuery]):
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
                InlineKeyboardButton("AC", callback_data=f"cardapio_1 {preco1} Acre"),
                InlineKeyboardButton("AL", callback_data=f"cardapio_10 {preco10} Alagoas"),
            ],
            
            [
                InlineKeyboardButton("AP", callback_data=f"cardapio_2 {preco2} Amapá"),
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
                InlineKeyboardButton("SKYWALKER2", callback_data=f"cardapio_10 {preco10} SKYWALKER"),
            ],
            
            [
                InlineKeyboardButton("RO", callback_data=f"cardapio_2 {preco2} SKYWALKER"),
                InlineKeyboardButton("SKYWALKER4", callback_data=f"cardapio_3 {preco3} SKYWALKER"),
                
            ],
            [
            InlineKeyboardButton("RR", callback_data=f"cardapio_4 {preco4} SKYWALKER"),
            InlineKeyboardButton("SP", callback_data=f"cardapio_5 {preco5} SKYWALKER"),
            ],
            
             [
            InlineKeyboardButton("SC", callback_data=f"cardapio_6 {preco6} SKYWALKER"),
                InlineKeyboardButton("SE", callback_data=f"cardapio_7 {preco7} SKYWALKER"),
            ],
             [
            InlineKeyboardButton("TO", callback_data=f"cardapio_8 {preco8} SKYWALKER"),
            ],
                        
            [
            InlineKeyboardButton("Voltar", callback_data=f"start"),
            ],
            
        ]
    )

    bot_logo, news_channel, support_user = cur.execute(
        "SELECT main_img, channel_user, support_user FROM bot_config WHERE ROWID = 0"
    ).fetchone()

    start_message = f"""Escolha o produto  que deseja comprar  após concluído, seu produto será enviado para o enredeço fonrcido por você!
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
    
    
    

@Client.on_callback_query(filters.regex("^cardapio_1 (?P<value>\w+) (?P<id>.+)"))
async def cardapio_1(c: Client, m: Union[Message, CallbackQuery]):
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
                InlineKeyboardButton("Comprar",callback_data=f"buy {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("VOLTAR🔙",callback_data="cardapio"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/Z1YGhcg/SKY.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
oleo skywalker
<b>Preco:</b> {cardapio_1}


O Oleo de Skywalker provem de um
cruzamento dominante de Indicas
campeas – Blueberry e Mazar.

Neste perfil você pode experimentar
um incrível aroma de Mirtilo,
balanceado com notas Tropicais,
refrescantes e levemente terrosos.

É ideal para quem sofre de dores 
leves, insônia, estresse ou ansiedade.

Os usuários desta cepa potente
são tratados com uma experiência
fora deste mundo, pontuada por elevações 
corporais profundas e sentimentos de euforia.

Espalhe a terra sob seus pés e deixe as forças guiá-lo.
Precauções: Manter ao abrigo da luz e calor.

O armazenamento inadequado pode causar degradação.
Ficou com alguma dúvida?
Acesse nosso FAQ ou entre
em contato com um de nossos especialistas.

características
Specification 
Peso
0,1 kg
Dimensões
2 × 2 × 2 cm


#skywalker #skywalker
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)

    
@Client.on_callback_query(filters.regex("^cardapio_2 (?P<value>\w+) (?P<id>.+)"))
async def cardapio_2(c: Client, m: Union[Message, CallbackQuery]):
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
                InlineKeyboardButton("Comprar",callback_data=f"buy {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("VOLTAR🔙",callback_data="cardapio"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/Z1YGhcg/SKY.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
oleo skywalker
<b>Preco:</b> {cardapio_1}


O Oleo de Skywalker provem de um
cruzamento dominante de Indicas
campeas – Blueberry e Mazar.

Neste perfil você pode experimentar
um incrível aroma de Mirtilo,
balanceado com notas Tropicais,
refrescantes e levemente terrosos.

É ideal para quem sofre de dores 
leves, insônia, estresse ou ansiedade.

Os usuários desta cepa potente
são tratados com uma experiência
fora deste mundo, pontuada por elevações 
corporais profundas e sentimentos de euforia.

Espalhe a terra sob seus pés e deixe as forças guiá-lo.
Precauções: Manter ao abrigo da luz e calor.

O armazenamento inadequado pode causar degradação.
Ficou com alguma dúvida?
Acesse nosso FAQ ou entre
em contato com um de nossos especialistas.

características
Specification 
Peso
0,1 kg
Dimensões
2 × 2 × 2 cm


#skywalker #skywalker
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
 
@Client.on_callback_query(filters.regex("^cardapio_3 (?P<value>\w+) (?P<id>.+)"))
async def cardapio_3(c: Client, m: Union[Message, CallbackQuery]):
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
                InlineKeyboardButton("Comprar",callback_data=f"buy {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("VOLTAR🔙",callback_data="cardapio"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/Z1YGhcg/SKY.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
oleo skywalker
<b>Preco:</b> {cardapio_1}


O Oleo de Skywalker provem de um
cruzamento dominante de Indicas
campeas – Blueberry e Mazar.

Neste perfil você pode experimentar
um incrível aroma de Mirtilo,
balanceado com notas Tropicais,
refrescantes e levemente terrosos.

É ideal para quem sofre de dores 
leves, insônia, estresse ou ansiedade.

Os usuários desta cepa potente
são tratados com uma experiência
fora deste mundo, pontuada por elevações 
corporais profundas e sentimentos de euforia.

Espalhe a terra sob seus pés e deixe as forças guiá-lo.
Precauções: Manter ao abrigo da luz e calor.

O armazenamento inadequado pode causar degradação.
Ficou com alguma dúvida?
Acesse nosso FAQ ou entre
em contato com um de nossos especialistas.

características
Specification 
Peso
0,1 kg
Dimensões
2 × 2 × 2 cm


#skywalker #skywalker
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)    
    

    
@Client.on_callback_query(filters.regex("^cardapio_4 (?P<value>\w+) (?P<id>.+)"))
async def cardapio_4(c: Client, m: Union[Message, CallbackQuery]):
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
                InlineKeyboardButton("Comprar",callback_data=f"buy {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("VOLTAR🔙",callback_data="cardapio"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/Z1YGhcg/SKY.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
oleo skywalker
<b>Preco:</b> {cardapio_1}


O Oleo de Skywalker provem de um
cruzamento dominante de Indicas
campeas – Blueberry e Mazar.

Neste perfil você pode experimentar
um incrível aroma de Mirtilo,
balanceado com notas Tropicais,
refrescantes e levemente terrosos.

É ideal para quem sofre de dores 
leves, insônia, estresse ou ansiedade.

Os usuários desta cepa potente
são tratados com uma experiência
fora deste mundo, pontuada por elevações 
corporais profundas e sentimentos de euforia.

Espalhe a terra sob seus pés e deixe as forças guiá-lo.
Precauções: Manter ao abrigo da luz e calor.

O armazenamento inadequado pode causar degradação.
Ficou com alguma dúvida?
Acesse nosso FAQ ou entre
em contato com um de nossos especialistas.

características
Specification 
Peso
0,1 kg
Dimensões
2 × 2 × 2 cm


#skywalker #skywalker
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
                
                            
@Client.on_callback_query(filters.regex("^cardapio_5 (?P<value>\w+) (?P<id>.+)"))
async def cardapio_5(c: Client, m: Union[Message, CallbackQuery]):
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
                InlineKeyboardButton("Comprar",callback_data=f"buy {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("VOLTAR🔙",callback_data="cardapio"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/Z1YGhcg/SKY.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
oleo skywalker
<b>Preco:</b> {cardapio_1}


O Oleo de Skywalker provem de um
cruzamento dominante de Indicas
campeas – Blueberry e Mazar.

Neste perfil você pode experimentar
um incrível aroma de Mirtilo,
balanceado com notas Tropicais,
refrescantes e levemente terrosos.

É ideal para quem sofre de dores 
leves, insônia, estresse ou ansiedade.

Os usuários desta cepa potente
são tratados com uma experiência
fora deste mundo, pontuada por elevações 
corporais profundas e sentimentos de euforia.

Espalhe a terra sob seus pés e deixe as forças guiá-lo.
Precauções: Manter ao abrigo da luz e calor.

O armazenamento inadequado pode causar degradação.
Ficou com alguma dúvida?
Acesse nosso FAQ ou entre
em contato com um de nossos especialistas.

características
Specification 
Peso
0,1 kg
Dimensões
2 × 2 × 2 cm


#skywalker #skywalker
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
                                           
                                                                                  
@Client.on_callback_query(filters.regex("^cardapio_6 (?P<value>\w+) (?P<id>.+)"))
async def cardapio_6(c: Client, m: Union[Message, CallbackQuery]):
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
                InlineKeyboardButton("Comprar",callback_data=f"buy {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("VOLTAR🔙",callback_data="cardapio"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/Z1YGhcg/SKY.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
oleo skywalker
<b>Preco:</b> {cardapio_1}


O Oleo de Skywalker provem de um
cruzamento dominante de Indicas
campeas – Blueberry e Mazar.

Neste perfil você pode experimentar
um incrível aroma de Mirtilo,
balanceado com notas Tropicais,
refrescantes e levemente terrosos.

É ideal para quem sofre de dores 
leves, insônia, estresse ou ansiedade.

Os usuários desta cepa potente
são tratados com uma experiência
fora deste mundo, pontuada por elevações 
corporais profundas e sentimentos de euforia.

Espalhe a terra sob seus pés e deixe as forças guiá-lo.
Precauções: Manter ao abrigo da luz e calor.

O armazenamento inadequado pode causar degradação.
Ficou com alguma dúvida?
Acesse nosso FAQ ou entre
em contato com um de nossos especialistas.

características
Specification 
Peso
0,1 kg
Dimensões
2 × 2 × 2 cm


#skywalker #skywalker
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)                                                                                                                         
                                                                                                                                                                  
  
@Client.on_callback_query(filters.regex("^cardapio_7 (?P<value>\w+) (?P<id>.+)"))
async def cardapio_7(c: Client, m: Union[Message, CallbackQuery]):
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
                InlineKeyboardButton("Comprar",callback_data=f"buy {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("VOLTAR🔙",callback_data="cardapio"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/Z1YGhcg/SKY.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
oleo skywalker
<b>Preco:</b> {cardapio_1}


O Oleo de Skywalker provem de um
cruzamento dominante de Indicas
campeas – Blueberry e Mazar.

Neste perfil você pode experimentar
um incrível aroma de Mirtilo,
balanceado com notas Tropicais,
refrescantes e levemente terrosos.

É ideal para quem sofre de dores 
leves, insônia, estresse ou ansiedade.

Os usuários desta cepa potente
são tratados com uma experiência
fora deste mundo, pontuada por elevações 
corporais profundas e sentimentos de euforia.

Espalhe a terra sob seus pés e deixe as forças guiá-lo.
Precauções: Manter ao abrigo da luz e calor.

O armazenamento inadequado pode causar degradação.
Ficou com alguma dúvida?
Acesse nosso FAQ ou entre
em contato com um de nossos especialistas.

características
Specification 
Peso
0,1 kg
Dimensões
2 × 2 × 2 cm


#skywalker #skywalker
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)  
  

  
@Client.on_callback_query(filters.regex("^cardapio_8 (?P<value>\w+) (?P<id>.+)"))
async def cardapio_8(c: Client, m: Union[Message, CallbackQuery]):
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
                InlineKeyboardButton("Comprar",callback_data=f"buy {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("VOLTAR🔙",callback_data="cardapio"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/Z1YGhcg/SKY.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
oleo skywalker
<b>Preco:</b> {cardapio_1}


O Oleo de Skywalker provem de um
cruzamento dominante de Indicas
campeas – Blueberry e Mazar.

Neste perfil você pode experimentar
um incrível aroma de Mirtilo,
balanceado com notas Tropicais,
refrescantes e levemente terrosos.

É ideal para quem sofre de dores 
leves, insônia, estresse ou ansiedade.

Os usuários desta cepa potente
são tratados com uma experiência
fora deste mundo, pontuada por elevações 
corporais profundas e sentimentos de euforia.

Espalhe a terra sob seus pés e deixe as forças guiá-lo.
Precauções: Manter ao abrigo da luz e calor.

O armazenamento inadequado pode causar degradação.
Ficou com alguma dúvida?
Acesse nosso FAQ ou entre
em contato com um de nossos especialistas.

características
Specification 
Peso
0,1 kg
Dimensões
2 × 2 × 2 cm


#skywalker #skywalker
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)    

        
                
@Client.on_callback_query(filters.regex("^cardapio_9 (?P<value>\w+) (?P<id>.+)"))
async def cardapio_9(c: Client, m: Union[Message, CallbackQuery]):
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
                InlineKeyboardButton("Comprar",callback_data=f"buy {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("VOLTAR🔙",callback_data="cardapio"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/Z1YGhcg/SKY.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
oleo skywalker
<b>Preco:</b> {cardapio_1}


O Oleo de Skywalker provem de um
cruzamento dominante de Indicas
campeas – Blueberry e Mazar.

Neste perfil você pode experimentar
um incrível aroma de Mirtilo,
balanceado com notas Tropicais,
refrescantes e levemente terrosos.

É ideal para quem sofre de dores 
leves, insônia, estresse ou ansiedade.

Os usuários desta cepa potente
são tratados com uma experiência
fora deste mundo, pontuada por elevações 
corporais profundas e sentimentos de euforia.

Espalhe a terra sob seus pés e deixe as forças guiá-lo.
Precauções: Manter ao abrigo da luz e calor.

O armazenamento inadequado pode causar degradação.
Ficou com alguma dúvida?
Acesse nosso FAQ ou entre
em contato com um de nossos especialistas.

características
Specification 
Peso
0,1 kg
Dimensões
2 × 2 × 2 cm


#skywalker #skywalker
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)                        

                                        
@Client.on_callback_query(filters.regex("^cardapio_10 (?P<value>\w+) (?P<id>.+)"))
async def cardapio_10(c: Client, m: Union[Message, CallbackQuery]):
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
                InlineKeyboardButton("Comprar",callback_data=f"buy {cardapio_1} {id}"),
            ],
[
                InlineKeyboardButton("VOLTAR🔙",callback_data="cardapio"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/Z1YGhcg/SKY.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
oleo skywalker
<b>Preco:</b> {cardapio_1}


O Oleo de Skywalker provem de um
cruzamento dominante de Indicas
campeas – Blueberry e Mazar.

Neste perfil você pode experimentar
um incrível aroma de Mirtilo,
balanceado com notas Tropicais,
refrescantes e levemente terrosos.

É ideal para quem sofre de dores 
leves, insônia, estresse ou ansiedade.

Os usuários desta cepa potente
são tratados com uma experiência
fora deste mundo, pontuada por elevações 
corporais profundas e sentimentos de euforia.

Espalhe a terra sob seus pés e deixe as forças guiá-lo.
Precauções: Manter ao abrigo da luz e calor.

O armazenamento inadequado pode causar degradação.
Ficou com alguma dúvida?
Acesse nosso FAQ ou entre
em contato com um de nossos especialistas.

características
Specification 
Peso
0,1 kg
Dimensões
2 × 2 × 2 cm


#skywalker #skywalker
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)                                                                                
                                                                                                                                                                
#@Client.on_callback_query(filters.regex(r"^buy (?P<value>\w+) (?P<id>.+)"))
#async def buy_food(c: Client, m: CallbackQuery):
#	await m.message.delete()
#	user_id = m.from_user.id
#	qry = m.matches[0]["value"]
#	id = m.matches[0]["id"]
#	start_message = f"SEU PEDIIDO FOI FEITO, ID: {id}"




#if None in (dados[0], dados[2]) and select_pay == "mercado pago":
#        name = await m.message.ask("Informe o cep", reply_markup=ForceReply())
#else:
	
#@Client.on_callback_query(
#    filters.regex(r"buy (?P<value>.+) (?P<id>.+)")
#)
#async def buy(c: Client, m: CallbackQuery):
#    await m.message.delete()
#    dados = cur.execute("SELECT cpf, name, email FROM users  WHERE id =?", [m.from_user.id]).fetchone()
#    qry = m.matches[0]["value"]
#    id = qry = m.matches[0]["value"]
#    buy = "buy"
#    
#if None in (dados[0], dados[2]) and buy == "buy":
#    name = await m.message.ask("Informe o nome do cep", reply_markup=ForceReply())
#   # isExist = os.path.exists(name.text)
#else:
#	await m.edit_message_text(f"""<b>Seu pedido foi efetuado com sucesso</b>
#Valor: {qry}
#Pedido: {id}

#Observações: podemos entrar em contato com você caso algo aconteça com seu pedido🍟

#Endereço de entrega: """,)
@Client.on_callback_query(
    filters.regex(r"buy (?P<value>.+) (?P<id>.+)")
)
async def buy(c: Client, m: CallbackQuery):

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
        
    await m.message.delete()
    name = await m.message.ask("""Informe o endereco completo de entrega\n
NOME:
CPF;
ENDEREÇO:
N⁰:
COMPLEMENTO: 
BAIRRO:
CIDADE:
ESTADO:
CEP:""", reply_markup=ForceReply())
    


    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(f"ID: #{id}", callback_data=f"{id}")],
        ]
    )


    await m.message.reply_text(
        f"""<b>Seu pedido foi efetuado com sucesso</b>
Valor: {qry}
Pedido: {id}

Observações: seu pedido estará em breve em sua casa!🍟

Endereço de entrega: {name.text}""", reply_markup=kb
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

Endereço de entrega: {name.text}

Status: Pago com sucesso"""	  
    await c.send_message(ADMIN_CHAT, adm_msg)

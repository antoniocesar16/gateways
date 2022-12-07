from typing import Union
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import BadRequest
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from database import cur, save
from utils import create_mention, get_info_wallet, dobrosaldo, get_price
from config import BOT_LINK
from config import BOT_LINK_SUPORTE



@Client.on_message(filters.command(["start", "menu"]))
@Client.on_callback_query(filters.regex("^start$"))
async def start(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id

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
                InlineKeyboardButton("✨ COMPRAR", callback_data="cardapio"),
                InlineKeyboardButton("💸 ADD SALDO", callback_data="add_saldo"),
            ],
            
            [
                InlineKeyboardButton("✈ COMPRAR FRETE", callback_data="frete"),
            ],

           
            [
                 InlineKeyboardButton("👤 SEU PERFIL", callback_data="user_info"),
                InlineKeyboardButton(
                                text="⚙ SUPORTE",
                                url=f"https://t.me/devneycc",
                            ),
                        ],
        ]
    )

    bot_logo, news_channel, support_user = cur.execute(
        "SELECT main_img, channel_user, support_user FROM bot_config WHERE ROWID = 0"
    ).fetchone()

    start_message = f"""OLÁ {m.from_user.first_name},
<a href='https://i.ibb.co/Z1YGhcg/SKY.jpg'>&#8204</a>
⭐Seja bem vindo⭐
❓Dúvidas❓ - chame o <a href='https://t.me/devneycc'>Suporte</a>
✅ O bico pode ou n ta segurando o documento!
👤 Todos documentos vem com foto!
💰 Faça recargas rapidamente pelo /pix!
🔰 docs virgens nunca vendidos antes!
📝 Antes de comprar leia as <a href='https://t.me/bestbotv3'>👉 Regras</a>

{get_info_wallet(user_id)}

💬 Dúvidas?
<a href='https://t.me/{BOT_LINK_SUPORTE}'>SUPORTE</a>
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)

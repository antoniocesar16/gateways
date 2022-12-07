from typing import Union

from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    ForceReply,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from config import ADMINS
from database import cur, save


@Client.on_message(filters.command("painel") & filters.user(ADMINS))
@Client.on_callback_query(filters.regex("^painel$") & filters.user(ADMINS))
async def panel(c: Client, m: Union[Message, CallbackQuery]):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("🚦 Status do bot", callback_data="bot_status"),
                InlineKeyboardButton("🏦 Conta manual", callback_data="change_lara"),
            ],
            
            [
                InlineKeyboardButton("💠 Pix auto", callback_data="auto_pay"),
                
            ],
            [
                InlineKeyboardButton(
                    "👤 Usuários", switch_inline_query_current_chat="search_user "
                ),
                InlineKeyboardButton("🛠 Outras configs", callback_data="bot_config"),
            ],
           
        ]
    )

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text

    await send(
        """<b>🛂 Painel de administração da Loja</b>
<i>- Selecione abaixo o que você deseja visualizar ou modificar.</i>""",
        reply_markup=kb,
    )


    

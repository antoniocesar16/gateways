"""
Este plugin executa de um jeito similar ao `bot_status.py`, antes dos outros,
cancelando o processamento da mensagem pelo bot de usuários blacklistados.
"""


from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)

from config import ADMINS
from database import cur
from utils import is_user_banned


@Client.on_message(
    ~filters.user(ADMINS) & filters.regex(r"^/") & ~filters.channel, group=-2
)
async def is_blacklisted_msg(c: Client, m: Message):
    if is_user_banned(m.from_user.id):
        msg_count = cur.execute(
            "SELECT COUNT() FROM antiflood WHERE user_id = ?", [m.from_user.id]
        ).fetchone()[0]

        if msg_count <= 1:
            await m.reply_text(
                f"<b>⛔️ Você foi banido do bot.</b> Caso ache que isso é um erro, entre em contato com o suporte do bot."
            )
        await m.stop_propagation()


@Client.on_callback_query(~filters.user(ADMINS), group=-2)
async def is_blacklisted_cq(c: Client, m: CallbackQuery):
    if is_user_banned(m.from_user.id):
        msg_count = cur.execute(
            "SELECT COUNT() FROM antiflood WHERE user_id = ?", [m.from_user.id]
        ).fetchone()[0]

        if msg_count <= 1:
            await m.answer(
                f"<b>⛔️ Você foi banido do bot.</b> Caso ache que isso é um erro, entre em contato com o suporte do bot.",
                show_alert=True,
                cache_time=30,
            )
        await m.stop_propagation()


@Client.on_inline_query(~filters.user(ADMINS), group=-2)
async def is_blacklisted_inline(c: Client, m: InlineQuery):
    if is_user_banned(m.from_user.id):
        msg_count = cur.execute(
            "SELECT COUNT() FROM antiflood WHERE user_id = ?", [m.from_user.id]
        ).fetchone()[0]

        results = [
            InlineQueryResultArticle(
                title="⛔️ Você foi banido do bot.",
                input_message_content=InputTextMessageContent(
                    f"<b>⛔️ Você foi banido do bot.</b> Caso ache que isso é um erro, entre em contato com o suporte do bot."
                ),
            )
        ]

        if msg_count <= 1:
            await m.answer(results, cache_time=30, is_personal=True)
        await m.stop_propagation()

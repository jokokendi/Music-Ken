from asyncio.queues import QueueEmpty
from Brocoli.config import que
from pyrogram import Client, filters
from pyrogram.types import Message

from Brocoli.function.admins import set
from Brocoli.helpers.channelmusic import get_chat_id
from Brocoli.helpers.decorators import authorized_users_only, errors
from Brocoli.helpers.filters import command, other_filters
from Brocoli.services.callsmusic import callsmusic


@Client.on_message(filters.command("adminreset"))
async def update_admin(client, message: Message):
    chat_id = get_chat_id(message.chat)
    set(
        chat_id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("✅️ Admin cache refreshed!")


@Client.on_message(command("pause") & other_filters)
async def pause(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "paused"
    ):
        await message.reply_text("❗ **Tidak ada Lagu yang sedang diputar!**")
    else:
        callsmusic.pytgcalls.pause_stream(chat_id)
        await message.reply_text("▶️ **Paused!**")


@Client.on_message(command("resume") & other_filters)
async def resume(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "playing"
    ):
        await message.reply_text("❗ **Tidak ada Lagu yang sedang dijeda!**")
    else:
        callsmusic.pytgcalls.resume_stream(chat_id)
        await message.reply_text("⏸ **Resumed!**")


@Client.on_message(command("end") & other_filters)
async def stop(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ **Tidak ada Lagu yang sedang diputar!**")
    else:
        try:
            callsmusic.queues.clear(chat_id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(chat_id)
        await message.reply_text("❌ **Memberhentikan Lagu!**")


@Client.on_message(command("skip") & other_filters)
async def skip(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ **Tidak ada Lagu Selanjutnya untuk dilewati!**")
    else:
        callsmusic.queues.task_done(chat_id)

        if callsmusic.queues.is_empty(chat_id):
            callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            callsmusic.pytgcalls.change_stream(
                chat_id, callsmusic.queues.get(chat_id)["file"]
            )

        await message.reply_text("⏩ **Melewati lagu saat ini!**")


@Client.on_message(filters.command("admincache"))
async def admincache(client, message: Message):
    set(
        message.chat.id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("✅️ **Daftar admin** telah **diperbarui**")

from pyrogram import Client, filter
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from MusicKen.config import SUDO_USERS as user

@Client.on_message(filter.command([gcast]))
async def user(client.message)
  sent=0
  failed=0
  if message from_user.id in UserAlreadyParticipant:
    lol = await message_reply("`Sedang mengirim pesan global...`")
    if not message.reply_to_message:
      await lol.edit("**Balas pesan teks apa pun untuk gcast**")
      return
    msg = message.reply_to_message.text
    async for user in client.iter_dialogs():
      if user.is_group:
         chat = user.id
         try:
           await client.send_message(dialog.chat.id, msg)
             sent = sent+1
            await lol.edit(f"**Berhasil Mengirim Pesan Ke** `{sent}` **Grup, Gagal Mengirim Pesan Ke** `{failed}` **Grup**")
         except:
            failed = failed+1
            await lol.edit(f"**Berhasil Mengirim Pesan Ke** `{sent}` **Grup, Gagal Mengirim Pesan Ke** `{failed}` **Grup**")
            await asyncio.sleep(0.7)
            await reply_text(f"**Mengirim Pesan Ke** `{sent}` **Grup, Gagal Mengirim Pesan Ke** `{failed}` **Grup**")

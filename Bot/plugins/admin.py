from pyrogram.types import Message
from pyrogram import Client, filters
from Bot.broadcast import get_from_userbase,get_count,edit_count
from Bot.utils import is_sudo, sub_res

sudo_cmd = filters.create(is_sudo)

@Client.on_message(filters.forwarded & filters.private & sudo_cmd)
async def get_user(client: Client, message: Message):
    mention = message.forward_from.mention
    id = message.forward_from.id
    count = get_count(id)
    joined = await sub_res(client,id)
    text = f"User : {mention}\nUser Id : <code>{id}</code>\n\nRefferal Count : {count}\n\n{joined}"
    await message.reply(text)

@Client.on_message(filters.command('clean') & filters.private & sudo_cmd)
async def clean(client: Client, message: Message):
    id = message.text.split(' ')[1]
    edit_count(id,0)
    await message.reply("Users referal count has been cleared")

@Client.on_message(filters.command('edit') & filters.private & sudo_cmd)
async def edit(client: Client, message: Message):
    id = message.text.split(' ')[1]
    count = message.text.split(' ')[2]
    edit_count(id,int(count))
    await message.reply("Users referal count has been edited")

@Client.on_message(filters.command('get') & filters.private & sudo_cmd)
async def get(client: Client, message: Message):
    id = message.text.split(' ')[1]
    count = get_count(id)
    await message.reply(f"Users referal count is {count}")
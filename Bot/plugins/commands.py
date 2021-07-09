from Bot.bot import Bot
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove
from Bot.values import start_keyboard, help_keyboard, about_keyboard, help_text, start_text, about_text
from Bot.utils import is_subscribed1, is_subscribed2, is_sudo
from Bot.broadcast import *

subscribed1 = filters.create(is_subscribed1)
subscribed2 = filters.create(is_subscribed2)
sudo_cmd = filters.create(is_sudo)


@Client.on_message(filters.command('start') & filters.private)
async def start(client: Client, message: Message):
    if not len(message.command) > 1:
        if not present_in_userbase(message.from_user.id):
            add_to_userbase(message.from_user.id,0)
    else:
        reffered = message.command[1]
        count = int(get_count(reffered)) + 1
        if not present_in_userbase(message.from_user.id):
            add_to_userbase(message.from_user.id,reffered)
            edit_count(reffered,count)
    await message.reply(
        text=start_text.format(mention=message.from_user.mention),
        quote=True,
        reply_markup=InlineKeyboardMarkup(start_keyboard)
    )
    reply_markup = ReplyKeyboardMarkup([[KeyboardButton("✅ Verify")]])
    text = "You need to join <b>@Theburster</b> and <b>@Bursterbins</b> in order to use this bot.<b>So please join channel and enjoy bot</b>"
    await message.reply(
        text=text,
        reply_markup=reply_markup
    )



@Client.on_message(filters.command('help') & filters.private)
async def help(client: Client, message: Message):
    await message.reply(
        text=help_text,
        quote=True,
        reply_markup=InlineKeyboardMarkup(help_keyboard)
    )
    return


@Client.on_message(filters.command('about') & filters.private)
async def about(client: Client, message: Message):
    await message.reply(
        text=about_text,
        quote=True,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(about_keyboard)
    )
    return


@Client.on_callback_query()
async def callback(client: Client, query):
    data = query.data
    if data == 'help':
        await query.message.edit(
            text=help_text,
            reply_markup=InlineKeyboardMarkup(help_keyboard)
        )
        return

    elif data == "about":
        await query.message.edit(
            text=about_text,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(about_keyboard)
        )
        return

    elif data == 'close':
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
        try:
            await query.message.delete()
        except:
            pass
        return
    else:
        return


@Client.on_message(filters.command('broadcast') & filters.private & sudo_cmd)
async def users(client: Bot, message: Message):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton("Cancel"), KeyboardButton("Confirm")]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.reply("Send the message that you want to Broadcast")
    response = await client.listen(chat_id=message.chat.id)
    preview = await response.copy(message.chat.id)
    await client.send_message(chat_id=message.chat.id, text="Do you want to send the Broadcast",
                              reply_markup=reply_markup)
    while True:
        confirm = await client.listen(chat_id=message.chat.id)
        if confirm.text == "Cancel":
            break
        elif confirm.text == "Confirm":
            break
        else:
            continue
    if not confirm.text == "Confirm":
        await client.send_message(chat_id=message.chat.id, text=f"Broadcast Cancelled",
                                  reply_markup=ReplyKeyboardRemove())
        return
    await client.send_message(chat_id=message.chat.id, text="Sending Broadcast",
                              reply_markup=ReplyKeyboardRemove())
    users = full_userbase()
    success = 0
    for user in users:
        try:
            await preview.copy(int(user.chat_id))
            success += 1
        except FloodWait as e:
            await asyncio.sleep(e.x)
            await preview.copy(int(user.chat_id))
            print(f"Broadcast send to {user.chat_id}")
            success += 1
        except UserIsBlocked:
            print(f"Broadcast failed to {user.chat_id} (Blocked)")
        except PeerIdInvalid:
            print(f"Broadcast failed to {user.chat_id} (PeerId)")
        except InputUserDeactivated:
            print(f"Broadcast failed to {user.chat_id} (Deactivated)")
            del_from_userbase(user.chat_id)
    try:
        failed = len(users) - success
        await message.reply("Broadcast send Successfully")
        await message.reply(
            f"<b>Statistics :</b>\n\n\n👥Total users : {len(users)}\n\n✅Successfull : {success}\n\n❌Failed : {failed}")
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await message.reply("Broadcast send Successfully")
        await message.reply(
            f"<b>Statistics :</b>\n\n\n👥Total users : {len(users)}\n\n✅Successfull : {success}\n\n❌Failed : {failed}")


@Client.on_message(filters.command('users') & filters.private & sudo_cmd)
async def get_users(client: Client, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text="Counting Users....")
    users = full_userbase()
    await msg.edit(f"{len(users)} users are using this bot ")


from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from Bot.utils import is_subscribed1, is_subscribed2


@Client.on_message(filters.private & filters.text)
async def forcesub(client: Client, message: Message):
    reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Join The Burster", url="https://t.me/Theburster")],
         [InlineKeyboardButton("Join Burster Bins", url="https://t.me/Bursterbins")]]
    )
    reply_markup_a = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Join The Burster", url="https://t.me/Theburster")]]
    )
    reply_markup_b = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Join Burster Bins", url="https://t.me/Bursterbins")]]
    )
    text = "You need to join <b>@Theburster</b> and <b>@Bursterbins</b> in order to use this bot.<b>So please join channel and enjoy bot</b>"
    text_a = "You need to join <b>@Theburster</b> in order to use this bot. <b>So please join channel and enjoy bot</b>"
    text_b = "You need to join <b>@Bursterbins</b> in order to use this bot. <b>So please join channel and enjoy bot</b>"
    if not (await is_subscribed1(client,client, message) | await is_subscribed2(client,client, message)):
        await message.reply(
            text=text,
            reply_markup=reply_markup
        )
    elif not await is_subscribed1(client,client, message):
        await message.reply(
            text=text_a,
            reply_markup=reply_markup_a
        )
    elif not await is_subscribed2(client,client, message):
        await message.reply(
            text=text_b,
            reply_markup=reply_markup_b
        )
    else:
        if message.text == '✅ Verify':
            text="<b>You have been verified</b>\nNow You can reffer and earn free amazon prime account"
            reply_markup = ReplyKeyboardMarkup(
                [
                    [KeyboardButton("😍 Invite users & Earn Points 😍")],
                    [
                        KeyboardButton("💰 My Points"),
                        KeyboardButton("💲Withdraw Points")
                    ],
                    [
                        KeyboardButton("How to do ❓"),
                        KeyboardButton("📞Support")
                    ]
                ]
            )
            await message.reply(text,reply_markup=reply_markup)
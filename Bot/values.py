from pyrogram.types import InlineKeyboardButton
from Bot.config import NO_OF_REFFERAL

start_text = "<b>Hello {mention}\n\nI am a Amazon Prime Generator Bot, Refer this bot with your friends and earn free Amazon Prime account</b>"
help_text = f"🥳<b>Welcome To Amazon Prime Bot</b>🥳\n\n<b>▪️How to get Amazon Prime?</b>\n<i>Just Invite Your Friends In This Bot By your Unique Referral Link And Get Free Amazon Prime Account.</i>\n\n<b>▪️How to Invite ?</b>\n<i>Click On the</i> <b>😍 Invite users & Earn Points 😍</b> <i>button on the bot and you will get your unique referral link just share the link with your friends.</i>\n\n<b>▪️When My Referral Points Will add To My Points ?</b>\n<i>You will get points after your Referral will complete first verify Step Of the bot Using Your Referral Link</i>\n\n<b>▪️What is minimum Withdraw Limit</b>\n<i>After Earning {NO_OF_REFFERAL} points you can withdraw your points for Amazon account</i>"
about_text = "<b>ABOUT OWNER</b>\n@Primevideo_burster_bot\n\n<b>ABOUT Programmer</b>\n\n<b>○ Programmer : <a href='https://t.me/CodeXBotzSupport'>CodeXBotz Support</a>\n○ Language : <a href='https://www.python.org/'>Python 3</a>\n○ Library : <a href='https://github.com/pyrogram/pyrogram'>Pyrogram Asyncio 1.2.9</a>\n○ Channel : <a href='https://t.me/CodeXBotz'>Code 𝕏 Botz</a></b>\n\nCodeXBotz is not responsible for misuse of this bot.We intend to create bots"

start_keyboard = [
    [
        InlineKeyboardButton(text = '🤔 Help', callback_data = "help"),
        InlineKeyboardButton(text = '🤖 About', callback_data = "about")
    ],
    [
        InlineKeyboardButton(text = 'Close 🔒', callback_data = "close")
    ]
]

help_keyboard = [
    [
        InlineKeyboardButton(text = '🤖 About', callback_data = 'about'),
        InlineKeyboardButton(text = 'Close 🔒', callback_data = 'close')
    ]
]
about_keyboard = [
    [
        InlineKeyboardButton(text = '🤔 Help', callback_data = 'help'),
        InlineKeyboardButton(text = 'Close 🔒', callback_data = 'close')
    ]
]
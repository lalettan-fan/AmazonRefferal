from pyrogram.types import Message
from pyrogram import Client, filters
from Bot.broadcast import get_count
from Bot.config import NO_OF_REFFERAL

@Client.on_message(filters.text & filters.private & ~ filters.forwarded & ~ filters.regex('Verify'))
async def prime(client: Client, message: Message):
    user_id = message.from_user.id
    count = get_count(user_id)
    rem_count = int(NO_OF_REFFERAL) - int(count)
    botuname = client.username
    if message.text == "😍 Invite users & Earn Points 😍":
        text = f"<b>⏯️ Total Invites : {count} Users\n\n💎Refer and Get 1 Points For Every User You Invite 🍎 \n\n🔗 Your Referral Link ⬇️\nhttps://t.me/{botuname[1:]}?start={user_id}</b>\n\n<b>⚠️ Please Note That Referal Points Will Add When Your Referral Will Complete The Verification Step Of Bot</b>\n\n<i>⚠️ If you leave our any channel, Your all points will convert to 0 anytime.</i>"
    elif message.text == "💰 My Points":
        text = f"You have reffered {count} users"
    elif message.text == "💲Withdraw Points":
        if rem_count > 0:
            text = f"<b>⏯️ Total Invites : {count} Users</b>\n\nYou Need to reffer {rem_count} new users to get free prime account"
        else:
            text = "Congratulation,\nYou are eligible to get a free <b>Amazon Prime</b> account.\n\nContact me on @Theburster_bot to claim your account"
    elif message.text == "How to do ❓":
        text = f"🥳<b>Welcome To Amazon Prime Bot</b>🥳\n\n<b>▪️How to get Amazon Prime?</b>\n<i>Just Invite Your Friends In This Bot By your Unique Referral Link And Get Free Amazon Prime Account.</i>\n\n<b>▪️How to Invite ?</b>\n<i>Click On the</i> <b>😍 Invite users & Earn Points 😍</b> <i>button on the bot and you will get your unique referral link just share the link with your friends.</i>\n\n<b>▪️When My Referral Points Will add To My Points ?</b>\n<i>You will get points after your Referral will complete first verify Step Of the bot Using Your Referral Link</i>\n\n<b>▪️What is minimum Withdraw Limit</b>\n<i>After Earning {NO_OF_REFFERAL} points you can withdraw your points for Amazon account</i>"
    elif message.text == "📞Support":
        text = "Send Your Question to this bot 👇\n\n@Theburster_bot"
    else:
        return
    await message.reply(text)
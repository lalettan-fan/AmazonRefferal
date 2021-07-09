from pyrogram.errors import UserNotParticipant
from Bot.config import AUTH_CHANNEL1, AUTH_CHANNEL2, SUDO


async def is_subscribed1(_, client, message):
    user_id = message.from_user.id
    if not AUTH_CHANNEL1:
        return True
    try:
        chat_member = await client.get_chat_member(chat_id=int(AUTH_CHANNEL1), user_id=user_id)
    except UserNotParticipant:
        return False
    if chat_member.status in ["creator", "administrator", "member", "restricted"]:
        return True
    else:
        return False


async def is_subscribed2(_, client, message):
    user_id = message.from_user.id
    if not AUTH_CHANNEL2:
        return True
    try:
        chat_member = await client.get_chat_member(chat_id=int(AUTH_CHANNEL2), user_id=user_id)
    except UserNotParticipant:
        return False
    if chat_member.status in ["creator", "administrator", "member", "restricted"]:
        return True
    else:
        return False

async def sub_res(client,user_id):
    text = ''
    if AUTH_CHANNEL1:
        try:
            chat_member = await client.get_chat_member(chat_id=int(AUTH_CHANNEL1), user_id=user_id)
        except UserNotParticipant:
            text1 = "<b>@Theburster</b> : ❌"
        if chat_member.status in ["creator", "administrator", "member", "restricted"]:
            text1 = "<b>@Theburster</b> : ✅"
        else:
            text1 = "<b>@Theburster</b> : ❌"
        text = text1
    if AUTH_CHANNEL2:
        try:
            chat_member = await client.get_chat_member(chat_id=int(AUTH_CHANNEL2), user_id=user_id)
        except UserNotParticipant:
            text2 = "<b>@Bursterbins</b> : ❌"
        if chat_member.status in ["creator", "administrator", "member", "restricted"]:
            text2 = "<b>@Bursterbins</b> : ✅"
        else:
            text2 = "<b>@Bursterbins</b> : ❌"
        if text:
            text += f"\n{text2}"
        else:
            text = text2
    return text


async def is_sudo(_, client, message):
    user_id = message.from_user.id
    if not SUDO:
        return False
    sudo = SUDO.split(' ')
    if str(user_id) in sudo:
        return True
    else:
        return False

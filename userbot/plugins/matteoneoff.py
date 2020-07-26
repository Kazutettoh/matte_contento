import asyncio
from userbot import bot
from userbot.system import register
from telethon.tl.functions.account import UpdateProfileRequest
from telethon import events
from telethon.events import StopPropagation
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import ReportSpamRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon import functions, types
from telethon.tl.functions.messages import GetAllChatsRequest
from telethon.tl.functions.messages import GetAllChatsRequest


mexScuola = "**⛔️ Al momento sono OFFLINE.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!.**"
exempt = []
mutedList = []
autoNiceText = False

# MUTE

@register(outgoing=True, pattern="^.off$")
async def changeName(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        name = "ッ𝙼𝚊𝚝𝚝𝚎™ [𝕆𝔽𝔽𝕃𝕀ℕ𝔼]"
        await bot(UpdateProfileRequest(first_name=name, last_name=""))
        global message
        message = "**⛔️ Al momento sono OFFLINE.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!.**"
        await e.edit("`Ora sei Offline`")

@register(outgoing=True, pattern="^.on$")
async def changeName(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        name = "ッ𝙼𝚊𝚝𝚝𝚎™ [𝕆ℕ𝕃𝕀ℕ𝔼]"
        await bot(UpdateProfileRequest(first_name=name, last_name=""))
        global message
        message = "**⛔️ Al momento sono OFFLINE.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!.**"
        await e.edit("`Ora sei Online`")

@register(outgoing=True, pattern="^.oncod$")
async def changeName(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        name = "ッ𝙼𝚊𝚝𝚝𝚎™ [𝕆ℕ𝕃𝕀ℕ𝔼 su call of duty]"
        await bot(UpdateProfileRequest(first_name=name, last_name=""))
        global message
        message = "**⛔️ Al momento sto giocando a cod.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!.**"
        await e.edit("`Ora sei su call of duty`")

@register(outgoing=True, pattern="^.onpubg$")
async def changeName(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        name = "ッ𝙼𝚊𝚝𝚝𝚎™ [𝕆ℕ𝕃𝕀ℕ𝔼 SU PUBG]"
        await bot(UpdateProfileRequest(first_name=name, last_name=""))
        global message
        message = "**⛔️ Al momento sono import pubg.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!.**"
        await e.edit("`Ora sei su pbg`")

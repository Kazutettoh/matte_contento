#By github.com/CometaLunare all rights reserved

import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd(pattern=r"police")) 
async def _(event): 
    if event.fwd_from: 
        return 
    animation_interval = 0.2 
    animation_ttl = range(0, 12) 
    await event.edit("🚨 👮‍") 
    animation_chars = [ 
         
            
            
"🔴🔴🔴🔴 🔵🔵🔵🔵\n🔴🔴🔴🔴 🔵🔵🔵🔵\n🔴🔴🔴🔴 🔵🔵🔵🔵",

"🔵🔵🔵🔵 🔴🔴🔴🔴\n🔵🔵🔵🔵 🔴🔴🔴🔴\n🔵🔵🔵🔵 🔴🔴🔴🔴",

"🔴🔴🔴🔴 🔵🔵🔵🔵\n🔴🔴🔴🔴 🔵🔵🔵🔵\n🔴🔴🔴🔴 🔵🔵🔵🔵",

"🔵🔵🔵🔵 🔴🔴🔴🔴\n🔵🔵🔵🔵 🔴🔴🔴🔴\n🔵🔵🔵🔵 🔴🔴🔴🔴",

"🔴🔴🔴🔴 🔵🔵🔵🔵\n🔴🔴🔴🔴 🔵🔵🔵🔵\n🔴🔴🔴🔴 🔵🔵🔵🔵",

"🔵🔵🔵🔵 🔴🔴🔴🔴\n🔵🔵🔵🔵 🔴🔴🔴🔴\n🔵🔵🔵🔵 🔴🔴🔴🔴",

"🔴🔴🔴🔴 🔵🔵🔵🔵\n🔴🔴🔴🔴 🔵🔵🔵🔵\n🔴🔴🔴🔴 🔵🔵🔵🔵",

"🔵🔵🔵🔵 🔴🔴🔴🔴\n🔵🔵🔵🔵 🔴🔴🔴🔴\n🔵🔵🔵🔵 🔴🔴🔴🔴",

"🔴🔴🔴🔴 🔵🔵🔵🔵\n🔴🔴🔴🔴 🔵🔵🔵🔵\n🔴🔴🔴🔴 🔵🔵🔵🔵",

"🔵🔵🔵🔵 🔴🔴🔴🔴\n🔵🔵🔵🔵 🔴🔴🔴🔴\n🔵🔵🔵🔵 🔴🔴🔴🔴",

"Ti hanno arrestato! Down♿️🤡"

 
 ] 
 
    for i in animation_ttl: 
        await asyncio.sleep(animation_interval) 
        await event.edit(animation_chars[i % 12])
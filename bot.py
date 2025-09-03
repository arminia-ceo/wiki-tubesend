#Console
print('=================================Console Log===================================')
print('Now Importing...')

#Imports
import bale
from bale import Update, Message, Bot, User, Chat
import logging
import os, re
import time
import json
from pytube import YouTube
import requests
print('Importing Finished!')
print()
print('Being Ready...')

#Token
tokenbot = "1924438837:CmnfkuGOXpXhc2mCNKn9PELkw1wJ8NomNSdbnqtC"
bot = bale.Bot(token = tokenbot)

#Ready
@bot.listen('on_ready')
async def on_ready():
        print(bot.user.first_name, "is Ready!")
        print()
        print()
        print('===================================Massage=====================================')
        
#Update
@bot.event
async def on_update(update: Update):
        print("Update Id:", update.update_id)

#List Of Massages
startmassage = """
*ممنون از ادمین تایید شده محترم ویکی ماینکرفت که می‌تواند از این بات استفاده کند، کپشن شما، همان کپشن تنظیم شده است 💚
برای تغییر کپشن، از کامند caption/ استفاده کنید، در صورت ست نکردن کپشن، متن نو کپشن با تگ ویکی ماینکرفت ارسال می‌شود ✍️
در صورت ست نکردن چنل با کامند channel/، فایل مستقیم به ویکی ماینکرفت می‌رود! ⚠️

لطفا لینک یوتیوب مد نظر خود را ارسال بفرمایید تا پس از بررسی های لازم، اون رو به چنل ویکی ماینکرفت ارسال کنیم 🎖️*
"""

youtubesender = """
*فایل یویتوب شما با کپشن تنظیم شده شما (در صورت تنظیم نبودن، با کپشن پیش‌فرض) در کانال ارسال شد 💚

لطفا در صورت بروز مشکل با پشتیبانی این ربات صحبت کرده و مشکل آن را برطرف کنید : @arminia_ceo 🫵*
"""

nousername = """
*درود بر شما کاربر گرامی! متاسفانه یا شما آیدی بله نداشته یا جزو ادمین هایی که دسترسی به این قابلیت دارند نیستید 🫠

لطفا در صورت بروز مشکل با پشتیبانی این ربات صحبت کرده و مشکل آن را برطرف کنید : @arminia_ceo 🫵*
"""

captionmass = """
*برای تنظیم کپشن، ابتدای پیام خود کد زیر را نوشته و ادامه آن را به صورت دقیق برابر کپشن تایین شده خود بزارید ✍️*

!Caption:
!Caption:دقيقا پيام خودتون
"""

channelmass = """
*برای تنظیم چنل، ابتدای پیام خود کد زیر را نوشته و ادامه آن را به صورت دقیق برابر چنل تایین شده خود بزارید، مثال در زیر پیام! ✍️*

!Channel:
!Channel:@channelid
"""

thatsok = """
*کپشن شما تایید شد و ویدیو های یوتیوبی که ارسال می‌کنید، از این پس با این کپشن ارسال خواهند شد 💚

با تشکر از همکاری شما ادمین عزیز ✍️*
"""

channelok = """
*چنل مد نظر شما تایید شد و ویدیو های یوتیوبی که ارسال می‌کنید، از این پس به این چنل ارسال خواهند شد 💚

با تشکر از همکاری شما ادمین عزیز ✍️*
"""

errortime = """
* متاسفانه شما دارید از کامند یا یک لینک اشتباهی استفاده می‌کنید، لطفا دوباره تلاش کنید ✍️

لطفا در صورت بروز مشکل با پشتیبانی این ربات صحبت کرده و مشکل آن را برطرف کنید : @arminia_ceo 🫵*
"""

default = """
*نو کپشن 🫵*

#wiki_minecraft
"""

#Lists & Allow
list_of_commands = ["/start","start","/caption","caption","/channel","channel"]
allowlist = ["arminia_ceo"]
#Massage
@bot.listen("on_message")
async def when_message(message: bale.Message):
        username = ''
        username = message.from_user.username
        ider = message.from_user.id
        first = message.from_user.first_name
        mainuser = message.from_user.username
        print('Username: @', mainuser, sep ='')
        print('ID:', ider)
        print('Command:', message.content)
        print()
        if not isinstance(mainuser, str) or mainuser not in allowlist :
                await message.reply(nousername)
        else :
                dowmloadlocation = "./temp/"
                link = message.content        
                pattern = r"https?:\/\/(?:www\.)?youtu(?:be\.com\/(?:watch\?v=|shorts\/)|\.be\/)([\w\-]+)(?:[&?][\w=]*)?"
                result = re.match(pattern, link)
                usernameman = '@' + message.from_user.username
                if message.content == "/start" or message.content == "start":
                        await message.reply(startmassage)
                elif message.content == "/caption" or message.content == "caption":
                        await message.reply(captionmass)
                elif message.content == "/channel" or message.content == "channel":
                        await message.reply(channelmass)
                elif message.content[0:9] == "!Caption:":
                        with open("save.json", "r") as f:
                                data = json.load(f)
                        data[usernameman] = message.content[9:]
                        json_str = json.dumps(data, indent=4)
                        with open("save.json", "w") as f:
                            f.write(json_str)
                        await message.reply(thatsok)
                elif message.content[0:9] == "!Channel:":
                        with open("channel.json", "r") as f:
                                data = json.load(f)
                        data[usernameman] = message.content[9:]
                        json_str = json.dumps(data, indent=4)
                        with open("channel.json", "w") as f:
                            f.write(json_str)
                        await message.reply(channelok)
                elif result :
                        # Download video from youtube
                        youtube = YouTube(link)
                        youtube_stream = youtube.streams.get_highest_resolution()
                        youtube_stream.download(dowmloadlocation)
                        # Send video to user
                        file_name = youtube.streams.get_highest_resolution().default_filename
                        file_dir = f"{dowmloadlocation}{file_name}"
                        tokenbase = tokenbot
                        urlbase = f"https://tapi.bale.ai/bot{tokenbase}"
                        #Caption
                        with open("save.json", "r") as f:
                                data = json.load(f)
                        if usernameman in date:
                                captionfile = data[usernameman]
                        else :
                                captionfile = default
                        #Channel
                        with open("channel.json", "r") as f:
                                data = json.load(f)
                        if usernameman in date:
                                channelsend = data[usernameman]
                        else :
                                channelsend = "@wiki_minecraft"
                        #Continue
                        files = {
                            "video": open(file_dir, 'rb')
                        }
                        data = {
                            "chat_id": ider,
                            "caption": captionfile
                        }
                        response = requests.post(f"{urlbase}/sendVideo", data = data, files = files)
                        print(response.json())
                        # Delete video from disk after sending to user
                        os.remove(file_dir)
                        await message.reply(youtubesender)
                else :
                        await message.reply(errortime)  
bot.run()

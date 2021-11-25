# 902442789982322700
# OTAyNDQyNzg5OTgyMzIyNzAw.YXefVw.fkgY5TP9InEUMzvAnxDVRguuoQ4

import discord
from discord.ext import commands
from asyncio import sleep 
bot = commands.Bot(command_prefix="")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('เรียก พี่พีเจ'))
    print("P'PJ Ready for surprise N'Nuey!")

@bot.command()
async def พี่พีเจ(ctx):
    emBed = discord.Embed(
            title="Mp3player", description="เล่นไฟล์ mp3 จากบอทดิสคอร์ด", color=0x71afe5)
    emBed.set_thumbnail(
            url="https://o.remove.bg/downloads/45b4ff7e-00c0-476d-90b3-0aadab121687/image-removebg-preview.png")
    emBed.add_field(name="พิมพ์ เล่น แล้ววรรคตามด้วยชื่อเพลงที่มี",
                        value='แค่คุณ ของขวัญ หวานเย็น อาจเพราะ เธอคือความฝัน อยากเจอ สาวเซี่ยงไฮ้ รักแรกพบ ฟ้า เธอทั้งนั้น นิโคติน รักเมียที่สุดในโลก เรื่องราวที่เราเขียน ให้ฉันดูแลเธอ หลงรัก รักฉันเพราะอะไร unfriend undo')
    emBed.set_footer(text="https://github.com/jiraphanz",
                         icon_url="https://avatars.githubusercontent.com/u/88519295?v=4")
    await ctx.channel.send(embed=emBed)

@bot.command()
async def เล่น(ctx, message):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/ffmpeg.exe", 
            source="{0}.mp3" .format(message)))
    while vc.is_playing():
        await sleep(1)
    await vc.disconnect()



@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


bot.run("OTAyNDQyNzg5OTgyMzIyNzAw.YXefVw.fkgY5TP9InEUMzvAnxDVRguuoQ4")

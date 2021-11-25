import discord
from discord.ext import commands
from asyncio import sleep 

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('call !mp3'))
    print("MP3player ready!")

@bot.command()
async def mp3(ctx):
    emBed = discord.Embed(
            title="Mp3player", description="เล่นไฟล์ mp3 จากบอทดิสคอร์ด", color=0x71afe5)
    emBed.set_thumbnail(
            url="https://o.remove.bg/downloads/45b4ff7e-00c0-476d-90b3-0aadab121687/image-removebg-preview.png")
    emBed.add_field(name="นำไฟล์ mp3 ใส่ในโฟลเดอร์",
                        value='พิมพ์ !play ตามด้วยชื่อไฟล์')
    emBed.set_footer(text="https://github.com/jiraphanz",
                         icon_url="https://avatars.githubusercontent.com/u/88519295?v=4")
    await ctx.channel.send(embed=emBed)

@bot.command()
async def play(ctx, message):
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


bot.run("your token")

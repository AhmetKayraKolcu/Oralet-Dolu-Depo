import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='+', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
@bot.command()
async def heh(ctx, count_heh = 5):
    if count_heh > 1000:
        await ctx.send("beni tekerleme yapan adam mı sandın")
    else:
        await ctx.send("he"* count_heh)
@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def nabion(ctx):
    await ctx.send('iyiyim sen')

@bot.command()
async def napıyorsun(ctx):
    await ctx.send('iyiyim sen')

@bot.command()
async def bende_iyi_çok_şükür(ctx):
    await ctx.send('tmm bay')

@bot.command()
async def bye(ctx):
    await ctx.send('ağlamaya başlar')


bot.run("")

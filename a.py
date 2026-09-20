import discord
from discord.ext import commands
import os, random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Você logou como {bot.user}')

@bot.command()
async def mem(ctx):
    a = ["mem1.png","mem2.png","mem3.png","mem4.png"]
    chance = [10, 30, 50, 10]

    img_name = random.choices(a, weights=chance, k=1)[0]
    with open(f'h/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run(TOKEN)

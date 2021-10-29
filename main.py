import os
import asyncio
import discord
from discord.ext import commands

from constants import *

intents = discord.Intents.all()
discord.member = True
bot = commands.Bot(command_prefix = '.', intents = intents)

bot.remove_command('help')

@bot.event
async def on_ready():
        print('\nWelcome')
        print('------------------')
        print('Logged in as {}'.format(bot.user.name))
        print('ID:\n{}'.format(bot.user.id))
        print('------------------')
        print('Log:\n')
        bot.loop.create_task(status_task())
        
async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game('.help'), status=discord.Status.online)
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game('discord.gg/bQzf79Y'), status=discord.Status.online)
        await asyncio.sleep(5)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(TOKEN)

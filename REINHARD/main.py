import os
import discord
from itertools import cycle
from discord.ext import commands, tasks

from constants import *

intents = discord.Intents.all()
discord.member = True
bot = commands.Bot(command_prefix = '.', intents = intents)

game = cycle(['.help'])
bot.remove_command('help')

@bot.event
async def on_ready()
    print('\nWelcome')
    print('------------------')
    print('Logged in as {}'.format(bot.user.name))
    print('ID:\n{}'.format(bot.user.id))
    print('------------------') 
    print('Log:\n')
    change_status.start()
       
@tasks.loop(seconds=100) 
async def change_status():
    await bot.change_presence(activity=discord.Game(next(game)), status=discord.Status.online)

for filename in os.listdir("REINHARD/cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(TOKEN)

import os
import discord
from itertools import cycle
from discord.ext import commands, tasks
from discord import app_commands

from REINHARD.additionals.data import *
intents = discord.Intents.all()
discord.member = True

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=".", intents= intents)
        async def startup(self):
            await bot.wait_until_ready()
            await bot.tree.sync(guild = discord.Object(id = 488677373835870208))
            print('Sucessfully synced applications commands')
            print(f'Connected as {bot.user}')
            async def setup_hook(self):
                game = cycle(['.help', '/help'])

                print('--------------------')
                log.info('Logged in as {}'.format(bot.user.name))
                log.info('ID: {}'.format(bot.user.id))
                print('--------------------') 
                change_status.start()
                    
                @tasks.loop(seconds=5) 
                async def change_status():
                    await bot.change_presence(activity=discord.Game(next(game)), status=discord.Status.online)

                for filename in os.listdir("REINHARD/cogs"):
                    if filename.endswith(".py") and filename != "__init__.py":
                        bot.load_extension(f"REINHARD.cogs.{filename[:-3]}")    
bot = Bot()
bot.run(TOKEN)

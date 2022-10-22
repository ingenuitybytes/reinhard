import os
from itertools import cycle

import discord
from discord import app_commands
from discord.ext import commands, tasks

from REINHARD.additionals.data import *

game = cycle(['.help', '/help'])

reinhard = commands.Bot(command_prefix=".", intents=discord.Intents.all())

class reinhard(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False;
        
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await self.tree.sync(guild = discord.Object(id = 488677373835870208))
            self.synced = True

            print('--------------------')
            log.info('Logged in as {}'.format(self.user.name))
            log.info('ID: {}'.format(self.user.id))
            print('--------------------') 
            change_status.start()
                
            @tasks.loop(seconds=5) 
            async def change_status():
                await self.change_presence(activity=discord.Game(next(game)), status=discord.Status.online)

            for filename in os.listdir("REINHARD/cogs"):
                if filename.endswith(".py") and filename != "__init__.py":
                    self.load_extension(f"REINHARD.cogs.{filename[:-3]}") 
                    
reinhard.run(TOKEN)

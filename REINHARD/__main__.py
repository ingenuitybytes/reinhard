import os
from itertools import cycle

import discord
from discord.ext import commands, tasks

from REINHARD.additionals.data import *

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='.', 
            intents=discord.Intents.all(),
            application_id=APPLICATION_ID
            )

    async def setup_hook(self):
        for filename in os.listdir("REINHARD/cogs"):
            if filename.endswith(".py") and filename != "__init__.py":
                await self.load_extension(f"REINHARD.cogs.{filename[:-3]}")
                await bot.tree.sync(guild=discord.Object(id=826868484138598400))


    async def on_ready(self):
        print('--------------------')
        log.info('Logged in as {}'.format(self.user.name))
        log.info('ID: {}'.format(self.user.id))
        print('--------------------')

        game = cycle(['/help', '/new'])
        @tasks.loop(seconds=5) 
        async def change_status():
            await self.change_presence(activity=discord.Game(next(game)), status=discord.Status.online)
        change_status.start()

bot = MyBot()
bot.run(TOKEN)

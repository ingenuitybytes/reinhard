import os
from itertools import cycle

import discord
from discord import app_commands
from discord.ext import commands, tasks

from REINHARD.additionals.data import *


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='.', 
            intents=discord.Intents.all(),
            application_id=APPLICATION_ID,
            )

    async def setup_hook(self):
        for filename in os.listdir("REINHARD/cogs"):
            if filename.endswith(".py") and filename != "__init__.py":
                await self.load_extension(f"REINHARD.cogs.{filename[:-3]}")
                await bot.tree.sync(guild=discord.Object(id=GUILD_ID))

    async def on_ready(self):
        print('--------------------')
        log.info('Logged in as {}'.format(self.user.name)) #type: ignore
        log.info('ID: {}'.format(self.user.id)) #type: ignore
        print('--------------------')

        game = cycle(['Robolox', 'Fornite'])
        @tasks.loop(seconds=5) 
        async def change_status():
            await self.change_presence(status=discord.Status.online, activity=discord.Streaming(name=next(game), url='https://www.twitch.tv/.'))
        change_status.start()


bot = MyBot()
bot.run(TOKEN)
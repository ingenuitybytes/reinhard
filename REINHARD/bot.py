#!/usr/bin/env python3
'''This is the main file of the bot.
It contains the bot class.
'''

# Import modules and files
from discord.ext import commands, tasks
from itertools import cycle

import discord
import os

from resources import Token
import utils


# Bot class
class MyBot(commands.Bot):
    # Constructor
    def __init__(self) -> None:
        super().__init__(
            command_prefix='.', 
            intents=discord.Intents.all(),
            application_id=Token.APPLICATION_ID,
        )
    # Methods
    async def setup_hook(self):
        for filename in os.listdir("REINHARD/cogs/slash"):
            if filename.endswith(".py") and filename != "__init__.py":
                await self.load_extension(f"REINHARD.cogs.slash.{filename[:-3]}")
                await bot.tree.sync(guild=discord.Object(id=Token.GUILD_ID))
        for filename in os.listdir("REINHARD/cogs/context-menu"):
            if filename.endswith(".py") and filename != "__init__.py":
                await self.load_extension(f"REINHARD.cogs.context-menu.{filename[:-3]}")
                await bot.tree.sync(guild=discord.Object(id=Token.GUILD_ID))
        for filename in os.listdir("REINHARD/cogs/reaction"):
            if filename.endswith(".py") and filename != "__init__.py":
                await self.load_extension(f"REINHARD.cogs.reaction.{filename[:-3]}")
                await bot.tree.sync(guild=discord.Object(id=Token.GUILD_ID))
    async def on_ready(self):
        print('--------------------')
        utils.log.info('Logged in as {}'.format(self.user.name)) #type: ignore
        utils.log.info('ID: {}'.format(self.user.id)) #type: ignore
        print('--------------------')
        utils.log.info('All cogs are ready') #type: ignore
        print('--------------------')
        
        game = cycle(['Roblox', 'Fornite'])  # type: ignore
        @tasks.loop(seconds=5) 
        async def change_status():
            await self.change_presence(status=discord.Status.online, activity=discord.Streaming(name=next(game), url='https://www.twitch.tv/.'))
        change_status.start()
    # async def on_disconnect(self):
    #     utils.log.info('Disconnected')

bot = MyBot()
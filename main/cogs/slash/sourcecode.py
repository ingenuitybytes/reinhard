#!/usr/bin/env python3
from discord.ext import commands
from discord import app_commands

import discord

from resources import Link, Token
import utils


class Sourcecode(commands.Cog):
   def __init__(self, bot: commands.Bot) -> None:
      self.bot = bot
      
   @commands.Cog.listener()
   async def on_ready(self):
      utils.log.info("Sourcecode cog is ready")

   @app_commands.command(
      name="sourcecode",
      description="Get the sourcecode of the bot",
      )

   async def sourcecode(self, interaction: discord.Interaction) -> None:
      await interaction.response.send_message(Link.GITHUB_LINK, ephemeral=False)
      
   @sourcecode.error
   async def sourcecode_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
      if isinstance(error, app_commands.errors.MissingAnyRole):
         await interaction.response.send_message("You don't have the required role to use this command.", ephemeral=True)
      if isinstance(error, app_commands.errors.CommandInvokeError):
         await interaction.response.send_message("An error occured while executing this command.", ephemeral=True)
         

async def setup(bot: commands.Bot) -> None:
   await bot.add_cog(
      Sourcecode(bot)#,
      #guilds = [discord.Object(id=Token.GUILD_ID)]
      )
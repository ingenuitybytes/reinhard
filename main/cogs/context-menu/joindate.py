#!/usr/bin/env python3
from discord.ext import commands
from discord import app_commands

import discord

from resources import Token
import utils


class JoinDate(commands.Cog):
   def __init__(self, bot: commands.Bot) -> None:
      self.bot = bot
      self.ctx_menu = app_commands.ContextMenu(
         name='Show Join Date',
         callback=self.show_join_date
      )
      self.bot.tree.add_command(self.ctx_menu)

   # async def cog_unload(self) -> None:
   #    self.bot.tree.remove_command(self.ctx_menu.name, type=self.ctx_menu.type)

   # You can add checks too
   # @app_commands.checks.has_permissions(ban_members=True)
   @app_commands.guilds(discord.Object(id=Token.GUILD_ID))
   async def show_join_date(self, interaction: discord.Interaction, member: discord.Member):
      await interaction.response.send_message(f'{member} joined at {discord.utils.format_dt(member.joined_at)}')  # type: ignore

   @commands.Cog.listener()
   async def on_ready(self):
      utils.log.info("Join Date cog is ready")


async def setup(bot: commands.Bot) -> None:
   await bot.add_cog(
      JoinDate(bot)#,
      #guilds = [discord.Object(id=Token.GUILD_ID)]
      )
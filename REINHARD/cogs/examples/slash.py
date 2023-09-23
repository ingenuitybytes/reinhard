import discord
from discord import app_commands
from discord.ext import commands

from REINHARD.additionals.data import *


class Slash(commands.Cog):
   def __init__(self, bot: commands.Bot) -> None:
      self.bot = bot
      
   @commands.Cog.listener()
   async def on_ready(self):
      log.debug("Test cog is ready")

   @app_commands.command(
      name="test",
      description="Test description"
      )
   @app_commands.checks.has_any_role(
      "Admin", "Moderator", "Owner"
   )
   @app_commands.checks.cooldown(1, 50.0, key=lambda i: (i.guild_id, i.user.id))
   
   async def test(self, interaction: discord.Interaction) -> None:
      await interaction.response.send_message("test", ephemeral=False)
      
   @test.error
   async def test_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
      if isinstance(error, app_commands.errors.MissingAnyRole):
         await interaction.response.send_message("You don't have the required role to use this command.", ephemeral=True)
      if isinstance(error, app_commands.errors.CommandOnCooldown):
         timeRemaining=str(round(error.retry_after, 2))
         await interaction.response.send_message(f"You are on cooldown. Try again in {timeRemaining} seconds.", ephemeral=True)
      if isinstance(error, app_commands.errors.CommandInvokeError):
         await interaction.response.send_message("An error occured while executing this command.", ephemeral=True)
         

async def setup(bot: commands.Bot) -> None:
   await bot.add_cog(
      Slash(bot),
      guilds = [discord.Object(id=GUILD_ID)]
      )
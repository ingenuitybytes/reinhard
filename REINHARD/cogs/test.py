import discord
from discord import app_commands
from discord.ext import commands

class test(commands.Cog):
   def __init__(self, bot: commands.Bot) -> None:
      self.bot = bot
    
    

   @app_commands.command(
      name="test",
      description="test description"
      )
   async def test(self, interaction: discord.Interaction) -> None:
      await interaction.response.send_message("test", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
   await bot.add_cog(
      test(bot),
      guilds = [discord.Object(id=826868484138598400)]
      )
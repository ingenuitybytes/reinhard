import discord
from discord import app_commands
from discord.ext import commands

class App(commands.Cog):
   def __init__(self, bot: commands.Bot) -> None:
      self.bot = bot

   @tree.context_menu(name= "Hello")
   async def hello(self, interaction: discord.Interaction, message: DiscordMessage) -> None:
      await interaction.response.send_message("Hello")

async def setup(bot: commands.Bot) -> None:
   await bot.add_cog(
      App(bot),
      guilds = [discord.Object(id=826868484138598400)]
      )
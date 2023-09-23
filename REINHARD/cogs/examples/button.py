import discord
from discord.ext import commands

from REINHARD.additionals.data import *


class Buttons(discord.ui.View):
   def __init__(self, *, timeout=180):
      super().__init__(timeout=timeout)
      
   @discord.ui.button(label="clickme", style=discord.ButtonStyle.gray)
   async def my_button(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.send_message("Button clicked", ephemeral=True)
         
class Button(commands.Cog):
   def __init__(self, bot):
      self.bot = bot
      
   @commands.Cog.listener()
   async def on_ready(self):
      log.debug("Button cog is ready")
      
   @commands.command()
   async def click(self, ctx): 
      await ctx.send("Click the button", view=Buttons())

async def setup(bot):
   await bot.add_cog(
      Button(bot),
      guilds = [discord.Object(id=GUILD_ID)]
      )
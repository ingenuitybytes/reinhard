import discord
from discord import app_commands, ui
from discord.ext import commands

from REINHARD.additionals.data import *

class Questionnaire(ui.Modal, title='Questionnaire Response'):
   name = ui.TextInput(label='Name')
   answer = ui.TextInput(label='Answer', style=discord.TextStyle.paragraph)
   async def on_submit(self, interaction: discord.Interaction):
      await interaction.response.send_message(f'Thanks for your response, {self.name}!', ephemeral=True)

class Select(discord.ui.Select):
   def __init__(self):
      options=[
         discord.SelectOption(label="Option 1",emoji="👌",description="This is option 1!"),
         discord.SelectOption(label="Option 2",emoji="✨",description="This is option 2!"),
         discord.SelectOption(label="Option 3",emoji="🎭",description="This is option 3!")
         ]
      super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
      
   async def callback(self, interaction: discord.Interaction):
      await interaction.response.send_modal(Questionnaire())

class SelectView(discord.ui.View):
   def __init__(self, *, timeout = 180):
      super().__init__(timeout=timeout)
      self.add_item(Select())

class Modal(commands.Cog):
   def __init__(self, bot):
      self.bot = bot
      
   @commands.Cog.listener()
   async def on_ready(self):
      log.debug("Modal cog is ready")
         
   @commands.command()
   async def modal(self, ctx): 
      await ctx.send("Modal!", view=SelectView())

async def setup(bot: commands.Bot) -> None:
   await bot.add_cog(
      Modal(bot),
      guilds = [discord.Object(id=826868484138598400)]
      )
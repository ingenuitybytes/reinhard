#!/usr/bin/env python3
from discord.ext import commands
from discord import app_commands

import discord

from resources import Token, BlurpleEmoji
import utils


class Announcement(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        utils.log.debug("Announcements cog is ready")
    
    @app_commands.command(
        name="announcement",
        description="Post announcement on the server",
        )
    #@app_commands.checks.has_any_role(
    #    "Admin", "Moderator", "Owner"
    #)
    async def announcement(self, interaction: discord.Interaction) -> None:
        embed0=discord.Embed(title='<:blurpleannouncements:880180645140246568>  `  ANKÜNDIGUNGEN  `', description='Wir möchten sicherstellen, dass du über alle wichtigen Entwicklungen auf dem Server informiert bist. Von neuen Features und Funktionen bis hin zu Veranstaltungen und Wettbewerben – hier findest du alles, was du wissen musst.', color=0x5865F2)
        embed0.set_footer(text='Bitte lies diese Nachricht sorgfältig durch, damit du informiert bleibst.', icon_url=self.bot.user.avatar) #type: ignore
        await interaction.response.send_message(embed=embed0)
        
    @announcement.error
    async def rules_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.errors.MissingAnyRole):
            await interaction.response.send_message("You don't have the required role to use this command.", ephemeral=True)
        if isinstance(error, app_commands.errors.CommandInvokeError):
            await interaction.response.send_message("An error occured while executing this command.", ephemeral=True)
 
            
async def setup(bot: commands.Bot) -> None:
   await bot.add_cog(
      Announcement(bot)#,
      #guilds = [discord.Object(id=Token.GUILD_ID)]
      )
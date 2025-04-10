#!/usr/bin/env python3
from discord.ext import commands

import discord

from resources import Token, BlurpleEmoji
import utils


class Welcome(commands.Cog):
   def __init__(self, bot: commands.Bot):
      self.bot = bot
   
   @commands.Cog.listener()
   async def on_ready(self):
      utils.log.info("Welcome cog is ready")

   @commands.Cog.listener()
   async def on_member_join(self, member: discord.Member):
      channel = utils.get_channel_by_name(member.guild, "willkommen")
      channel_id = channel.id #type: ignore
      
      embed = discord.Embed(title=f'**HALLO {member.name}!**', description='{} {}\n**Info:**\nBitte bestätige die Regeln, um Zugriff auf die freie Rollenauswahl zu bekommen.\nWenn du Fragen hast, wende dich an einen der <@&601422939765604400>.'.format((BlurpleEmoji.BLURBLEYES_EMOJI), member.mention), color=0x5865F2)
      embed.set_thumbnail(url=member.avatar)     
      
      await self.bot.get_channel(channel_id).send(embed=embed) #type: ignore

   @commands.Cog.listener()
   async def on_member_remove(self, member: discord.Member):
      channel = utils.get_channel_by_name(member.guild, "willkommen")
      channel_id = channel.id #type: ignore
      
      embed = discord.Embed(title=f'**TSCHÜSS {member.name}!**', description='{} {}\n**Info:**\n{} hat die Gruppe verlassen. Wir werden dich vermissen!'.format((BlurpleEmoji.BLURPLENO_EMOJI), member.mention, member.name), color=0x5865F2)
      embed.set_thumbnail(url=member.avatar)

      await self.bot.get_channel(channel_id).send(embed=embed) #type: ignore
     

async def setup(bot: commands.Bot) -> None:
   await bot.add_cog(
      Welcome(bot),
      guilds = [discord.Object(id=Token.GUILD_ID)]
      )
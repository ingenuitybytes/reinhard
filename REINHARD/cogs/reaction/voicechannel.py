from discord.ext import commands

from REINHARD.utils.setup import *
from REINHARD.utils.helper import *


class VoiceChannel(commands.Cog):
   def __init__(self, bot):
      self.bot = bot
      
   @commands.Cog.listener()
   async def on_ready(self):
      log.debug("Voice Channel cog is ready")   
      
   current_channels = list()
        
   @commands.Cog.listener()
   async def on_voice_state_update(self, member, before, after):
                        
################mainSection################       
      if before.channel is not None:
            for channel in self.current_channels:
               if before.channel.name == f"👤〡{channel} MEETING".upper() and len(before.channel.members) == 0:
                  await before.channel.delete()
                  self.current_channels.remove(channel)
                  break

      if after.channel is not None:
            if after.channel.name == TEMP_MAIN_CHANNEL:
               if get_channel_by_name(after.channel.guild, f"👤〡{member.name} MEETING".upper()) is None:
                  channel = await create_voice_channel(after.channel.guild, f"👤〡{member.name} MEETING".upper(), category_name=TEMP_MAIN_CATEGORY, user_limit=after.channel.user_limit, bitrate=after.channel.bitrate)
                  if channel is not None:
                        await member.move_to(channel)
                        self.current_channels.append(member.name)
               else:
                  await member.move_to(get_channel_by_name(after.channel.guild, f"👤〡{member.name} MEETING".upper()))

################schuleSection################
      if before.channel is not None:
         for channel in self.current_channels:
            if before.channel.name == f"👤〡{channel} LERNEN".upper() and len(before.channel.members) == 0:
               await before.channel.delete()
               self.current_channels.remove(channel)
               break
                                             
      if after.channel is not None:
         if after.channel.name == TEMP_SCHULE_CHANNEL:
            if get_channel_by_name(after.channel.guild, f"👤〡{member.name} LERNEN".upper()) is None:
               channel = await create_voice_channel(after.channel.guild, f"👤〡{member.name} LERNEN".upper(), category_name=TEMP_SCHULE_CATEGORY, user_limit=after.channel.user_limit, bitrate=after.channel.bitrate)
               if channel is not None:
                  await member.move_to(channel)
                  self.current_channels.append(member.name)
            else:
               await member.move_to(get_channel_by_name(after.channel.guild, f"👤〡{member.name} LERNEN".upper()))

async def setup(bot: commands.Bot) -> None:
   await bot.add_cog(
      VoiceChannel(bot),
      guilds = [discord.Object(id=GUILD_ID)]
      )
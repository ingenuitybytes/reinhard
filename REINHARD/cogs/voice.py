from discord.ext import commands

from REINHARD.additionals.utils import *
from REINHARD.additionals.data import *

################noError+finishedLog################
class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):           
################mainSection################       
        if before.channel is not None:
            if before.channel.category_id == get_category_by_name(before.channel.guild, TEMP_MAIN_CATEGORY).id:
                print(f"{member.name} left a temp channel")
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
            if before.channel.category_id == get_category_by_name(before.channel.guild, TEMP_SCHULE_CATEGORY).id:
                print(f"{member.name} left a temp channel")
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

def setup(bot):
    bot.add_cog(Voice(bot))
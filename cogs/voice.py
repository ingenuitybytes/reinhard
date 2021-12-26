from discord.ext import commands
import re

from utils import *

################noError+finishedLog################
class Voice(commands.Cog):
    
    current_streamers = list()
    current_channels = list()
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if not before.channel:
            print(f'{member.name} joined {after.channel.name}')
        if before.channel and not after.channel:
            print(f"{member.name} left voicechannel!")
        if before.channel and after.channel:
            if before.channel.id != after.channel.id:
                print(f"{member.name} switched voicechannels")
                if member.voice.self_stream:
                    print(f"{member.name} started streaming")
                    self.current_streamers.append(member.id)
                elif member.voice.self_mute:
                    print(f"{member.name} muted")
                elif member.voice.self_deaf:
                    print(f"{member.name} deafened")
                else:
                    for streamer in self.current_streamers:
                        if member.id == streamer:
                            if not member.voice.self_stream:
                                print(f"{member.name} stopped streaming")
                                self.current_streamers.remove(member.id)
                            break
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
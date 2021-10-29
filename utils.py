import discord
from discord.ext import commands

from settings import *

async def notify_user(member, message):
    if member is not None:
        channel = member.dm_channel
        if channel is None:
            channel = await member.create_dm()
        await channel.send(message)

def mods_or_owner():
    def predicate(ctx):
        return commands.check_any(commands.is_owner(), commands.has_role(MODERATOR_ROLE_NAME))
    return commands.check(predicate)
    
async def create_text_channel(guild, channel_name):
        category = get_category_by_name(guild, "TEXTCHANNEL")
        await guild.create_text_channel(channel_name, category=category)
        channel = get_channel_by_name(guild, channel_name)
        return channel
        
async def create_voice_channel(guild, channel_name, category_name, user_limit, bitrate):
        category = get_category_by_name(guild, category_name)
        await guild.create_voice_channel(channel_name, category=category, user_limit=user_limit, bitrate=bitrate)
        channel = get_channel_by_name(guild, channel_name)
        return channel

def get_channel_by_name(guild, channel_name):
        channel = None
        for c in guild.channels:
                if c.name == channel_name.lower():
                        channel = c
                        break
        return channel

def get_category_by_name(guild, category_name):
        category = None
        for c in guild.categories:
                if c.name == category_name:
                        category = c
                        break
        return category
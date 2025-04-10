#!/usr/bin/env python3

# Import modules and files
from discord.ext import commands
from datetime import datetime

currentTime = datetime.now().strftime("%d/%b/%Y %H:%M:%S")

class Style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

async def notify_user(member, message):
    if member is not None:
        channel = member.dm_channel
        if channel is None:
            channel = await member.create_dm()
        await channel.send(message)

def mods_or_owner():
    def predicate(ctx):
        return commands.check_any(commands.is_owner(), commands.has_role('Moderatoren'))
    return commands.check(predicate)  # type: ignore
    
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
                if c.name == channel_name:
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
        
def join_voice_channel(ctx):
        return 0
#!/usr/bin/env python3
from discord.ext import commands

import discord

from resources import Token, Channel
import utils


class VoiceChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        utils.log.info("Voice Channel cog is ready")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        await self.dynamic_channel_manage(Channel.TEMP_MAIN_CHANNEL, lambda x: x.startswith("👤〡"),
                                          lambda member: f"👤〡{member}'s room", member, before, after)

    async def dynamic_channel_manage(self, create_channel, dynamic_channel_match, dynamic_channel_create, member,
                                     before, after):
        if after.channel is not None:
            if after.channel.name == create_channel:
                owned_dynamic_channel = dynamic_channel_create(member.name)
                if utils.get_channel_by_name(after.channel.guild, owned_dynamic_channel) is None:
                    channel = await utils.create_voice_channel(after.channel.guild, owned_dynamic_channel,
                                                               category_name=str(after.channel.category),
                                                               user_limit=after.channel.user_limit,
                                                               bitrate=after.channel.bitrate)
                    if channel is not None:
                        await member.move_to(channel)
                else:
                    await member.move_to(utils.get_channel_by_name(after.channel.guild, owned_dynamic_channel))

        if before.channel is not None:
            if dynamic_channel_match(before.channel.name) and len(before.channel.members) == 0:
                await before.channel.delete()


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        VoiceChannel(bot),
        guilds=[discord.Object(id=Token.GUILD_ID)]
    )
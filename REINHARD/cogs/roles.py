import discord
from discord.ext import commands

from REINHARD.additionals.utils import mods_or_owner
from REINHARD.additionals.data import *

class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

################admincommand################
    @commands.command()
    @mods_or_owner()
    async def setuproles(self, ctx):
        await ctx.message.delete()
        
        embed = discord.Embed(title='**DIE ROLLEN**', description='Hier sind alle frei wählbaren Rollen aufgelistet. Wähle wirklich nur jene, die dich betreffen, um möglichen Spam zu vermeiden. Um eine Rolle auszuwählen, reagiere mit entsprechem Emote.\nWenn du Fragen hast, wende dich an einen der <@&601422939765604400>.\n\n**Frei wählbare Rollen:**', color=0x5865F2, timestamp= ctx.message.created_at)
                                  
        #embed.set_author(name="Page 1/1")
        embed.set_thumbnail(url="https://discords.com/_next/image?url=https%3A%2F%2Fcdn.discordapp.com%2Femojis%2F876446498840256562.png%3Fv%3D1&w=128&q=75")
        
        embed.add_field(name=f"**GAMES** {BLURPLEINTEGRATION_EMOJI}", value=f"{MINECRAFT_EMOJI} • Minecraft\n{AVORION_EMOJI} • Avorion\n{SCRAP_EMOJI} • Scrap Mechanic\n{KERBAL_EMOJI} • Kerbal Space Program\n{FACTORIO_EMOJI} • Factorio", inline=True)
        embed.add_field(name=f"**PROGRAMMIEREN** {BLURPLEEMPLOYEE_EMOJI}", value=f"{UNITY_EMOJI} • Unity", inline=True)
        
        embed.set_footer(text="Stand", icon_url=self.bot.user.avatar_url)
        message = await ctx.channel.send(embed=embed)
        
        await message.add_reaction(f'{MINECRAFT_EMOJI}')
        await message.add_reaction(f'{AVORION_EMOJI}')
        await message.add_reaction(f'{SCRAP_EMOJI}')
        await message.add_reaction(f'{KERBAL_EMOJI}')
        await message.add_reaction(f'{FACTORIO_EMOJI}')
        await message.add_reaction(f'{UNITY_EMOJI}')  
   
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = discord.utils.get(self.bot.get_all_channels(), name=RULEROLECHANNEL)
        channel_id = channel.id
        if payload.channel_id == channel_id:
            member = payload.member
            guild = member.guild
            emoji = payload.emoji.name
            print(emoji)
            if emoji == "minecraft":
                role = discord.utils.get(guild.roles, name="MINECRAFT")
                await member.add_roles(role)
            if emoji == "avorion":
                role = discord.utils.get(guild.roles, name="AVORION")
                await member.add_roles(role)
            if emoji == "scrap":
                role = discord.utils.get(guild.roles, name="SCRAP")
                await member.add_roles(role)
            if emoji == "ksp":
                role = discord.utils.get(guild.roles, name="KERBAL")
                await member.add_roles(role)
            if emoji == "factorio":
                role = discord.utils.get(guild.roles, name="FACTORIO")
                await member.add_roles(role)
            if emoji == "unity":
                role = discord.utils.get(guild.roles, name="UNITY")
                await member.add_roles(role)
        
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        channel = discord.utils.get(self.bot.get_all_channels(), name=RULEROLECHANNEL)
        channel_id = channel.id
        if payload.channel_id == channel_id:
            guild = await(self.bot.fetch_guild(payload.guild_id))
            emoji = payload.emoji.name
            if emoji == "minecraft":
                role = discord.utils.get(guild.roles, name="MINECRAFT")
                member = await(guild.fetch_member(payload.user_id))
                if member is not None:
                    await member.remove_roles(role)
            if emoji == "avorion":
                role = discord.utils.get(guild.roles, name="AVORION")
                member = await(guild.fetch_member(payload.user_id))
                if member is not None:
                    await member.remove_roles(role)
            if emoji == "scrap":
                role = discord.utils.get(guild.roles, name="SCRAP")
                member = await(guild.fetch_member(payload.user_id))
                if member is not None:
                    await member.remove_roles(role)
            if emoji == "ksp":
                role = discord.utils.get(guild.roles, name="KERBAL")
                member = await(guild.fetch_member(payload.user_id))
                if member is not None:
                    await member.remove_roles(role)
            if emoji == "factorio":
                role = discord.utils.get(guild.roles, name="FACTORIO")
                member = await(guild.fetch_member(payload.user_id))
                if member is not None:
                    await member.remove_roles(role)
            if emoji == "unity":
                role = discord.utils.get(guild.roles, name="UNITY")
                member = await(guild.fetch_member(payload.user_id))
                if member is not None:
                    await member.remove_roles(role)
                
def setup(bot):
    bot.add_cog(Roles(bot))
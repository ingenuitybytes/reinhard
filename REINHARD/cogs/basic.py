import discord

from discord import Spotify

from discord.ext import commands
from utils import *

from constants import *

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def invite(self, ctx):
        link = await ctx.channel.create_invite(max_age=1)
        await ctx.send(link)

    @commands.command()
    async def sourcecode(self, ctx):
        await ctx.send(GITHUB_LINK)

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='**HILFE ZUM BOT**', description='Hier sind alle Befehle von {} aufgelistet. Um einen Befehl aufzurufen, benutze den Prefix `.`\nWenn du Fragen hast, wende dich an einen der <@&601422939765604400>.\n\n**Befehle:**'.format(self.bot.user.mention), color=0x5865F2, timestamp= ctx.message.created_at)
                                  
        #embed.set_author(name="Page 1/1")
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        
        embed.add_field(name=f"**VERWALTUNG** {BLURPLEEMPLOYEE_EMOJI}", value="`profile`\n`delete`\n`invite`\n`say`", inline=True)
        embed.add_field(name=f"**INFORMATIONEN** {BLURPLESHOP_EMOJI}", value="`sourcecode`\n`userinfo`\n`spotify`", inline=True)
        embed.add_field(name=f"**MINIGAMES** {BLURPLEROCKET_EMOJI}", value="**Coming soon...!**", inline=True)
        
        embed.set_footer(text="Stand", icon_url=self.bot.user.avatar_url)
        await ctx.channel.send(embed=embed)    
        
    @commands.command()
    async def userinfo(self, ctx):
        args = ctx.message.content.split(' ')
        if len(args) == 2:
            member = ctx.message.mentions[0]
            embed = discord.Embed(title='Userinfo für {}'.format(member.name),
                                    description='{}'.format(member.mention), color=0x5865F2)
            embed.add_field(name='Server beigetreten', value=member.joined_at.strftime('%d/%m/%Y, %H:%M:%S'),
                            inline=True)
            embed.add_field(name='Discord beigetreten', value=member.created_at.strftime('%d/%m/%Y, %H:%M:%S'),
                            inline=True)
            rollen = ''
            for role in member.roles:
                if not role.is_default():
                    rollen += '{} \r\n'.format(role.mention)
            if rollen:
                embed.add_field(name='Rollen', value=rollen, inline=True)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text='Für weitere Funktionen .help Befehl eingeben')
            await ctx.channel.send(embed=embed)

    @commands.command()
    async def spotify(self, ctx, user: discord.Member=None):
        if user == None:         
            user = ctx.author         
            pass 
        if user.activities:
            for activity in user.activities:
                if isinstance(activity, Spotify):
                    channel = discord.utils.get(self.bot.get_all_channels(), name=MUSICCHANNEL)
                    channel_id = "<#" + str(channel.id) + ">"
                    embed = discord.Embed(
                        title = "SPOTIFY",
                        description = "\n{} {}\n{} hört sich **{}** seit **{}** an. Falls du auch Musik hören willst, kannst du das ganz einfach im {} Kanal machen.\nWenn du Fragen hast, wende dich an einen der <@&601422939765604400>.\n\n**Informationen:**".format(BLURBLEYES_EMOJI ,user.mention,user.name, activity.title, activity.created_at.strftime("%H:%M"), channel_id, MODERATOR_ROLE_NAME),
                        color = 0x5856F2, timestamp= ctx.message.created_at)
                        
                    embed.set_thumbnail(url=activity.album_cover_url)
                    
                    embed.add_field(name=f"**SONG** {BLURPLESTAR_EMOJI}", value=activity.title)
                    embed.add_field(name=f"**ALBUM** {BLURPLESHOP_EMOJI}", value=activity.album)
                    embed.add_field(name=f"**KÜNSTLER** {BLURPLEROLES_EMOJI}", value=activity.artist)
                    
                    embed.set_footer(icon_url=self.bot.user.avatar_url, text="Stand")
                    await ctx.send(embed=embed)
    
    @commands.command()
    @commands.is_owner()
    async def say(self, ctx, *args):
        await ctx.message.delete()
        await ctx.send(" ".join(args))
    
    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.content == "<:lauch:884903755621994557>":
            await ctx.delete()
            await ctx.channel.send(f"{ctx.author.name} hat einen kleinen Schwanz.")
            print("Hello")
 
def setup(bot):
    bot.add_cog(Basic(bot))
import discord
from discord.ext import commands

from REINHARD.additionals.data import *

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(self.bot.get_all_channels(), name="willkommen")
        channel_id = channel.id
        
        embed = discord.Embed(title=f'**HALLO {member.name}!**', description='{} {}\n**Info:**\nBitte bestätige die Regeln, um Zugriff auf die freie Rollenauswahl zu bekommen.\nWenn du Fragen hast, wende dich an einen der <@&601422939765604400>.'.format(BLURBLEYES_EMOJI, member.mention), color=0x5865F2)

        embed.set_thumbnail(url=member.avatar_url)     

        #embed.set_footer(text="Beigetreten", icon_url=self.bot.user.avatar_url)
        
        await self.bot.get_channel(channel_id).send(embed=embed)
   
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(self.bot.get_all_channels(), name="willkommen")
        channel_id = channel.id
        
        embed = discord.Embed(title='**TSCHÜSS {member.name}!**', description='{} {}\n**Info:**\n{member.name} hat die Gruppe verlassen. Wir werden dich vermissen!'.format(BLURPLENO_EMOJI, member.mention), color=0x5865F2)
        
        embed.set_thumbnail(url=member.avatar_url)     

        #embed.set_footer(text="Verlassen", icon_url=self.bot.user.avatar_url)
        
        await self.bot.get_channel(channel_id).send(embed=embed)
     
def setup(bot):
    bot.add_cog(Welcome(bot))
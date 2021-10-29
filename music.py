import discord
from discord.ext import commands
from discord.flags import Intents
import youtube_dl
from utils import mods_or_owner

from settings import *

class Music(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot
        
################admincommand################ 
    @commands.command()
    @mods_or_owner()
    async def setupmusic(self, ctx):
        await ctx.message.delete()
        
        embed = discord.Embed(title='**MUSIKAUSWAHL**', description='Verbinde dich mit einem Voicechannel und gib einen Name oder Url eines Liedes in diesen Kanal ein.\nWenn du Fragen hast, wende dich an einen der <@&601422939765604400>.\n\n**Lieder:**', color=0x5865F2, timestamp= ctx.message.created_at)
                                  
        #embed.set_author(name="Page 1/1")
        embed.set_thumbnail(url="https://discords.com/_next/image?url=https%3A%2F%2Fcdn.discordapp.com%2Femojis%2F857126121602285578.png%3Fv%3D1&w=128&q=75")
        
        embed.add_field(name=f"**WARTESCHLANGE** {BLURPLESEARCH_EMOJI}", value="**1** • ...\n**2** • ...", inline=True)
        embed.add_field(name=f"**FAVORITEN** {BLURPLESTAR_EMOJI}", value="**Coming soon...!**", inline=True)
        
        embed.set_footer(text="Stand", icon_url=self.bot.user.avatar_url)
        message = await ctx.channel.send(embed=embed)
        
        await message.add_reaction(f'{PLAYORPAUSE_EMOJI}')
        await message.add_reaction(f'{STOP_EMOJI}')
        await message.add_reaction(f'{NEXTTRACK_EMOJI}')
        await message.add_reaction(f'{COUNTERCLOCKWISE_EMOJI}')
        await message.add_reaction(f'{SHUFFLETRACKS_EMOJI}')
        await message.add_reaction(f'{STAR_EMOJI}')
        await message.add_reaction(f'{CROSSMARK_EMOJI}')

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            return
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move.to(voice_channel)
    
    @commands.command()        
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()
    
    @commands.command()
    async def play(self, ctx, url):
        ctx.voice_client.stop()
        vc = ctx.voice_client
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            #source2 = discord.PCMVolumeTransformer(source, volume=0.5)
            vc.play(source)
    
    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused")
    
    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("Resume")
    
    @commands.Cog.listener()
    async def on_message(self, ctx):
        channel = discord.utils.get(self.bot.get_all_channels(), name=MUSICCHANNEL)
        channel_id = channel.id
        if ctx.channel.id == channel_id:
            vc = discord.utils.get(self.bot.voice_clients)
            #if ctx.author.bot:
            #    return
            #else:
            vc.stop()
            #vc = ctx.voice_client
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(ctx.content, download=False)
                url = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url, **FFMPEG_OPTIONS)
                #source2 = discord.PCMVolumeTransformer(source, volume=0.5)
                vc.play(source)    
            await ctx.delete()
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        user = self.bot.get_user(payload.user_id)
        if not user.bot:
            channel = discord.utils.get(self.bot.get_all_channels(), name=MUSICCHANNEL)
            channel_id = channel.id
            if payload.channel_id == channel_id:
                message = await channel.fetch_message(payload.message_id)
                await message.remove_reaction(payload.emoji, user)
                
                emoji = payload.emoji.name
                vc = discord.utils.get(self.bot.voice_clients)
                if emoji == "stop":
                    await vc.disconnect()
                if emoji == "playorpause":
                    vc.pause()
        
def setup(bot):
    bot.add_cog(Music(bot))
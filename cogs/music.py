import discord
import asyncio
from discord.ext import commands
from discord.flags import Intents
import youtube_dl
from utils import mods_or_owner

from constants import *



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
    
    @commands.Cog.listener()
    async def on_message(self, ctx):
        channel = discord.utils.get(self.bot.get_all_channels(), name=MUSICCHANNEL)
        channel_id = channel.id
        if ctx.channel.id == channel_id:
            message = ctx.content
            await ctx.delete()
            
            if ctx.author.voice is None:
                return

            vc = discord.utils.get(self.bot.voice_clients)
            voice_channel = ctx.author.voice.channel
        
            vc = await self.set_voice_client(voice_channel, vc)

            if vc.is_connected():
                await self.youtube_playing(message, vc) 
            else:
                print("Voice_Client ist nicht verbunden!")
               
    async def set_voice_client(self, voice_channel, vc):
        if vc is None:
            await voice_channel.connect()
            vc = discord.utils.get(self.bot.voice_clients)
        elif vc.channel is voice_channel:
            vc = discord.utils.get(self.bot.voice_clients)
            vc.stop()
        else:
            vc = discord.utils.get(self.bot.voice_clients)
            vc.stop()
            await vc.move_to(voice_channel)
            #await asyncio.sleep(2)
        return vc
                
    async def youtube_playing(self, message, vc):
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(message, download=False)
                if 'entries' in info:
                    url2 = info["entries"][0]["formats"][0]['url']
                    print("SEARCH")
                elif 'formats' in info:
                    print("URL")
                    url2 = info["formats"][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
                vc.play(source)
            
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
                    if vc.is_playing():
                        vc.pause()
                    else:
                        vc.resume()
                                    
def setup(bot):
    bot.add_cog(Music(bot))
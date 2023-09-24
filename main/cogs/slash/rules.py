#!/usr/bin/env python3
from discord.ext import commands
from discord import app_commands

import discord

from resources import Token, BlurpleEmoji
import utils


class Rules(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        utils.log.debug("Rules cog is ready")
    
    @app_commands.command(
        name="rules",
        description="Get the rules of the server",
        )
    #@app_commands.checks.has_any_role(
    #    "Admin", "Moderator", "Owner"
    #)
    async def rules(self, interaction: discord.Interaction) -> None:
        
        embed0=discord.Embed(title='<:rulebook:1093653038243266590>  `  DAS REGELWERK  `', description='Um diese Community positiv und produktiv zu halten, stimmst du den folgenden Regeln zu, indem du weiterhin den TGM&someotherdudes Server nutzt.', color=0x5865F2)
        # embed0.set_thumbnail(url='https://discords.com/_next/image?url=https%3A%2F%2Fcdn.discordapp.com%2Femojis%2F876864260632870973.png%3Fv%3D1&w=128&q=75')
        
        embed0.set_footer(text='Alle Regeln gelten für jeden Channel auf dem Server, sofern nicht anders angegeben.', icon_url=self.bot.user.avatar) #type: ignore 
        
        embed1=discord.Embed(title='', description='', color=0x5865F2)

        embed1.add_field(name='`  Regel 0  `  Halte folgende Terms & Policies ein:', value='• [Nutzungsbedingungen](https://discord.com/terms)\n• [Community-Richtlinien](https://discord.com/guidelines)', inline=False)
        
        embed1.add_field(name='`  Regel 1  `  Sei respektvoll.', value='Behandle andere so, wie du selbst behandelt werden möchtest, und gehe von den besten Absichten aus. Belästige oder attackiere niemanden und beteilige dich nicht an hasserfülltem oder generell bösartigem Verhalten (z.B. Sexismus, Rassismus, Homophobie, etc.). Halte die Negativität auf einem Minimum.', inline=False)
        
        embed1.add_field(name='`  Regel 2  `  Keine anstößigen Inhalte.', value='Das Teilen von NSFW- oder gewalttätigen/beunruhigenden Inhalten durch Nachrichten oder innerhalb von Discord-Profilen ist strengstens untersagt.', inline=False)
        
        embed1.add_field(name='`  Regel 3  `  Bleib beim Thema.', value='Sei dir bewusst, was andere Benutzer in einem Kanal als hilfreich oder interessant empfinden könnten, wenn du postest. Bleib beim Thema, um die Gespräche fokussiert und produktiv zu halten.', inline=False)
        
        embed1.add_field(name='`  Regel 4  `  Kein Spamming.', value='Spamme oder flute den Server nicht mit Nachrichten, da dies störend ist. Massen-Pings, Nachrichten in Großbuchstaben, wiederholtes Posten in kurzer Zeit oder das nacheinander Veröffentlichen sehr ähnlicher Beiträge gelten als Formen von Spamming.', inline=False)
        
        embed1.add_field(name='`  Regel 5  `  Verzichte auf das Teilen von persönlich identifizierbaren Informationen (PII).', value='Bitte teile auf dem Server keine persönlichen oder sensiblen Informationen. Doxxing anderer Personen ist verboten.', inline=False)
        
        embed1.add_field(name='`  Regel 6  `  Keine politischen und religiösen Diskussionen oder Inhalte.', value='Benutzer aus aller Welt besuchen diesen Server. Um eine respektvolle und zivilisierte Atmosphäre auf unserem Server aufrechtzuerhalten, vermeide bitte alle religiösen und politischen Diskussionen oder Inhalte.', inline=False)
        
        embed1.add_field(name='`  Regel 7  `  Keine Eigenwerbung, Anfragen oder Werbung.', value='Poste oder sende keine Nachrichten an Mitglieder dieses Servers, um Produkte oder -Projekte zu bewerben.', inline=False)
        
        embed1.add_field(name='`  Regel 8  `  Teile oder nutze Inhalte aus diesem Server nicht ohne Einwilligung des Schöpfers.', value='Wir erlauben kein Crawlen, Scrapen oder anderweitiges externes Verwenden von Inhalten oder Links, die in diesem Discord-Server gepostet wurden, ohne ausdrückliche Zustimmung des Urhebers.', inline=False)
        
        embed1.add_field(name='`  Regel 9  `  Umgehe nicht den AutoMod-Filter.', value='Versuche nicht, unsere Serverfilter durch die Verwendung von ähnlichen oder bedeutungslosen Variationen von Wörtern zu umgehen, sowie durch die Verwendung einzigartiger Zeichen. Bitte beachte, dass die Verwendung deines Serverprofils zum Umgehen des Filters zu Verstößen führen kann.', inline=False)
        
        embed1.add_field(name='`  Regel 10  `  Respektiere die Moderatoren.', value='Respektiere die Moderatoren und die Entscheidungen, die sie treffen. Wenn du eine Frage oder einen Vorschlag hast, kannst du gerne einen Moderator kontaktieren. Wenn du jedoch nicht mit einer Entscheidung einverstanden bist, kannst du dich an einen anderen Moderator wenden.', inline=False)

        embed1.set_footer(text='Die Server-Regeln können ohne vorherige Ankündigung geändert werden.', icon_url=self.bot.user.avatar) #type: ignore
         
        await interaction.response.send_message(embeds=(embed0, embed1))
    
    
    @rules.error
    async def rules_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.errors.MissingAnyRole):
            await interaction.response.send_message("You don't have the required role to use this command.", ephemeral=True)
        if isinstance(error, app_commands.errors.CommandInvokeError):
            await interaction.response.send_message("An error occured while executing this command.", ephemeral=True)
 
            
async def setup(bot: commands.Bot) -> None:
   await bot.add_cog(
      Rules(bot)#,
      #guilds = [discord.Object(id=Token.GUILD_ID)]
      )
import discord
from discord import app_commands
from discord.ext import commands

from REINHARD.utils.setup import *


class Rules(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        log.debug("Rules cog is ready")
    
    @app_commands.command(
        name="rules",
        description="Get the rules of the server",
        )
    @app_commands.checks.has_any_role(
        "Admin", "Moderator", "Owner"
    )

    async def rules(self, interaction: discord.Interaction) -> None:
        
        embed=discord.Embed(title='**DAS REGELWERK**', description='...ja, auch hier gibt es ein paar Regeln, um das gemeinsame miteinander auf dem Server zu ermöglichen. Nimm dir bitte die Zeit und lese dir das Regelwerk einmal durch. Bestätige es anschließend noch, um Zugriff auf die persönliche Rollenzuweisung zu bekommen.\n\n**Zusammenfassung:**\nBenimm dich, sei Freundlich und gehe keinem auf den Geist. Benutzte deinen Menschenverstand, um zu entscheiden was erlaubt ist und was nicht. Wenn du Fragen hast, wende dich an einen der <@&601422939765604400>.\n\n**Langform:**\n', color=0x5865f2, timestamp=interaction.created_at)
        
        #embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://discords.com/_next/image?url=https%3A%2F%2Fcdn.discordapp.com%2Femojis%2F876864260632870973.png%3Fv%3D1&w=128&q=75")

        embed.add_field(name=f'**ALLGEMEIN** {(emojis['BLURPLEANNOUNCEMENTS_EMOJI'])}', value='• [**Nutzungsbedingungen**](https://discord.com/terms) und [**Community-Richtlinien**](https://discord.com/guidelines) einhalten\n • verwende keinen beleidigenden Benutzernamen oder Status\n • keine Themen über Politik und Religion\n • jegliche Art von __Werbung__ oder __NSFW Inhalte__ = **Ban**', inline=False)
        embed.add_field(name=f'**TEXTKANÄLE** {(emojis['BLURPLETEXTCHANNEL_EMOJI'])}', value='• pro Nachricht max. 8 Emojis / 4 @Erwähnungen / 3 Spoiler\n • jegliche Art von Spam oder CAPS ist nicht erwünscht\n • sende nur Links, die erlaubt sind | Liste erlaubter Links\n • schreibe im vorgesehenen Kanal\n • erwähne keinen mit der <@&820402128383901758> oder <@&488680209730764811> Rolle', inline=False)
        embed.add_field(name=f'**SPRACHKANÄLE** {(emojis['BLURPLEVOICECHANNEL_EMOJI'])}', value='• keine Aufnahmen ohne Erlaubnis aller Beteiligten\n • unterlasse störende/rauschende Geräusche\n • wechsle nicht ständig die Channel', inline=False)
        embed.add_field(name=f'**DAS TEAM** {(emojis['BLURPLEEMPLOYEE_EMOJI'])}', value='• verteilt Verwarnungen & Strafen nach eigenem ermessen\n • kann Regeln vorübergehend aufheben/verschärfen\n • hat dir gegenüber ein Weisungsrecht', inline=False)
        embed.add_field(name=f'**SCHLUSSWORT** {(emojis['BLURPLETICKET_EMOJI'])}', value='Das Regelwerk kann jederzeit geändert werden, halte dich bitte selbständig auf dem Laufenden. Gegen nicht aufgeführte Aktionen werden wir, wenn es nötig ist, ebenfalls moderativ durchgreifen.', inline=False)
        embed.set_footer(text="Stand", icon_url=self.bot.user.avatar) #type: ignore
        
        await interaction.response.send_message(embed=embed)
        
    @rules.error
    async def rules_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.errors.MissingAnyRole):
            await interaction.response.send_message("You don't have the required role to use this command.", ephemeral=True)
        if isinstance(error, app_commands.errors.CommandInvokeError):
            await interaction.response.send_message("An error occured while executing this command.", ephemeral=True)
            

async def setup(bot: commands.Bot) -> None:
   await bot.add_cog(
      Rules(bot),
      guilds = [discord.Object(id=GUILD_ID)]
      )
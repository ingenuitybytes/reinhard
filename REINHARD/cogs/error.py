from discord.ext import commands
from REINHARD.additionals.data import log

class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        await ctx.send("Please check with **.help** the usage of this command or talk to one of the **moderators**")
        log.error(ex)
              
def setup(bot):
    bot.add_cog(Error(bot))
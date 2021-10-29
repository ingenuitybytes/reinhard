from discord.ext import commands

class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ex)
        await ctx.send("Please check with **.help** the usage of this command or talk to one of the **moderators**")
              
def setup(bot):
    bot.add_cog(Error(bot))
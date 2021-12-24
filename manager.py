from discord.ext import commands

class Manager(commands.Cog):
    '''bot manager'''
    def __init__(self, bot):
        self.bot = bot
    
    # Indica que o bot está online
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Estou Online como {self.bot.user}!')
    # def on_ready 
    #   
def setup(bot):
    bot.add_cog(Manager(bot))
from discord.ext import commands
from commands.msg_aleatoria import *

class Sorte(commands.Cog):
    '''Sorte commands'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='sorte')
    async def MostrarSorte(self, ctx):
        nome = ctx.author
        resposta = f':four_leaf_clover: Sorte do(a) {nome.mention} :four_leaf_clover:\n {Msg.MsgSorte()}'

        # Os emojis devem estar em formato unicode para add_reaction
        await ctx.message.add_reaction('\N{four leaf clover}')
        await ctx.send(resposta)
# def MostrarSorte

def setup(bot):
    bot.add_cog(Sorte(bot))
from discord.ext import commands
import discord

class Info(commands.Cog):
    '''Bot Infos'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['ajuda', 'sobre'])
    async def Ajuda(self, ctx):
        embed_ajuda = discord.Embed (
            title = ':four_leaf_clover: Sobre BiscoitoDaSorte',
            description = 'Biscoito da Sorte foi feito com o intuito inicialmente de servir como teste de desenvolvimento de BOT, assim o criador pôde aprender os conceitos principais de como construir BOTs personalizados para a plataforma, utilizando a linguagem de programação Python.\n\n:computer: **Comandos (=): **\n`=comandos`',
            color = 0x00B70F,
        )
        await ctx.message.add_reaction('\N{four leaf clover}')
        await ctx.send(embed=embed_ajuda)
    # def Ajuda

    @commands.command(name='comandos')
    async def Comandos(self, ctx):
        embed_comandos = discord.Embed (
            title = ':four_leaf_clover: Comandos BiscoitoDaSorte',
            description = ('**=comandos**: Mostra uma lista de comandos que podem ser utilizados no BiscoitoDaSorte.\n'
                            +'**=sorte**: Mostra uma mensagem aleatória, pode trazer bons conselhos e avisos.\n'
                            +'**=tempo**: Mostra informações do tempo e clima da região.'),
            color = 0x00B70F,
        )
        await ctx.message.add_reaction('\N{four leaf clover}')
        await ctx.send(embed=embed_comandos)
    # def Comandos

def setup(bot):
    bot.add_cog(Info(bot))
import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument

class Talks(commands.Cog):
    '''Talks with user'''
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.message.add_reaction('\N{four leaf clover}')

            if '=tempo' or '=clima' or '=temperatura' in ctx.message.content:
                embed = discord.Embed(
                    title = f':thermometer: Como usar o `=tempo`?',
                    description = ('**:test_tube: Exemplo de uso:**'+
                        ' `=tempo São Paulo`\n'+
                        'Exibe informações sobre clima e tempo em São Paulo.\n\n'+
                        '**:game_die: Variações: **\n`=tempo` `=clima` `=temperatura`'),
                    color = 0x00B70F
                )
                embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.message.channel.send(embed=embed)

        elif isinstance(error, CommandNotFound):
            await ctx.message.add_reaction('\N{Warning Sign}')
            await ctx.send(f'{ctx.author.mention} \n:four_leaf_clover: O comando não existe!' +
                '\nDigite =comandos, para ver todos os comandos')
        
        else:
            raise error
    # def on_command_error
# class Talks

def setup(bot):
    bot.add_cog(Talks(bot))
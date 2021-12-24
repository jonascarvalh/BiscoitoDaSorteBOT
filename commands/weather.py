from discord.ext import commands
import discord

from WeatherPy import *
from WeatherPy.Temperatura import Temperatura

class Weather(commands.Cog):
    '''Talks with user'''
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['tempo', 'temperatura', 'clima'])
    async def Tempo(self, ctx, *, city):
        temperatura, umidade, pressao, temp_min, temp_max, localidade, descricao = Temperatura(city)

        embed_tempo = discord.Embed (
            title = f'Previsão do tempo de {city}, {localidade}',
            description = (descricao),
            color = 0x00B70F
        )
        embed_tempo.add_field(name=':thermometer: Temperatura',
            value=(f'**Atual: **{temperatura} °C\n**Máx: **{temp_max} °C \n **Mín:** {temp_min} °C')
        )
        embed_tempo.add_field(name=':droplet: Úmidade', value=('%.1f %%' % umidade))
        embed_tempo.add_field(name=':mountain_snow: Pressão', value=(f'{pressao} kPa'))

        await ctx.message.add_reaction('\N{four leaf clover}')
        await ctx.send(content=ctx.author.mention, embed=embed_tempo)
    # def Tempo 

def setup(bot):
    bot.add_cog(Weather(bot))
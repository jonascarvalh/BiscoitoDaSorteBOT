import discord
from discord.ext  import commands
from MsgAleatoria import *

# Criando o objeto
bot = commands.Bot('=')

# Indica que o bot está online
@bot.event
async def on_ready():
    print(f'Estou Online como {bot.user}!')
# def on_ready

# Comando: =sorte
# Imprime uma frase aleatória
@bot.command(name='sorte')
async def MostrarSorte(ctx):
    nome = ctx.author
    resposta = f':four_leaf_clover: Sorte do(a) {nome.mention} :four_leaf_clover:\n {MsgSorte()}'

    # Os emojis devem estar em formato unicode para add_reaction
    await ctx.message.add_reaction('\N{four leaf clover}')
    await ctx.send(resposta)
# def MostrarSorte

# Comando: =ajuda
# Mostra informações sobre o bot
@bot.command(name='ajuda')
async def Ajuda(ctx):
    embed_ajuda = discord.Embed (
        title = ':four_leaf_clover: Sobre BiscoitoDaSorte',
        description = 'Biscoito da Sorte foi feito com o intuito inicialmente de servir como teste de desenvolvimento de BOT, assim o criador pôde aprender os conceitos principais de como construir BOTs personalizados para a plataforma, utilizando a linguagem de programação Python.\n\n:computer: **Comandos (=): **\n`=comandos`',
        color = 0x00B70F,
    )
    await ctx.message.add_reaction('\N{four leaf clover}')
    await ctx.send(embed=embed_ajuda)
# def Ajuda

# Comando: =comandos
# Mostra todos os comandos do bot
@bot.command(name='comandos')
async def Comandos(ctx):
    embed_comandos = discord.Embed (
        title = ':four_leaf_clover: Comandos BiscoitoDaSorte',
        description = '**=comandos**: Mostra uma lista de comandos que podem ser utilizados no BiscoitoDaSorte.\n**=sorte**: Imprime uma mensagem aleatória, pode trazer bons conselhos e avisos.\n',
        color = 0x00B70F,
    )
    await ctx.message.add_reaction('\N{four leaf clover}')
    await ctx.send(embed=embed_comandos)
# def Comandos

# Executando o BOT, deixando-o online
# Você deve passar o token obtido em:
# https://discord.com/developers/applications
bot.run('teste')
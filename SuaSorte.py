import discord
from discord.ext import commands
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
    resposta = f':four_leaf_clover: Sorte do(a) @{nome} :four_leaf_clover:\n {MsgSorte()}'
    await ctx.send(resposta)
# def MostrarSorte

# Comando: =ajuda
# Mostra informações sobre o bot
@bot.command(name='ajuda')
async def Ajuda(ctx):
    await ctx.send('Imagina uma mensagem de ajuda')
# def Ajuda

# Comando: =comandos
# Mostra todos os comandos do bot
# Ainda será feito...

# Executando o BOT, deixando-o online
# Você deve passar o token obtido em:
# https://discord.com/developers/applications
bot.run('token')
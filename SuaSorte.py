from decouple import config
from discord.ext  import commands
import os 

# Criando o objeto
bot = commands.Bot('=')

def load_cogs(bot):
    bot.load_extension('manager')
    bot.load_extension('tasks.talks')

    for file in os.listdir('commands'):
        if file.endswith('.py'):
            cog = file[:-3]
            bot.load_extension(f'commands.{cog}')

load_cogs(bot)

# Executando o BOT, deixando-o online
# Você deve passar o token obtido em:
# https://discord.com/developers/applications
TOKEN = config('TOKEN')
bot.run(TOKEN)
import discord
import os
from discord.ext import commands

# Récupérer le token du bot et l'ID du serveur depuis les variables d'enviro>
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('DISCORD_GUILD_ID'))

intents = discord.Intents.default()
intents.members = True  # Nécessaire pour accéder aux membres du serveur

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    guild = bot.get_guild(GUILD_ID)
    if guild:
        print(f'Connecte a : {guild.name}')
    else:
        print('Guild not found')

@bot.command()
async def send_message(ctx, *, message: str):
    """Commande pour envoyer un message à tous les membres du serveur."""
    guild = bot.get_guild(GUILD_ID)
    if guild:
        for member in guild.members:
            try:
                await member.send(message)
                print(f'{member.name}a bien recu le mp de {bot.user.name}')
            except discord.Forbidden:
                print(f'{member.name}a desactive son mp')
    else:
        await ctx.send('serveur non trouve')

bot.run(TOKEN)

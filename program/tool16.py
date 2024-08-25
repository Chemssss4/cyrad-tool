# par pitié ne pas volé mon code et ne rien modiffié svp sah
import os
import discord
from discord.ext import commands
from pystyle import Colors



def afficher_titre_cleardm():
    """Affiche le titre de l'outil."""
    print(f"{Colors.red}Outil de Nettoyage de DM{Colors.reset}")

def definir_titre(titre):
    """Définit le titre de la fenêtre du terminal (Windows uniquement)."""
    if os.name == 'nt':
        os.system(f"title {titre}")

def main():
    """Point d'entrée principal du script."""
    pass


definir_titre("Nettoyage DM")

afficher_titre_cleardm()


token = input(f"{Colors.red}Votre Token de Compte : {Colors.reset}")
print(f"{Colors.red}Écrivez \"!clear\" dans l'un de vos DM pour supprimer vos messages{Colors.reset}")


bot = commands.Bot(command_prefix="!", self_bot=True)
bot.remove_command("help")

@bot.command()
async def clear(ctx, limit: int=None):
    """Commande pour supprimer les messages dans les DM du bot."""
    passe = 0
    echoue = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == bot.user.id:
            try:
                await msg.delete()
                passe += 1
            except Exception as e:
                echoue += 1
                print(f"{Colors.red}Échec de la suppression du message : {e}{Colors.reset}")
    
    print(f"{Colors.red}\nSupprimé {passe} messages avec {echoue} échecs{Colors.reset}")
    input(f"{Colors.red}\nAppuyez sur ENTRÉE pour quitter{Colors.reset}")
    main()


bot.run(token, bot=False)

if __name__ == "__main__":
    main()

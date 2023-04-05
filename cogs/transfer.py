from nextcord.ext import commands
import nextcord, database
class Transfer(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name='transfer', description='Donne de l\'argent à quelqu\'un', guild_ids = [1091820169300545537])
  async def Transfer_slash(self,interaction: nextcord.Interaction,montant: int = nextcord.SlashOption(name="montant", description="Le nombre d'argent que tu veux donner",required=True), member: nextcord.Member = nextcord.SlashOption(name="membre", description="Le membre auquel tu veux donner de l'argent", required=True)):
    if database.get_coin(interaction.user.id) < montant:
      await interaction.response.send_message(
        "Tu n'as pas assez d'argent pour faire cela!", ephemeral=True)
      return
    database.remove(interaction.user.id, montant)
    database.add(member.id, montant)
    await interaction.response.send_message(embed=nextcord.Embed(title=f'Transfer de {interaction.user.name} à {member.name}', description=f'**Nombre de jetons transférés** **:** **{str(montant)} jetons**\n**Nouveau nombre de jetons** **:** **{database.get_coin(member.id)} jetons**\n__**Classement**__ **:** **{database.get_classement(member.id)}**',  color=0xa84300).set_thumbnail(member.avatar.url))

def setup(bot):
  bot.add_cog(Transfer(bot))

from nextcord.ext import commands
import nextcord, database
class Remove(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name='remove', description='Retirer de l\'argent à quelqu\'un', guild_ids = [1091820169300545537])
  async def Remove_slash(self,interaction: nextcord.Interaction,montant: int = nextcord.SlashOption(name="montant", description="Le nombre d'argent que tu veux donner",required=True), member: nextcord.Member = nextcord.SlashOption(name="membre", description="Le membre auquel tu veux donner de l'argent", required=True)):
    if not 1091825227215929364 in [role.id for role in interaction.user.roles]:
      await interaction.response.send_message("Tu ne peux pas faire cela!", ephemeral=True)
      return
    database.remove(member.id, montant)
    await interaction.response.send_message(embed=nextcord.Embed(title=f'Supression de fond à {member.name} de {montant} jetons', description=f'**Nouveau nombre de jetons** **:** **{database.get_coin(member.id)} jetons**\n__**Classement**__ **:** **{database.get_classement(member.id)}**',  color=0xa84300).set_thumbnail(member.avatar.url))

def setup(bot):
  bot.add_cog(Remove(bot))

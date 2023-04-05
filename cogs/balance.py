from nextcord.ext import commands
import nextcord, database
class Balance(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name='balance', description='Te montre la balance de quelqu\'un', guild_ids = [1091820169300545537])
  async def balance_slash(self, interaction: nextcord.Interaction, member: nextcord.Member = nextcord.SlashOption(name="membre", description="Le membre auquel tu veux voir le compte (si vide c'est toi)", required=False)):
    if member is None:
      member = interaction.user
    money = database.get_coin(member.id)
    await interaction.response.send_message(embed=nextcord.Embed(title=f'Balance de {member.name}', description=f'**Nombre de jetons** **:** **{money} jetons**\n__**Classement**__ **:** **{database.get_classement(member.id)}**', color=0xa84300).set_thumbnail(member.avatar.url))

def setup(bot):
  bot.add_cog(Balance(bot))

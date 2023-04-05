from nextcord.ext import commands
import nextcord, database
class Top(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name='top', description='Te montre le top 3', guild_ids = [1091820169300545537])
  async def classement_slash(self, interaction: nextcord.Interaction):
    cont = ''
    top3 = database.get_top_3()
    for i in range(len(top3)):
      cont += f"__**{str(i + 1)}**__ : <@{top3[i]['_id']}> **|** **{top3[i]['tokens']} jetons\n**"
    await interaction.response.send_message(embed=nextcord.Embed(title='Classement', description=cont, color=0xa84300).set_image("https://cdn.discordapp.com/attachments/1092258425339121784/1092604555155484682/Fichier_3.png"))

def setup(bot):
  bot.add_cog(Top(bot))

import discord

from .helpers import verification
from discord.ext import commands

class Tools(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help='🔧View the last joins.')
    async def joinlog(self, ctx):
        return
    
    @commands.command(help='🔧Show an example verification challenge.')
    async def verifydemo(self, ctx):
        challenge = verification.get_challenge()
        await ctx.send(embed=discord.Embed(title='Verification Challenge Demo', description=challenge[0], color=discord.Color(0x00ffff)).set_footer(text=f'Correct answer: {challenge[1]}'))

def setup(client):
    client.add_cog(Tools(client))
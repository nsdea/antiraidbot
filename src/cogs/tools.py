import discord
from discord.ext import commands

class Tools(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help='🔧View the last joins.')
    async def joinlog(self, ctx):
        return

def setup(client):
    client.add_cog(Tools(client))
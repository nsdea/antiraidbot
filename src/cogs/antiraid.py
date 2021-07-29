import discord
from discord.ext import commands

class AntiRaid(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        pass

def setup(client):
    client.add_cog(AntiRaid(client))
import discord

client = discord.Client()

TOKEN = "YOUR_TOKEN_HERE"

@client.event
async def on_ready():
    print(f"Logged in as: {client.user.name}")
    print("------")
    for guild in client.guilds:
        if guild.owner is not None and guild.owner.id == client.user.id:
            print(f"Deleting server: {guild.name}")
            await guild.delete()
    print("Finished, no more servers to delete.")
    await client.close()

client.run(TOKEN, bot=False)

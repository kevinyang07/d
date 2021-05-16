from discord.ext import commands
import discord
import time
import datetime

print("Starting please wait.")

token = "ODQzNTE1NTczNjczNTI1MjQ4.YKFADA.--ijhd7dHV5kPwtiOZTk_Vi36pI"
bot = commands.Bot(".", self_bot=True)
now = datetime.datetime.now()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="mm")) # You can delete this line or change ducchub to your server name, its just a custom status
    print("pp")

@bot.command()
async def farm(ctx):
    print("Starting farm.")
    while True:
        await ctx.send('pls beg')
        await ctx.send('pls pm')
        await ctx.send('f')
        await ctx.send('pls fish')
        await ctx.send("pls hunt")
        await ctx.send("pls sell fish all")
        await ctx.send("pls sell deer all")
        await ctx.send("pls sell duck all")
        await ctx.send("pls sell rabbit all")
        await ctx.send("pls sell skunk all")
        await ctx.send("pls dig")
        await ctx.send("pls dep all")
        await ctx.send("pls use note")
        await ctx.send("all")
        time.sleep(10)



bot.run(token, bot=False)

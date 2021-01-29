import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix="->")
client.remove_command("help")


@client.command()
async def animegirl(ctx):
    i = 0
    while i < 3:
        embed = discord.Embed(
            title="Toma tu chica 7u7",
            colour=discord.Colour.red()
        )
        
        values = lolisi()
        embed.set_image(url=values)

        await ctx.send(embed=embed)

        i += 1


        

def lolisi():
    uwuse = ["https://i.pinimg.com/originals/9a/ad/d1/9aadd10855fffd866c97619af3acfa2c.jpg",
             "https://data.whicdn.com/images/174142895/original.jpg",
             "https://www.androidred.com/wp-content/uploads/2018/12/anime-girl-purple-hair.jpg",
             "https://www.ultrahdwallpaper.in/uploads/cache/544981391/Cute-Anime-Girl-Wallpaper-HD-1300x0-MM-100.jpg",
             "https://i.ytimg.com/vi/A1fkIvmbD_4/maxresdefault.jpg",
             "https://data.whicdn.com/images/321030626/large.jpg", "https://wallpaperaccess.com/full/2061.png",
             "https://wallpaperaccess.com/full/24545.jpg"]
    values = random.choice(uwuse)
    return values



@client.command()
async def lolis(ctx):
    embed = discord.Embed(
        title="Pinshe pervertido, no te las dare ahora",
        colour=discord.Colour.red()
    )

    embed.set_image(url="https://thumbs.gfycat.com/ConcreteVibrantDalmatian-size_restricted.gif")
    await ctx.send(embed=embed)


@client.command()
async def uwu(ctx):
    uwus = ["Me gustan las lolis UwU", "Amen a su lider Emma UwU", "Las waifus no se profanan", "Me das comida uwu?",
            "Te amo UwU", "UwU", "Lolis uwu", "Los gatitos UwU", "Amen me chicos uwu", "Alimentamen UwU",
            "Te gustan las nekos? UwU",
            "Dame una galleta UwU", "Amo este server UwU"]
    value = random.choice(uwus)
    embed = discord.Embed(
        title=value,
        colour=discord.Colour.red()
    )
    author = ctx.author.mention
    await ctx.send(author, embed=embed)


@client.command(pass_context=True)
async def help(ctx):
    author = ctx.author.mention

    embed = discord.Embed(
        colour=discord.Colour.blue()
    )

    embed.set_author(name="Help")
    embed.add_field(name="->uwu", value="Responde cosas lindas", inline=False)
    embed.add_field(name="->animegirl", value="Imagenes de anime especialmente chicas", inline=False)
    embed.add_field(name="->lolis", value="FBI, OPEN UP", inline=False)
    await ctx.send(author, embed=embed)


client.run('token')

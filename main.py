import discord
import random
from discord.ext import commands
from bs4 import *
import requests as rq
from hentai import Hentai, Format
from hentai import Utils, Sort, Option, Tag

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
    values = random.sample(uwuse, k=1)
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
    values = lolisi()
    embed.set_image(url=values)
    author = ctx.author.mention
    await ctx.send(author, embed=embed)


@client.command()
async def konachan(ctx, tag: str):
    i = 0

    def tags():
        return tag

    def photos():
        tag = tags()

        textatg = "https://konachan.com/post?tags="
        textatg = textatg + tag
        imagess = rq.get(textatg)
        sopa = BeautifulSoup(imagess.text, "html.parser")
        links = []
        image5 = sopa.select('a[href^="https://konachan.com/jpeg"]')

        for img in image5:
            links.append(img['href'])

        values2 = random.choice(links)
        return values2

    while i < 3:
        embed = discord.Embed(
            title="Toma tu chica 7u7",
            colour=discord.Colour.red()
        )
        values = photos()
        embed.set_image(url=values)

        await ctx.send(embed=embed)

        i += 1


@client.group(name="nhentai")
async def nhentai(ctx):
    pass


@nhentai.command(name="tags")
async def tags_subcommand(ctx, tags: str):
    def photos():

        popo = "tag:" + tags
        links = []

        for doujin in Utils.search_all_by_query(query=popo, sort=Sort.PopularWeek):
            links.append(doujin.id)


        links2 = random.choice(links)


        return links2

    doujin2 = Hentai(photos())
    pog1 = doujin2.title(Format.Pretty)
    pog2 = photos()
    pog3 = [tag.name for tag in doujin2.tag]

    embed2 = discord.Embed(
        title=pog1,


        colour=discord.Colour.red()
    )
    embed2.add_field(name="id", value=pog2, inline=False)
    embed2.add_field(name="tags", value=", ".join(pog3), inline=False)
    await ctx.send(embed=embed2)



    doujin3 = doujin2.image_urls

    for x in doujin3:
        embed = discord.Embed(
            colour=discord.Colour.red()
        )



        embed.set_image(url=x)

        await ctx.send(embed=embed)



@nhentai.command(name="id")
async def id_subcommand(ctx, number: int):



    links2 = Hentai(number)
    pog1 = links2.title(Format.Pretty)
    pog3 = [tag.name for tag in links2.tag]

    embed2 = discord.Embed(
        title=pog1,


        colour=discord.Colour.red()
    )
    embed2.add_field(name="id", value=number.__str__(), inline=False)
    embed2.add_field(name="tags", value=", ".join(pog3), inline=False)
    await ctx.send(embed=embed2)

    doujin4 = links2.image_urls


    for x in doujin4:
        embed = discord.Embed(
            colour=discord.Colour.red()
        )

        embed.set_image(url=x)

        await ctx.send(embed=embed)


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
    embed.add_field(name="->Konachan", value="Photos 7u7", inline=False)
    await ctx.send(author, embed=embed)


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Game(name="uwu", url="https://thumbs.gfycat.com/ConcreteVibrantDalmatian-size_restricted.gif"))




client.run('token')

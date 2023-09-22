import re
from random import randint

from dotenv import load_dotenv

import os

import discord
from discord.ext import commands
load_dotenv()

config = {
    'token': os.getenv('TOKEN'),
    'prefix': '!',
}

wishes = [
    "Have a good time!:3",
    "May Luna guide you!UwU",
    "It'll be, as Pinkie once said: ''Appletastic'';3",
    "Stay safe, little pony^^",
    "And don't forget to enjoy upcoming night! It is going to be beautiful, i just know it!",
    "May all your dreams be sweet tonight!"
]
countries = [
    "Changeling Lands", "Equestria", "Kingdom of Olenia", "Stalliongrad", "Griffonian Empire,Kingdom of Wingbardy", "Kingdom of Aquileia", "River Republic", "Hippogriffia", "Arcturian Order", "Blackrock's Bandits", "Buffalo Chiefdom", "Barony of Rumare", "Barrad Magocracy", "City of Flowena", "County of Greifwald", "Crystal Empire", "Dread League", "Griffon Liberation Army", "Griffon Frontier", "Griffonian Republic", "Jaki-Clan", "Our Town", "Austurland", "Kingdom of Pingland", "Kingdom of Yakyakistan", "New Mareland", "Nova Griffonia", "Kása Free State", "House Avian", "Sunstriker Clan", "Skyfall Trade Federation", "Grand Duchy of Feathisia", "Flag of Falcorian Queendom Falcorian Queendom Flag of Barony of Arantiga Barony of Arantiga Flag of Bakaran Republic Bakaran Republic", "Lake City", "Diamond Mountain", "Nimbusia", "Kingdom of Wittenland", "Pònaidhean", "Gryphian Host", "Ordensstaat Hellquill", "County of Longsword", "Principality of Lushi", "Farbrook", "Firtree Villages", "Greneclyf", "Kingdom of Brodfeld", "Socialist Republic of Skynavia", "Kingdom of Vedina", "Federated Parishes of Sicameon", "County of Cyanolisia", "Republic of Asterion", "Free Towns of Gryphus", "Strawberry Duchy", "Barony of Angriver", "County of Bronzehill", "Greifenmarschen", "Katerin Principality", "Yale Rectorate", "Haukland", "Township of Fezera", "County of Francistria", "Duchy of Talouse", "Free City of Romau", "Celestial State", "Confederation of Southern States", "Disciples of the Night", "Aztlan Free State", "Lunar Empire", "Baltimare Republic", "Solar Empire", "Imperium Crystale", "Vanhoover Commune", "Las Pegasus", "Manehattan Protectorate", "Equestrian Liberation Front", "Republic of Tarrin"
]
reccomendStart = [
    "Oh, you should definitely watch ",
    "You want me to chose? Hee hee! Well, i think, you'll like ",
    "Hmmmm... te... no... seve... no no no... maybe... Oh, I know. Why don't you watch "
]
episodes = []
file = open('episodes.txt', 'r')
line = '_'
while(line):
    line = file.readline()
    line = line.replace('\n', '')
    episodes.append(line)
episodes.remove('')
print(episodes)



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

"""@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        await ctx.reply(ctx.content)"""

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.reply(f'Hello!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def mango(ctx): # Создаём функцию и передаём аргумент ctx.
    ctx.reply(f'EEEEEEEEEE!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.command()
async def roll(ctx, arg):
    if ((re.fullmatch(r'(\d+)?[dDкК]\d+', arg))):
        splited = re.findall(r'\d+', arg)
        if len(splited) == 1:
            await ctx.reply(f'{randint(1, int(splited[0]))}')
        else:
            times = int(splited[0])
            limit = int(splited[1])
            result = ''
            for i in range (0, times):
                result += str(randint(-11, limit)) + " "
            await ctx.reply(f'{result}')

@bot.command()
async def MLPrecommend(ctx):
    ep = randint(0, 220)
    s = 0
    name = episodes[ep]
    if ep >= 65:
        s += 3
        ep -= 65
    s += ep//26 + 1
    ep = ep%26 + 1
    tempName = name.replace(' ', '-')
    tempName = tempName.replace('(', '')
    tempName = tempName.replace(')', '')
    tempName = tempName.replace('!', '')
    tempName = tempName.replace(",", '')
    tempName = tempName.replace("'", '-')
    tempName = tempName.replace('"', '-')
    tempName = tempName.replace("---", '-')
    tempName = tempName.replace("--", '-')
    tempName = tempName.lower()
    link = "thedoctorteam.ru/project/mlp/season-" + str(s) + "/" + tempName + "/original"
    await ctx.reply(f"{reccomendStart[randint(0, len(reccomendStart)-1)]}{ep} episode of {s} season of My Little Pony:"
                    f" Friendship is Magic. It's title is ''{name}''. Here is a link for you: {link}."
                    f" {wishes[randint(0, len(wishes)-1)]}")
@bot.command()
async def coin(ctx):
    x = randint(1, 2)
    if x > 0:
        await ctx.reply("heads")
    else:
        await ctx.reply("tails")

@bot.command()
async def EaWCountryPick(ctx):
    n = randint(0, len(countries))
    await ctx.reply(f"I don't really like this game, but if you want... Well, you can play as countries[n]")
bot.run(config['token'])


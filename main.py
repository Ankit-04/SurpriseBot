import os
from typing import AnyStr
import imdb
from discord.ext import commands
import random
import asyncio
from dotenv import load_dotenv
from quoters import Quote
import randfacts


load_dotenv()
client = commands.Bot(command_prefix="-")
ia = imdb.IMDb()


@client.event
async def on_ready():
    print(f'{client.user} is connected')

@client.command()
async def hello(ctx):
    await ctx.send(f"```Hello {ctx.author},im the surprise bot, I have a bunch of features \nhere's a list of all of them to get you started: \n movie \n shows \n quote \n random fact \n book```")

@client.command()
async def movie(ctx):
    results = ia.get_top250_movies()
    index = random.randint(0,249)
    await ctx.send(f"{results[index]['title']}")

@client.command()
async def show(ctx):
    list_shows = [
        "Game of Thrones",
        "Breaking Bad",
        "TWD: The Walking Dead",
        "How I Met Your Mother",
        "Friends",
        "Sherlock",
        "Stranger Things",
        "The Big Band Theory",
        "Dexter",
        "True Detective",
        "Lost",
        "Prison Break",
        "House of Cards",
        "Black Mirror",
        "The Office",
        "House of Cards",
        "Family Guy"
    ]
    await ctx.send(random.choice(list_shows))
@client.command()
async def book(ctx):
    list_book = [
        "Coraline by Neil Gaiman",
        "The Color Purple: A Novel by Alice Walker",
        "The Collected of Edgar Allan Po by Edgar Allan Poe",
        "The Code of the Woosters by P.G. Wodehouse",
        "A Clockwork Orange by Anthony Burgess",
        "The Call of the Wild by Jack London",
        "Charlotte's Web by E. B White",
        "Charlie and the Chocolate Factory by Roald Dahl",
        "The Catcher in the Rye by J.D. Salinger",
        "Catch-22 by Joseph Heller",
        "The Brothers Karamazov by Fyodor Dostoevsky",
        "Brave New World by Aldous Huxley",
        "The Book Thief by Markus Zusak",
        "Beloved by Toni Morrison",
        "Adventures of Huckleberry Finn by Mark Twain",
        "The Adventures of Sherlock Holmes by Arthur Conan Doyle",
        "The Alchemist by Paulo Coelho",
        "The Aleph and Other Stories by Jorge Luis Borges",
        "Animal Farm by George Orwell",
        "The Aleph and Other Stories by Jorge Luis Borges",
        "Animal Farm by George Orwell",
        "Aesop's Fables by Aesop",
        "Alice's Adventures in Wonderland by Lewis Carroll",
        "Anna Karenina by Leo Tolstoy"
    ]
    await ctx.send(random.choice(list_book))

@client.command()
async def quote(ctx):
    await ctx.send(Quote.print())

@client.command()
async def fact(ctx):
    await ctx.send(randfacts.getFact(True))

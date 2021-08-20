from datetime import date, timedelta
import discord
import os
import yfinance as yf
import plotly.graph_objs as go
import plotly.express as px
import kaleido

Token = 'ODY2Mzg1NzgyNzc2Mzk3ODQ0.YPRyow.-6RjmaoIWV8t3PhjYMP2rDycT9A'
client = discord.Client()
dates = ["week", "month", "year", "decade"]


def get_figure(symbol,date1,date2):
    stock = yf.Ticker(symbol)
    old = stock.history(start=date1, end=date2)
    old = old.reset_index()
    for i in ['Open', 'High', 'Close', 'Low']:
        old[i] = old[i].astype('float64')

    fig = px.line(old, x="Date", y="Open ($)", title=(symbol.upper() + ' Stock Price Chart'))
    if not os.path.exists("images"):
        os.mkdir("images")
    fig.write_image("images/figure.png", engine="kaleido")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$tock'):
        words = message.content[6:]
        list_of_words = words.split()
        stock = list_of_words[0]
        if "week" in message.content:
            today = date.today() - timedelta(days=10)
            d1 = today.strftime("%Y-%m-%d")
            today = date.today() - timedelta(days=3)
            d2 = today.strftime("%Y-%m-%d")
            get_figure(stock, d1, d2)
            await message.channel.send(file=discord.File('images/figure.png'))
        elif "month" in message.content:
            today = date.today() - timedelta(days=33)
            d1 = today.strftime("%Y-%m-%d")
            today = date.today() - timedelta(days=3)
            d2 = today.strftime("%Y-%m-%d")
            get_figure(stock, d1, d2)
            await message.channel.send(file=discord.File('images/figure.png'))
        elif "year" in message.content:
            today = date.today() - timedelta(days=368)
            d1 = today.strftime("%Y-%m-%d")
            today = date.today() - timedelta(days=3)
            d2 = today.strftime("%Y-%m-%d")
            get_figure(stock, d1, d2)
            await message.channel.send(file=discord.File('images/figure.png'))
        elif "decade" in message.content:
            today = date.today() - timedelta(days=3653)
            d1 = today.strftime("%Y-%m-%d")
            today = date.today() - timedelta(days=3)
            d2 = today.strftime("%Y-%m-%d")
            get_figure(stock, d1, d2)
            await message.channel.send(file=discord.File('images/figure.png'))
        else:
            await message.channel.send("Did you remember to put a date interval?")


client.run(Token)

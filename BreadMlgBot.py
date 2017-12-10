import discord
import asyncio
import random
import requests
import io
import config
import safygiphy

client = discord.Client()
g = safygiphy.Giphy()
ownerid = "268093844791230464"

minutes = 0

@client.event
async def on_ready ():
    print('Bot On')
    print(client.user.name)
    print(client.user.id)
    print('charme')

@client.event
async def on_message(message):
    if message.content.startswith('-game') and message.author.id == ownerid:
        game = message.content[6:]
        await client.change_presence(game=discord.Game(name=game))
        await client.send_message(message.channel, "Game alterado com sucesso")

    if message.content.startswith('-teste'):
        await client.send_message(message.channel, "tf2 e melhor que cs")

    if message.content.startswith('-mlg'):
        response = requests.get("https://i.ytimg.com/vi/vvDqdDYVpuQ/maxresdefault.jpg", stream=True)
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='mlg.jpg', content='toma' )

    if message.content.startswith('-ajuda'):
        await client.send_message(message.channel, "Comandos -ajuda -coin -mlg")

    if message.content.startswith('-pao'):
        response = requests.get("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcST7XhTvxsJYEkxvXZiMMEkOEvmBgsMDp13merkQmZDcB0c0wBLUw", stream=True)
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='pao.jpg', content='Toma' )

    if message.content.startswith('-gif'):
        gif_tag = message.content[6:]
        rgif = g.random(tag=str(gif_tag))
        response = requests.get(
            str(rgif.get("data", []).get('image_original_url')), stream=True
        )
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='sla.gif', content='Ta ae seu gif')

    if message.content.startswith('-coin'):
        choice = random.randint(1,2)
        if choice == 1:
           await client.send_message(message.channel, "🌑 Cara")
    if choice == 2:
       await client.send_message(message.channel, "🌕 Coroa")

client.run(config.token)

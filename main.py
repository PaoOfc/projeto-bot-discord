import discord
import os

client = discord.Client()
token_discord = os.environ['DISCORD_TOKEN']


@client.event
async def on_ready():
    print('Estamos online como {0.user}. Exemplo'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('!kids-hello'):
      await message.channel.send('Hello!')
    
    if message.content.startswith('!kids-mensagem'):
      mensagem = str(message.content).replace('!kids-mensagem ', '')
      await message.channel.send(mensagem)

    if message.content.startswith('!kids-somar 2+2'):
      mensagem = str(message.content).replace('!kids-somar ', '')
      mensagem = mensagem.split('+')
      numero1 = int(mensagem[0])
      numero2 = int(mensagem[1])
      await message.channel.send(str(numero1+numero2))

client.run(token_discord)
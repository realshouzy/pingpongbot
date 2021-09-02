import discord
import os
import json
import random
import asyncio
from keep_alive import keep_alive

bot = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

@bot.event
async def ch_pr():
  await bot.wait_until_ready()

  statuses = [f"Ping Pong on {len(bot.guilds)} servers", "pp!help"]

  while not bot.is_closed():
 
    status = random.choice(statuses)
    await bot.change_presence(activity=discord.Game(name=status))
  
    await asyncio.sleep(5)
    print('Status changed')


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  if message.content.startswith('Ping'):
    await message.channel.send('Pong')
    print('Played Ping Pong')

  if message.content.startswith('ping'):
    await message.channel.send('Pong')
    print('Played ping Pong')

  if message.content.startswith('pp!help'):
    await message.channel.send('So the main function of this bot is to write "Pong" when you write "Ping"(or "ping"). It also has a few commands with the prefix "pp!", like "pp!ping" for the latency, "pp!invite" to get the invite link of the bot and "pp!vote" to get the vote link of the bot. You can also read the code if you want with "pp!code".')
    print('Stats sent')

  if message.content.startswith('pp!ping'):
    await message.channel.send(f'The ping is {round(bot.latency * 1000)}ms')
    print('Ping sent')
    
  if message.content.startswith('pp!invite'):
    await message.channel.send('Invite the bot to other server: https://discord.com/api/oauth2/authorize?client_id=831066967287791627&permissions=3072&scope=bot')
    print('Invitelink sent')

  if message.content.startswith('pp!stats'):
    await message.channel.send(f'Playing Ping Pong on {len(bot.guilds)} servers.')
    print('Stats sent')

  if message.content.startswith('pp!vote'):
    await message.channel.send('You can vote for the bot here: https://top.gg/bot/831066967287791627/vote')
    print('Votelink sent')

  if message.content.startswith('pp!website'):
    await message.channel.send('https://ping-pong-bot.shouzy.repl.co/')
    print('Websitelink sent')

  if message.content.startswith('pp!code'):
    await message.channel.send('You can finde the code here: https://gist.github.com/realshouzy/3ef3c7df753d2e8ce7db159f00cd0006')
    print('Codelink sent')
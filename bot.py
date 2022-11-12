import discord
from discord.ext import commands
from datetime import datetime
import random
import asyncio


client = commands.Bot(command_prefix='!')
client.remove_command("help")

TOKEN = ''

@client.command()
async def help(ctx):
    author = ctx.message.author 
     
    embed = discord.Embed(colour = discord.Colour.orange())


    embed.set_author(name='help')
    embed.add_field(name='!ping', value='returns pong')
    embed.add_field(name='!clear, !delete (+ number)', value='Clears amount of hat specified')

    await ctx.send(author, embed=embed)

alarm_time = '7.00'#24hrs



@client.event
async def on_ready():
    print('Bot Online.')

@client.command()
async def time_check(ctx):
    await client.wait_until_ready()
    while not client.is_closed:
        now = datetime.strftime(datetime.now(), '%H:%M')
        channel = ctx.channel
        messages = ('Test')
        if now == alarm_time:
           await ctx.send(channel, messages)
           time = 90
        else:
           time = 1
        await asyncio.sleep(time)

@client.command(alisas=['delete'])
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'{amount} messages deleted.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms.')

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')  
    
@client.event
async def on_member_join(member):
     print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
     print(f'{member} has left a server.')   

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['yes',
                 'no',
                 'Possibly',
                 'as i see it, yes.',
                 'ask again later.',
                 'my sources say no',
                 'most likely',
                 'my reply is no',
                 'withoud a  doubt',
                 'i sayt no is no',
                 'yes of course',
                 'you ask again',
                 'no sorry',
                 'I dont know',]
                 
    await ctx.send(f'question: {question}\nanswer: {random.choice(responses)}')

client.run(TOKEN)
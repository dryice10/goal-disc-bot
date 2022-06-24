# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 16:20:54 2022

@author: Yop
"""

import os
import socket
import struct
from discord.ext import commands

import nest_asyncio
nest_asyncio.apply()
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
print("DISCORD_GUILD variable was: "+ GUILD)

MOTD = "u playing jak?"
GPATH = r"c:\Users\Yop\source\repos\jak-project"

#
#Function definitions
#
def sendForm(form):
    header = struct.pack('<II', len(form), 10)
    clientSocket.sendall(header + form.encode())
    print("Sent: " + form)
    return



#
#Launch REPL, connect bot, and mi
#
os.system(r'start "'+ MOTD +'" /d '+GPATH+' task repl') #repl cmd window

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket.connect(("127.0.0.1", 8181))

data = clientSocket.recv(1024)
print(data.decode())

sendForm("(lt)")
sendForm("(mi)")

sendForm("(send-event *target* 'get-pickup (pickup-type eco-blue) 1.0)")



#
#
#DISCORD SETUP
#
#
COMMAND_ROLE = "Commands"

MOD_ROLE = "Mod"

PREFIX = "!"

#creates an instance of the Bot class, i imagine
bot = commands.Bot(command_prefix = PREFIX)

#
#COMMANDS
#
@bot.command(name="test")
@commands.has_role(COMMAND_ROLE)
async def test(ctx):
    #print('test command detected')
    if ctx.guild.name==GUILD:
        await ctx.send("test u")

@bot.command(name="rj")
@commands.has_role(COMMAND_ROLE)
async def rj(ctx):
    #print('rj command detected')
    if ctx.guild.name==GUILD:
        await ctx.send("rj u")

@bot.command(name="trip")
@commands.has_role(COMMAND_ROLE)
async def trip(ctx):
    if ctx.guild.name==GUILD:
        sendForm("(send-event *target* 'loading)")

@bot.command(name="redeco")
@commands.has_role(COMMAND_ROLE)
async def ecoRed(ctx):
    if ctx.guild.name==GUILD:
        sendForm("(send-event *target* 'get-pickup (pickup-type eco-red) 5.0)")

@bot.command(name="blueeco")
@commands.has_role(COMMAND_ROLE)
async def ecoBlue(ctx):
    if ctx.guild.name==GUILD:
        sendForm("(send-event *target* 'get-pickup (pickup-type eco-blue) 5.0)")

@bot.command(name="greeneco")
@commands.has_role(COMMAND_ROLE)
async def ecoGreen(ctx):
    if ctx.guild.name==GUILD:
        sendForm("(send-event *target* 'get-pickup (pickup-type eco-green) 5.0)")

@bot.command(name="yelloweco")
@commands.has_role(COMMAND_ROLE)
async def ecoYellow(ctx):
    if ctx.guild.name==GUILD:
        sendForm("(send-event *target* 'get-pickup (pickup-type eco-yellow) 5.0)")

@bot.command(name="absorb")
@commands.has_role(COMMAND_ROLE)
async def absorbDist(ctx, num: int):
    if ctx.guild.name==GUILD:
        num = str(num)
        sendForm("(set! (-> *FACT-bank* suck-suck-dist) (meters "+num+"))")
        sendForm("(set! (-> *FACT-bank* suck-bounce-dist) (meters "+num+"))")

@bot.command(name="timer")
@commands.has_role(COMMAND_ROLE)
async def timer(ctx):
    if ctx.guild.name==GUILD:
        sendForm("(test-timer)")


#this line actually runs the bot
bot.run(TOKEN)





####
'''
Examples:

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


'''
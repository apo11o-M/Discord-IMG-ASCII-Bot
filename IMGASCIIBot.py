# IMG Enhancer Bot.py

import os
import discord
import png_to_ascii
import numpy as np
from numpy import asarray


from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = "!")

helpList = "!enhance ___: do stuff"

@bot.event
async def on_ready():
    print("Program Start..")
    print(f'{bot.user.name} is connected')


@bot.command(name = 'asciify', help = helpList)
async def testing(ctx, img_address):

    response = "ASCIIFYing... This may take a while\n"
    result, width, height = png_to_ascii.convertImg(img_address)

    print(result)
    temp = ""
    for i in range(height):
        for j in range(width): 
            temp = temp + result[i][j]      
            # print(temp)  
            # print(result[i][j])
            # print("\n")
        temp += "\n"

    #await ctx.send(response)
    await ctx.send(temp)
    

bot.run(TOKEN)


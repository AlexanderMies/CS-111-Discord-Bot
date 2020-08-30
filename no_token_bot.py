import os
import discord
import random

# Token specifically for this CS 111 Bot, do not share, regen if comprimised
TOKEN = ('')

# Initialize an instance of bot client
client = discord.Client()

# Confirming bot is online via cmd prompt
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


# On-message event handler
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    bot_help = (
        "Hi I'm the CSC 111 Bot, here's a list of my commands: \n\n\n"
        "(!help) for this menu \n\n"
        "(!meet) for the date/time of zoom meetings \n\n"
        "(!contact) for Professor Santos' email \n\n"
        "(!blackboard) for a link to blackboard"
    )
       
    cs_111_meet = (
        'Our class meets from 9:30 to 11:45 EST on Wednesday \n and Friday for the Fall session'
    )

    contact_prof = (
        'You can reach the professor at josantos@bmcc.cuny.edu'
    )

    blackboard = (
        'Copy and paste this link for Blackboard: "rb.gy/wf3kgp"'
    )
    



    if message.content == '!meet':
        response = (cs_111_meet)
        await message.channel.send(response)
    
    elif message.content == '!contact':
        response = (contact_prof)
        await message.channel.send(response)   
    
    elif message.content == '!help':
        response = (bot_help)
        await message.channel.send(response)

    elif message.content == '!blackboard':
        response = (blackboard)
        await message.channel.send(response)
    
    elif message.content == 'raise-exception':
        raise discord.DiscordException


# Run the instance of client with unique Bot token
client.run(TOKEN)
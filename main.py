import os
import discord
from discord.ext import commands
import asyncio
from stay_on import alive


TOKEN = os.environ['TOKEN']

bot = commands.Bot(command_prefix="$")


success = discord.Embed(
                        title ='Successfully confessed',
                        description='Dil Khush ho gya?'
                     )
success.set_image(url="https://cdn.discordapp.com/attachments/944541869268951060/944622439684522024/Inko-kya-hi-pata-chalega.jpg")
success.set_footer(text="Do $confess in my DMs to confess")

@bot.event
async def on_ready():
  print("spilling all secrets")

@bot.command()
@commands.cooldown(2.0, 300.0, commands.BucketType.user)
async def confess(ctx,*args):
    
    if ctx.channel.type == discord.ChannelType.private:
        argcount = len(args)
        if argcount >= 1:
            
            message = (' '.join(args))
            #print(message)
            response = discord.Embed(
                        title ='New Confession!',
                        description=f'{message}'
                     )
            response.set_footer(text="Do $confess in my DMs to confess")
            channel = bot.get_channel(int(os.environ['CHANNEL']))
            await channel.send(embed=response)
            
            send = await ctx.send(embed=success)
                    
        else:
            response = discord.Embed(
              title ='Hue Hue Hue 🌚',
              description='What you want to confess?',
              colour = 0xc8a2c8
              )
            response.set_footer(text="It will timeout in 30 secs")
            response.set_thumbnail(url="https://cdn.discordapp.com/attachments/830822463611994142/944534656978665502/download.jpeg")
            send = await ctx.send(embed=response)
    
            try:
                
                confession = await bot.wait_for(
                        'message',
                        timeout=30,
                        check=lambda message: message.author == ctx.author
                    )
                
                if confession:
                    
                    response = discord.Embed(
                        title ='New Confession!',
                        description=f'{confession.content}'
                     )
                    response.set_footer(text="Do $confess in my DMs to confess")
                    channel = bot.get_channel(int(os.environ['CHANNEL']))
                    await channel.send(embed=response)
                    
                    
                    await ctx.send(embed=success)
            except asyncio.TimeoutError:
                message = discord.Embed(
                      title ='Try AGAIN',
                      colour = 0xc8a2c8
                      )
                message.set_footer(text="Bruhh restart")
                message.set_image(url="https://cdn.discordapp.com/attachments/944541869268951060/944595295780601907/Jaldi-Bol-Kal-Subah-Panvel-Nikalna-Hai-meme-template-of-Golmaal-3.jpg")
                await ctx.send(embed=message)
    else:
        message = discord.Embed(
          title ='zor zor se bol ke sabko scheme bata de!',
          description='If you confess in public, how the damn hell will that be anonymous?',
          colour = 0xc8a2c8
          )
        message.set_footer(text="are you mad or wot? next time try DM'ing me!")
        message.set_image(url="https://cdn.discordapp.com/attachments/94454186928951060/944596596056797224/download_1.jpeg")

        send = await ctx.send(embed=message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error , commands.CommandOnCooldown):
        message = discord.Embed(
          title ='Stop it get some help!',
          description='you are on a cooldown for {:.1f} mins'.format((error.retry_after)/60),
          colour = 0xc8a2c8
          )
        message.set_footer(text="Abe Padhai likhai karo IAS-YAS bano!")
        message.set_image(url="https://cdn.discordapp.com/attachments/946415206995746866/960491202510192640/stop.jpeg")
        send = await ctx.send(embed=message)
        
    

alive()
bot.run(TOKEN)

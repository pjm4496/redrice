import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


client = commands.Bot(command_prefix = '+')
client.remove_command("help")

@client.event
async def on_ready():
    print(f"{client.user} 서버에 연결되었습니다.")
    game = discord.Game("섹시재민 활동")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_member_join(member, guild):
  embed = discord.Embed(title="입 주 신 청", description="{member.mention} joined!")
  embed.set_footer(text="문의사항 : overrap#0071")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
  msg = await client.send_message(discord.Object(id="840364690990956557"),embed=embed)

@client.event
async def hello(ctx):
  await client.say("안녕")

@client.event
async def on_message(message):
      

      if message.content == "골플13":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 1동 3자리 남습니다.\n\nhttps://discord.gg/AA5YWEqjmv\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="골드🥇", inline=True)
        embed.add_field(name="최대티어", value="플레티넘🗿", inline=True)
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)


      if message.content == "골플12":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 1동 2자리 남습니다.\n\nhttps://discord.gg/AA5YWEqjmv\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="골드🥇", inline=True)
        embed.add_field(name="최대티어", value="플레티넘🗿", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "골플11":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 1동 1자리 남습니다.\n\nhttps://discord.gg/AA5YWEqjmv\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="골드🥇", inline=True)
        embed.add_field(name="최대티어", value="플레티넘🗿", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "골플23":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 2동 3자리 남습니다.경쟁 2동 \n\nhttps://discord.gg/KwnF2wuBtD\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="골드🥇", inline=True)
        embed.add_field(name="최대티어", value="플레티넘🗿", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "골플22":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 2동 2자리 남습니다.경쟁 2동 \n\nhttps://discord.gg/KwnF2wuBtD\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="골드🥇", inline=True)
        embed.add_field(name="최대티어", value="플레티넘🗿", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "골플21":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 2동 1자리 남습니다.경쟁 2동 \n\nhttps://discord.gg/KwnF2wuBtD\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="골드🥇", inline=True)
        embed.add_field(name="최대티어", value="플레티넘🗿", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "골플33":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 3동 3자리 남습니다.경쟁 3동 \n\nhttps://discord.gg/JPRgQYv5TU\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="골드🥇", inline=True)
        embed.add_field(name="최대티어", value="플레티넘🗿", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "골플32":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 3동 2자리 남습니다.경쟁 3동 \n\nhttps://discord.gg/JPRgQYv5TU\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="골드🥇", inline=True)
        embed.add_field(name="최대티어", value="플레티넘🗿", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "골플31":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 3동 1자리 남습니다.경쟁 3동 \n\nhttps://discord.gg/JPRgQYv5TU\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="골드🥇", inline=True)
        embed.add_field(name="최대티어", value="플레티넘🗿", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "실골33":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 3동 3자리 남습니다.경쟁 3동 \n\nhttps://discord.gg/JPRgQYv5TU\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="실버🥈", inline=True)
        embed.add_field(name="최대티어", value="골드🥇", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "실골32":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 3동 2자리 남습니다.경쟁 3동 \n\nhttps://discord.gg/JPRgQYv5TU\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="실버🥈", inline=True)
        embed.add_field(name="최대티어", value="골드🥇", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "실골31":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 3동 1자리 남습니다.경쟁 3동 \n\nhttps://discord.gg/JPRgQYv5TU\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="실버🥈", inline=True)
        embed.add_field(name="최대티어", value="골드🥇", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "실골23":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 2동 3자리 남습니다.경쟁 2동 \n\nhttps://discord.gg/KwnF2wuBtD\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="실버🥈", inline=True)
        embed.add_field(name="최대티어", value="골드🥇", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "실골22":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 2동 2자리 남습니다.경쟁 2동 \n\nhttps://discord.gg/KwnF2wuBtD\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="실버🥈", inline=True)
        embed.add_field(name="최대티어", value="골드🥇", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "실골21":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 2동 1자리 남습니다.경쟁 2동 \n\nhttps://discord.gg/KwnF2wuBtD\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="실버🥈", inline=True)
        embed.add_field(name="최대티어", value="골드🥇", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "실골13":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 1동 3자리 남습니다.\n\nhttps://discord.gg/AA5YWEqjmv\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="실버🥈", inline=True)
        embed.add_field(name="최대티어", value="골드🥇", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "실골12":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 1동 2자리 남습니다.\n\nhttps://discord.gg/AA5YWEqjmv\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="실버🥈", inline=True)
        embed.add_field(name="최대티어", value="골드🥇", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "실골11":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 1동 1자리 남습니다.\n\nhttps://discord.gg/AA5YWEqjmv\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="실버🥈", inline=True)
        embed.add_field(name="최대티어", value="골드🥇", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "브실13":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 1동 3자리 남습니다.\n\nhttps://discord.gg/AA5YWEqjmv\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="브론즈🥉", inline=True)
        embed.add_field(name="최대티어", value="실버🥈", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "브실12":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 1동 2자리 남습니다.\n\nhttps://discord.gg/AA5YWEqjmv\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="브론즈🥉", inline=True)
        embed.add_field(name="최대티어", value="실버🥈", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "브실11":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 1동 1자리 남습니다.\n\nhttps://discord.gg/AA5YWEqjmv\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="브론즈🥉", inline=True)
        embed.add_field(name="최대티어", value="실버🥈", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "브실23":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 2동 3자리 남습니다.\n\nhttps://discord.gg/KwnF2wuBtD\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="브론즈🥉", inline=True)
        embed.add_field(name="최대티어", value="실버🥈", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "브실22":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 2동 2자리 남습니다.\n\nhttps://discord.gg/KwnF2wuBtD\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="브론즈🥉", inline=True)
        embed.add_field(name="최대티어", value="실버🥈", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "브실21":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 2동 1자리 남습니다.\n\nhttps://discord.gg/KwnF2wuBtD\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="브론즈🥉", inline=True)
        embed.add_field(name="최대티어", value="실버🥈", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "브실33":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 3동 3자리 남습니다.\n\nhttps://discord.gg/JPRgQYv5TU\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="브론즈🥉", inline=True)
        embed.add_field(name="최대티어", value="실버🥈", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "브실32":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 3동 2자리 남습니다.\n\nhttps://discord.gg/JPRgQYv5TU\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="브론즈🥉", inline=True)
        embed.add_field(name="최대티어", value="실버🥈", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "브실31":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 3동 1자리 남습니다.\n\nhttps://discord.gg/JPRgQYv5TU\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="브론즈🥉", inline=True)
        embed.add_field(name="최대티어", value="실버🥈", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "플다13":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 1동 3자리 남습니다.\n\nhttps://discord.gg/AA5YWEqjmv\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="플레티넘🗿", inline=True)
        embed.add_field(name="최대티어", value="다이아💎", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "플다12":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 1동 2자리 남습니다.\n\nhttps://discord.gg/AA5YWEqjmv\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="플레티넘🗿", inline=True)
        embed.add_field(name="최대티어", value="다이아💎", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "플다11":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 1동 1자리 남습니다.\n\nhttps://discord.gg/AA5YWEqjmv\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="플레티넘🗿", inline=True)
        embed.add_field(name="최대티어", value="다이아💎", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)

      if message.content == "플다23":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 2동 3자리 남습니다.\n\nhttps://discord.gg/KwnF2wuBtD\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="플레티넘🗿", inline=True)
        embed.add_field(name="최대티어", value="다이아💎", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "플다22":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 2동 2자리 남습니다.\n\nhttps://discord.gg/KwnF2wuBtD\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="플레티넘🗿", inline=True)
        embed.add_field(name="최대티어", value="다이아💎", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "플다21":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 2동 1자리 남습니다.\n\nhttps://discord.gg/KwnF2wuBtD\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="플레티넘🗿", inline=True)
        embed.add_field(name="최대티어", value="다이아💎", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "플다33":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 3동 3자리 남습니다.\n\nhttps://discord.gg/JPRgQYv5TU\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="플레티넘🗿", inline=True)
        embed.add_field(name="최대티어", value="다이아💎", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "플다32":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 3동 2자리 남습니다.\n\nhttps://discord.gg/JPRgQYv5TU\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="플레티넘🗿", inline=True)
        embed.add_field(name="최대티어", value="다이아💎", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "플다31":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 3동 1자리 남습니다.\n\nhttps://discord.gg/JPRgQYv5TU\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        embed.add_field(name="최소티어", value="플레티넘🗿", inline=True)
        embed.add_field(name="최대티어", value="다이아💎", inline=True)
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)


      if message.content == "배치13":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 1동 3자리 남습니다.\n\nhttps://discord.gg/AA5YWEqjmv\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
       
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "배치12":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 1동 2자리 남습니다.\n\nhttps://discord.gg/AA5YWEqjmv\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
       
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "배치11":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 1동 1자리 남습니다.\n\nhttps://discord.gg/AA5YWEqjmv\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)

      if message.content == "배치23":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 2동 3자리 남습니다.\n\nhttps://discord.gg/KwnF2wuBtD\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "배치22":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 2동 2자리 남습니다.\n\nhttps://discord.gg/KwnF2wuBtD\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
       
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "배치21":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 2동 1자리 남습니다.\n\nhttps://discord.gg/KwnF2wuBtD\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "배치33":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 3동 3자리 남습니다.\n\nhttps://discord.gg/JPRgQYv5TU\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "배치32":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 3동 2자리 남습니다.\n\nhttps://discord.gg/JPRgQYv5TU\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        
        
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "배치31":
        embed = discord.Embed(title="입 영 통 지 서", description="𝐑𝐀𝐍𝐊 3동 1자리 남습니다.\n\nhttps://discord.gg/JPRgQYv5TU\n위 링크를 누르면 입장합니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078817292582952/7cba6a99e8cf555c.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      


      if message.content == "빠참13":
        embed = discord.Embed(title="입 영 통 지 서", description="𝗥𝗔𝗡𝗗𝗢𝗠 1동 3자리 남습니다.\n\nhttps://discord.gg/MJTTxWEhNt\n위 링크를 누르면 입장합니다.", color=0x00FFFF)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078880752795648/39f0d39c87ea91c1.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "빠참12":
        embed = discord.Embed(title="입 영 통 지 서", description="𝗥𝗔𝗡𝗗𝗢𝗠 1동 2자리 남습니다.\n\nhttps://discord.gg/MJTTxWEhNt\n위 링크를 누르면 입장합니다.", color=0x00FFFF)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078880752795648/39f0d39c87ea91c1.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "빠참11":
        embed = discord.Embed(title="입 영 통 지 서", description="𝗥𝗔𝗡𝗗𝗢𝗠 1동 1자리 남습니다.\n\nhttps://discord.gg/MJTTxWEhNt\n위 링크를 누르면 입장합니다.", color=0x00FFFF)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078880752795648/39f0d39c87ea91c1.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)

      if message.content == "빠참23":
        embed = discord.Embed(title="입 영 통 지 서", description="𝗥𝗔𝗡𝗗𝗢𝗠 2동 3자리 남습니다.\n\nhttps://discord.gg/fmShTphejx\n위 링크를 누르면 입장합니다.", color=0x00FFFF)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078880752795648/39f0d39c87ea91c1.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "빠참22":
        embed = discord.Embed(title="입 영 통 지 서", description="𝗥𝗔𝗡𝗗𝗢𝗠 2동 2자리 남습니다.\n\nhttps://discord.gg/fmShTphejx\n위 링크를 누르면 입장합니다.", color=0x00FFFF)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078880752795648/39f0d39c87ea91c1.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
     
      if message.content == "빠참21":
        embed = discord.Embed(title="입 영 통 지 서", description="𝗥𝗔𝗡𝗗𝗢𝗠 2동 1자리 남습니다.\n\nhttps://discord.gg/fmShTphejx\n위 링크를 누르면 입장합니다.", color=0x00FFFF)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078880752795648/39f0d39c87ea91c1.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "빠참33":
        embed = discord.Embed(title="입 영 통 지 서", description="𝗥𝗔𝗡𝗗𝗢𝗠 3동 3자리 남습니다.\n\nhttps://discord.gg/ZBukgahTN7\n위 링크를 누르면 입장합니다.", color=0x00FFFF)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078880752795648/39f0d39c87ea91c1.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "빠참32":
        embed = discord.Embed(title="입 영 통 지 서", description="𝗥𝗔𝗡𝗗𝗢𝗠 3동 2자리 남습니다.\n\nhttps://discord.gg/ZBukgahTN7\n위 링크를 누르면 입장합니다.", color=0x00FFFF)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078880752795648/39f0d39c87ea91c1.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "빠참31":
        embed = discord.Embed(title="입 영 통 지 서", description="𝗥𝗔𝗡𝗗𝗢𝗠 3동 1자리 남습니다.\n\nhttps://discord.gg/ZBukgahTN7\n위 링크를 누르면 입장합니다.", color=0x00FFFF)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078880752795648/39f0d39c87ea91c1.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)



      if message.content == "배틀13":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴮᴬᵀᵀᴸᴱ ʀᴏʏᴀʟ 1동 3자리 남습니다.\n\nhttps://discord.gg/zA9XhxUetr\n위 링크를 누르면 입장합니다.", color=0xFF9900)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078877123411979/01c788a76c2d98d7.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "배틀12":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴮᴬᵀᵀᴸᴱ ʀᴏʏᴀʟ 1동 2자리 남습니다.\n\nhttps://discord.gg/zA9XhxUetr\n위 링크를 누르면 입장합니다.", color=0xFF9900)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078877123411979/01c788a76c2d98d7.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "배틀11":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴮᴬᵀᵀᴸᴱ ʀᴏʏᴀʟ 1동 1자리 남습니다.\n\nhttps://discord.gg/zA9XhxUetr\n위 링크를 누르면 입장합니다.", color=0xFF9900)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078877123411979/01c788a76c2d98d7.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)

      if message.content == "배틀23":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴮᴬᵀᵀᴸᴱ ʀᴏʏᴀʟ 2동 3자리 남습니다.\n\nhttps://discord.gg/4UnTMPZR68\n위 링크를 누르면 입장합니다.", color=0xFF9900)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078877123411979/01c788a76c2d98d7.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "배틀22":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴮᴬᵀᵀᴸᴱ ʀᴏʏᴀʟ 2동 2자리 남습니다.\n\nhttps://discord.gg/4UnTMPZR68\n위 링크를 누르면 입장합니다.", color=0xFF9900)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078877123411979/01c788a76c2d98d7.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
     
      if message.content == "배틀21":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴮᴬᵀᵀᴸᴱ ʀᴏʏᴀʟ 2동 1자리 남습니다.\n\nhttps://discord.gg/4UnTMPZR68\n위 링크를 누르면 입장합니다.", color=0xFF9900)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078877123411979/01c788a76c2d98d7.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "배틀33":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴮᴬᵀᵀᴸᴱ ʀᴏʏᴀʟ 3동 3자리 남습니다.\n\nhttps://discord.gg/QWkMHFN5VA\n위 링크를 누르면 입장합니다.", color=0xFF9900)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078877123411979/01c788a76c2d98d7.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "배틀32":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴮᴬᵀᵀᴸᴱ ʀᴏʏᴀʟ 3동 2자리 남습니다.\n\nhttps://discord.gg/QWkMHFN5VA\n위 링크를 누르면 입장합니다.", color=0xFF9900)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078877123411979/01c788a76c2d98d7.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      
      if message.content == "배틀31":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴮᴬᵀᵀᴸᴱ ʀᴏʏᴀʟ 3동 1자리 남습니다.\n\nhttps://discord.gg/QWkMHFN5VA\n위 링크를 누르면 입장합니다.", color=0xFF9900)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078877123411979/01c788a76c2d98d7.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)



      if message.content == "미니13":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴹᴵᴺᴵ ʀᴏʏᴀʟ 1동 3자리 남습니다.\n\nhttps://discord.gg/64tYfunUZu\n위 링크를 누르면 입장합니다.", color=0xF4CCCC)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078878696538152/6597878616541428.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "미니12":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴹᴵᴺᴵ ʀᴏʏᴀʟ 1동 2자리 남습니다.\n\nhttps://discord.gg/64tYfunUZu\n위 링크를 누르면 입장합니다.", color=0xF4CCCC)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078878696538152/6597878616541428.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "미니11":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴹᴵᴺᴵ ʀᴏʏᴀʟ 1동 1자리 남습니다.\n\nhttps://discord.gg/64tYfunUZu\n위 링크를 누르면 입장합니다.", color=0xF4CCCC)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078878696538152/6597878616541428.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "미니23":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴹᴵᴺᴵ ʀᴏʏᴀʟ 2동 3자리 남습니다.\n\nhttps://discord.gg/FZtEjKkGkj\n위 링크를 누르면 입장합니다.", color=0xF4CCCC)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078878696538152/6597878616541428.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "미니22":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴹᴵᴺᴵ ʀᴏʏᴀʟ 2동 2자리 남습니다.\n\nhttps://discord.gg/FZtEjKkGkj\n위 링크를 누르면 입장합니다.", color=0xF4CCCC)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078878696538152/6597878616541428.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "미니21":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴹᴵᴺᴵ ʀᴏʏᴀʟ 2동 1자리 남습니다.\n\nhttps://discord.gg/FZtEjKkGkj\n위 링크를 누르면 입장합니다.", color=0xF4CCCC)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078878696538152/6597878616541428.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "미니33":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴹᴵᴺᴵ ʀᴏʏᴀʟ 3동 3자리 남습니다.\n\nhttps://discord.gg/PSFADYpkQY\n위 링크를 누르면 입장합니다.", color=0xF4CCCC)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078878696538152/6597878616541428.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "미니32":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴹᴵᴺᴵ ʀᴏʏᴀʟ 3동 2자리 남습니다.\n\nhttps://discord.gg/PSFADYpkQY\n위 링크를 누르면 입장합니다.", color=0xF4CCCC)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078878696538152/6597878616541428.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "미니31":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴹᴵᴺᴵ ʀᴏʏᴀʟ 3동 1자리 남습니다.\n\nhttps://discord.gg/PSFADYpkQY\n위 링크를 누르면 입장합니다.", color=0xF4CCCC)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078878696538152/6597878616541428.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "미니43":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴹᴵᴺᴵ ʀᴏʏᴀʟ 4동 3자리 남습니다.\n\nhttps://discord.gg/58fHZm3wgP\n위 링크를 누르면 입장합니다.", color=0xF4CCCC)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078878696538152/6597878616541428.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "미니42":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴹᴵᴺᴵ ʀᴏʏᴀʟ 4동 2자리 남습니다.\n\nhttps://discord.gg/58fHZm3wgP\n위 링크를 누르면 입장합니다.", color=0xF4CCCC)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078878696538152/6597878616541428.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "미니41":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴹᴵᴺᴵ ʀᴏʏᴀʟ 4동 1자리 남습니다.\n\nhttps://discord.gg/58fHZm3wgP\n위 링크를 누르면 입장합니다.", color=0xF4CCCC)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078878696538152/6597878616541428.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "미니53":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴹᴵᴺᴵ ʀᴏʏᴀʟ 5동 3자리 남습니다.\n\nhttps://discord.gg/QDtahME4Bg\n위 링크를 누르면 입장합니다.", color=0xF4CCCC)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078878696538152/6597878616541428.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "미니52":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴹᴵᴺᴵ ʀᴏʏᴀʟ 5동 2자리 남습니다.\n\nhttps://discord.gg/QDtahME4Bg\n위 링크를 누르면 입장합니다.", color=0xF4CCCC)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078878696538152/6597878616541428.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "미니51":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴹᴵᴺᴵ ʀᴏʏᴀʟ 5동 1자리 남습니다.\n\nhttps://discord.gg/QDtahME4Bg\n위 링크를 누르면 입장합니다.", color=0xF4CCCC)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078878696538152/6597878616541428.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "미니63":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴹᴵᴺᴵ ʀᴏʏᴀʟ 6동 3자리 남습니다.\n\nhttps://discord.gg/c4W5NEeHtv\n위 링크를 누르면 입장합니다.", color=0xF4CCCC)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078878696538152/6597878616541428.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "미니62":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴹᴵᴺᴵ ʀᴏʏᴀʟ 6동 2자리 남습니다.\n\nhttps://discord.gg/c4W5NEeHtv\n위 링크를 누르면 입장합니다.", color=0xF4CCCC)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078878696538152/6597878616541428.gif")
        await message.channel.send("@here".format(message.author.mention))
        await message.channel.send(embed=embed)
      if message.content == "미니61":
        embed = discord.Embed(title="입 영 통 지 서", description="ᴹᴵᴺᴵ ʀᴏʏᴀʟ 6동 1자리 남습니다.\n\nhttps://discord.gg/c4W5NEeHtv\n위 링크를 누르면 입장합니다.", color=0xF4CCCC)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840078878696538152/6597878616541428.gif")
        await message.channel.send(f"@everyone 연우추천 스쿼드!")
        await message.channel.send(embed=embed)
      
      if message.content == "/구인명령어":
        embed = discord.Embed(title="구인 명령어", description="[원하는 모드'방번호','구인수']\n\n배틀\n미니\n빠참\n경쟁(배치,브실,실골,골플,플다)\n\nex.)\n 빠참13 = 빠른참가모드 1동 3명 구한다.\n    골플13 = 경쟁전 골드~플레티넘까지 1동 3명 구한다.", color=0xF4CCCC)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809743575906517033/840104010429628446/redrice.gif")
        await message.channel.send(f"{message.author.mention}님 숙지하기로 약속~★")
        await message.channel.send(embed=embed)





access_token = os.environ['BOT_TOKEN']
client.run('BOT_TOKEN')

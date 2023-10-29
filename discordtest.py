import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is connected to the Discord!')

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel is not None: 
        # '한섭 일반 만들기' 채널에 들어갔을 때
        if after.channel.name == '한섭 일반 만들기': 
            n = 1
            while True:
                if discord.utils.get(member.guild.channels, name=f'한섭 일반 {n}') is None: 
                    break
                n += 1
            category = discord.utils.get(member.guild.categories, name='📍𝐕𝐎𝐈𝐂𝐄  (𝐋𝐢𝐯𝐞 O 관전 O)')
            channel = await member.guild.create_voice_channel(name=f'한섭 일반 {n}', category=category) 
            await member.move_to(channel) 

        # '한섭 경쟁 만들기' 채널에 들어갔을 때
        elif after.channel.name == '한섭 경쟁 만들기': 
            n = 1
            while True:
                if discord.utils.get(member.guild.channels, name=f'한섭 경쟁 {n}') is None: 
                    break
                n += 1
            category = discord.utils.get(member.guild.categories, name='📍𝐕𝐎𝐈𝐂𝐄  (𝐋𝐢𝐯𝐞 O 관전 O)')
            channel = await member.guild.create_voice_channel(name=f'한섭 경쟁 {n}', category=category) 
            await member.move_to(channel)

        # '아섭 일반 만들기' 채널에 들어갔을 때
        elif after.channel.name == '아섭 일반 만들기': 
            n = 1
            while True:
                if discord.utils.get(member.guild.channels, name=f'아섭 일반 {n}') is None: 
                    break
                n += 1
            category = discord.utils.get(member.guild.categories, name='📍𝐕𝐎𝐈𝐂𝐄  (𝐋𝐢𝐯𝐞 O 관전 O)')
            channel = await member.guild.create_voice_channel(name=f'아섭 일반 {n}', category=category) 
            await member.move_to(channel)

        # '아섭 경쟁 만들기' 채널에 들어갔을 때
        elif after.channel.name == '아섭 경쟁 만들기': 
            n = 1
            while True:
                if discord.utils.get(member.guild.channels, name=f'아섭 경쟁 {n}') is None: 
                    break
                n += 1
            category = discord.utils.get(member.guild.categories, name='📍𝐕𝐎𝐈𝐂𝐄  (𝐋𝐢𝐯𝐞 O 관전 O)')
            channel = await member.guild.create_voice_channel(name=f'아섭 경쟁 {n}', category=category) 
            await member.move_to(channel)

        # '수다방 만들기' 채널에 들어갔을 때
        elif after.channel.name == '수다방 만들기': 
            n = 1
            while True:
                if discord.utils.get(member.guild.channels, name=f'수다방 {n}') is None: 
                    break
                n += 1
            category = discord.utils.get(member.guild.categories, name='📍𝐕𝐎𝐈𝐂𝐄  (𝐋𝐢𝐯𝐞 O 관전 O)')
            channel = await member.guild.create_voice_channel(name=f'수다방 {n}', category=category) 
            await member.move_to(channel) 

        # '기타 게임 만들기' 채널에 들어갔을 때
        elif after.channel.name == '기타 게임 만들기': 
            n = 1
            while True:
                if discord.utils.get(member.guild.channels, name=f'기타 게임 {n}') is None: 
                    break
                n += 1
            category = discord.utils.get(member.guild.categories, name='📍𝐕𝐎𝐈𝐂𝐄  (𝐋𝐢𝐯𝐞 O 관전 O)')
            channel = await member.guild.create_voice_channel(name=f'기타 게임 {n}', category=category) 
            await member.move_to(channel)

    if before.channel is not None: 
        # '한섭 일반 n' 채널에서 나갔을 때
        if '한섭 일반 ' in before.channel.name and before.channel.name != '한섭 일반 만들기' and len(before.channel.members) == 0: 
            await before.channel.delete() 

        # '한섭 경쟁 n' 채널에서 나갔을 때
        elif '한섭 경쟁 ' in before.channel.name and before.channel.name != '한섭 경쟁 만들기' and len(before.channel.members) == 0: 
            await before.channel.delete()

        # '아섭 일반 n' 채널에서 나갔을 때
        elif '아섭 일반 ' in before.channel.name and before.channel.name != '아섭 일반 만들기' and len(before.channel.members) == 0: 
            await before.channel.delete()

        # '아섭 경쟁 n' 채널에서 나갔을 때
        elif '아섭 경쟁 ' in before.channel.name and before.channel.name != '아섭 경쟁 만들기' and len(before.channel.members) == 0: 
            await before.channel.delete()

         # '수다방 n' 채널에서 나갔을 때
        elif '수다방 ' in before.channel.name and before.channel.name != '수다방 만들기' and len(before.channel.members) == 0: 
            await before.channel.delete() 

        # '기타 게임 n' 채널에서 나갔을 때
        elif '기타 게임 ' in before.channel.name and before.channel.name != '기타 게임 만들기' and len(before.channel.members) == 0: 
            await before.channel.delete()

bot.run('MTE2ODA5NDUwNzA0OTQyNzAwNA.GjuXml.hSq_OHig44TCXczsHHx7yzk_QWUu5oKbi5kgY4')

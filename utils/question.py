import discord 
import asyncio 
from utils import config
from discord.utils import get
import json

async def go_message(client, message):
    if message.guild is None:
        messages = []
        if message.content == "!문의도움":
            embed = discord.Embed(title='문의봇 명령어 안내', color=0x50bcdf)
            embed.add_field(name="문의종료 방법", value='```!문의종료```',inline=False)
            await message.channel.send(embed=embed)
        elif message.content == "!문의종료":
            if isinstance(message.channel, discord.channel.DMChannel):
                print('1')
                guild_main = client.get_guild(int(config.config('id')))
                category = get(guild_main.categories, id=int(config.config('id')))
                channel = await guild_main.create_text_channel(message.author.name, category=category)
                print('2')
                for i in messages:
                    await channel.send(i)
                embed = discord.Embed(title='종료', description="체크 아이콘을 눌러 답변을 시작합니다",color=0x50bcdf)
                check = await channel.send(embed=embed)
                if message.author.id not in config.user_data('user_data'):
                    data2 = None
                    with open("datas/user_data.json", 'w', encoding='utf-8 sig') as file:
                        data = {
                            f"{check}":{
                                "user": message.author,
                                'answering': False
                            }
                        }
                        fiel.update(data)
                        json.dump(data, file)
                    with open("datas/user_data.json", 'r', encoding='utf-8 sig') as file2:
                        data2 = file2.load()
                    with open("datas/user_data.json", 'w', encoding='utf-8 sig') as write2:
                        data2 = data2['check_messages'].append(check)
                        json.dump(data2,write2)
                await check.add_reaction('✅')
        else:
            messages.append(message.content)

async def resend_message(message):
    with open("datas/user_data.json", 'r', encoding='utf-8 sig') as file2:
        data2 = file2.load()
        if data2[message] is not None:
            data2[message]['answering'] = True

async def resend_save(message):
    with open("datas/user_data.json", 'r', encoding='utf-8 sig') as file2:
        data2 = file2.load()
        for i in data2['check_messages']:
            if message.channel.id in data2[i]:
                a = open("datas/answers.json", 'r', encoding='utf-8 sig')
                bb = a.load()
                a.close()
                with open("datas/answers.json", 'w', encoding='utf-8 sig')as write3:
                    if i in bb:
                        for b in bb:
                            if b == i:
                                bb[b]['answer'] = message.content
                                json.dump(bb,write3)
                    else:
                        data33={
                            f"{i}":{
                                "answer": message.content                          
                            }
                        }
                        bb.append(data33)
                        json.dump(bb,write3)

async def resend(message):
    with open("datas/user_data.json", 'r', encoding='utf-8 sig') as file2:
        data2 = file2.load()
        for i in data2['check_messages']:
            if message.channel.id in data2[i]:
                a = open("datas/answers.json", 'r', encoding='utf-8 sig')
                bb = a.load()
                a.close()
                with open("datas/answers.json", 'w', encoding='utf-8 sig')as write3:
                    if i in bb:
                        for b in bb:
                            if b == i:
                                embed = discord.Embed(title='답변 도착', description=b['answer'],color=0x50bcdf)
                                i['user'].send()
                                bb.pop(b)
                                json.dump(bb,write3)
                                a = open("../datas/user_data.json", 'w', encoding='utf-8 sig')
                                data2.pop(i)
                                json.dump(data2,a)
                                a.close()


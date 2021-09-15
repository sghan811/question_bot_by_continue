from utils import config
from utils import black as black_control
from utils import question
import discord
from os import system

intents = discord.Intents.all()
client = discord.Client(Intents=intents)


@client.event
async def on_ready():
    system('cls')
    print("준비 완료")

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    elif message.author.id in config.black_user('black_user'):
        await message.reply(embed=discord.Embed(title="블랙리스트 등용자", description="사용 불가"))
    elif message.channel.id in config.user_data('user_data'):
        await question.resend_save(message)
    elif message.content == "!답변종료":
        await question.resned(message)
    else:
        await question.go_message(client,message)
@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "✅":
        message1 = config.config('user-data')
        if reaction.message in message1['check_messages']:
            await question.resend_message(reaction.message)

client.run(config.config("token"))
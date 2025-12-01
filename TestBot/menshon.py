import os
from dotenv import load_dotenv
from discord.ext import commands
import discord

load_dotenv()
token = os.getenv("HELLO_TEST_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents) 

VOICE_CHANNEL_NAME = "一般"

@bot.event
async def on_ready():
    print(f'{bot.user} がログインしました！')

@bot.command(name='vc-ping')
async def vc_ping_command(ctx):
    # ctx はコマンドのコンテキスト（メッセージ、チャンネル、ギルドの情報を含む）
    guild = ctx.guild
    
    # ... (ボイスチャンネル取得とメンション処理はそのまま)
    voice_channel = discord.utils.get(guild.voice_channels, name=VOICE_CHANNEL_NAME)
    
    if not voice_channel:
        await ctx.send("そのボイスチャンネルが見つかりません。")
        return

    members = voice_channel.members
    if len(members) == 0:
        await ctx.send("ボイスチャンネルに誰もいません。")
        return

    mentions = " ".join(member.mention for member in members)
    await ctx.send(f"VCにいる人: {mentions}")

# client.run(token) の代わりに
bot.run(token)
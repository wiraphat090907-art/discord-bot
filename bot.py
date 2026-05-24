import nextcord
from nextcord.ext import commands
import os

intents = nextcord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)

SERVER_ID = 1434589749926035520
VOICE_CHANNEL_ID = 1478411164672200844

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Streaming(
        name="BOT",
        url="https://www.twitch.tv/doidoi"
    ))
    guild = bot.get_guild(SERVER_ID)
    vc = nextcord.utils.get(guild.channels, id=VOICE_CHANNEL_ID)
    await guild.change_voice_state(channel=vc, self_mute=False, selfdeaf=True)
    print(f'✅ บอทพร้อมแล้ว: {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send(f'🏓 Pong! {round(bot.latency * 1000)}ms')

bot.run(os.environ["DISCORD_TOKEN"])

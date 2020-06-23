from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='.')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def z(ctx):
    await ctx.send(':poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop:')
    await ctx.send(':poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop:')
    await ctx.send(':poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop:')
    await ctx.send(':poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop:')
    await ctx.send(':poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop:')
    await ctx.send(':poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop:')
    await ctx.send(':poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop:')
    await ctx.send(':poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop:')
    await ctx.send(':poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop:')
    await ctx.send(':poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop::poop: 何優天然:poop:')
    
@client.event
async def on_voice_state_update(member, before):
     await member.send('誰かがボイスチャンネルに接続したよ')

bot.run(token)

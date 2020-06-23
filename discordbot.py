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
    await ctx.send('何優天然')
    
@bot.command()
async def (ctx):
    await ctx.send('test')

bot.run(token)

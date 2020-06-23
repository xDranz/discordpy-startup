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
     await ctx.send('ボイスチャンネルに接続したよ')
        
@client.event
async def on_message(ctx):
   if ctx.author.bot:　　　　　　　　　　　　　　　
       return #発言者がBOTなら無視
   if message.content == 'test_bot':　　　　 #発言に返信する
       await ctx.channel.send('呼んだ?') #返信内容は''で括る。

bot.run(token)

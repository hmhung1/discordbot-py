import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot đã sẵn sàng! Đăng nhập dưới tên: {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def hello(ctx):
    await ctx.send('Chào bạn!')

@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    embed = discord.Embed(title=f'Thông tin người dùng: {member.name}', color=0x00ff00)
    embed.add_field(name='ID', value=member.id)
    embed.add_field(name='Tên người dùng', value=member.name)
    embed.add_field(name='Tình trạng', value=member.status)
    embed.set_thumbnail(url=member.avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def serverinfo(ctx):
    embed = discord.Embed(title='Thông tin server', color=0x00ff00)
    embed.add_field(name='Tên server', value=ctx.guild.name)
    embed.add_field(name='ID server', value=ctx.guild.id)
    embed.add_field(name='Số thành viên', value=ctx.guild.member_count)
    embed.add_field(name='Ngày tạo', value=ctx.guild.created_at.strftime('%d/%m/%Y'))
    embed.set_thumbnail(url=ctx.guild.icon.url)
    await ctx.send(embed=embed)

bot.run('YOUR_BOT_TOKEN')

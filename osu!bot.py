import discord
from discord.ext import commands
import aiosqlite
import aiohttp

# Configure intents
intents = discord.Intents.default()
intents.messages = True  # Ensure that message events are enabled

# Create an instance of a bot with a command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Your Google Sheet link
google_sheet_link = 'YOUR_TOURNEY_SHEET_LINK'

# osu! API key (replace with your actual API key)
osu_api_key = 'YOUR_OSU_API_KEY'  # Replace with your actual API key

@bot.event
async def on_ready():
    # Create or connect to the SQLite database
    async with aiosqlite.connect('osu_profiles.db') as db:
        # Create a table to store user profiles if it doesn't exist
        await db.execute('''CREATE TABLE IF NOT EXISTS profiles (
            user_id INTEGER PRIMARY KEY,
            osu_link TEXT,
            osu_username TEXT
        )''')
        await db.commit()
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')

async def fetch_osu_profile(username):
    url = f'https://osu.ppy.sh/api/get_user?k={osu_api_key}&u={username}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            if data and isinstance(data, list):
                user_id = data[0]['user_id']
                profile_link = f'https://osu.ppy.sh/users/{user_id}'
                return profile_link, username
            return None, None

@bot.command(name='link')
@commands.cooldown(1, 30, commands.BucketType.user)
async def link(ctx, username: str):
    profile_link, valid_username = await fetch_osu_profile(username)
    if profile_link:
        user_id = ctx.author.id
        async with aiosqlite.connect('osu_profiles.db') as db:
            # Check if the osu! username is already linked to another user
            async with db.execute('SELECT user_id FROM profiles WHERE osu_username = ?', (valid_username,)) as cursor:
                row = await cursor.fetchone()
                if row and row[0] != user_id:
                    await ctx.send(f'The osu! username "{valid_username}" is already linked to another Discord account.')
                    return
            # Link the osu! profile to the current user
            await db.execute('''INSERT OR REPLACE INTO profiles (user_id, osu_link, osu_username) VALUES (?, ?, ?)''',
                             (user_id, profile_link, valid_username))
            await db.commit()
        await ctx.send(f'{ctx.author.mention}, your osu! profile has been linked successfully: {profile_link}')
    else:
        await ctx.send(f'{ctx.author.mention}, osu! profile for username "{username}" not found. Please check the username and try again.')

@bot.command(name='unlink')
@commands.cooldown(1, 60, commands.BucketType.user)
async def unlink(ctx):
    user_id = ctx.author.id
    async with aiosqlite.connect('osu_profiles.db') as db:
        await db.execute('DELETE FROM profiles WHERE user_id = ?', (user_id,))
        await db.commit()
    await ctx.send(f'{ctx.author.mention}, your osu! profile has been unlinked.')

@bot.command(name='osu')
@commands.cooldown(1, 5, commands.BucketType.user)
async def osu(ctx):
    user_id = ctx.author.id
    async with aiosqlite.connect('osu_profiles.db') as db:
        async with db.execute('SELECT osu_link FROM profiles WHERE user_id = ?', (user_id,)) as cursor:
            row = await cursor.fetchone()
            if row:
                osu_link = row[0]
                embed = discord.Embed(title='Osu Profile', description=f'[Click here to view the profile]({osu_link})', color=discord.Color.blue())
                await ctx.send(embed=embed)
            else:
                await ctx.send(f'{ctx.author.mention}, you have not linked your osu! profile yet. Use `!link <osu_username>` to link it.')

@bot.command(name='sheet')
@commands.cooldown(1, 5, commands.BucketType.user)
async def sheet(ctx):
    embed = discord.Embed(title='Google Sheet', description=f'[Click here to view the sheet]({google_sheet_link})', color=discord.Color.blue())
    await ctx.send(embed=embed)

@bot.command(name='commands')
async def commands_list(ctx):
    embed = discord.Embed(
        title='Command List',
        description='Here are the available commands:',
        color=discord.Color.blue()
    )
    embed.add_field(name='!sheet', value='Displays a link to the tournament history sheet.', inline=False)
    embed.add_field(name='!unlink', value='Unlinks your osu! profile from your Discord account.', inline=False)
    embed.add_field(name='!link <osu_username>', value='Links your osu! profile to your Discord account.', inline=False)
    embed.add_field(name='!osu', value='Displays a link to your linked osu! profile.', inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Command on cooldown. Try again in {error.retry_after:.1f} seconds.", delete_after=10)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument.", delete_after=10)
    else:
        print(f"Error in {ctx.command}: {error}")

# Run the bot with your token
bot.run('YOUR_BOT_TOKEN')  # Replace with your actual bot token

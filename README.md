# osu! Discord Bot

A Discord bot for managing osu! profiles and linking them to Discord accounts. This bot allows users to link their osu! usernames and retrieve their profile links directly within Discord.

## Features

- Link osu! profiles to Discord accounts
- Retrieve and display linked osu! profiles
- Unlink osu! profiles
- Display a link to a Google Sheet with tournament history

## Requirements

- Python 3.11
- `discord.py` library
- `aiosqlite` library
- `aiohttp` library

## Setting Up Your Discord Bot

1. **Create a Discord application**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Click on the "New Application" button.
   - Give your application a name and click "Create".

2. **Create a bot**:
   - In your application settings, go to the "Bot" tab on the left sidebar.
   - Click the "Add Bot" button, then confirm by clicking "Yes, do it!".
   - Your bot is created! Here you can see your bot token.

3. **Get your bot token**:
   - Under the "Bot" tab, click on "Reset Token" to get a new token. Copy this token, as you'll need it to run your bot.

4. **Invite your bot to a server**:
   - Go to the "OAuth2" tab.
   - Under "Scopes", select the `bot` checkbox.
   - Under "Bot Permissions", select the permissions your bot will need (e.g., `Send Messages`, `Read Message History`).
   - Copy the generated URL and paste it into your browser to invite your bot to your Discord server.

## Getting Your osu! API Key

1. **Create an osu! account**:
   - Go to the [osu! website](https://osu.ppy.sh/) and create an account if you don't have one.

2. **Get your API key**:
   - Visit your [osu! API key page](https://osu.ppy.sh/home/account/edit) while logged in.
   - Copy your API key from the "API Key" section.

## Google Sheet Setup

1. **Create a Google Sheet**:
   - Go to [Google Sheets](https://sheets.google.com) and create a new sheet.
   - Set up your sheet as needed for your tournament history.
   - [Link](https://docs.google.com/spreadsheets/d/1hlngeWJaxbcC499_V0Yo2mcit6aaMAGq7Vcnq0dc4Lk/edit?usp=sharing) to my personal sheet.

2. **Get the shareable link**:
   - Click on the "Share" button in the top right corner of the Google Sheets page.
   - Set the sharing permissions to "Anyone with the link" can view, then copy the link.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/benjaminzhang121/osu-discord.git
   cd osu-discord
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required libraries**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables**:
   Create a `.env` file in the project root and add the following:
   ```plaintext
   DISCORD_TOKEN=YOUR_BOT_TOKEN
   GOOGLE_SHEET_LINK=YOUR_TOURNEY_SHEET_LINK
   OSU_API_KEY=YOUR_OSU_API_KEY
   ```
   You can also simply replace the values in the bot.py file itself.

5. **Run the bot**:
   ```bash
   python bot.py  # Replace with your bot's filename if it's different
   ```

## Usage

- Use `!link <osu_username>` to link your osu! profile.
- Use `!unlink` to unlink your osu! profile.
- Use `!osu` to retrieve your linked osu! profile.
- Use `!sheet` to display the link to the tournament history sheet.
- Use `!commands` to list all available commands.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [discord.py](https://discordpy.readthedocs.io/en/stable/) for the Discord API wrapper.
- [aiohttp](https://docs.aiohttp.org/en/stable/) for asynchronous HTTP requests.
- [aiosqlite](https://aiosqlite.omnilib.dev/en/latest/) for asynchronous SQLite database access.

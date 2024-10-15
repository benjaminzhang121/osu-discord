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

4. **Run the bot**:
   ```bash
   python bot.py  # Replace with your bot's filename if it's different
   ```

## Usage

- Use `!link <osu_username>` to link your osu! profile.
- Use `!unlink` to unlink your osu! profile.
- Use `!osu` to retrieve your linked osu! profile.
- Use `!sheet` to display the link to the tournament history sheet.
- Use `!commands` to list all available commands.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [discord.py](https://discordpy.readthedocs.io/en/stable/) for the Discord API wrapper.
- [aiohttp](https://docs.aiohttp.org/en/stable/) for asynchronous HTTP requests.
- [aiosqlite](https://aiosqlite.omnilib.dev/en/latest/) for asynchronous SQLite database access.

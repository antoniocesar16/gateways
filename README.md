# Cyberspace bot

This source serves as a base for Cyberspace store bots.
It aims to be as modular as possible, allowing adding new features with minor effort.

## Example config file

```python
# Your Telegram bot token.
BOT_TOKEN = "1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Telegram API ID and Hash. This is NOT your bot token and shouldn't be changed.
API_ID = 611335
API_HASH = "d524b414d21f4d37f08684c1df41ac9c"

# Chat used for logging errors.
LOG_CHAT = -1001567213817

# Chat used for logging user actions (like buy, gift, etc).
ADMIN_CHAT = -1001567213817

# How many updates can be handled in parallel.
# Don't use high values for low-end servers.
WORKERS = 20

# Admins can access panel and add new materials to the bot.
ADMINS = [1089910057]

# Sudoers have full access to the server and can execute commands.
SUDOERS = [1089910057]

# All sudoers should be admins too
ADMINS.extend(SUDOERS)

GIFTERS = []
```

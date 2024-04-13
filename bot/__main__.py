import asyncio
from bot import Bot, Ubot

Bot.start()
Ubot.start()

loop = asyncio.get_event_loop()
loop.run_forever()

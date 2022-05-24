import asyncio
import time


class Connection:
    async def connect(self) -> None:
        print("Connecting")
        #time.sleep(1)
        await asyncio.sleep(1)
        print("Connected")
    async def disconnect(self) -> None:
        print("Disconnecting")
        #time.sleep(1)
        await asyncio.sleep(1)
        print("Disconnected")
    async def send_message(self, message: str) -> None:
        print("Sending message")
        #time.sleep(1)
        await asyncio.sleep(1)
        print(f"You send \"{message}\"")
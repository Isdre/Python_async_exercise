import asyncio
import time


class Connection:
    def connect(self) -> None:
        print("Connecting")
        time.sleep(1)
        #await asyncio.sleep(1)
        print("Connected")
    def disconnect(self) -> None:
        print("Disconnecting")
        time.sleep(1)
        #await asyncio.sleep(1)
        print("Disconnected")
    def send_message(self, message: str) -> None:
        print("Sending message")
        time.sleep(1)
        #await asyncio.sleep(1)
        print(f"You send \"{message}\"")
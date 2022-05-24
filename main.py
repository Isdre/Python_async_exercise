import aiohttp
import asyncio
import time
import connect
import string

M = string.ascii_lowercase

async def main() -> None:
    print("START")
    c = connect.Connection()
    await c.connect()
    await asyncio.gather(*[c.send_message(a) for a in M])
    await c.disconnect()
    print("END")

print("Timer started...")
start = time.time()
if __name__ == "__main__":
    asyncio.run(main())

end = time.time()
total_time = end - start
print("Timer stopped")
print(f"Total time: {total_time}")#3.028290033340454
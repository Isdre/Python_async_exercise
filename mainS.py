import aiohttp
import asyncio
import time
import connectS
import string

M = string.ascii_lowercase

def main() -> None:
    print("START")
    c = connectS.Connection()
    c.connect()
    for a in M:
        c.send_message(a)
    c.disconnect()
    print("END")

print("Timer started...")
start = time.time()
if __name__ == "__main__":
    main()

end = time.time()
total_time = end - start
print("Timer stopped")
print(f"Total time: {total_time}")#28.147026538848877
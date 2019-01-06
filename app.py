import asyncio
import serial_asyncio
import aiohttp

from settings import config

session = aiohttp.ClientSession()
loop = asyncio.get_event_loop()


async def post_data(data):
    post_data = {
        "data": data.decode().strip(),
        "machine": config.machine_id,
        "port": config.serial_port,
    }
    async with session.post(config.endpoint, data=post_data) as resp:
        print("hitting endpoint")
        print(resp.status)
        print(await resp.text())


class Output(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        print("port opened", transport)

    def data_received(self, data):
        print("data received", repr(data))
        loop.create_task(post_data(data))
        if b"\n" in data:
            self.transport.close()

    def connection_lost(self, exc):
        print("port closed")
        self.transport.loop.stop()


serial_monitor = serial_asyncio.create_serial_connection(
    loop, Output, config.serial_port, baudrate=config.baud
)
loop.run_until_complete(serial_monitor)
loop.run_forever()
loop.close()

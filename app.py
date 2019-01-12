import asyncio
import serial_asyncio
import aiohttp

from settings import config

session = aiohttp.ClientSession()
loop = asyncio.get_event_loop()

valid_commands = ["U"]  # User


def validateScan(data):
    if str(data).startswith(config.magic_str):
        if data[len(config.magic_str)] in valid_commands:
            return True
    return False


def parse_scan(data):
    command = data[len(config.magic_str)]
    payload = data[len(config.magic_str) + 1 :]
    return command, payload


async def post_data(data):
    data = data.decode().strip()

    if not validateScan(data):
        print(f"Got invalid scan data {data}")
        return

    command, payload = parse_scan(data)

    post_data = {
        "data": {
            "command": command,
            "payload": payload,
            "machine": config.machine_id,
            "port": config.serial_port,
            "api_key": config.api_key,
        }
    }
    async with session.post(config.endpoint, json=post_data) as resp:
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

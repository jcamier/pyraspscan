import asyncio
import serial_asyncio
import aiohttp

endpoint = 'http://localhost:8000/scan'

session = aiohttp.ClientSession()
loop = asyncio.get_event_loop()

async def post_data(data):
    post_data = {'data':data.decode()}
    async with session.post(endpoint, data=post_data) as resp:
        print('hitting endpoint')
        print(resp.status)
        print(await resp.text())

class Output(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        print('port opened', transport)
        transport.serial.rts = False  # You can manipulate Serial object via transport
        transport.write(b'Hello, World!\n')  # Write serial data via transport

    def data_received(self, data):
        print('data received', repr(data))
        loop.create_task(post_data(data))
        if b'\n' in data:
            self.transport.close()

    def connection_lost(self, exc):
        print('port closed')
        self.transport.loop.stop()

    def pause_writing(self):
        print('pause writing')
        print(self.transport.get_write_buffer_size())

    def resume_writing(self):
        print(self.transport.get_write_buffer_size())
        print('resume writing')

coro = serial_asyncio.create_serial_connection(loop, Output, '/dev/ttyACM0', baudrate=115200)
loop.run_until_complete(coro)
loop.run_forever()
loop.close()

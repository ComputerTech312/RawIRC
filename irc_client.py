import asyncio
import aioconsole

class IRCClient:
    def __init__(self, server, port):
        self.server = server
        self.port = port

    async def connect(self):
        try:
            self.reader, self.writer = await asyncio.open_connection(self.server, self.port)
        except Exception as e:
            from exceptions import ConnectionFailedException
            raise ConnectionFailedException(self.server, self.port, e)

    async def recv_messages(self):
        while True:
            try:
                line = await self.reader.readline()
                line = line.decode().strip()
                print(line)

                # Respond to PING messages from the server to avoid being disconnected
                if line.startswith("PING"):
                    response = f"PONG {line.split()[1]}\r\n"
                    self.writer.write(response.encode())
                    await self.writer.drain()
            except Exception as e:
                from exceptions import MessageReceiveException
                raise MessageReceiveException(e)

    async def send_messages(self):
        while True:
            try:
                message = await aioconsole.ainput(">")
                self.writer.write(f"{message}\r\n".encode())
                await self.writer.drain()
            except Exception as e:
                from exceptions import MessageSendException
                raise MessageSendException(e)

    async def run(self):
        await self.connect()
        await asyncio.gather(self.recv_messages(), self.send_messages())

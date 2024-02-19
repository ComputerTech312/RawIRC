import asyncio
import aioconsole
import sys

class IRCClient:
    def __init__(self, server, port):
        self.server = server
        self.port = port

    async def connect(self):
        try:
            self.reader, self.writer = await asyncio.open_connection(self.server, self.port)
        except Exception as e:
            print(f"Failed to connect to {self.server}:{self.port} - {str(e)}")
            sys.exit(1)

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
                print(f"Failed to receive message: {str(e)}")

    async def send_messages(self):
        while True:
            try:
                message = await aioconsole.ainput(">")
                self.writer.write(f"{message}\r\n".encode())
                await self.writer.drain()
            except Exception as e:
                print(f"Failed to send message: {str(e)}")

    async def run(self):
        await self.connect()
        await asyncio.gather(self.recv_messages(), self.send_messages())

# Check if command line arguments were provided
if len(sys.argv) < 3:
    print("Usage: python raw.py <server> <port>")
    sys.exit(1)

try:
    server = sys.argv[1]
    port = int(sys.argv[2])
except ValueError:
    print("Port must be an integer.")
    sys.exit(1)
except Exception as e:
    print(f"Failed to parse command line arguments: {str(e)}")
    sys.exit(1)

client = IRCClient(server, port)
asyncio.run(client.run())

import asyncio
import sys
from irc_client import IRCClient
from exceptions import ConnectionFailedException, MessageReceiveException, MessageSendException, InvalidPortException, CommandLineArgumentException

# Check if command line arguments were provided
if len(sys.argv) < 3:
    print("Usage: python main.py <server> <port>")
    sys.exit(1)

try:
    server = sys.argv[1]
    port = int(sys.argv[2])
except ValueError:
    raise InvalidPortException()
except Exception as e:
    raise CommandLineArgumentException(e)

client = IRCClient(server, port)
try:
    asyncio.run(client.run())
except (ConnectionFailedException, MessageReceiveException, MessageSendException) as e:
    print(str(e))
    sys.exit(1)

class ConnectionFailedException(Exception):
    def __init__(self, server, port, original_exception):
        self.message = f"Failed to connect to {server}:{port} - {str(original_exception)}"
        super().__init__(self.message)

class MessageReceiveException(Exception):
    def __init__(self, original_exception):
        self.message = f"Failed to receive message: {str(original_exception)}"
        super().__init__(self.message)

class MessageSendException(Exception):
    def __init__(self, original_exception):
        self.message = f"Failed to send message: {str(original_exception)}"
        super().__init__(self.message)

class InvalidPortException(Exception):
    def __init__(self):
        self.message = "Port must be an integer."
        super().__init__(self.message)

class CommandLineArgumentException(Exception):
    def __init__(self, original_exception):
        self.message = f"Failed to parse command line arguments: {str(original_exception)}"
        super().__init__(self.message)

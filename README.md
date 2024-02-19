# IRC Client

This is a simple IRC client implemented in Python using asyncio and aioconsole. It allows you to connect to an IRC server and send/receive messages.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7 or higher

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ComputerTech312/RawIRC.git
    cd RawIRC
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv rawirc
    ```

3. Activate the virtual environment:
    ```bash
    source rawirc/bin/activate
    ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the IRC client, run the following command:

```bash
python rawirc.py <server> <port>

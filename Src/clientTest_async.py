from pymodbus.client.tcp import AsyncModbusTcpClient
from pymodbus.exceptions import ModbusIOException
import asyncio
import logging

"""Logging Setup"""
logging.basicConfig()
_logger = logging.getLogger(__file__)
_logger.setLevel("DEBUG")

"""Setup Defaults"""
default_ip = '127.0.0.1'
default_port = 502


# def setup_async_client():
#     client = AsyncModbusTcpClient('127.0.0.1', port=502)
#     return client

def setup_async_client(ip: str = default_ip, port: int = default_port):
    client = AsyncModbusTcpClient(ip, port=port)
    return client


async def run_async_client(client, modbus_calls=None):
    """Run sync client."""
    _logger.info("### Client starting")
    await client.connect()
    assert client.connected
    if modbus_calls:
        return await modbus_calls(client)
    client.close()
    _logger.info("### End of Program")


async def read_input_register(client):
    """Test connection works."""
    try:
        rr = await client.read_input_registers(0, 1)
        # assert rr.registers[0] == 150
        # print(rr.registers[0])
        return rr.registers[0]
        # return rr.registers[0]
    except ModbusIOException:
        pass


# async def output_register(register):
#     return register[0]


async def read_from_server(setup_client=setup_async_client(), call=None):
    """Combine setup and run."""
    return await run_async_client(setup_client, modbus_calls=call)


# client = setup_async_client('127.0.0.1', 502)
"""Assigning function object to operation and passing entire function
This will give flexibility when wanting to do a different type of operation
such as write from client"""
# operation = read_input_register

# if __name__ == "__main__":
#     asyncio.run(read_from_server(client, operation), debug=True)  # pragma: no cover

if __name__ == "__main__":
    asyncio.run(read_from_server(), debug=True)  # pragma: no cover

#
# if __name__ == "__main__":
#     asyncio.run(read_from_server(), debug=True)  # pragma: no cover

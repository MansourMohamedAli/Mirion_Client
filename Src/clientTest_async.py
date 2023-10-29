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


def setup_async_client(ip: str = default_ip, port: int = default_port):
    return AsyncModbusTcpClient(ip, port=port)


async def run_async_client(client, modbus_calls=None):
    """Run sync client."""
    _logger.info("### Client starting")
    await client.connect()
    if client.connected is True:
        if modbus_calls:
            return await modbus_calls(client)
    else:
        client.close()
        _logger.info("### End of Program")
        return 0


    # assert client.connected, 'Client not connected'
    # if modbus_calls:
    #     return await modbus_calls(client)
    # client.close()
    # _logger.info("### End of Program")


async def read_input_register(client):
    """Test connection works."""
    try:
        rr = await client.read_input_registers(0, 1)
    except ModbusIOException as e:
        _logger.error(e)
        return 1000
    else:
        """If try is successful"""
        return rr.registers[0]


async def read_from_server(setup_client=setup_async_client(), call=None):
    """Combine setup and run."""
    # return await run_async_client(setup_client, modbus_calls=call)
    return await run_async_client(setup_client, modbus_calls=call)


"""Assigning function object to operation and passing entire function
This will give flexibility when wanting to do a different type of operation
such as write from client"""
# client = setup_async_client('127.0.0.1', 502)
# operation = read_input_register


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # asyncio.run(read_from_server(client, operation), debug=True)  # pragma: no cover
    asyncio.run(read_from_server(), debug=True)  # pragma: no cover

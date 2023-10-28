# import asyncio
#
# import Mirion as mir
# import clientTest_async as mbc  # mbc = modbus client
#
# client = mbc.setup_async_client('127.0.0.1', 502)
# operation = mbc.read_input_register
#
#
# async def main():
#     # loop = asyncio.get_event_loop()
#     # loop.create_task(mir.run_mirion())
#     # loop.create_task(mbc.read_from_server(client, operation))
#     # loop.run_forever()
#
#     task1 = asyncio.create_task(mir.run_mirion())
#     task2 = asyncio.create_task(mbc.read_from_server(client, operation))
#     await asyncio.gather(task1, task2)
#
# asyncio.run(main())

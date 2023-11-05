# import asyncio
# import time
# import threading
# import concurrent.futures
# from clientTest_async import read_from_server, setup_async_client, write_regs
# from Mirion import run_mirion
#
# client = setup_async_client('127.0.0.1', 502)
# operation = write_regs
#
# start = time.perf_counter()
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#
#
# def start_client():
#     asyncio.run(read_from_server(client, operation), debug=True)  # pragma: no cover
#
#
# def start_mirion():
#     asyncio.run(run_mirion(), debug=True)  # pragma: no cover
#
#
# # with concurrent.futures.ThreadPoolExecutor() as executor:
# #     f1 = executor.submit(start_client)
# #     f2 = executor.submit(start_mirion)
#
#
# """We can't pass in do_someting(seconds) because that will execute the function,
# # Instead I need to pass in args=[seconds]"""
#
# t1 = threading.Thread(target=start_client)
# t2 = threading.Thread(target=start_mirion)
#
# t1.start()
# t2.start()
#
# # t1.join()
# # t2.join()
#
# finish = time.perf_counter()
#
# print(f'Time:{finish - start}')

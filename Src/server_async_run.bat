cd C:\Python\Modbus\VirtualEnv\Scripts
call activate.bat

cd C:\Python\Modbus\src
python server_async_Example.py -c tcp -f socket -l debug -p 502 --store sequential

pause
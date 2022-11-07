import os
from signal import pause
import can
import time

# print("OS start ", os.system('sudo ip link set can0 up type can bitrate 125000 dbitrate 8000000 restart-ms 1000 berr-reporting on fd on'))
# can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
# print(can0)
# print("can0 initial ", can0)

time.sleep(1.0)

# bus = can.Bus(channel='can0', interface='socketcan')
# message = bus.recv(1.0)  # Timeout in seconds.

# if message is None:
#     print('Timeout occurred, no message.')
# else:
#     print("CAN device detected")
#     msg = can0.recv(1.0)
#     print("can0 message ", msg)
#     print(hex(msg.arbitration_id))

# time.sleep(5.0)
os.system('sudo ifconfig can0 down')

baudRates = [10, 125000, 250000] #, 20, 33.333, 40, 47.619, 50, 83.333, 92.238, 100, 125, 200, 250, 500, 800, 1000] 

for i in baudRates:
    os.system('sudo ip link set can0 up type can bitrate %s dbitrate 8000000 restart-ms 1000 berr-reporting on fd on' % (i))
    # print("Test i = ", i)
    print("OS Start - i = ",i, os.system('sudo ip link set can0 up type can bitrate %s dbitrate 8000000 restart-ms 1000 berr-reporting on fd on' % (i)))
    
    try:
        bus = can.Bus(channel='can0', interface='socketcan')
        message = bus.recv(1.0)  # Timeout in seconds. 
        if message != None:
            can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
            print("CAN device detected")
            msg = can0.recv(1.0)
            print("can0 message ", msg)
            print(hex(msg.arbitration_id))
            time.sleep(2.0)
            print(msg.data)
            os.system('sudo ifconfig can0 down')
            break
        else:
            exit()
    except NameError:    
        if message is None:
            # os.system('sudo ip link set can0 up type can bitrate %s dbitrate 8000000 restart-ms 1000 berr-reporting on fd on', i)
            print('Timeout occurred, no message.')
        else:
            can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
            print("CAN device detected")
            msg = can0.recv(1.0)
            print("can0 message ", msg)
            print(hex(msg.arbitration_id))
    except:
        print("terawer")




print("OS stop ", os.system('sudo ifconfig can0 down'))
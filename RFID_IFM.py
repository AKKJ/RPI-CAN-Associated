import os
from signal import pause
import can
import time


time.sleep(1.0)
os.system('sudo ifconfig can0 down')

# baudRates = [5, 10, 20, 33.333, 40, 47.619, 50, 83.333, 92.238, 100, 125, 200, 250, 500, 800, 1000] # Error: argument "33333.0" is wrong: invalid "bitrate" value
# baudRates = [5, 10, 20, 33, 40, 47, 50, 83, 92, 100, 125, 200, 250, 500, 800, 1000] 
baudRates = [100, 125, 200, 250]

for i in baudRates:
    i = i*1000
    time.sleep(1.0)
    os.system('sudo ip link set can0 up type can bitrate %s dbitrate 8000000 restart-ms 1000 berr-reporting on fd on' % (i))
    
    try:
        bus = can.Bus(channel='can0', interface='socketcan')
        message = bus.recv(1.0)  # Timeout in seconds. 
        if (message.arbitration_id == 1824): #(message != None) and
            print("Baud rate found = ", i , "kbit/s")
            can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
            print("CAN device detected")
            msg = can0.recv(1.0)       
            print("can0 message ", msg)
            print(hex(msg.arbitration_id))
            time.sleep(1.0)
            print(type(msg.data))
            if (msg.data == b'\x7f'):
                print("message")
                # os.system('sudo cansend can0 000#01.20')
                msgData = can.Message(is_extended_id=False, arbitration_id=0x000, data=[0x05]) 
                # print(msgData)
                bus.send(msgData)
                time.sleep(0.1)
                print(msg.data)
            print(msg.data)
            time.sleep(1.0)
            os.system('sudo ifconfig can0 down')
            break
        else:
            exit()
    except NameError:    
        if message is None:
            print('Timeout occurred, no message.')
    except:
        print("Baud rate = ", i , "kbit/s")
        os.system('sudo ifconfig can0 down')




print("OS stop ", os.system('sudo ifconfig can0 down'))
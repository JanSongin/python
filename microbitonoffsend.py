#You need to install the pyserial package to use the serial ports
import serial
import serial.tools.list_ports as list_ports
import time
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

cred = credentials.Certificate("C:/Users/Jan/Documents/test-dc64b-firebase-adminsdk-7jnbj-4f16c3e5d3.json")#might need changes
firebase_admin.initialize_app(cred,{'databaseURL': 'https://test-dc64b-default-rtdb.europe-west1.firebasedatabase.app/'})

PID_MICROBIT = 516
VID_MICROBIT = 3368
TIMEOUT = 0.1


def find_comport(pid, vid, baud):
    ''' return a serial port '''
    ser_port = serial.Serial(timeout=TIMEOUT)
    ser_port.baudrate = baud
    ports = list(list_ports.comports())
    print('scanning ports')
    for p in ports:
        if (p.pid == pid) and (p.vid == vid):
            print('found target device pid: {} vid: {} port: {}'.format(
                p.pid, p.vid, p.device))
            ser_port.port = str(p.device)
            return ser_port
    return None



print('looking for microbit')
ser_micro = find_comport(PID_MICROBIT, VID_MICROBIT, 115200)
if not ser_micro:
    print('microbit not found')
else:    
    ser_micro.open()
    source = "Home"
    ref = db.reference().child('light_log')
    while True:
        data = str(ser_micro.readline().decode('utf-8'))
        data = data.replace(" ","")
        data = data.replace("\r\n","")
        if (data == "1"):
            data = "On"
        elif(data == "0"):
            data = "Off"
        #else:
            #print("Error")  
        #print(data)
        if data.isalpha():
            print(data)
            ref.update({str(int(time.time())):{'On or Off':data, 'Location':source}})
        #else:
            #print("No data :(")
        #time.sleep(0.1)
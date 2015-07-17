from pymongo import MongoClient
import serial, time, signal, re

client = MongoClient('mongodb://localhost:9000/users')
db = client.users
col = db.rssi

def main():
    port_name = "/dev/ttyACM0"
    baud_rate = 115200
    
    # Creat serial port objects
    ser = serial.Serial(port=port_name, baudrate=baud_rate, timeout=1)
    ser.flushInput()
    ser.flushOutput()
    
    while(1):
        string = ser.readline()
        #print string
        hello = string.split()
        print hello[:1]
        col.update(
                {"name":hello[:1]},
                {
                    "$set": {"rssi":hello[1:]}
                },
                upsert = True
        )

if __name__ == '__main__':
    main()

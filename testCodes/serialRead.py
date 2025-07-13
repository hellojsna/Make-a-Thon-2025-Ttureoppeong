import serial

ser = serial.Serial(
    port='/dev/cu.HC-06',
    baudrate=9600,
)

while True:
    if ser.readable():
        print(ser.read().decode(), end='')
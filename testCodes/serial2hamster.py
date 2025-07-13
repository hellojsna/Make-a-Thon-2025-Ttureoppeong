from roboid import *
import serial

from serial.tools import list_ports
ports = list_ports.comports()
print("Available ports:")
for port in ports:
    print(port.device)

port_index = int(input("사용할 포트 index를 입력하세요: "))
port = ports[port_index].device

ser = serial.Serial(
    port=port,
    baudrate=9600,
)

while True:
    if ser.readable():
        readValue = ser.readline().decode().strip()
        print(readValue)
        if float(readValue) > 500.0:
            break

h=Hamster()
wait_until_ready()
while h.left_proximity() < 30 and h.right_proximity() < 30:

    h.wheels(60)

    wait(20)

h.stop()

h.note(60)
wait(20)
h.note(0)
h.wheels(-60)
from roboid import *
import subprocess
import time


while True: # 햄스터봇이 이동할 때까지 반복
    try:
        result = subprocess.run(
            ["curl", "-s", "--max-time", "10", "http://192.168.4.1/api/getLevelSensor"], # ESP8266 SoftAP에 연결된 상태에서 cURL을 사용하여 수위 센서 값을 가져옴
            capture_output=True, text=True
        )
        if result.returncode == 0: # cURL이 성공적으로 실행되었으면
            value = float(result.stdout.strip())
            if value > 200 and value < 500:
                print("")
            elif value > 500: # 감지된 수위가 500 이상이면 루프를 종료
                break
        else:
            print("cURL error:", result.stderr) # cURL 응답 오류
    except Exception as e:
        print("Error fetching sensor value:", e) # cURL 실행 오류
    time.sleep(1)

h = Hamster()
wait_until_ready() # 햄스터봇이 준비될 때까지 대기
while h.left_proximity() < 60 and h.right_proximity() < 60: # 장애물을 감지할 때까지

    h.wheels(60) # 앞으로 이동
    wait(20)

h.stop() # 정지

# TODO: 원위치로 복귀 구현
# wait(500)
# h.wheels(-60)
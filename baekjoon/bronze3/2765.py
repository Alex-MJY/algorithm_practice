# 지름, 회전수, 시간이 공백으로 구분
# 지름은 inch단위의 실수이며, 회전수는 정수이다. 시간은 초단위의 실수
# 입력은 회전수가 0이면 끝난다. 실수는 소수점 셋째자리이하까지 주어진다.
# 총거리(miles)와 평균 속도를 출력


counter = 0
while True:
    diameter, spin, time = map(float, input().split())
    if spin == 0:
        break
    distance = diameter / 63360 * 3.1415927 * spin
    total_time = distance / (time / 3600)
    
    counter += 1
    print(f"Trip #{counter}: {distance:.2f} {total_time:.2f}")
     

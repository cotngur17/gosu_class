T = int(input())


# i : 정류장 번호, 단계
# cnt : 현재 i번 정류장까지 오는데 충전 ㅎ ㅚㅅ수
def drive(i, cnt):
    global min_cnt
    # 1. 기저 조건(종료 조건)
    # 마지막 정류장
    # 마지막 정류장 뒤로 좀 넘어가도 도착할 수 있으니 >= 사용
    if i >= N:
        min_cnt = min(cnt, min_cnt)
        return
    if cnt >= min_cnt:
        return

    # 2. 재귀 호출
    # 다음 단계로 넘어갈 수 있는 경우의 수(branch) 생각
    # 현재 정류장 번호는 i, 현재 정류장의 충전 용량은 bus_stop[i]
    # 우리가 다음에 갈 수 있는 거리는 1 ~ bus_stop[i] 까지 가능

    for j in range(bus_stop[i], 0, -1):
        # 충전횟수 + 1, 다음에 갈 정류장 번호는 i + j
        drive(i + j, cnt + 1)


for tc in range(1, T + 1):
    # 맨 앞 숫자는 N, 정류장 개수
    # 나머지 숫자들은 bus_stop, 각 정류장의 충전지 용량
    N, *bus_stop = map(int, input().split())

    bus_stop = [0] + bus_stop

    min_cnt = 9999999

    drive(1, -1)

    print(f"#{tc} {min_cnt}")

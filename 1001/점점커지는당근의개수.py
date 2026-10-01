T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 1 # 당근이 증가하는 구간의 길이
    max_cnt = 1 # 증가하는 구간의 최대 길이
    for i in range(1, N):
        if arr[i] > arr[i-1]:
            cnt += 1    # 당근이 점점 커지면 구간의 길이에 +1
        else:
            cnt = 1     # 작아지면 다시 초기화

        if cnt > max_cnt:   # 최댓값보다 크면 최댓값으로 갱신
            max_cnt = cnt

    print(f"#{tc} {max_cnt}")


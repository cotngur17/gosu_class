T = int(input()) # 전체 테스트 케이스 개수

for tc in range(1, T + 1):
    N = int(input()) # 현재 테스트 케이스의 자연수 개수
    arr = list(map(int, input().split())) # 리스트 생성

    # 숫자가 계속 작아지는지 여부를 저장할 변수 (기본값 1)
    result = 1

    # N개의 숫자에 대해 이웃한 두 숫자를 비교 (N-1번 비교)
    for i in range(N - 1):
        # 앞의 숫자가 뒤의 숫자보다 작거나 같으면 규칙 위반
        if arr[i] <= arr[i + 1]:
            result = 0
            break  # 한 번이라도 규칙을 어기면 더 이상 검사할 필요 없이 종료

    print(f"#{tc} {result}")
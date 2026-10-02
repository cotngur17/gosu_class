T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    panel = [list(map(int, input().split())) for _ in range(N)]
    lens = [list(map(int, input().split())) for _ in range(M)]

    size = N - M + 1

    result = [[0] * size for _ in range(size)]

    # 렌즈의 시작 위치
    for i in range(size):
        for j in range(size):

            total = 0

            # M x M 렌즈 영역 계산
            for r in range(M):
                for c in range(M):
                    total += panel[i + r][j + c] + lens[r][c]

            result[i][j] = total

    print(f"#{tc}")

    for row in result:
        print(*row)  # 출력예시처럼 언패킹

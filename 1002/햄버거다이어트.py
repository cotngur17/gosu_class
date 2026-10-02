T = int(input())


def hamburger(i, score, kcal):
    global max_score

    # 칼로리 초과하면 더 볼 필요 없음
    if kcal > L:
        return

    # 모든 재료를 확인한 경우
    if i == N:
        max_score = max(max_score, score)
        return

    # 1. 현재 재료를 선택하는 경우
    hamburger(
        i + 1,
        score + ingredients[i][0],
        kcal + ingredients[i][1]
    )

    # 2. 현재 재료를 선택하지 않는 경우
    hamburger(i + 1, score, kcal)


for tc in range(1, T + 1):
    N, L = map(int, input().split())

    ingredients = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    max_score = 0

    hamburger(0, 0, 0)

    print(f"#{tc} {max_score}")
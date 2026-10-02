T = int(input())


# i : 상품 번호, 단계
# produce(1) : 1번 상품을 어디서 생산할지...
# produce(2) : 2번 상품을 어디서 생산할지...
# ...
# produce(N) : N번 상품을 어디서 생산할지.. 결정하고 중단
# selected : 이전에 생산한 공장은 제외하도록 저장
# cost : 지금까지 생산한 비용의 합
def produce(i, selected, cost):
    global min_cost

    # 0. 가지치기
    # 내가 이전에 계산한 최소 비용보다 현재 생산 비용이 더 크면
    # 더이상 진행할 필요가 없다.
    if cost > min_cost:
        return

    # 1. 기저 조건(종료 조건)
    if i == N:
        min_cost = min(min_cost, cost)
        return

    # 2. 재귀 호출
    # 다음 단계로 가는 경우의 수(branch) 계산 해서 반복문으로 재귀 호출
    for j in range(N):
        # j : 공장 번호
        # j번 공장이 이전에 생산한적이 없다면 i번 상품을 생산하자.
        if j not in selected:
            # selected.append(j)
            produce(i + 1, selected + [j], cost + matrix[i][j])
            # selected.pop()


for tc in range(1, T + 1):
    # 상품의 개수, 공장수 N
    # N개의 상품을 N개의 공장에서 각각 하나씩 생산해야한다.
    N = int(input())

    # matrix[1][3] = 1번 상품을 3번 공장에서 생산할때 비용
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 문제에서 원하는 답 : 최소 생산 비용
    min_cost = 99999999999

    # 0번 상품부터 생산 시작, 어떤 공장도 사용하지 않은 상태, 비용 합은 0부터
    produce(0, [], 0)

    print(f"#{tc} {min_cost}")

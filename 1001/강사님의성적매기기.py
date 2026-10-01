T = int(input())

grades = ['A+', 'A0', 'A-', 'B+', 'B0',
          'B-', 'C+', 'C0', 'C-', 'D0'] # 등급 생성


for tc in range(1, T + 1):

    N, K = map(int, input().split())
    score = []  # 총점 담을 리스트 생성

    for i in range(N):
        mid, final, homework = map(int, input().split())    # 중간, 기말, 과제 점수
        total = mid * 0.35 + final * 0.45 + homework * 0.2  # 총점
        score.append(total)

    target = score[K-1] # K번째 학생의 점수

    rank = 0    # K번째 학생보다 점수가 높은 학생 수

    for i in range(N):

        if score[i] > target:  # K번째 학생보다 높은 학생 수를 구하여 순위 인덱스를 구함
            rank += 1


    # 한 등급당 N//10명이므로 N//10이 2일경우 2명까지 같은 등급 부여

    grade = grades[rank//(N//10)]

    print(f"#{tc} {grade}")
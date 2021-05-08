from collections import deque

def solution(places):
    answer = [1]*5
    
    q = deque()
    people = []
    for i in range(5) :
        for j in range(5) :
            for k in range(5) :
                if places[i][j][k] == 'P' :
                    people.append((j, k))
                    q.append((j, k))
        # 고정
        r1, c1 = people[0][0], people[0][1]
        while q :
            r2, c2 = q.popleft()
            if manhattanChecker(r1, r2, c1, c2) :
                if not partitionChecker(places, r1, r2, c1, c2) :
                    answer[i] = 0
                    break
            # 고정점 변경
            r1, c1 = r2, c2
            
    return answer

def partitionChecker(places, r1, r2, c1, c2) :
    # 사이 확인
    # 상-하
    if abs(r1-r2) > 0 and abs(c1-c2) > 0 :
        row = -(r1-r2)
        col = -(c1-c2)
        if places[row][c1] == 'X' and places[r1][col] == 'X' :
            return True
    elif r1-r2 == 0 :
        row = max(r1-r2) - 1
        if places[row][c1] == 'X' :
            return True
    elif c1-c2 == 0 :
        col = max(c1-c2) - 1
        if places[r1][col] == 'X' :
            return True
        


def manhattanChecker(r1, r2, c1, c2) :
    if abs(r1-r2) + abs(c1-c2) <= 2 :
        return True

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
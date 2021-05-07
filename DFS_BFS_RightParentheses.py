def solution(p):
    # 입력이 빈 문자열일 경우 빈 문자열 반환
    answer = ''
    if p == '' :
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    if properChecker(u) :
        # True면 u에 solution 함수를 거친 v를 더한 것이 답
        answer = u + solution(v)
    else :
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        # 괄호 방향 뒤집기
        for i in range(len(u)) :
            if u[i] == '(' :
                u[i] = ')'
            else :
                u[i] = '('
        # 리스트를 문자열로 변환
        answer += "".join(u)
    return answer
                

# 균형잡힌 문자열이라면 마지막 괄호의 인덱스 반환
def balanced_index(p) :
    count = 0   # 왼쪽 괄호 개수
    for i in range(len(p)) :
        if p[i] == '(' :
            count += 1
        else :
            count -= 1
        if count == 0 :
            return i

# 올바른 문자열인지 판단
# 왼쪽이 있으면 반드시 오른쪽이 있어야 하며 왼쪽부터 등장해야 함
# -> 따라서 왼쪽 먼저 등장하지 않으면 False
# 반복문이 다 끝나면 count == 0이 되지 않았다는 뜻이므로 return True
def properChecker(p) :
    count = 0
    for i in p :
        if i == '(' :
            count += 1
        else :
            # 왼쪽 먼저 등장하지 않아 False
            if count == 0 :
                return False
            count -= 1
    return True

    
    
    
    
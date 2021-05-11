def solution(new_id):
    temp1 = ''
    new_id = list(new_id)

    acceptableList = ['-', '_', '.']
    for id in new_id :
        if id.isalpha() :
            temp1 += id.lower()
        elif id.isdigit() or id in acceptableList :
            temp1 += id
        
    while '..' in temp1 :
        temp1 = temp1.replace('..', '.')

                
    # 처음과 끝 마침표 처리
    if temp1[0] == '.' : 
        temp1 = temp1[1:] 
    if temp1[-1] == '.' :
        temp1 = temp1[:-1] 

    # 빈 문자열 처리       
    if temp1 == "" :
        temp1 += "a"
     
    # 길이 수 조절
    if len(temp1) >= 16 :
        temp1 = temp1[:15]
        if temp1[-1] == '.' :
            temp1 = temp1[:-1]

    if len(temp1) <= 2 :
        while len(temp1) != 3 :
            temp1 += temp1[-1]
    return temp1

print(solution("abcdefghijklmn.p"))
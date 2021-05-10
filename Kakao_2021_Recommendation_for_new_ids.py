def solution(new_id):
    temp1 = ''
    new_id = list(new_id)

    # 제거하려는 것은 "#"로 치환한다.
    acceptableList = ['-', '_', '.']
    for i in range(1, 9) :
        acceptableList.append(str(i))
    lowerAlpha = [chr(65+i) for i in range(26)]
    upperAlpha = [chr(97+i) for i in range(26)]
    Alpha = lowerAlpha + upperAlpha
    for id in new_id :
        if id in Alpha :
            temp1 += id.lower()
        elif id in acceptableList :
            temp1 += id
    temp1 = list(temp1)
    # 연속된 마침표 처리
    stickIndex = 0
    while stickIndex + 1 < len(temp1) :
        if temp1[stickIndex] == '.' and temp1[stickIndex+1] == '.' :
            del temp1[stickIndex]
        else :
            stickIndex += 1
    temp1 = "".join(temp1)

    # 처음과 끝 마침표 처리
    i = 0
    j = 1
    while True :
        if len(temp1) == 1 and temp1 == "." :
            temp1 = ""
            break
        if len(temp1) >= 2 :
            if temp1[0] == '.'  :
                temp1 = temp1[1:]
            elif temp1[-1] == '.' :
                temp1 = temp1[:-1]
            else :
                break

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

left_people = [i for i in range(1, 101)]

# 초기 stickIndex = 0이다.
# 따라서 pokedOut = 1이 된다.
# pokedOut이 탈락하고 다음 인덱스 stickIndex가 탈락....
# pokedOut은 나머지 값이기 때문에 다음 턴이 될 경우
# 다시 1부터로 원상 복귀가 가능함
# 즉, stickIndex가 0으로 원상복귀 되는 순간이 온다.
# 그러면 다음 턴이 반복되는 것이다.

def Josephus(left_people, stickIndex) :
	if len(left_people) == 1 :
		return left_people[0]
	
	pokedOut = (stickIndex + 1) % len(left_people)
	del left_people[pokedOut]
	stickIndex = pokedOut
	return Josephus(left_people,stickIndex)

print(Josephus(left_people, 0))

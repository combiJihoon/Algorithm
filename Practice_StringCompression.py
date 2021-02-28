def solution(s):
# "abcabcdede"
  mid=len(s)//2 + 1
  answer=len(s)

  for step in range(1, mid) :
    compressed=""
    prev=s[:step]
    count=1
    for j in range(step, len(s), step) :
      if prev==s[j:j+step] :
        count+=1
      else :
        compressed+=str(count)+prev if count>=2 else prev
        prev=s[j:j+step]
        count=1
    compressed+=str(count)+prev if count>=2 else prev
    answer=min(answer, len(compressed))
  return answer, compressed



s=["aabbaccc", "ababcdcdababcdcd", "ababc"]
for i in s :
  print(solution(i))

def matrix_rotation_by_90(a) :
  n=len(a)   # 행 개수
  m=len(a[0])   # 열 개수
  result=[[0]* n for _ in range(m)]
  for i in range(n) :
    for j in range(m) :
      result[j][n-i-1]=a[i][j]
  return result
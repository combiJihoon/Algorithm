n = int(input())
homes = list(map(int, input().split()))
homes.sort()

smaller_index_d = 0
larger_index_d = 0
if n % 2 != 0 :
	print(homes[n//2])
else :
	for i in range(len(homes)) :
		smaller_index_d += abs(homes[i]-homes[(n//2)-1])
		larger_index_d += abs(homes[i]-homes[(n//2)])
	if smaller_index_d <= larger_index_d :
		print(homes[(n//2)-1])
	else :
		print(homes[(n//2)])
arr = list(map(int,input().split()))
key = int(input())
if key in arr:
	print(arr.index(key))
else:
	print("Not found")
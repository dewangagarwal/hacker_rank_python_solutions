n = int(input())
arr = list(map(int, input().split()))
a=max(arr)
i=0
while(i<n):
    if a==max(arr):
        arr.remove(max(arr))
    i+=1
print(max(arr))


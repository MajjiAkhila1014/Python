arr=[1,2,3,4,5]
k=3 # we have to start from 3,4,5,1,2
first=arr[k-1:]
second=arr[:k-1]
first.extend(second)
print(first)
print(second)

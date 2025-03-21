#cognizant question
n = int(input("n : ")) # length of list and output list
arr = [int(input(f'arr index {i} :')) for i in range(n)] #given list
k = int(input("k : ")) # jump size
result = [0]*n
cnt = 0
index = 0
while cnt < n :
    result[cnt] = arr[index]
    index = (index + k) % n
    cnt += 1

print(result)
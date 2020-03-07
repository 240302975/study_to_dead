a = [1, 3, 4, 6, 7, 7, 8, 9, 11]
for index, i in enumerate(a):
    # print(index,i)
    a[index] += 1
print(a)


b = [1, 3, 4, 6, 7, 7, 8, 9, 11]
b = list(map(lambda x: x + 1, b))
print(b)


c = [1, 3, 4, 6, 7, 7, 8, 9, 11]
c = [i + 1 for i in c]
print(c)

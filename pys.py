list = [[1,2,3],[4,5],[6,7,8,9]]
print(list)

result = sorted(list)
print(result)

result = sorted(list, key=len)
print(result)

result = sorted(list, key=sum)
print(result)

result = sorted(list, key=lambda sublist: sum(sublist))
print(result)
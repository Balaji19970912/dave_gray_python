#use of reduce function

from functools import reduce

arr1 = [1,2,3,4,5,6,7,8,9,10]

total = reduce(lambda acc, curr: acc+curr, arr1,10)

# print(total)
# print(sum(arr1,10))

arr2 = ['apple']

total_char = reduce(lambda acc,curr: acc+len(curr), arr2, 0)

print(total_char)
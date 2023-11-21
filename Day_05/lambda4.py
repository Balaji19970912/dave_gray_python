#use filter for lambda

arr1 = [1,2,3,4,5,6,7,8,9,10]

odd_numbers = filter(lambda res: res %2 != 0, arr1)

print(list(odd_numbers))
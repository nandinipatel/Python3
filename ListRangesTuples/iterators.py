# string = "1234567890"

# for char in string:
#     print(char)
# print("-" * 10)
# for char in iter(string):
#     print(char)

numbers = [1,2,3,4,5,6,7,8,9,0]
#print(numbers)

iterator = iter(numbers)

for num in numbers:
    print(next(iterator))
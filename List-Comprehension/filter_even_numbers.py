list_of_strings = input().split(',')

res = [int(i) for i in list_of_strings]

result = [n for n in res if n % 2 == 0]

print(result)
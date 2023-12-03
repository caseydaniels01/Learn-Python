
#Old
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n+1
#     new_list.append(add_1)
# print(new_list)


#New
# numbers = [1, 2, 3]
# new_list = [n+1 for n in numbers]
# print(new_list)



names = ["Alex", "Beth", "Amanda", "Caroline", "Dave", "Freddie"]

# short_names = [n for n in names if len(n) < 5]
# print(short_names)

# long_names = [n.upper() for n in names if len(n) > 5]
# print(long_names)
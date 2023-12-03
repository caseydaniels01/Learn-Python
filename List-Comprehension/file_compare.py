
with open(r"c:\Users\casey\OneDrive\Desktop\Code - VSCode\Learn-Python\Learn-Python\List-Comprehension\file1.txt", mode="r") as file:
    contents_one = file.readlines()

with open(r"c:\Users\casey\OneDrive\Desktop\Code - VSCode\Learn-Python\Learn-Python\List-Comprehension\file2.txt", mode="r") as file:
    contents_two = file.readlines()

# strip_one = set([n.strip() for n in contents_one])
# strip_two = set([n.strip() for n in contents_two])

# result = strip_one.intersection(strip_two)
# res = sorted([int(i) for i in result])

# print(res)

result = [int(num) for num in contents_one if num in contents_two]
print(result)

# sentence = input().split(' ')
# result = {word:len(word) for word in sentence}

sentence = input()
result = {word:len(word) for word in sentence.split()}

print(result)
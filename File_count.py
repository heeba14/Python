file = open("count_file.txt","r")
dict1 = {}
message=file.read()
print("message is:",message)
text = message.split()

print("item is",text)
for item in text:
    if item in dict1:
        dict1[item] += 1
    else:
        dict1[item] = 1

print("output",dict1)
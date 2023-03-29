string1 = input()
string2 = input()

count = 0
for i in range(len(string1)):
    if string1[i:].startswith(string2):
        count += 1
    
count1 = 0
for i in range(len(string2)):
    if string2[i:].startswith(string1):
        count1 += 1

if count1 > count:
    count = count1

print(count)

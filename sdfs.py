a = input().lower()
word = list(set(a))
how = []

for i in word:
    count = a.count(i)
    how.append(count)

if how.count(max(how)) >= 2:
    print("?")
else:
    print(word[(how.index(max(how)))].upper())
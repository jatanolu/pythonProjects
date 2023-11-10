for i in range (4):
    print(i)

x = list(range(5))
print(x)

supplies = ["pens", "staplers", "flame-throwers", "binders"]
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

cat = ["fat", "orange", "loud"]
size, color, disposition = cat

spam = ["hello", "hi", "howdy", "heyas"]
print(spam.index('hello'))
spam.append("hey")
print(spam)

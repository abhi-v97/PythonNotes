x = list(range(10))
y = [3, 7, 10]

for i in y:
    if i in x:
        print(i, "is here")
    else:
        print(i, "is not here")
        break
    print("123")
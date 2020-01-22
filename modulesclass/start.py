from lib.calc import plus, minus, mult, dev

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
print("Що зробити? Введіть цифру")
n = int(input("1-додати, 2-відняти, 3-помножити, 4-поділити "))

if n == 1:
    res = plus(a, b)
    print(a, "+", b, "=", res)
elif n == 2: 
    print(a, "-", b, "=", minus(a, b))
elif n == 3:
    res = mult(a, b)
    print(a, "x", b, "=", res)
elif n == 4:
    print(a, ":", b, "=", dev(a, b))
else:
    print("Введіть пункт з меню!")

# res = plus(2, 2)
# print("Result=>", res)

# res = minus(2, 2)
# print("Result=>", res)

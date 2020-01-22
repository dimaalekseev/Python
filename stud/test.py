from lib.module import *
counter = 0
print("Welcome to Test")

if q1() == "b":
    counter += 1
if q2() == "a":
    counter += 1
if q3() == "c":
    counter += 1
if q4() == "b":
    counter += 1
if q5() == "a":
    counter += 1
if q6() == "c":
    counter += 1
if q7() == "a":
    counter += 1
if q8() == "c":
    counter += 1
if q9() == "a":
    counter += 1
if q10() == "b":
    counter += 1

print("Ваш результат:", counter)

if counter==9 and counter==10:
    print("Відмінно!")
elif counter==7 and counter==8:
    print("Добре")
elif counter==5 and counter==6:
    print("Посередньо")
else:
    print("Незадовільно")

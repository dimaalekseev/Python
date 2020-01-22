#Написати програму яка в залежності від введеної години виводить: good night, good day, good evening, good morning.

# time=int(input('Введіть годину доби 0-23'))

# if time>=5 and time<=11:
#     print('Good Morning!')
# elif time>=12 and time<=16:
#     print('Good day!')
# elif time>=17 and time<=21:
#     print('Good evening!')
# elif time>=22 or time==23 or time>=0 and time<=4:
#     print('Good night!')
# else:
#     print('Введіть число з діпазону 0-23!')


#Відомо, що 1 дюйм дорівнює 2.54 см. Розробити програму, що переводить дюйми в сантиметри и навпаки. Діалог с користувачем реалізувати через систему меню.

units=input("Виберіть одиниці виміру:\n\
\t1-сантиметри в дюйми,\n\
\t2-дюйми в сантиметри,\n")

num=float(input("Введіть значення:"))

if units=='1':
    print("%s дюймів"%(num*2.14))
elif units=='2':
    print("%s сантиметрів"%(num/2.14))
        



# რიცხვების შედარება მითითებულ რიცხვზე :

a=int(input("შეიყვანეთ რიცხვი 1 (ნაკლები უნდა იყოს მეორეჯერ შეიყვანილზე ან უდრიდეს მას) : "))

b=int(input('შეიყვანეთ რიცხვი 2 (მეტი უნდა იყოს პირველჯერ შეიყვანილზე ან უდრიდეს მას) : '))

c=int(input('შეიყვანეთ რიცხვი რომელსაც გინდათ რომ შეადაროთ ეს რიცხვები : '))

if a<=b :
    Number_List=list(range(a,b))
    for i in Number_List :
     if i < c :
         print( str(Number_List) + "ნაკლებია c ზე ! ")
         break
     if i == c :
         print( str(Number_List) + "უდრის c ს ! ")
         break
     if i > c :
         print( str(Number_List) + "მეტია c ზე ! ")
         break
else :
    print('b ნაკლებია a ზე !')

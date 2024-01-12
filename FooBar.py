number = int(input("Enter number to check :"))

if number % 3 == 0 and number % 5 == 0:
    print("FOOBAR")
elif number % 3 == 0 :
    print("FOO")
elif number % 5 == 0 :
    print("BAR")
else : 
    print("FOOFOOBARBAR")


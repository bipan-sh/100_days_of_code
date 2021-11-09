
fizz = "fizz"
buzz = "buzz"
fizzbuzz = "fizzbuzz"

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(fizzbuzz) 
    
    else :
        if number % 3 == 0:
            print(fizz)
            
        else :
            if number % 5 == 0 :
                print(buzz)

            else:
                print(number)

print("\n\n\n\n")
#Tried the below code but hadn't worked before so went the long way with the code above
#after watching the solution on the video, it works, don't know what I had previously done wrong 
for number2 in range(1, 101):
    if number2 % 3 == 0 and number2 % 5 == 0:
        print('Fizzbuzz')

    elif number2 % 3 == 0:
        print('Fizz')

    elif number2 % 5 == 0:
        print('Buzz')

    else :
        print(number2)




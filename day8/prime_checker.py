#Write your code below this line 👇


def prime_checker(number):
    not_prime_number = []
    prime_number = [2]

    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is divisible by {i}")
            not_prime_number.append(number)

    if number in not_prime_number:
        print(f"{number} is not a prime number")

    else:
        print(f"{number} is a prime number")


#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)





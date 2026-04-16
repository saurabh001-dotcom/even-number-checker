def number_checker(num):
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")

num = int(input("Enter a Number: "))
number_checker(num)
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        if num % 3 == 0:
            print("Fizz")
        else:
            if num % 5 == 0:
                print("Buzz")
            else:
                print(num)

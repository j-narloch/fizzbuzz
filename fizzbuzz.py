#range must be 51 because it will display numbers to 50
for fizzbuzz in range (51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
    elif fizzbuzz % 3 == 0:
        print("Fizz")
    elif fizzbuzz % 5 == 0:
        print("Buzz")
        continue
    print(fizzbuzz)

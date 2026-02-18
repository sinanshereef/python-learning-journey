


# Q1 — FizzBuzz (Beginner)
#
# Problem description:
# Write a function fizzbuzz(n) that returns a list of strings for the integers from 1 to n (inclusive) with the following rules:
#
# For multiples of 3, use "Fizz" instead of the number.
#
# For multiples of 5, use "Buzz".
#
# For numbers that are multiples of both 3 and 5, use "FizzBuzz".
#
# Otherwise, use the number itself as a string (e.g., "7").
#
# Input/Output examples:
#
# fizzbuzz(5) ➜ ["1", "2", "Fizz", "4", "Buzz"]
#
# fizzbuzz(15) ➜ ends with "...", "13", "14", "FizzBuzz"]



def fizzbuzz(n):
    result=[]
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            result.append("fizzbuzz")
        elif i%3==0:
            result.append("fizz")
        elif i%5==0:
            result.append("buzz")
        else:
            result.append(i)
    return result

finall=fizzbuzz(15)
print(finall)
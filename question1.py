'''FizzBuzz Variation (Classic Logic Test)
Question:
Write a program that prints numbers from 1 to 100.
 But for multiples of 3, print "Fizz" instead of the number, and for multiples of 5,
 print "Buzz". For numbers which are multiples of both 3 and 5, print "FizzBuzz".'''
for a in range(1,101):
    if a%3==0 and a%5==0:
        print("FizzBuzz")
    elif a%5==0:
        print("Buzz")
    elif a%3==0:
        print("Fizz")
    else :
        print(a)

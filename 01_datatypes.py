#sum of the digits of two digit number

two_digit_number=input("Type a two digit number:")

first_digit=two_digit_number[0]
second_digit=two_digit_number[1]

first_digit=int(first_digit)    #type conversion string to int type
second_digit=int(second_digit)

print("sum of digits is:", first_digit + second_digit)
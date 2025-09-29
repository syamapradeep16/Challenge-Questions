# Program to check whether a number is an Armstrong number or not

num = int(input('Enter the number:'))

def armstrong(num):
    n = len(str(num))
    sum = 0
    temp = num  
    while temp > 0:
        last_digit = temp % 10
        exp = last_digit ** n
        sum = sum + exp
        temp = temp // 10
    return sum == num

if armstrong(num):
    print('The given number', num, 'is an armstrong number')
else:
    print('The given number', num, 'is not an armstrong number')

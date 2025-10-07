#Program to find the list of prime numbers in a range of numbers

num_start = int(input('Enter the starting number:'))
num_end = int(input('Enter the ending number:'))
prime_list = []
def check_prime(num):
    prime = True
    if num == 1 or num == 0:
        prime = False
    else:
        for i in range (2, num):
            if (num % 2) == 0:
                prime = False
    return prime

for i in range(num_start,num_end +1):
    if (check_prime(i)) == True:
        prime_list.append(i)
    
print(prime_list)
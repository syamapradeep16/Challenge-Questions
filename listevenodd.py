#Program to create first 100 numbers, list of even and odd numbers and list of numbers divisible by both 5 & 3
num = []
even = []
odd = []
div = []
#create list of first 100 numbers
for i in range(1,101):
    num.append(i)
print ('Numbers:', num)

#create list of even and odd numbers
for j in range(1, 101):
    if j % 2 == 0:
        even.append(j)
    else:
        odd.append(j)
print ('Even numbers:', even)
print ('Odd numbers:', odd)

#create list of numbers divisible by both 5 and 3
for k in range (1,101):
    if k % 5 == 0 and k % 3 == 0:
        div.append(k)
print ('Numbers divisible by 5 & 3:', div)


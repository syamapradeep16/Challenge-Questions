#Roman to Integer Conversion

def romantoint(roman):
    s = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    total = 0

    for i in range(len(roman)):
        if i < len(roman)-1 and s[roman[i]] <= s[roman[i + 1]]:
            total = total - s[roman[i]]
            i = i + 1
        else:
            total = total + s[roman[i]]
    return total

roman = input('Enter a Roman numeral:').upper()
print('Integer Value:', romantoint(roman))


number = int(input())
fullN = number
roman = ""
while number >= 1000:
    roman = roman+"M"
    number = number-1000
if number >= 900:
    roman = roman +"CM"
    number = number-900
while number >= 500:
    roman = roman+"D"
    number = number-500
if number >= 400:
    roman = roman +"CD"
    number = number-400
while number >= 100:
    roman = roman+"C"
    number = number-100
if number >= 90:
    roman = roman +"XC"
    number = number-90
while number >= 50:
    roman = roman+"L"
    number = number-50
if number >= 40:
    roman = roman +"XL"
    number = number-40
while number >= 10:
    roman = roman+"X"
    number = number-10
if number >= 9:
    roman = roman +"IX"
    number = number-9
while number >= 5:
    roman = roman+"V"
    number = number-5
if number >= 4:
    roman = roman +"IV"
    number = number-4
while number >= 1:
    roman = roman+"I"
    number = number-1
print(roman)
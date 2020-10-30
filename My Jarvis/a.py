num = int(input('number: '))
tmp = num
reverse = 0
while tmp>0:
    rem = tmp%10
    reverse = (reverse*10) + rem
    tmp //= 10
print(reverse)
if num == reverse:
    print('palindrome')
else:
    print('Not palindrome')
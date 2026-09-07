n=int(input("enter the number: "))

original = n
reverse = 0

while n > 111:
    digit =n % 10
    reverse = reverse * 10 + digit
    n= n // 10

if original == reverse:
    print("palindrome")
else:
    print("not a palindrome")
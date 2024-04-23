
print()
print()
print("        ==================Simple Calculator=====================        ")
print()
print()
number1 = int(input("Enter the first number : "))
number2 = int(input('Enter the second number : '))
operator = input('Enter The operator : ')
print()
if operator=='+':
    print('The Addition of the number is : ',number1+number2)
    print()
    print()
elif operator=='-':
    print('The Substraction of the number is : ',number1-number2)
    print()
    print()
elif operator=='*':
    print('The Multiplication of the  number is : ',number1*number2)
    print()
    print()
elif operator=='/':
    print('the Division Of the number : ',number1/number2)
    print()
    print()
else:
    print('!!!! INVALID OPERATOR !!!!')
    print()
    print()
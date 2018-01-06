try:
    num1 = input('Please Input a num: \n')
    num1 = int(num1)
    num2 = input('Another num: \n')
    num2 = int(num2)

except ValueError:
    print("Sorry, I really needed a number.")
else:
    ans = num1 + num2
    print('Answer is: \n', ans)

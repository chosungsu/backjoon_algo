num1, num2 = input().split()
num1_reverse = int(num1[::-1])  # [::-1] : 역순
num2_reverse = int(num2[::-1])

if num1_reverse > num2_reverse:
    print(num1_reverse)
else :
    print(num2_reverse)
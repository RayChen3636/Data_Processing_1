# 範例~ try and except
num1 = input("請輸入數值1:")
num2 = input("請輸入數值2:")
try:
    print(int(num1) + int(num2))
except ValueError:
    print("輸入必須為數值")
    num1 = input("請輸入數值1:")
    num2 = input("請輸入數值2:")
    print(int(num1) + int(num2))


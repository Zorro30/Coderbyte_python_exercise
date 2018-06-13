def CheckNums(num1,num2): 

    if num2 > num1:
        return 'true'
    elif num2 < num1:
        return 'false'
    elif num2 == num1:
        return '-1'
    
num1,num2 = input("Enter two numbers separated by:").split(',')
print(CheckNums(num1,num2))
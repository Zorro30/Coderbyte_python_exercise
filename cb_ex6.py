def TimeConvert(num): 

    n = int(num)//60
    m = int(num)%60
    return str(n) + ':' + str(m)
    
print (TimeConvert(input("Enter the number of minutes:")))
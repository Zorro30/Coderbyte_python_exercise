def SimpleAdding(num): 

    count = 0
    if num == ' ' or num == '':
        print ("Enter a good number!")
        exit(0)
    else:
        val = int(num)
        for i in range(1, val+1):
            count +=i
    return count
     
print (SimpleAdding(input("Enter the number:")))

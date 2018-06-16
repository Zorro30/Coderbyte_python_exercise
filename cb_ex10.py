def PentagonalNumber(n):
    a = 1
    for i in range(1,n):
        a +=5 * i

    return a

print (PentagonalNumber(int(input("Enter the layer number:"))))
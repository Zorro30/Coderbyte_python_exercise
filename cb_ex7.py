def AlphabetSoup(str): 
    
    return (''.join(sorted(str)))
    #return (''.join(sorted(str), reverse = True)) --> for descending order.
    
print (AlphabetSoup(input("Enter the string to arrange:")))
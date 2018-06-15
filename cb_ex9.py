def difficultNumber(num):
    count=0

    while num !=6174:
        num = list(str(num))
        if len(num) < 4:
            while len(num) != 4:
                num.insert(1,'0')
        elif len(num) > 4:
            print ("The number should only be 4 digit.")
            break
        

        count +=1

        des = int(''.join(sorted(num, reverse=True)))
        asc = int(''.join(sorted(num)))

        if des == asc :
            print ("Please enter a 4 digit number with atleast two distinct digits.")
        else:
            num = int(des) - int(asc)
    return count

value = int(input("Enter the 4 digit number:"))
print(difficultNumber(value))
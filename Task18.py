def nums(age):
    if age % 2 ==0:
        start1 = 0
        while start1<=age:
            print(start1)
            start1 += 2
    else:
        start2 = 1
        while start2<=age:
            print(start2)
            start2 += 2
        

nums(20)
nums(33)
        
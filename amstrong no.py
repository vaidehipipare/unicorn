#wap to input any no print whether amstrong no


#no = int(input("Enter the value on n: "))
#sum = 0

#for d in no:
 #   x = int(d)
  #  cube = x*x*x
   # sum+=cube


#if sum == int(no):
 #   print("it is armstrong no ")
#else:
 #   print("it is not armstrong no")





for i in range(153,1001,1):
    sum = 0
    i = str(i)
    for d in no:
        x = int(d)
        cube = x*x*x
        sum+=cube

    if sum==i:
        print(i)
    

    if sum == int(no):
        print("it is armstrong no ")
    else:
        print("it is not armstrong no")

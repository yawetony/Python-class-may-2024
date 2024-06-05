def continue_function(x,y,z):
            
        for i in range(x,y,z):
                if i %2== 0:
                        print(i)
                        continue
                

x= int(input("Enter the start value: "))
y= int(input("Enter the stop value: "))
z= int(input("Enter the step value: " ))

continue_function(x,y,z)
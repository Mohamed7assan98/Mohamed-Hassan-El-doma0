print("welcome")
a=[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
z = 'true'
x = 1
while (z == 'true'): 
    print("player",x) 
    y=int(input("Number of plays: "))
    if y==1:
        m = int(input("The Number: "))
        a.pop(m)
        a.insert(m,'*')
    else:
        m = int(input("First Number: "))
        n = int(input("Second Number:"))
        a.pop(m)
        a.insert(m,'*')
        a.pop(n)
        a.insert(n,'*')
    for j in range(0,20):
        if a[j]=='*':
            z = 'false'
            b = x
        else:
            z='true'
            break
    if x==2:
        x=1
    else:
        x+=1
    
    print(a)
print("THE WINNER IS PLAYER ",b)
    

 




        
    

















    

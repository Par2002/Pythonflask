#Day 5 Assignment
#control flow
a=int(input("Enter the Number of of range:"))
for i in range(0,a):
    if i%5==0 or i%7==0:
        print(i)
#_____________________________________________________
b=int(input("Enter the number of terms you want to print:"))
t=0
for j in range (1,b+1):
    b2='2'*j
    #t==int(b2)
    print(int(b2),end=" ")
    t=t+int(b2)
    if j==b:
        break
    b2=print( ' + ',end="")
    #t=t+int(b2)
print()
print(t)
#___________________________________________________________
o=0
while(1):
    l=int(input("Enter the number:"))
    o=o+l
    print(o)
    v=input("Do you want to quit if yess press q else press y:")
    
    if v=='q':
        break
    else:
        
        pass
#____________________________________________________________
x=int(input("Enter the number :"))
a7=1
for z in range(x,0,-1):
    a7=z*a7
print("Factorial is:",a7)
#_________________________________________________________
y='python language is the best programing language'
for d in range(len(y)):
    end_val="-"
    if y[d]==' ':
        end_val=''
    elif d==len(y)-1:
        end_val=''
    elif y[d+1]==' ':
        end_val=''

    if d%2==0:
        print(y[d].upper(),end=end_val)
    else:
         print(y[d].lower(),end=end_val)

    







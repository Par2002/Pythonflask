a=int(input('Enter the number you want in the list:'))

L1=[]
for i in range(0,a):
    b=int(input('Enter the number:'))
    L1.append(b)
print(L1)
b=int(input('Enter the letter you want in the list:'))
L2=[]
for j in range(0,b):
    q=input('Enter the letter:')
    L2.append(q)
print(L2)
c={}
for i in range (0,len(L1)):
    for j in range (0,len(L2)):
        c[L1[i]]=L2[j]
        L2.remove(L2[j])
        break
print(c)
# _______________________________________________________________________________
a=input('Enter the str:')
v=0
w=0
for i in a:
    if i.isdigit():
        
        v=v+1
        
    elif i.isalpha():

        # w=a.isalpha()
        w= w+1
    else:
        pass

print('Letters:',v)
print('Digits:',w)
# _____________________________________________________________________________________

def parth():
    e=input("Enter the words you want in the list:")
    a=list(e.split(" "))
    m=len(a[0])
    temp=a[0]
    
    for i in a:
        if(len(i)>m):
            m=len(i)
            temp=i

    print("Length of the longest word is:",temp,m)

    return
parth()
# ______________________________________________________________

o=int(input("Enter the number of rows:"))
value=1
for i in range(0,o):
    for j in range(0,i+1):
        print(value,end='')
    value+=1
    

    print()
# _________________________________________________

def prime(n):
    if n==1 or n==0:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False

        else:
            return True

a=int(input("enter number: "))

i=10
flag=0
if prime(a):
    while True:
        if int((a-(a%i))/i)==0:
            break
        else:
            if prime(int((a-(a%i))/i)):
                flag+=1
        i=i*10
if flag!=0 :
    print("Russian Prime")
elif flag==0 and int((a-(a%10))/10)==0 and prime(a):
    print("Russian Prime")
else:
    print("Not Russian Prime")


    
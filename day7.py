
#Assignment day 7
# # ____________________________________________________
a=['a','e','i','o','u']
b=input("Enter the words:")
d=b.lower()
c=[i for i in range(len(d)) for j in a  if d[i]==j]
print(c)
# ________________________________________________
h=str(input("Enter the string:"))

g=h.split()
for f in g[::-1]:
    c=f
    print(c,end=' ')
print()

# __________________________________________________

m=int(input("Enter the numbers you want in the list:"))
n=[]
for s in range(0,m):
    g=int(input("Enter the number:"))

    n.append(g)
print(n)
x=[]
# x=[x.append(t) for t in n if t not in x]
for t in n:
    if t not in x:
        x.append(t)
        
print(x) 


























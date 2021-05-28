#Day 6 Assignment
a=[]
b=int(input("Enter the numner of element you want in the list:"))
for i in range(0,b):
    c=int(input("Enter the number:"))
    a.append(c)
print(a)
e=0
d=0
for j in a:
    if j%2==0:
      e += 1
    else:
      d +=1
print("Even number in the list: ",e) 
print("odd number in the list: ",d) 
# _______________________________________________
v=sorted(a)
print("Minimum number of the list:" ,v[0])
print("Maximum number of the list:" ,v[-1])
# ___________________________________________
w=a[::-1]
if a==w:
  print("Yes,it's a palindrome")
else:
  print("no it's not a palindrome")

#__________________________________________
for g in range(len(a)):
  h=a[g]
  f=str(h)
  f=f[::-1]
  f=int(f)

  if f==h:
      print("Yes",f,"it's a palindrome")
  else:
      print("no",f," it's not a palindrome")



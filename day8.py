# Day 8:

all_courses = ['Python', 'Java', 'Machine Learning', 'Big data', 'C programming', 'Oracle SQL', 'Power Bi', 'Go lang', 'C++ Graphics', 'React JS', 'Ruby Rails', 'Flask', 'HTML & CSS', 'Salesforce', 'Javascript', 'Django']

user={}
user['Name']=input('Enter name:')
user['E mail']=input('Enter email:')
user['courses']=[]


print(user,end='')

while True:
  print ('show the menu:')
  print('1.show cources')
  print('2.My courses')
  print('3.show profile')
  print('4.Edit your profile')
  print('0.exit')
  choice = int(input('Enter your choice : '))
  if choice == 0:
     exit(1)
  elif choice == 1:
      for i in range(0,len(all_courses)):
          print(f'{i+1}.{all_courses[i]}')
      v=int(input("Enter the courses which you want:"))
      user['courses'].append(all_courses[v-1])
      all_courses.pop(v-1)
  elif choice == 2:
      print("Your enrolled cources are:")
      for j in range(len(user['courses'])):
          print(f'{j+1}.{user["courses"][j]}')

#     show enrolled courses
  elif choice == 3:
      for key,value in user.items():
          if key=='courses':
              print(key,'=',end="")
              for j in user['courses']:
                  print(j,end=",")
              print()    
          else:
              print(key,'==',value)

  elif choice == 4:
      
    b=input("Enter the course which you want to delete yes or no ")
    if b=='y':
        for j in range(len(user['courses'])):
          print(f'{j+1}.{user["courses"][j]}')
        c=int(input("Which you want to delete:"))
        all_courses.append(user['courses'][c-1])
        user['courses'].pop(c-1)


    else:
        continue


    #   for k in user['courses']:
    #      c=all_courses+ user['courses'][k]
    #      print(c)


        #   print(key,'=',value)
    # Display user profile
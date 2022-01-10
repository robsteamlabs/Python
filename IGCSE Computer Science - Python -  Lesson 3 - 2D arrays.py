#What are we covering in Lesson 3?
#how to output entire data structure
#how to output maximum value in list
#how to output data from different elements in 1 and 2d list
#how to use if and else
#how to use nesting with if and else
#how to set up a computer program that checks for username and passwords
#boolean data types - what are they, how do they work?

#Your Task
#Once you have been through this lesson, you will set up your own program using similar techniqes that gives users access to a computer system if username and password are accepted within X number of tries



#2D list with student marks

Student_marks = [[23,23],[77,99],[11,78]]
for list_one in Student_marks:
  for data_elements in list_one:
    print (data_elements, end="")
print("")

#prints out entire 2D data structure without spaces

maximum_marks = 0
for person in Student_marks:
  for marks in person:
    if marks > maximum_marks:
      maximum_marks = marks
print (maximum_marks)

#prints out biggest item of data in 2D list

Student_Accounts = ["User 1", "Harry", "Spurs","User 2", "Jeremy", "Grandma"]
print (Student_Accounts)#printing out an entire list
print (Student_Accounts[0])#printing out data by entire index
print (Student_Accounts[0][1])#printout out data by index and individual piece of data

New_User = input("What is your user number, enter in the format User + Number :")
Student_Accounts.append(New_User)
New_User_Name = input("Enter the new users username :")
Student_Accounts.append(New_User_Name)
New_User_Password = input("Enter the new users password")
Student_Accounts.append(New_User_Password)
print (Student_Accounts)#printing out an entire list


login_username = input("Enter your login :")
Entry = False

while Entry == False:
  if login_username in Student_Accounts:
    print("username accepted")
    Entry = True
  else:
    print("username not accepted")
    login_username = input("Enter your login :")
    Entry = False


Student_Accounts = ["User 1", "Harry", "Spurs","User 2", "Jeremy", "Grandma"]

#login and password - nested statements
login_username = input("Enter your login :")
username_password = input("Enter your password")
Entry_U = False
Entry_P = False

while Entry_U == False:
  if login_username in Student_Accounts:
    print("username accepted")
    Entry_U = True
    while Entry_P == False:
      if username_password in Student_Accounts:
        print ("You now have access to the system")
        Entry_P = True
      else:
        print("password not accepted")
        username_password = input("Enter your password again :")
        Entry_P = False
  else:
    print("username not accepted")
    login_username = input("Enter your login :")
    Entry_U = False

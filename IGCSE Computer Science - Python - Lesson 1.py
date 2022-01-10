#We will use REPL to demonstrate your understanding of programming in IGCSE Computer Science
#For anything which involves file handling, we will need to alternative software.  Links to programming environments are on Google Classroom
print ("Hello Year 10 2021 Computer Scientists")#sample print statement
First_Name = input("Enter your first name: ")#example of how to set up variable and store data without specifying data type
print ("Good to meet you",First_Name)
Last_Name = str(input("Enter your last name: "))#example of string data type
Age = int(input("Enter your age here: "))#example of integer data type
Weight = float(input("Enter your weight here: "))#example of float data type
for c in range(4):
  print (First_Name)
Fav_Food = ("PIzza")
Q_Fav_Food = str(input("What is your favourite food? :"))
while Q_Fav_Food != Fav_Food:
  print ("I am convinced there is only one correct answer")
  Q_Fav_Food = str(input("What is your favourite food? :"))
print("glad to see we like the same foods!!!!")


#example of constant with comparison, get this to loop by yourself
Age_Preset = int(22)

Age_Question = int(input("How old are you??? :"))
if Age_Question < Age_Preset:
  print("I am older than you")
else:
  print("You are older than me")

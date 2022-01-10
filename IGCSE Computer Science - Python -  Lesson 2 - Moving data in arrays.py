Year_10_Names = ["Jon", "Barry", "Nemo"]#1 dimensional
Y10M =[["Lisa", "Matilda", "Grace"],["Jon","Barry","Nemo"]]#2 dimensional




print(Year_10_Names[0])#printing out singular items from a 1D list
print(Y10M[1][0])#printing out singular items from a 2D list

Mixed_GB = [["Paulette", "Geri"],["Paul","Garry","Terry"]]#jagged list
#a jagged list is a 2D list that has different size 1D lists, the one above has two items in the first and 3 in the second
print(Mixed_GB[0][1])

#limited Loop
#The below code allows you to add new data to a particular part of the array, experiment with the code and identify exactly what it is doing
for student in Mixed_GB:
  if Mixed_GB.index(student) == 0:
    question = input("enter a new piece of data :")
    student.append(question)
print(Mixed_GB)

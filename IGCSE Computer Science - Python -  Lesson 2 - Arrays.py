New_List = []#no data in list
print (New_List)#this will print out list, currently it is empty

#how to add data to the list
New_List.append("Rob")

#Output list with the piece open
print(New_List)

#append second piece of data
New_List.append(7)
#The data item we are cappending is the value 7, it is bad practice to append data of different data types, try to avoid that where necessary
print(New_List)

#how to prefill your list with numbers

Number_List = []#this is a new empty list
for i in range(12):
  Number_List.append(i)
print(Number_List)

#index positions in a list
#How do they work?
#What does the below code do?
Number_List.insert(4, 99999)
Number_List.insert(7,"Bob")

print(Number_List)

#Teacher name goes at the beginning of the list
#now add 5 friend names
Year_10 = ["rob","Harry"]

#removing data from a list
Year_10.remove("Harry")
print(Year_10)

#Deleting an item of data from an index position without knowing the actual piece of data you are deleting
del(Number_List[8])
print(Number_List)
#What data item did this remove from Number_List?

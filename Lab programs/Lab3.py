#Mean, Variance and Standard Deviation

n = int(input("Enter the number students: "))
list1 = []
for i in range(n):
  marks = int(input("Enter marks of each student in python: "))
  list1.append(marks)
print("List containing marks of student: ", list1)
print("-"*50)
sum = 0 
for i in list1:
  sum += i
print("Sum of all the elements in the list: ", sum)
x_bar = sum/len(list1)
print("Mean: ", x_bar)
var = 0 
for i in list1:
  var = var + ((i - x_bar)**2)/len(list1)
print("Variance: ", var)
std_dev = var**0.5
print("Standard Deviation: ", std_dev)

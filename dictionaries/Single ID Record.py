a = {}
a['Emp_Name'] = input('Enter employee name : ')
a['ID'] = input('Enter employee ID :  ')
a['Age'] = input('Enter employee Age :  ')
a['Salary'] = input('Enter employee salary :  ')

print("\n\n-----------EMPLOYEE STATUS-----------------")

for key, value in a.items():
	print(key,": ", value)
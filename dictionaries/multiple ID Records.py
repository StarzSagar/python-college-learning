n = int(input("How many students data you wanna insert ?\n : "))
a={}

# Input taking Part

for i in range(1,n+1):
	print("\n----Enter Student ",i," Details----")
	a[i]=[input(" Enter Student Name : "),input(" Enter Student Roll No. : "),input(" Enter student Age : "),input(" Enter Student Marks : ")]






# Printing Part

print("\n\n------------RECORDS--------------\n")

				

b=['Name : ','Roll No : ','Age : ','Marks : ']
for j in range(1,n+1):
	print("\n----STUDENT ",j," Details----")
	for k in range(4):
		print(b[k],a[j][k])

	
	
	

x = ['first', 'second', 'third', 'fourth', 'fifth']
y = []
print("\n-----MARKS PERCENTAGE CONVERTER-----")
for i in range(5):
    marks = int(input(f"Enter marks of {x[i]} subject : "))
    y.append(marks)

z = sum(y)
percentage = (z/500)*100
print(f"\nTotal Marks : {z}")
print(f"Percentage : {percentage}%")

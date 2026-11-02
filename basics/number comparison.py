a,b,c,d = input("Enter four numbers :").split()
if a>=b and a>=c and a>=d :
	print(a ," is the greatest")
elif b>=c and b>=d :
	print(b," is the greatest")
elif c>=d :
	print(c," is the greatest")
else :
	print(d," is the greatest")
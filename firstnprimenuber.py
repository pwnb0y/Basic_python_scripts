#python script to print first n prime number
n=int(input("Enter any number"))
for i in range(n+1):
	if i<2:
		print(i,"is not prime")
	else:
		for j in range(2,i):
			if i%j==0:
				print(i,"is not prime")
				break
		else:
		 print(i,"is prime")
		 
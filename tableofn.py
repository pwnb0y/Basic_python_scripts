#python script to find table of given number
def table(n):
	for i in range(1,11):
		result=print(i,'x',n,'=',i*n)
	return(result)
table(int(input("[+]Enter a number:")))
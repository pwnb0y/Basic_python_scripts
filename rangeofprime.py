for num in range (1,20):
	if num<2:
		print("%d is not prime"%(num))
	else:
		for i in range(2,num):
			if num%i==0:
				j=num/i
				print("%d is equal to %d * %d"%(num,i,j))
				break
		else:
		 print("%d is Prime"%(num))		

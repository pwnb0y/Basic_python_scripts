#python script to remove dublicate from string
names=[]
n=int(input('Enter how many numbers you wan to enter'))
for i in range(n):
	print(i+1,"Enter name")
	names.append(input())
r=set(names)
names=list(r)
for x in names:
   print(x ,end=" ")
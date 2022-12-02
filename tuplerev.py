#python script to reverse a tuple
#list is mutable
#tuple is immutable

#for reverse in list
l=[1,2,3,4,5,6]
l.reverse()
print(l)
# for reverse in tuple
print(" " and "#"*30)
t=eval(input("Enter numbers separated by comma"))
print("User entered tuple is",t)
l=list(t)
l.reverse()
t=tuple(l)
print("Reverse of tuple is",t)
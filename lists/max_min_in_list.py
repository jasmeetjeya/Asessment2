count=int(input("enter the number of elements:"))
list=[]
for i in range (1,count+1):
    value=int(input("enter the element:"))
    list.append(value)
print(list)
print("the maximum element in a list: ",end='')
print(max(list))
print("the  minimum element in a list: ",end='')
print(min(list))
def LinearSearch(A,key):
    lengthOfArray=len(A)
    index=0
    while index < lengthOfArray:
        if A[index]==key:
            return index
        index=index+1
    return "Not Found"
A=[]
n=int(input("Enter lenth of List \n"))
for i in range(0,n):
    j=int(input())
    A.append(j)
print("Original List",*A)
key=int(input("Enter element to be searched \n"))
x=LinearSearch(A,key)
print(x)

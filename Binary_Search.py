# Binary Search using Recursion
"""
This program is to search any element in a list using Binary Search Technique
All the elements must be in sorted form
***
left=Left Index
right=Right Index
A= Array
"""
def BinarySearch(A,key,left,right):
    if left > right:
        return "Element Not Found"
    else:
        mid=(left+right)//2
        if key==A[mid]:
            return mid
        elif key < A[mid]:
            return BinarySearch(A,key,left,mid-1)
        elif key > A[mid]:
            return BinarySearch(A,key,mid+1,right)

def main():
    n=int(input("Enter length of sorted Array : "))
    A=[]
    for i in range(0,n):
        x=int(input())
        A.append(x)
    print("Before Searching ",*A)
    x=int(input("Enter element to search"))
    search=BinarySearch(A,x,0,n-1)
    print("At index ",search)
if __name__=="__main__":
    main()
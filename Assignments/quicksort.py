#[9. 3, 5, 2, 6, 7, 3]

def quick_sort(n): 
    #Set pivot as the last number 
    pivot = n[-1]
 
  # l irst nymber from the left that is lARGER
  # r number from the right is SMALLER 

    #Find l 
    for num in n:
      if num > pivot:
        l = n[i]
        lPos = i 
        break
      
    #Find r
    for i in range(len(n)-1, -1, -1):
        if n[i] < pivot:
           rPos = n[i]
           break
  
     #Check if l index is greater than r index 
    if lPos > rPos:
     #Switch pivot with item from left
    n[lPos], n
    else:  
    #Swap l and r vaules
   
    n[lPos] = n[rPos], n[lPos]

    print (n)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
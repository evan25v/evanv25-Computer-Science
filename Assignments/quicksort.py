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
    else:  
    #Swap l and r vaules
   
     n[lPos] = n[rPos], n[lPos]

    print (n)


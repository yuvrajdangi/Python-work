import array as ar

def SumofArray(arr):
    sum=0
    n = len(arr)
    for i in range(n):
        sum = sum + arr[i]
    return sum
  
#input values to list 
a = ar.array('i',[10, 21, 12, 13])
  
# display sum 
print ('Sum of the array is ', SumofArray(a) )
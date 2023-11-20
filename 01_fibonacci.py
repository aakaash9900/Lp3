def fibrecursive(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
         return fibrecursive(n-1) + fibrecursive(n-2)

def fibIter(n):
    prevNum = 0
    currrentNum = 1
    for i in range(1, n):
        prevPrevNum = prevNum
        prevNum = currrentNum
        currrentNum = prevNum + prevPrevNum
    return currrentNum


if __name__ == "__main__":
    n = int(input("Enter a Number:"))
    init = time.time()
    print ("Fibonacci Number using recursive is:  ", fibrecursive(n))
    #print("Fibonacci Number using Iterative is:  ", fibIter(n))
    print("Time taken: ",time.time() - init),"seconds"
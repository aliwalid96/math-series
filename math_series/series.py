# function fibonacci(n) {

#     if (n == 0) {
#         return 0;
#     } else if (n == 1) {
#         return 1;
#     } else {
#         return fibonacci(n - 1) + fibonacci(n - 2);

#     }

# }
def fibonacci(n):
    """
    The Fibonacci sequence is a type series where each number is the sum of the two that precede it.
     It starts from 0 and 1 usually. 
     The Fibonacci sequence is given by 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on. 
     The numbers in the Fibonacci sequence are also called Fibonacci numbers
    """

    if n==0:
        return 0
    elif n  ==1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
    Lucas numbers are similar to Fibonacci numbers.
     Lucas numbers are also defined as the sum of its two immediately previous terms.
      But here the first two terms are 2 and 1 whereas in Fibonacci numbers the first two terms are 0 and 1 
      respectively. 
    """
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
    

def sum_series(n,n1=0,n2=1):
        """
        recursive function if n1=0,n2=1 will call fibonacci and if n1=1,n2=1 will weok
        like lucas  
        """
        if n==0 :
           return n1
        elif n==1:
            return n2
        return sum_series(n-1,n1,n2)+sum_series(n-2,n1,n2)






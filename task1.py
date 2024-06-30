

# Code Alpha Task-1

# **** FABONACCI GENERATOR ****

def fibonacci(n):

    print("**** Enter The No of Fibonacci Sequence ****")

    fib_series = []
    a , b = 0 , 1                    # Initialize first two fabonacci numbers
    
    for _ in range(n):
        fib_series.append(a)        # Append the current Fibonacci number to the series

        a , b = b , a + b           # Update Fibonacci numbers: a becomes b, and b becomes the sum of a and b
    
    return fib_series


n = 10                              # Generate Fibonacci series up to the 10th term (0-indexed)
print(fibonacci(n))

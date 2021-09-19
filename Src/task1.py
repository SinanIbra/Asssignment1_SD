import time
def decorator1(func):
    '''Function decorator which executes the passed in function and prints its execution time, and the number of times it is called.'''


    
    def wrapper(*args, **kwargs):
        wrapper.count +=1
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__

        timeS = time.perf_counter()
        output = func(*args, **kwargs)
        e_time = time.perf_counter() - timeS
        
        print("function name is ",func.__name__, "and it was called" ,wrapper.count, "times.")
        print("execution time of this function is: ",'{0:.7f}'.format(e_time)," seconds.",'\n')

        return output
    wrapper.count = 0
    return wrapper

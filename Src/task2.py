import contextlib
import inspect
import time
import io

def decorator2(fun):
    ''' decorator 2 for task 2 to show details of objects
        counting how many times did we call it and execution time'''
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        with contextlib.redirect_stdout(io.StringIO()) as f:
            start = time.perf_counter()
            fun(*args, **kwargs)
            end = time.perf_counter()
        out = f.getvalue()
        print(f"{fun.__name__} call {wrapper.count} executed in " +
              '{0:.7f}'.format(end-start)+" sec")
        print("Name:\t", fun.__name__)
        print("Type:\t", type(fun))
        print("Sign:\t", inspect.signature(fun))
        print("Args:\t", "positional ", args, "\n", "\tkey=worded ", kwargs)
        print("Doc:\t", fun.__doc__, sep='\t')
        print("Source:", *inspect.getsourcelines(fun)[0], sep='\t')
        print(f"Output:\t", out)
    wrapper.count = 0
    return wrapper

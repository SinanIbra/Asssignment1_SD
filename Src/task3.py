import contextlib
import inspect
import time
import io

fun_table = []
class decorator3:
    """ decorator 3 sends the specifications of a function to output.txt and sorts the functions by the execution time"""
    def __init__(self, fun):
        self.fun = fun
        decorator3.count = 0

    def __call__(self, *args, **kargs):
        decorator3.count += 1
        global fun_table
        result = []
        with contextlib.redirect_stdout(io.StringIO()) as f:
            s = time.perf_counter()
            res = self.fun(*args, **kargs)
            e = time.perf_counter()
        out = f.getvalue()
        with open('output.txt', 'a') as w:
            w.writelines(f"{self.fun.__name__} call {decorator3.count} executed in "+'{0:.7f}'.format(e-s)+" sec\n")
            w.writelines(f"Name:\t{self.fun.__name__}\n")
            w.writelines(f"Type:\t{type(self.fun)}\n")
            w.writelines(f"Sign:\t{inspect.signature(self.fun)}\n")
            w.writelines(f"Args:\tpositional {args}\n\tkey=worded{kargs}\n")
            w.writelines(f"Doc:\t{self.fun.__doc__}\n")
            temp = '\t'
            w.writelines(f"Source:{temp.join([line for line in inspect.getsourcelines(self.fun)[0]])}")
            w.writelines("\n")
            w.writelines(f"Output:\t{res}")
            w.writelines("\n")
        fun_table.append((self.fun.__name__, e-s))
        decorator3.count = 0
        print(result)
        return result

def print_t3_table():
    fun_table.sort(key=lambda x: x[1])
    ''' sort by second element in the list (execution time'''
        
    result = [[fun[0], i, '{0:.9f}'.format(fun[1])+"s"] for i, fun in enumerate(fun_table)]
    print("   Method    ", " RANK    ", "  TIME")
    for i in range(0,len(result)):
        print (result[i])

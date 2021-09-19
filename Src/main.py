import cmath
from task1 import decorator1
from task2 import decorator2
from task3 import decorator3
from task3 import print_t3_table
from task4 import decorator_fun_4
from task4 import decorator_class_4


#-------# Task 1 #-------#

@decorator1
def loop_for(start,finish):
    for i in range(start,finish):
        x=i

@decorator1
def loop_while(start,finish):
    i=start
    while i <finish:
        i+=1
        x=i
        
loop_for(0,10)
loop_while(0,10)
loop_while(0,100)
loop_while(0,1000000)
loop_for(0,1000000)

#-------# Task 2 #------#
x=2
fun_lambda_A = lambda x: x * x * x # third power of x
fun_lambda_A.__doc__ = "third power lambda function. "
fun_lambda_A = decorator2(fun_lambda_A)

fun_lambda_B = lambda x: x * x  # square of x
fun_lambda_B.__doc__ = "Square lambda function."
fun_lambda_B = decorator2(fun_lambda_B)

fun_lambda_A(1010)
fun_lambda_B(1010)

fun_lambda_A(712)
fun_lambda_B(12)

fun_lambda_A(217)
fun_lambda_B(217)

#-------# Task 3 #-------#
@decorator3
def Pascal_Tri(n):
    """
    Pascal triangle from lab , parameters;  n: height of triangle
    """
    trow = [1]
    y = [0]
    for x in range(max(n,0)):
        print(trow)
        trow = [l + r for l, r in zip(trow + y, y + trow)]
        
@decorator3
def Quad_solve(a, b, c):
    """
    quadratic solver function , parameters;
    a: coefficient before x**2 b: coefficient before x c: last coefficient
    if delta is less than zero; we have complex roots, out of the range of real numbers.
    """
    r1,r2=0,0
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        r1 = (-b - cmath.sqrt(delta)) / (2 * a)
        r2 = (-b + cmath.sqrt(delta)) / (2 * a)
        return r1, r2
    else:
        return -1


Quad_solve(-10, 10, 10)
Pascal_Tri(12)

print_t3_table()


#-------# Task 4 #-------#

@decorator_fun_4
def fun_energy(m):
    '''calculates the energy of a particle when travelling at the speed of light, m is the mass of partical in kg'''
    energy = m * 300000000**2    # e==mc^2, energy in jouls
    return energy

fun_even =lambda x: true if int(x%2==0) else false
fun_even.__doc__ = "returns true if the number is even "
fun_even = decorator_class_4(fun_even)

fun_odd =lambda x: true if int(x%2==1) else false
fun_odd.__doc__ = "returns true if the number is odd "
fun_odd = decorator_fun_4(fun_odd)

print(fun_energy(0.0000001))   #should print the value; the function has no error
print(fun_even("wrong input")) #should print None; the function an error
print(fun_odd("wrong input"))  #should print None; the function an error



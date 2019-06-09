## printing the series and finding the value of the series by substituting 

from sympy import Symbol,pprint,init_printing
init_printing(order='rev-lex')
def print_series(n,x_value):
    x=Symbol('x')
    series= x
    for i in range(2,n+1):
        series = series + (x**i)/i 
    pprint (series)
    series_val=series.subs({x:x_value})
    print (series_val)
n = int(input(' Enter the number of terms you want in the series : '))
x_value=int(input('Enter the value of x : '))
print_series(n,float(x_value))




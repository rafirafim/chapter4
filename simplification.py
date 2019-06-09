from sympy import Symbol,pprint,expand,sympify
from sympy.core.sympify import SympifyError

##defining the function to calculate the product of two expression
def prod(expr1,expr2,n):
    x=Symbol('x')
    product = expand(expr1*expr2)
    val=product.subs({x:n})
    pprint (product)
    print (val)

##taking the value of the expression from the user
expr1=sympify(input('Enter the first expression : '))
expr2=sympify(input('Enter the second expression : '))

## Taking the vale for the substitution of x
n=int(input('Enter the value of x : '))

## Calling the defined function
prod(expr1,expr2,n)
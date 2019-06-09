from sympy import Symbol,pprint,solve,sympify
x=Symbol('x')
y=Symbol('y')
expr1=sympify(input('Enter the first expression '))
expr2=sympify(input('Enter the second expression '))
soln=solve(expr1,expr2)
pprint(expr1)
pprint(expr2)
print (soln)
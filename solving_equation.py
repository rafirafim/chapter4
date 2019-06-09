from sympy import Symbol,solve,sympify
def solve_expr(expr):
    x=Symbol('x')
    solution=solve(expr)
    print (solution)
     
         

expr=sympify(input('Enter the expression :'))

solve_expr(expr)
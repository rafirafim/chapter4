from sympy import Symbol,solve,pprint,sympify
##defining the function to find the solton
def fn( ):
    s=Symbol('s')
    u=Symbol('u')
    t=Symbol('t')
    a=Symbol('a')
    expr=u*t+(1/2)*a*t**2-s
    t_expr=solve(expr,t,dict=True)
    pprint (t_expr)

fn()
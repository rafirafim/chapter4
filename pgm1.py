from sympy import Symbol,pprint
x=Symbol('x')
f= input("Enter the expression : ")
s=int(input("enter the value of x : "))
fs=f.subs({'x':3})
print (f)
pprint (f)
print (fs)
def f(x):
    def g():
        x='abc'
        print 'x_g()=', x
    def h():
        z=x
        print 'z_h()=', z
    x=x+1
    print 'x_f()=', x
    g()
    h()
    print 'x_f()=', x
    return g



x=3
z=f(x)
print 'x_global=', x
print 'z_global=', z
z()

def fun1(a,b=0 , *args , **kwargs):
    print("a =",a)
    print("b =",b)
    print("args: ", args)
    print("kwargs: ", kwargs)
    
fun1(2,3,'python','assignment',first="python",last="assignment")

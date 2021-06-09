"""Division fonction"""
def dividedby_op(a,b):
    """Operation fonction"""
    divided_res= a/b;
    """If condition"""
    if b==0:
        print("Error you cannot divided by 0. Please enter an appropriate number") 
    else:
        print("{0} / {1} = {2}".format(a,b,divided_res))
        


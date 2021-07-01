def sqroot(numb):
    import math
    if not (type(numb) == int):
        raise TypeError('Invalid number.\nPlease enter only integers.')
    else:
        val = math.sqrt(numb)
        return '√ of %.2f is %d' %(numb,val)
    
    """sqroot(2.4)"""
    """sqroot(1)"""
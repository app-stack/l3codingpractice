def div(a,b):
    try:
      res = a/b;
    except ZeroDivisionError:
      print("You cannot divide by zero, sorry.")
      
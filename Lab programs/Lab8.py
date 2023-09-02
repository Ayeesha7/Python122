#Write a function named DivExp which takes TWO parameters
#a, b and returns a value c (c=a/b). Write suitable assertion for
#a>0 in function DivExp and raise an exception for when b=0.
#Develop a suitable program which reads two values from the
#console and calls a function DivExp.

def DivExp(a,b):
  try:
    assert a>0, "Number 'a' is Negative"
    if b==0:
      raise ZeroDivisionError("Zero Division Error")
    c = a/b
    return c
  except ZeroDivisionError as e:
    print(e)
  except AssertionError as e:
    print("Assertion failure: " + str(e))

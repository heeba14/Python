
# To use standard Exceptions as base class
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg
try:
    raise Networkerror("ERROR")
except Networkerror as e:
    print(e.args)
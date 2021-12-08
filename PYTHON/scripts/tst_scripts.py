import os
import sys

try:
  print("__file__: {}".format(os.path.dirname(__file__)))
  abs_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
except:
  print("CWD: {}".format(os.getcwd()))
  abs_dir=abs_dir=os.path.abspath(os.path.join(os.getcwd(), "PYTHON"))
finally:
  print("Everything OK: {}".format(abs_dir))
  sys.path.insert(0, abs_dir)

import projpkg as pp

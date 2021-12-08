# Archivo de contexto para notebooks cuando no se usan desde RStudio / reticulate

import os
import sys

try:
  # Caso normal
  abs_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
  sys.path.insert(0, abs_dir)
except:
  print("Couldn't find __file__. CWD: {}".format(os.getcwd()))
  


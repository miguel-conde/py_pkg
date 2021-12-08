# Archivo de contexto para ejecución de scripts desde RStudio / reticulate

import os
import sys

try:
  # RStudio / reticulate
  abs_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), "PYTHON"))
  sys.path.insert(0, abs_dir)
except:
  print("Couldn't find __file__.CWD: {}".format(os.getcwd()))
  


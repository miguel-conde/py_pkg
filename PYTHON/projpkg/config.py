from pathlib import Path
import os
import sys

try:
  PY_HOME=os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
except:
  # RStudio / Reticulate
  PY_HOME=abs_dir=os.path.abspath(os.path.join(os.getcwd(), "PYTHON"))
  print("CWD: {}".format(PY_HOME))
finally:
  # print("Everything OK. PY_HOME: {}".format(PY_HOME))
  DATA_DIR = Path(PY_HOME, 'data')
  DL_DIR = Path(DATA_DIR, "datalake")
  DW_DIR = Path(DATA_DIR, "datawarehouse")
  DL_FILE_HOUSING = Path(DL_DIR, "housing_data.csv")

URI_DATASET = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'



import csv
import os

from surprise import SVD
from surprise import Dataset
from surprise import Reader

def get_grades():
  return {
    "014": {
      0: {"course": "TIRA", "grade": 5, "generated": True},
      1: {"course": "TITO", "grade": 4, "generated": False},
      2: {"course": "OHPE", "grade": 3, "generated": False}
    },
    "015": {
      0: {"course": "TIRA", "grade": 1, "generated": True},
      1: {"course": "TITO", "grade": 2, "generated": False},
      2: {"course": "OHPE", "grade": 2, "generated": False}
    }
  }
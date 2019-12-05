import csv
import os
import pandas as pd

from surprise import SVD
from surprise import Dataset
from surprise import Reader

def get_grades(algo, id, courses):
  grades = {}
  for c in courses:
    result = algo.predict(str(id), c)
    grades[c] = result.est

  return grades
  }

def get_fit(df):
  reader = Reader(rating_scale=(1, 5))
  data = Dataset.load_from_df(df[['id', 'course', 'grade']], reader)
  algo = SVD()
  return algo.fit(data.build_full_trainset())

def update_model(df, id, course_grades_dict):
  for c in course_grades_dict.keys():
    df = df.append({'id': str(id), 'course': c, 'grade': str(course_grades_dict[c])}, ignore_index=True)
  return df

def load_data(path)
    df = pd.read_csv(path, sep = ",", parse_dates = True)
    del df['date']
    return df


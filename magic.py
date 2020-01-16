import csv
import os
import pandas as pd

from surprise import SVD
from surprise import Dataset
from surprise import Reader

path = '/srv/flask_app/data/credits.csv'

# courses_dict should be a python dictonary with course names as keys and grades as values


def get_grades(course_grades_dict):
    df = load_data(path)
    df = update_data(df, "1", course_grades_dict)
    algo = get_fit(df)

    grades = {}
    for c in pd.unique(df.course):
        result = algo.predict(str("1"), c)
        grades[c] = result.est

    return grades


def get_fit(df):
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df[['id', 'course', 'grade']], reader)
    algo = SVD()
    return algo.fit(data.build_full_trainset())

# course_grades_dict should be a python dictionary where keys are the course names
# and values are grades from those courses
# id should be a number
# This function adds the courses that the student has done into the pandas dataframe


def update_data(df, id, course_grades_dict):
    for c in course_grades_dict.keys():
        df = df.append({'id': str(id), 'course': c, 'grade': str(
            course_grades_dict[c])}, ignore_index=True)
    return df

# This loads a csv-file from a location defined by path
# Returns the dataset as a pandas dataframe


def load_data(path):
    print(os.getcwd())
    df = pd.read_csv(path, sep=",", parse_dates=True)
    del df['date']
    return df

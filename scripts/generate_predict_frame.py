import pandas as pd
from datetime import date, datetime, timedelta
from os import makedirs
from os.path import exists
import csv
from random import randint
from time import time
import argparse
import logging

calls_hour_output_path = "/home/schiessl/Verteego/demos/callcenter-demo/data/ml-predict/predict-calls-hour.csv"

first_day_to_predict = date.today()
nb_days_to_predict = 30
hours_range = range(0,24)
priority_list = [0, 1, 2]
reason_list = []

#weekdays config
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


date_range = pd.date_range(start=first_day_to_predict, end=first_day_to_predict + timedelta(days=nb_days_to_predict),freq="H")
df = pd.DataFrame(index=date_range)
df["year"] = df.index.year
df["month"] = df.index.month
df["day"] = df.index.day
df["weekday"] = df.index.weekday
df["weekday"] = df["weekday"].map(lambda x: weekdays[x])
df["hour"] = df.index.hour
df.to_csv(calls_hour_output_path, index=False)


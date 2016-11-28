import pandas as pd
from datetime import date, timedelta, datetime
import argparse

# set possible arguments
parser = argparse.ArgumentParser(description="Predict y depending on x")
parser.add_argument('--nb_days', '-n', help="Number of days of the prediction.", action="store", type=int, default=1)
parser.add_argument('--date', '-d', help="Date of the first day of the forecast", action="store",
                    default=date.today())
parser.add_argument('--start_hour', '-s', help="First hour of the day.", action="store", type=int, default=0)
parser.add_argument('--end_hour', '-e', help="Last hour of the day.", action="store", type=int, default=23)
parser.add_argument('--mode', '-m', help="Prediction mode. use 'default', 'priority' or 'reason' ", action="store", default="default")

# parse arguments
args = parser.parse_args()

# parse date from string if necessary
args.date = datetime.strptime(str(args.date), "%Y-%m-%d")

#output path
calls_hour_output_path = "/home/schiessl/Verteego/demos/callcenter-demo/data/ml-predict/"

# weekdays config
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# lists of items to be used
lists = {
    "default" : [0],
    "priority" : [0, 1, 2],
    "reason" : ["TT", "AA", "IN", "NE", "NW", "PE", "PS"]
}

# generate all data frames
df = {}
for i in lists[args.mode]:
    df[i] = pd.DataFrame(index=pd.date_range(start=args.date, end=args.date + timedelta(days=args.nb_days),freq="H", closed="left"))
    #df[i]["nb_calls"] = 0
    df[i][args.mode] = i
    df[i]["year"] = df[i].index.year
    df[i]["month"] = df[i].index.month
    df[i]["day"] = df[i].index.day
    df[i]["weekday"] = df[i].index.weekday
    df[i]["weekday"] = df[i]["weekday"].map(lambda x: weekdays[x])
    df[i]["hour"] = df[i].index.hour


#merge data frames
df_final = pd.concat([value for value in df.itervalues()])

#write to csv
df_final.to_csv(calls_hour_output_path + "predict-calls-" + args.mode + ".csv", index=False)

print df_final
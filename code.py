import pandas as pd
import csv
import plotly.graph_objects as graph_objects

df = pd.read_csv("data1.csv")
print(df.groupby("level")["attempt"].mean())

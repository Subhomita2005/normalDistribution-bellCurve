import pandas as pd
import csv
import plotly.figure_factory as ff
df = pd.read_csv("HeightWeight.csv")
fig=ff.create_distplot([df["Weight(Pounds)"].tolist()],["weight"],show_hist=False)
fig.show()
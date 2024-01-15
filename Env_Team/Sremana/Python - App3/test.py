import pandas as pd

from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Day'] = data['Timestamp'].dt.date
#data['Day'] = pd.to_numeric(data['Day'], errors='coerce')
day_average = data.groupby(['Day']).mean('Day')
print(data.dtypes)
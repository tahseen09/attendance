import pandas as pd

path = "OS.csv"
csv = pd.read_csv(path)
count = csv['Roll'].value_counts()
print(count)

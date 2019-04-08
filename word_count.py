import pandas as pd

csv = pd.read_csv("OS.csv")
count = csv['Roll'].value_counts()
print(count)

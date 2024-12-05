# review ex3
# From marks.csv write a python script that uses pandas to:
# -prints student names sorted by their marks
# -prints avg mark

import pandas as pd

data = pd.read_csv('marks.csv')

sorted_data = data.sort_values(by='Mark', ascending=False)

print("Students sorted by their marks:")
print(sorted_data['Name'].to_string(index=False))

average_mark = data['Mark'].mean()
print(f"\nAverage mark: {average_mark:.2f}")


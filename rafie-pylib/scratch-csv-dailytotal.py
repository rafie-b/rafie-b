import csv
import matplotlib.pyplot as plt
import numpy as np

dates = []
daily_sum = []

# Open the CSV file
try:
    with open('/content/drive/MyDrive/Climate-Sense/deslizamentos-test.csv', 'r', encoding='utf-8') as csvfile:
        # Use ';' as the delimiter
        csvreader = csv.reader(csvfile, delimiter=';')
        # Skip the header row
        next(csvreader)
        # Loop through each row
        for row in csvreader:
            # Append the date and daily sum to their respective lists
            dates.append(row[0])
            daily_sum.append(int(row[1]))
except UnicodeDecodeError:
    with open('/content/drive/MyDrive/Climate-Sense/deslizamentos-test.csv', 'r', encoding='iso-8859-1') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        next(csvreader)
        for row in csvreader:
            dates.append(row[0])
            daily_sum.append(int(row[1]))

# Plot the line chart
fig, ax = plt.subplots(figsize=(12,3))
ax.plot(dates, daily_sum)
ax.set_xlabel('Date')
ax.set_ylabel('Daily Sum')
ax.set_title('Daily Sum over Time')

# Customize the x-axis
x_ticks = np.arange(0, len(dates), 60)
ax.set_xticks(x_ticks)
ax.set_xticklabels(dates[::60], rotation=45, ha='right')#, fontsize=6)

plt.show()

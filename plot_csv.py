import pandas as pd
import matplotlib.pyplot as plt

csv_file_path = "/path/to/y_at_x_0.csv"

df_y_at_x_0 = pd.read_csv(csv_file_path)

print(df_y_at_x_0.head(100))

df_y_at_x_0.plot(x="time", y="y")
plt.show()

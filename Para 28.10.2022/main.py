# room12 = WaterCounter(1, 2, 34, 45)
# room22 = WaterCounter(2, 2, 4, 5)
# room32 = WaterCounter(3, 2, 654, 658)
#
# room13 = WaterCounter(1, 3, 215, 217)
# room23 = WaterCounter(2, 3, 245, 247)
# room33 = WaterCounter(3, 3, 8, 9)
#
# room14 = WaterCounter(1, 4, 54, 76)
# room24 = WaterCounter(2, 4, 3, 4)
# room34 = WaterCounter(3, 4, 1, 6)

class WaterCounter:
    def __init__(self, room_number, month_number, current_water, previous):
        self.room_number = room_number
        self.month_number = month_number
        self.current = current_water
        self.previous = previous

import pandas as pd
df = pd.read_csv("water_data.txt")

df["water"] = df[" prev_counter"] - df[" counter"]
df["Price"] = df["water"] * 2.5
import matplotlib.pyplot as plt

plt.plot(df["Price"])
plt.show()



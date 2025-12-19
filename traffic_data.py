import pandas as pd
import numpy as np

np.random.seed(42)

def generate_traffic_data(days=90):
    data = []
    for day in range(days):
        for minute in range(16 * 60, 18 * 60, 5):  # 16:00-18:00
            hour = minute // 60
            is_peak = 1 if 16.5 <= hour + (minute % 60)/60 <= 17.5 else 0
            
            vehicles = int(
                50 +
                is_peak * np.random.randint(80, 200) +
                np.random.randint(-10, 10)
            )
            pedestrians = vehicles * np.random.randint(2, 4)

            data.append([
                day, hour, is_peak, vehicles, pedestrians
            ])

    return pd.DataFrame(
        data,
        columns=["day", "hour", "is_peak", "vehicles", "pedestrians"]
    )

df = generate_traffic_data()
df.to_csv("traffic.csv", index=False)
print(df.head())

import os
import pandas as pd

# # CONSTANTS
WEATHER_FILE = "weather_data.csv"
SQUIRREL_FILE = "squirrel_census.csv"

cwd = os.path.dirname(os.path.relpath(__file__))

# Print the hottest temperature of the data in Farheneit
weather_path = cwd + "/" + WEATHER_FILE
data = pd.read_csv(weather_path)
hottest_day = data[data["temp"] == data["temp"].max()]
hottest_temp_farheneit = (hottest_day.temp.values[0] * 9/5 ) + 32
print(f"Hottest temperature: {hottest_temp_farheneit}°F")

# Create a csv containing the amount of squirrels based on fur color
squirrel_path = cwd + "/" + SQUIRREL_FILE
data = pd.read_csv(squirrel_path)
fur_types = data["Primary Fur Color"].value_counts()
fur_data_df = pd.DataFrame({"Fur Color": fur_types.index, "Count": fur_types.values})
fur_data_df.to_csv(cwd + "/squirrel_fur_census.csv")

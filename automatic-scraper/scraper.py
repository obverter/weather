# To add a new cell, type ''
# To add a new markdown cell, type ' [markdown]'

# sourcery skip: for-index-underscore
import pandas as pd
import requests
from secrets import TOKEN, STATION


response = requests.get(
    f"https://swd.weatherflow.com/swd/rest/observations/station/{STATION}?token={TOKEN}"
)

weather = response.json()
current = pd.DataFrame(weather["obs"])


# This is reading the headlines.csv file and converting it to a dataframe.
existing = pd.read_csv("weather.csv", index_col=[0])
# existing = pd.read_csv("weather.csv")


# Creating a list of dataframes, and then concatenating them.

export = pd.concat([current, existing])

export = export.sort_values(
    by=["timestamp"],
    ascending=[False],
    ignore_index=True,
)

export = export.drop_duplicates(subset=["timestamp"], keep="first")

# Writing the dataframe to a csv file.
export.to_csv("weather.csv")
export.to_json("weather.json")

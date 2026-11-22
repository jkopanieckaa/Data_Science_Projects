import pandas as pd
from functions import get_specific_demand_days, weather_demand_stats, compare_weather_demand

df = pd.read_csv("day.csv")
high_demand = get_specific_demand_days(df, 6000)
print(f"High demand days count: {high_demand.shape[0]}")

assert (high_demand['cnt'] > 6000).all()
assert not high_demand.empty

clear_average_demand, clear_days_count = weather_demand_stats(df,1)
print(f"Average demand on days with clear skies ({clear_days_count}): {round(clear_average_demand,2)} bike rentals per day")

misty_cloudy_average_demand, misty_cloudy_days_count = weather_demand_stats(df,2)
print(f"Average demand on misty or cloudy days ({misty_cloudy_days_count}): {round(misty_cloudy_average_demand,2)} bike rentals per day")

result = compare_weather_demand(df, 1, 2)
if result is not None:
    rental_difference, percentage_difference = result
    print(f"Difference: {rental_difference:.2f} rentals per day")
    print(f"Percentage difference: {percentage_difference:.2f}%")





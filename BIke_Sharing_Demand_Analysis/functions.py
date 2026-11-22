import streamlit as st

def get_specific_demand_days(df, threshold):
    high_demand_days = df.loc[df['cnt'] > threshold]
    return high_demand_days[['dteday','season','temp','cnt']]

def weather_demand_stats(df, weather_code):
    weather_days = df.loc[df['weathersit'] == weather_code]
    mean = weather_days['cnt'].mean()
    days_count = weather_days.shape[0]
    return mean, days_count

def compare_weather_demand(df,weather_code_1,weather_code_2):
    average_demand_1, days_count_1 = weather_demand_stats(df,weather_code_1)
    average_demand_2, days_count_2 = weather_demand_stats(df,weather_code_2)

    if days_count_1 == 0:
        print(f"No observations found for weather code: {weather_code_1}")
        return None
    elif days_count_2 == 0:
        print(f"No observations found for weather code: {weather_code_2}")
        return None

    difference_in_demand = average_demand_1 - average_demand_2
    percentage_difference = difference_in_demand / average_demand_2 *100
    return difference_in_demand, percentage_difference








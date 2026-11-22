import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Bike Sharing Demand Analysis")
st.markdown("This [dataset](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset) contains daily bike rental counts for 2011 and 2012")
df = pd.read_csv('day.csv')

year = st.pills("Select year:",('2011','2012'), selection_mode="single")
month = st.pills('Select month:',['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], selection_mode = 'single')
weather = st.pills('Select weather condition:',['Clear skies or partly cloudy','Mist or cloudy','Light snow or rain'], selection_mode = 'single')
if year is None and month is None and weather is None:
    info = st.caption('If none of the above options is selected, the results will contain all data')

months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
          'Nov': 11, 'Dec': 12}
years = {'2011': 0,'2012': 1}
weather_dict = {'Clear skies or partly cloudy': 1,'Mist or cloudy': 2,'Light snow or rain': 3}


filtered_df = df.copy()
if year is not None or month is not None or weather is not None:
    if year is not None:
        filtered_df = filtered_df[filtered_df['yr'] == years[year]]

    if month is not None:
        filtered_df = filtered_df[filtered_df['mnth'] == months[month]]

    if weather is not None:
        filtered_df = filtered_df[filtered_df['weathersit'] == weather_dict[weather]]



st.dataframe(filtered_df,height=250)

if not filtered_df.empty:
    rentals_count = filtered_df['cnt'].sum()
    avg_daily_rentals = int(round(filtered_df['cnt'].mean(),0))
    days_analyzed = filtered_df.shape[0]

    col1, col2, col3 = st.columns(3)
    col1.metric("Rentals count",rentals_count)
    col2.metric("Average daily rentals",avg_daily_rentals)
    col3.metric("Days analyzed",days_analyzed)

    filtered_df['dteday'] = pd.to_datetime(filtered_df['dteday'])

    if month is not None or weather is not None:
        fig_rentals = px.line(filtered_df, x = 'dteday',y = 'cnt', markers = True)
        fig_rentals.update_layout(xaxis_title='Date',yaxis_title='Rentals count')
        st.plotly_chart(fig_rentals)
    elif (month is None and year is not None) or (month is None and year is None and weather is None):
        monthly_demand = filtered_df.groupby(['yr', 'mnth'])['cnt'].mean().reset_index()
        monthly_demand['date'] = pd.to_datetime(dict(year=monthly_demand['yr'] + 2011, month=monthly_demand['mnth'], day=1))
        fig_rentals = px.line(monthly_demand, x='date', y='cnt', markers=True)
        st.plotly_chart(fig_rentals)
else:
    st.error("No data found for the selected filters")
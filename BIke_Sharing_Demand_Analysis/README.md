# 🚲 Bike Sharing Demand Analysis

An interactive data analytics project exploring daily bike rental demand in 2011 and 2012. It combines exploratory data analysis (EDA) in Jupyter Notebook with a **Streamlit dashboard** built using **Python, Pandas, and Plotly**.

**Dataset:** [Bike Sharing Dataset — UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset)

## Project overview

The goal is to understand how bike rental demand changed over time and how it varies across seasons and weather conditions. The project also provides an interactive way to explore the underlying data.

Key questions include:

- How did bike rental demand change between 2011 and 2012?
- Which months had the strongest year-over-year growth?
- How does average daily demand differ between weather conditions?

## Dashboard features

- **Interactive filters:** select a year, month, and weather condition - leave filters unselected to examine all available data.
- **Data table:** inspect the records matching the current filters.
- **Summary KPIs:** total rentals, average daily rentals, and number of days analyzed for the current selection.
- **Rental demand trend:** daily rental counts for detailed selections, or monthly average daily rentals for a broader time view.
- **Year-over-year comparison:** monthly average daily rentals in 2011 versus 2012, shown as two lines.
- **Weather comparison:** average daily rentals across weather categories.


The year-over-year and weather comparison charts summarize the **entire dataset** and do not change with the main filters.

## Selected findings

These findings come from the project's exploratory analysis of the UCI daily dataset:

| Finding                     | Result |
|-----------------------------| --- |
| Clear / partly cloudy days  | About **4,876.79** rentals per day on average |
| Misty / cloudy days         | About **4,035.86** rentals per day on average |
| March 2012 vs March 2011    | Average daily rentals rose from **2,065.97** to **5,318.55** (**+157.44%**) |
| January–December comparison | Average daily rentals were higher in 2012 than in the corresponding month of 2011 for every month examined |



## Project structure

```text
Bike_Sharing_Demand_Analysis/
├── app.py                     # Streamlit dashboard 
├── data_exploration.ipynb     # Exploratory analysis and visualizations
├── day.csv                    # Original daily rental dataset
└── README.md                  # Project documentation
```

## Getting started

**1. Clone or download the repository**, then open the project folder in a terminal.

**2. Install the required packages:**

```bash
python -m pip install requirements.txt
```

**3. Launch the dashboard in project directory**:

```bash
python -m streamlit run app.py
```

Streamlit will display a local URL, typically `http://localhost:8501`, where you can use the dashboard.

## Tools

**Python · Pandas · NumPy · Matplotlib · Plotly · Streamlit · Jupyter Notebook**


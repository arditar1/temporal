#pip install streamlit # Install streamlit first
import streamlit as st # Then import it
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Your Streamlit app code here
st.title("Hello, Streamlit!")

st.set_page_config(page_title="Bike Sharing Analysis", layout="centered")

st.title("Bike Sharing Ridership Analysis")

url = "https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/bike_sharing.csv"
df = pd.read_csv(url)

df['dteday'] = pd.to_datetime(df['dteday'])

df = df.sort_values('dteday')

st.subheader("Total Ridership Over Time")
fig1, ax1 = plt.subplots()
ax1.plot(df['cnt']) 
st.pyplot(fig1)
# Load the dataset
url = "https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/bike_sharing.csv"
df = pd.read_csv(url)

# Convert 'dteday' column to datetime
df['dteday'] = pd.to_datetime(df['dteday'])

# Sort by date (just in case)
df = df.sort_values('dteday')

# Plot total ridership over time
plt.figure(figsize=(10, 5))
plt.plot(df['dteday'], df['cnt'], color='blue')
plt.xlabel('Date')
plt.ylabel('Total Ridership')
plt.title('Total Bike Ridership Over Time')
plt.grid(True)
plt.tight_layout()
plt.show()
# Load the dataset
url = "https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/bike_sharing.csv"
df = pd.read_csv(url)

# Map numeric seasons to names
season_map = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
df['season_name'] = df['season'].map(season_map)

# Group by season and sum total ridership
season_totals = df.groupby('season_name')['cnt'].sum().reindex(['Winter', 'Spring', 'Summer', 'Fall'])

# Plot
plt.figure(figsize=(8, 5))
plt.bar(season_totals.index, season_totals.values, color='skyblue')
plt.xlabel('Season')
plt.ylabel('Total Ridership')
plt.title('Total Ridership by Season')
plt.tight_layout()
plt.show()
# Load the dataset
url = "https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/bike_sharing.csv"
df = pd.read_csv(url)

# Convert date column
df['dteday'] = pd.to_datetime(df['dteday'])
df = df.sort_values('dteday')

# Title
st.title("📈 Rolling Average / Weekly Total Ridership")

# Radio button for user selection
option = st.radio(
    "Select plot type:",
    ("7-day average", "14-day average", "Weekly total")
)

# Plot based on selection
fig, ax = plt.subplots(figsize=(10, 5))

if option in ["7-day average", "14-day average"]:
    window = 7 if option == "7-day average" else 14
    df['rolling'] = df['cnt'].rolling(window=window).mean()
    ax.plot(df['dteday'], df['cnt'], label='Daily Ridership', alpha=0.4)
    ax.plot(df['dteday'], df['rolling'], label=f'{window}-day Rolling Average', color='red')
    ax.set_title(f"{window}-Day Rolling Average of Ridership")

elif option == "Weekly total":
    df_weekly = df.set_index('dteday').resample('W')['cnt'].sum()
    ax.plot(df_weekly.index, df_weekly.values, label='Weekly Total Ridership', color='green')
    ax.set_title("Total Ridership by Week")

# Common axis labels
ax.set_xlabel("Date")
ax.set_ylabel("Total Ridership")
ax.legend()
ax.grid(True)
st.pyplot(fig)

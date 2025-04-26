import pandas as pd
import os
from glob import glob

# Define seasonal month mapping (Australian seasons)
season_months = {
    'Summer': ['December', 'January', 'February'],
    'Autumn': ['March', 'April', 'May'],
    'Winter': ['June', 'July', 'August'],
    'Spring': ['September', 'October', 'November']
}

def load_all_temperatures_data(folder_path):
    files = glob(os.path.join(folder_path, "*.csv"))
    all_data = [pd.read_csv(file) for file in files]
    return pd.concat(all_data, ignore_index=True)

def calculate_seasonal_averages(df):
    seasonal_avg = {}
    for season, months in season_months.items():
        valid_months = [month for month in months if month in df.columns]
        seasonal_avg[season] = df[valid_months].mean().mean()
    return seasonal_avg

def find_largest_temperatures_range(df):
    months = [m for m in season_months['Summer'] + season_months['Autumn'] + 
              season_months['Winter'] + season_months['Spring'] if m in df.columns]
    df['MaxTemp'] = df[months].max(axis=1)
    df['MinTemp'] = df[months].min(axis=1)
    df['Range'] = df['MaxTemp'] - df['MinTemp']
    max_range = df['Range'].max()
    return df[df['Range'] == max_range]['STATION_NAME'].unique().tolist()

def find_warmest_and_coolest_stations(df):
    months = [m for m in season_months['Summer'] + season_months['Autumn'] + 
              season_months['Winter'] + season_months['Spring'] if m in df.columns]
    df['YearlyAvg'] = df[months].mean(axis=1)
    max_avg = df['YearlyAvg'].max()
    min_avg = df['YearlyAvg'].min()
    warmest = df[df['YearlyAvg'] == max_avg]['STATION_NAME'].unique().tolist()
    coolest = df[df['YearlyAvg'] == min_avg]['STATION_NAME'].unique().tolist()
    return warmest, coolest

if __name__ == "__main__":
    folder = "temperatures"
    df = load_all_temperatures_data(folder)

    # 1. Seasonal averages
    seasonal_averages = calculate_seasonal_averages(df)
    with open("average_temp.txt", "w") as f:
        f.write("Season\tAverage_Temperature\n")
        for season, avg in seasonal_averages.items():
            f.write(f"{season}\t{avg:.2f}\n")

    # 2. Station(s) with the largest temperature range
    largest_range_stations = find_largest_temperatures_range(df)
    with open("largest_temp_range_station.txt", "w") as f:
        f.write("Station(s) with the largest temperature range:\n")
        for station in largest_range_stations:
            f.write(f"- {station}\n")

    # 3. Warmest and coolest station(s)
    warmest, coolest = find_warmest_and_coolest_stations(df)
    with open("warmest_and_coolest_station.txt", "w") as f:
        f.write("Warmest Station(s):\n")
        for station in warmest:
            f.write(f"- {station}\n")
        f.write("\nCoolest Station(s):\n")
        for station in coolest:
            f.write(f"- {station}\n")

    print("✅ Analysis complete. Output files have been created.")
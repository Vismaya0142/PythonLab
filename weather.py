# Step 1: Create a list of dictionaries for each day's data

weather_data = [
    {"date": "2024-08-01", "max_temp": 29, "min_temp": 21, "humidity": 65},
    {"date": "2024-08-02", "max_temp": 31, "min_temp": 23, "humidity": 70},
    {"date": "2024-08-03", "max_temp": 28, "min_temp": 22, "humidity": 60},
    {"date": "2024-08-04", "max_temp": 30, "min_temp": 24, "humidity": 75},
    {"date": "2024-08-05", "max_temp": 32, "min_temp": 25, "humidity": 80},
    {"date": "2024-08-06", "max_temp": 33, "min_temp": 26, "humidity": 85},
    {"date": "2024-08-07", "max_temp": 27, "min_temp": 20, "humidity": 55},
    {"date": "2024-08-08", "max_temp": 34, "min_temp": 28, "humidity": 90},
    {"date": "2024-08-09", "max_temp": 35, "min_temp": 29, "humidity": 95},
    {"date": "2024-08-10", "max_temp": 36, "min_temp": 30, "humidity": 100},
]

# Step 2: Write a function to find the highest and lowest temperatures recorded during the period
def find_temperature_extremes(data):
    max_temp = max(data, key=lambda x: x['max_temp'])['max_temp']
    min_temp = min(data, key=lambda x: x['min_temp'])['min_temp']
    return max_temp, min_temp

# Step 3: Write a function to determine the number of days with temperatures above 30°C
def count_days_above_threshold(data, threshold=30):
    return sum(1 for day in data if day['max_temp'] > threshold)

# Step 4: Write a function to compute the average humidity over the specified period
def calculate_average_humidity(data):
    total_humidity = sum(day['humidity'] for day in data)
    return total_humidity / len(data)

# Testing the functions
max_temp, min_temp = find_temperature_extremes(weather_data)
days_above_30 = count_days_above_threshold(weather_data)
average_humidity = calculate_average_humidity(weather_data)

print(f"Highest temperature recorded: {max_temp}°C")
print(f"Lowest temperature recorded: {min_temp}°C")
print(f"Number of days with temperatures above 30°C: {days_above_30}")
print(f"Average humidity over the period: {average_humidity:.2f}%")

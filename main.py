import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data/temperature_data.csv")

temperature = np.array(data["Temperature"])

# Temperature category function
def get_category(temp):
    if temp >= 28:
        return "Hot"
    elif temp >= 24:
        return "Normal"
    else:
        return "Cold"


# Apply category to every temperature
data["Category"] = data["Temperature"].apply(get_category)

# Statistics
average_temp = np.mean(temperature)
maximum_temp = np.max(temperature)
minimum_temp = np.min(temperature)
total_records = len(data)

hot = np.sum(temperature >= 28)
normal = np.sum((temperature >= 24) & (temperature < 28))
cold = np.sum(temperature < 24)


# Main window
root = tk.Tk()
root.title("Temperature Trend Visualization Dashboard")
root.geometry("1000x700")


# Title
tk.Label(
    root,
    text="Temperature Trend Visualization Dashboard",
    font=("Arial", 24, "bold")
).pack(pady=20)


# Summary
tk.Label(
    root,
    text=f"Average: {average_temp:.2f} °C     "
         f"Maximum: {maximum_temp} °C     "
         f"Minimum: {minimum_temp} °C     "
         f"Records: {total_records}",
    font=("Arial", 14, "bold")
).pack(pady=15)


# Category information
tk.Label(
    root,
    text=f"Hot: {hot}     Normal: {normal}     Cold: {cold}",
    font=("Arial", 15, "bold")
).pack(pady=10)


# Line Chart
def show_line_chart():

    plt.figure(figsize=(10, 5))

    plt.plot(
        data["Date"],
        data["Temperature"],
        marker="o"
    )

    plt.title("Daily Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


# Bar Chart
def show_bar_chart():

    plt.figure(figsize=(10, 5))

    plt.bar(
        data["Date"],
        data["Temperature"]
    )

    plt.title("Daily Temperature Bar Chart")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


# Pie Chart
def show_pie_chart():

    labels = ["Hot", "Normal", "Cold"]
    values = [hot, normal, cold]

    plt.figure(figsize=(7, 7))

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Temperature Category Distribution")

    plt.show()


# Buttons
tk.Button(
    root,
    text="Show Line Chart",
    font=("Arial", 14, "bold"),
    command=show_line_chart,
    width=20
).pack(pady=8)


tk.Button(
    root,
    text="Show Bar Chart",
    font=("Arial", 14, "bold"),
    command=show_bar_chart,
    width=20
).pack(pady=8)


tk.Button(
    root,
    text="Show Pie Chart",
    font=("Arial", 14, "bold"),
    command=show_pie_chart,
    width=20
).pack(pady=8)


# Run dashboard
root.mainloop()
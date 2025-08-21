import matplotlib.pyplot as plt

def predict_temperature(x):
    return 1 * x ** 2 - 4 * x + 5

def predict_humidity(x):
    return 0.5 * x ** 2 - 2 * x + 10

def predict_pressure(x):
    return 1.2 * x

# Generate x values from 0 to 10
x_values = list(range(11))

# Predictions
temps = [predict_temperature(x) for x in x_values]
hums = [predict_humidity(x) for x in x_values]
press = [predict_pressure(x) for x in x_values]

# Plotting
plt.plot(x_values, temps, label='Temperature (°C)', color='red', marker='o')
plt.plot(x_values, hums, label='Humidity (%)', color='blue', marker='s')
plt.plot(x_values, press, label='Pressure (hPa)', color='green', marker='^')

plt.title('Weather Predictions Dashboard')
plt.xlabel('Time Step (x)')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.show()

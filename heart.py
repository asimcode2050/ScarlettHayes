
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
times = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Time in minutes
heart_rates = np.array([72, 75, 78, 80, 82, 85, 90, 92, 95, 100])
times = times.reshape(-1, 1)
heart_rates = heart_rates.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(
    times, heart_rates, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
plt.scatter(X_test, y_test, color='black', label='Actual heart rate')
plt.plot(X_test, predictions, color='blue',
         linewidth=2, label='Predicted heart rate')
plt.xlabel('Time (minutes)')
plt.ylabel('Heart Rate (bpm)')
plt.legend()
plt.show()
for actual, predicted in zip(y_test, predictions):
    print(f'Actual: {actual[0]} bpm, Predicted: {predicted[0]:.2f} bpm')

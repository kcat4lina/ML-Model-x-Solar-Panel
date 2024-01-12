import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Collect data from photoresistors
photoresistor_data = []
for hour in range(24):
    photoresistor_readings = []
    for minute in range(60):
        # Read the photoresistor value
        photoresistor_value = analogRead(A0)

        # Add the photoresistor value to the list
        photoresistor_readings.append(photoresistor_value)

    # Calculate the average photoresistor value for the hour
    average_photoresistor_value = sum(photoresistor_readings) / len(photoresistor_readings)

    # Add the hour and average photoresistor value to the data list
    photoresistor_data.append((hour, average_photoresistor_value))

# Convert the data to a Pandas DataFrame
photoresistor_data_df = pd.DataFrame(photoresistor_data, columns=['hour', 'average_photoresistor_value'])

# Split the data into training and testing sets
X = photoresistor_data_df['average_photoresistor_value'].values.reshape(-1, 1)
y = photoresistor_data_df['hour'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model on the test set
y_pred = model.predict(X_test)
print(model.score(X_test, y_test))

# Use the model to predict the hour of the day based on a new photoresistor reading
new_photoresistor_value = analogRead(A0)
predicted_hour = model.predict([[new_photoresistor_value]])[0]
print("Predicted hour:", predicted_hour)

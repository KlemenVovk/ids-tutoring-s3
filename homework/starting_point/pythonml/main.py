import psycopg2
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import os
import mysql.connector

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=os.environ.get("POSTGRES_HOST"),
    database=os.environ.get("POSTGRES_DB"),
    user=os.environ.get("POSTGRES_USER"),
    password=os.environ.get("POSTGRES_PASSWORD")
)

# Fetch the California housing dataset from the database
query = "SELECT * FROM housing"
df = pd.read_sql_query(query, conn)
conn.close()

# Split the data into features and target
X = df.drop('y', axis=1)
y = df['y']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Calculate RMSE
rmse = mean_squared_error(y_test, predictions, squared=False)
print(f"RMSE: {rmse}")

# Save the predictions to a CSV file
if not os.path.exists("predictions"):
    os.mkdir("predictions")
pd.DataFrame(predictions).to_csv("predictions/predictions.csv", index=False)

# Connect to the MySQL database
conn = mysql.connector.connect(
    host=os.environ.get("MYSQL_HOST"),
    database=os.environ.get("MYSQL_DATABASE"),
    user=os.environ.get("MYSQL_USER"),
    password=os.environ.get("MYSQL_PASSWORD")
)

# Create the predictions table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    actual FLOAT,
    predicted FLOAT
)
"""
cursor = conn.cursor()
cursor.execute(create_table_query)
conn.commit()

# Insert the predictions into the database (use parameterized queries to prevent SQL injection)
insert_query = "INSERT INTO predictions (actual, predicted) VALUES (%s, %s)"
for i in range(len(y_test)):
    # change type from numpy.float64 to float
    cursor.execute(insert_query, (float(y_test.iloc[i]), float(predictions[i])))
conn.commit()
conn.close()

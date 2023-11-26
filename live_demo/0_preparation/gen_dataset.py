import numpy as np
import pandas as pd

SEED = 0
N_SAMPLES = 1000

np.random.seed(SEED)

# Define ranges for features
x_range = (10, 50)
y_range = (5, 30)
z_range = (2, 15)
material_types = ['steel', 'aluminum', 'copper']
complexity_range = (1, 10)
machining_processes = ['milling', 'drilling', 'turning']

# Generate random data
x_dimensions = np.round(np.random.uniform(*x_range, size=N_SAMPLES), 2)
y_dimensions = np.round(np.random.uniform(*y_range, size=N_SAMPLES), 2)
z_dimensions = np.round(np.random.uniform(*z_range, size=N_SAMPLES), 2)
material = np.random.choice(material_types, size=N_SAMPLES)
complexity = np.random.randint(*complexity_range, size=N_SAMPLES)
processes = np.random.choice(machining_processes, size=N_SAMPLES)

# Generate target feature (production time)
# Adjust the formula based on your specific needs
production_time = (
    0.5 * x_dimensions**2 + 
    0.6 * y_dimensions**1.5 +
    0.3 * z_dimensions**2 +
    0.4 * complexity**2 +
    np.where(material == 'Steel', 0.9, np.where(material == 'Aluminum', 0.5, 0.3)) +
    np.where(processes == 'Milling', 0.7, np.where(processes == 'Drilling', 0.8, 0.5)) +
    np.random.normal(scale=2, size=N_SAMPLES)
).astype(int)

# Create a DataFrame
data = pd.DataFrame({
    'x_cm': x_dimensions,
    'y_cm': y_dimensions,
    'z_cm': z_dimensions,
    'material': material,
    'complexity': complexity,
    'process': processes,
    'time_min': production_time
})

# Save the DataFrame to a CSV file
data.to_csv('../dataset.csv', index=False)

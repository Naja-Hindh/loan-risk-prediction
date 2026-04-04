import pandas as pd

# Select only important columns
cols = ['loan_amnt','term','int_rate','annual_inc','dti',
        'emp_length','home_ownership','purpose','loan_status']

# Load 15,000 rows from original dataset
df = pd.read_csv("data/loan.csv", usecols=cols, nrows=10000)

# Save as new smaller file
df.to_csv("data/sample_loan.csv", index=False)

print("Sample dataset created successfully!")

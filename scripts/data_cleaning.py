import pandas as pd

# Load dataset (20k rows only)
df = pd.read_csv("data/sample_loan.csv", low_memory=False)
# Select important columns
df = df[['loan_amnt', 'term', 'int_rate', 'annual_inc', 'dti',
         'emp_length', 'home_ownership', 'purpose', 'loan_status']]

print("Selected columns loaded")

# Remove missing values
df = df.dropna()

# Clean interest rate (remove %)
df['int_rate'] = df['int_rate'].astype(str).str.replace('%', '').astype(float)

# Clean term (convert '36 months' → 36)
df['term'] = df['term'].str.extract('(\d+)').astype(int)

# Convert target variable
df['loan_status'] = df['loan_status'].apply(
    lambda x: 1 if x == 'Fully Paid' else 0
)

print("\nCleaned Data Sample:")
print(df.head())

print("\nFinal Shape:", df.shape)

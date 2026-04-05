#Higher income borrowers tend to repay loans more successfully,
#while lower income groups show higher default risk.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data/sample_loan.csv", low_memory=False)

df['int_rate'] = df['int_rate'].astype(str).str.replace('%','').astype(float)
df['term'] = df['term'].astype(str).str.extract('(\d+)').astype(float)

df = df.dropna()

# Convert loan status
df['loan_status'] = df['loan_status'].apply(lambda x: 1 if x == 'Fully Paid' else 0)
sns.scatterplot(x='annual_inc', y='loan_amnt', hue='loan_status', data=df)
plt.title("Income vs Loan Amount (Default Analysis)")
plt.savefig("report/income_vs_loan.png")
plt.show()

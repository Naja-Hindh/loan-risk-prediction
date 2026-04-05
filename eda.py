

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Higher income borrowers tend to repay loans more successfully,
#while lower income groups show higher default risk.

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


#Higher interest rates are associated with increased default probability,
#indicating higher financial burden.


sns.boxplot(x='loan_status', y='int_rate', data=df)
plt.title("Interest Rate vs Loan Status")
plt.savefig("report/interest_vs_default.png")
plt.show()

#Larger loan amounts slightly increase the risk of default
#due to higher repayment pressure.

sns.boxplot(x='loan_status', y='loan_amnt', data=df)
plt.title("Loan Amount vs Default")
plt.savefig("report/loan_vs_default.png")
plt.show()

#Debt-to-income ratio, interest rate, and loan amount
#show strong influence on loan default risk.

numeric_df = df.select_dtypes(include=['number'])

plt.figure(figsize=(10,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.savefig("report/correlation.png")
plt.show()

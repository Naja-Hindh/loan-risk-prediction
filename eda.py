#Higher income borrowers tend to repay loans more successfully,
#while lower income groups show higher default risk.

sns.scatterplot(x='annual_inc', y='loan_amnt', hue='loan_status', data=df)
plt.title("Income vs Loan Amount (Default Analysis)")
plt.savefig("report/income_vs_loan.png")
plt.show()

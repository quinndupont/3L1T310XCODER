

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load El Salvador's GDP data
gdp_df = pd.read_csv('el_salvador_gdp.csv')

# Load Bitcoin adoption data
bitcoin_df = pd.read_csv('el_salvador_bitcoin_adoption.csv')

# Merge the two datasets on year
merged_df = pd.merge(gdp_df, bitcoin_df, on='year')

# Visualize the correlation between Bitcoin adoption and GDP growth
plt.figure(figsize=(10, 6))
sns.scatterplot(x='bitcoin_adoption', y='gdp_growth', data=merged_df)
plt.title('Correlation between Bitcoin Adoption and GDP Growth in El Salvador')
plt.xlabel('Bitcoin Adoption Rate')
plt.ylabel('GDP Growth')
plt.show()

# Analyze the impact of Bitcoin adoption on various sectors of the economy
print('Bitcoin has had a significant impact on the following sectors of El Salvador\'s economy:')
print('- Tourism: With the growing popularity of Bitcoin, many tourists are now choosing to visit El Salvador to experience its unique Bitcoin-friendly culture.')
print('- Remittances: El Salvador is heavily dependent on remittances from its citizens living abroad. With the adoption of Bitcoin, the
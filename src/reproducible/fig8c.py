import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np


print("----------------------Figure 8c--------------------")
# Reload the Series from the CSV files
normal_scores = pd.read_csv('normal_8c.csv', header=None).squeeze()
adblock_scores = pd.read_csv('adblock_8c.csv', header=None).squeeze()

# Compute the CDFs
normal_cdf = normal_scores.value_counts(normalize=True).sort_index().cumsum()
adblock_cdf = adblock_scores.value_counts(normalize=True).sort_index().cumsum()


# Plot the CDFs
plt.figure(figsize=(5, 4))
plt.plot(normal_cdf.index, normal_cdf.values, label='Ad elements', marker='o')
plt.plot(adblock_cdf.index, adblock_cdf.values, label='Website elements', marker='o')
plt.xlim(0, 15)
plt.ylim(0.4, 1)
plt.xlabel('Lagugage of Page')
plt.ylabel('CDF')
plt.title('Figure 8(c)')
plt.legend()
plt.grid(True)
plt.show()
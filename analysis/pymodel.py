#!/usr/bin/python
import logging
import os

import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

sns.set_style("whitegrid")
sns.set_context("paper")

log_file = os.path.join('logs', 'pymodel_log.txt')
plots_dir = os.path.join('output', 'plots')

# Set up logging
logging.basicConfig(
    filename=log_file,
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)

logger = logging.getLogger('pymodel')

logger.info('Create plots directory if not already there')
os.makedirs(plots_dir, exist_ok=True)

logger.info('Create dataframe from input CSV')
df = pd.read_csv(os.path.join('output', 'input.csv'))

logger.info('Running correlation')
corr_df = df[['bmi', 'age', 'recent_salbutamol_count', 'bp_sys', 'bp_dias']].corr()

logger.info('Correlation: %s', str(corr_df['bmi'].to_dict()))

logger.info('Plotting correlation heatmap')
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(corr_df, annot=True, ax=ax)
ax.set_title("Example of a correlation heatmap")
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'corr_heatmap.png'))

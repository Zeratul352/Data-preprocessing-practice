import pandas as pd


def target_encode_smoothing(df, column, target, k):
    """
    Perform target encoding on a categorical column with smoothing.

    Parameters:
    df (pd.DataFrame): DataFrame containing the categorical column and target variable.
    column (str): Name of the categorical column to encode.
    target (str): Name of the target variable.
    k (float): Smoothing parameter to control the impact of small sample sizes.

    Returns:
    pd.DataFrame: DataFrame with an additional encoded column.
    """
    mean_target = df[target].mean()
    agg = df.groupby(column)[target].agg(['count', 'mean'])
    counts = agg['count']
    means = agg['mean']

    smooth = (counts * means + k * mean_target) / (counts + k)
    df['color_encoded'] = df[column].map(smooth)
    return df



# Example data
data = {
    'color': ['red', 'blue', 'green', 'red', 'blue', 'green'],
    'target': [1, 0, 0, 1, 1, 0]
}
df = pd.DataFrame(data)

# Apply the function to the dataset
df_encoded = target_encode_smoothing(df, 'color', 'target', k=2)
print(df_encoded)

import pandas as pd


def impute_missing_values(df):
    """
    Impute missing values in the dataset using mean, median, and mode.

    Parameters:
    df (pd.DataFrame): DataFrame with missing values.

    Returns:
    pd.DataFrame: DataFrame with missing values imputed.
    """
    a_mean = df['A'].mean()
    df['A'] = df['A'].fillna(a_mean)
    b_median = df['B'].median()
    df['B'] = df['B'].fillna(b_median)
    c_mode = df['C'].mode()
    df['C'] = df['C'].fillna(c_mode.iloc[0])
    return df


# Example data
data = {
    'A': [1, 2, None, 4],
    'B': [5, None, 7, 8],
    'C': ['cat', None, 'dog', 'dog']
}
df = pd.DataFrame(data)

# Apply the function to the dataset
df_imputed = impute_missing_values(df)
print(df_imputed)

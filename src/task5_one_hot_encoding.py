import pandas as pd


def group_rare_categories(df, column, threshold):
    """
    Group rare categories in a categorical column into a new category 'Other'.

    Parameters:
    df (pd.DataFrame): DataFrame containing the categorical column.
    column (str): Name of the column to process.
    threshold (int): Minimum number of occurrences required for a category to remain unchanged.

    Returns:
    pd.DataFrame: DataFrame with rare categories grouped as 'Other'.
    """
    #frequency = df[column].value_counts()
    #df[column].mask(frequency < threshold, 'Other')
    df.loc[df[column].value_counts()[df[column]].values < threshold, column] = "Other"
    return df


def one_hot_encode(df, column):
    """
    Perform one-hot encoding on a categorical column.

    Parameters:
    df (pd.DataFrame): DataFrame containing the categorical column.
    column (str): Name of the column to encode.

    Returns:
    pd.DataFrame: DataFrame with one-hot encoded columns.
    """
    return pd.get_dummies(df, columns=[column])


# Example data
data = {'color': ['red', 'blue', 'green', 'blue', 'red', 'yellow', 'green']}
df = pd.DataFrame(data)

# Apply the functions to the dataset
df = group_rare_categories(df, 'color', 2)
df_encoded = one_hot_encode(df, 'color')
print(df_encoded)

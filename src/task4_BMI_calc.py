import pandas as pd


def calculate_bmi(df):
    """
    Calculate the Body Mass Index (BMI) for each individual.

    Parameters:
    df (pd.DataFrame): DataFrame containing 'height' and 'weight' columns.

    Returns:
    pd.DataFrame: DataFrame with an additional 'BMI' column.
    """
    df['BMI'] = df['weight'] / (df['height'] ** 2)
    return df

def filter(x):
    if x < 18.5:
        return 'Underweight'
    elif x <= 24.9:
        return "Normal weight"
    elif x <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def categorize_bmi(df):
    """
    Categorize the BMI into Underweight, Normal weight, Overweight, and Obese.

    Parameters:
    df (pd.DataFrame): DataFrame containing the 'BMI' column.

    Returns:
    pd.DataFrame: DataFrame with an additional 'BMI_category' column.
    """
    
    df['BMI_category'] = df['BMI'].apply(filter)
    return df


# Example data
data = {
    'height': [1.60, 1.75, 1.82, 1.90, 1.65],
    'weight': [55, 80, 72, 90, 70]
}
df = pd.DataFrame(data)

# Apply the functions to the dataset
df = calculate_bmi(df)
df = categorize_bmi(df)
print(df)

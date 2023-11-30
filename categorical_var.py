import pandas as pd

# Creating a DataFrame with categorical variables
data = {'Gender': ['Male', 'Female', 'Male', 'Female', 'Trans'],
        'Education': ['High School', 'College', 'Postgraduate', 'College', 'High School']}
df = pd.DataFrame(data)

# Converting columns to categorical type
df['Gender'] = pd.Categorical(df['Gender'], categories=['Male', 'Female'], ordered=False)
df['Education'] = pd.Categorical(df['Education'], categories=['High School', 'College', 'Postgraduate'], ordered=True)

# Displaying the DataFrame
print(df)

import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']

# Create a new column ‘IsAlone’ which is 1 if the passenger is alone (i.e., FamilySize = 0), otherwise 0
data['IsAlone'] = np.where(data['FamilySize'] >= 0, 1, 0)
# data['IsAlone'] = (data['FamilySize'] >= 0).astype(int) # Alternate way
# 2. Convert ‘Sex' to numeric (male: 0, female: 1)
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
# 3. One-hot encode the ‘Embarked' column
data = pd.get_dummies(data, columns=['Embarked'])
# 4. Get the mean age of passengers
mean_age = data['Age'].mean()
print( mean_age)
# 5. Get the median fare of passengers
median_fare = data['Fare'].median()
print( median_fare)


# 6. Get the number of passengers by class
print( data['Pclass'].value_counts())
# 7. Get the number of passengers by gender
print( data['Sex'].value_counts())
# 8. Get the number of passengers by survival status
print( data['Survived'].value_counts())
# 9. Calculate the overall survival rate
survival_rate = data['Survived'].mean()
print(format(survival_rate))
# 10. Calculate the survival rate by gender
survival_by_gender = data.groupby('Sex')['Survived'].mean()
print( survival_by_gender)

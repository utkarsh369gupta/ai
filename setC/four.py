import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Hardcoded dataset
data = pd.DataFrame({
    'Petal Length': [1.4, 1.3, 4.7, 4.5, 5.5, 5.1, 4.9, 1.6, 4.2, 5.0],
    'Petal Width': [0.2, 0.2, 1.4, 1.5, 2.1, 1.9, 1.8, 0.4, 1.3, 1.5],
    'Species': ['Setosa', 'Setosa', 'Versicolor', 'Versicolor', 'Virginica', 
                'Virginica', 'Virginica', 'Setosa', 'Versicolor', 'Versicolor']
})

# Preprocess the data
# Convert categorical target to numerical
data['Species'] = data['Species'].astype('category').cat.codes

# Split the data into features and target
X = data[['Petal Length', 'Petal Width']]
y = data['Species']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Visualize the Decision Tree
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=['Petal Length', 'Petal Width'], class_names=['Setosa', 'Versicolor', 'Virginica'], filled=True)
plt.show()

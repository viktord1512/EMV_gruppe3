import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Read data
df = pd.read_csv("iris.csv")

# Head and tail
df.head(5) 
df.tail(5)

# Info
df.info()

# Descriptive statistics
df.describe()

# Handling Missing Values
df = df.dropna()

df_fillna = df.fillna(0) # Filling missing values with 0

# Load the Iris dataset
X = df.iloc[:, 2]
y = df.iloc[:, -1]

# Spilt the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a kNN classifier with a specified value of k (e.g., k=3)
k = 3
knn_classifier = KNeighborsClassifier(n_neighbors=k)

# Fit the classifier to the training data
knn_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn_classifier.predict(X_test)

#Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy og kNN with k={k}: {accuracy * 100:.2f}%")
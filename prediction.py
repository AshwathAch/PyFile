import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Read data from Excel file
df = pd.read_excel("data.xlsx")

# Feature Engineering (example: using lag features)
df["Prev_Color"] = df["Color"].shift(1)

# Drop rows with missing values
df = df.dropna()

# Split data into features and target
X = df[["Price", "Number", "Prev_Color"]]
y = df["Color"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Predict the next color
latest_data = df.tail(1)[["Price", "Number", "Color"]].values
next_color = clf.predict(latest_data)
print("Predicted Next Color:", next_color)

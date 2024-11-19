from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree
data = load_iris()
X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = (y_pred == y_test).mean()
print(f"Model accuracy: {accuracy:.2f}")
tree.plot_tree(model, feature_names=data.feature_names,
               class_names=data.target_names, filled=True)

import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from config.config import DATA_PATH


# -------------------------------
# Load dataset
# -------------------------------
data = pd.read_csv(DATA_PATH)


# -------------------------------
# Category list (cho GUI)
# -------------------------------
ALL_CATEGORIES = sorted(data["category"].unique())


# -------------------------------
# Feature Engineering
# -------------------------------

feature_cols = ["rating", "price", "popularity", "views"]

X = data[feature_cols].values
y = data["purchased"].values


# -------------------------------
# Normalize features
# -------------------------------

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)


# -------------------------------
# Train/Test split
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)


# -------------------------------
# Train model
# -------------------------------

model_linear = LinearRegression()
model_linear.fit(X_train, y_train)


# -------------------------------
# Evaluate model
# -------------------------------

y_pred = model_linear.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"Linear Regression RMSE: {rmse:.4f}")


# -------------------------------
# Predict purchase score
# -------------------------------

def predict_purchase_score(rating, price, popularity, views):

    user_input = np.array([[rating, price, popularity, views]])

    user_input_scaled = scaler.transform(user_input)

    score = model_linear.predict(user_input_scaled)[0]

    return score


# -------------------------------
# Recommendation Function
# -------------------------------

def recommend_products(category=None, max_price=None, top_k=8):

    df = data.copy()

    # filter category
    if category:
        df = df[df["category"] == category]

    # filter price
    if max_price:
        df = df[df["price"] <= max_price]

    # prepare features
    X_pred = df[feature_cols]

    X_pred_scaled = scaler.transform(X_pred)

    scores = model_linear.predict(X_pred_scaled)

    df["score"] = scores

    # sort by recommendation score
    df = df.sort_values("score", ascending=False)

    return df.head(top_k)[["product_name", "category", "price", "rating", "score"]]
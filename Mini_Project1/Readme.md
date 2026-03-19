# 🛒 Smart Product Recommendation System

### 📚 Machine Learning Mini Project

---

## 📌 1. Introduction

Trong các hệ thống thương mại điện tử hiện đại như Amazon, Shopee, việc **gợi ý sản phẩm (Recommendation System)** đóng vai trò quan trọng trong việc:

* Cá nhân hóa trải nghiệm người dùng
* Tăng doanh thu
* Tối ưu hành vi mua sắm

Dự án này xây dựng một **hệ thống gợi ý sản phẩm thông minh** sử dụng **Machine Learning (Linear Regression)** kết hợp với giao diện GUI bằng PyQt5.

---

## 🎯 2. Objectives

* Xây dựng mô hình dự đoán khả năng mua sản phẩm
* Áp dụng Linear Regression vào bài toán thực tế
* Thiết kế GUI trực quan giống hệ thống e-commerce
* Trực quan hóa dữ liệu và kết quả

---

## 🧠 3. Machine Learning Model

### 3.1 Linear Regression

Mô hình dự đoán điểm sản phẩm:

$$
\hat{y} = w_1 x_1 + w_2 x_2 + w_3 x_3 + w_4 x_4 + b
$$

Trong đó:

* $x_1$: rating
* $x_2$: price
* $x_3$: popularity
* $x_4$: views
* $w_i$: trọng số
* $b$: bias
* $\hat{y}$: score dự đoán

---

### 3.2 Vector Form

$$
\hat{y} = \mathbf{w}^T \mathbf{x} + b
$$

---

### 3.3 Loss Function (MSE)

$$
MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

---

### 3.4 Evaluation Metric (RMSE)

$$
RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
$$

---

### 3.5 Feature Scaling (Min-Max)

$$
x' = \frac{x - x_{min}}{x_{max} - x_{min}}
$$

---

## 🤖 4. Recommendation Strategy

### 4.1 Score Function

$$
Score(u, i) = w_1 \cdot rating_i + w_2 \cdot price_i + w_3 \cdot popularity_i + w_4 \cdot views_i + b
$$

---

### 4.2 Top-K Recommendation

$$
Recommend(u) = \operatorname{TopK}(Score(u, i))
$$

---

### 4.3 Hybrid (Advanced)

$$
Score = \alpha \cdot ContentScore + (1 - \alpha) \cdot MLScore
$$

---

## 📊 5. Dataset

Dataset gồm:

* product_name
* category
* rating
* price
* popularity
* views
* purchased
* score

📦 Size: ~5000 products

---

## ⚙️ 6. System Architecture

### 🔁 Flowchart

```
User Input
   │
   ▼
Filter (Category / Price / Search)
   │
   ▼
Feature Processing
   │
   ▼
Linear Regression Model
   │
   ▼
Score Prediction
   │
   ▼
Sort (Descending)
   │
   ▼
Top-K Products
   │
   ▼
Display GUI (Product Cards)
```

---

## 🖥 7. GUI Features

### 🎨 Interface

* Product cards (image, name, rating ⭐, price, score)
* Grid layout giống website thương mại điện tử

---

### 🔎 User Functions

* Search sản phẩm
* Filter category
* Filter price
* Top-K recommendation

---

### 🧺 Shopping Cart

* Add to cart
* Remove item
* Clear cart

---

### 🌙 UI Enhancement

* Dark mode
* Hover animation

---

## 📈 8. Visualization

Hệ thống hỗ trợ:

* 📊 Category Distribution
* 📉 Price Distribution
* 📈 RMSE Evaluation

---

## 🚀 9. Installation

### 1. Clone project

```bash
git clone <your-repo>
cd Mini_Project1/src
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run

```bash
python main.py
```

---

## 🧪 10. Results

* RMSE ≈ 0.48
* Gợi ý sản phẩm hợp lý
* GUI trực quan, dễ sử dụng

---

## 🔥 11. Demo Features

* 🔎 Search
* 🔥 Trending Products
* 🧺 Shopping Cart
* 🌙 Dark Mode
* 📊 Charts

---

## 🚧 12. Future Work

* Content-based filtering
* Collaborative filtering
* Deep Learning (Neural Networks)
* Web deployment (Flask / Streamlit)

---

## 🧾 13. Conclusion

Dự án đã chứng minh:

> Machine Learning có thể áp dụng hiệu quả trong hệ thống gợi ý sản phẩm.

Hệ thống có thể mở rộng để trở thành một nền tảng recommendation thực tế.

---

## 👨‍💻 Author

* Student: *Your Name*
* Course: Machine Learning
* Topic: Product Recommendation System

---

## ⭐ Final Note

Project này phù hợp cho:

* Demo môn Machine Learning
* Portfolio cá nhân
* Nền tảng phát triển hệ thống lớn hơn

---

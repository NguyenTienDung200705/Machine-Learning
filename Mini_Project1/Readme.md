# 🛒 Smart Product Recommendation System  

### 📚 Machine Learning Mini Project  

---

## 📌 1. Introduction  

Trong các hệ thống thương mại điện tử hiện đại như Amazon, Shopee, việc **gợi ý sản phẩm (Recommendation System)** đóng vai trò quan trọng trong việc:  

- Cá nhân hóa trải nghiệm người dùng  
- Tăng doanh thu  
- Tối ưu hành vi mua sắm  

Dự án này xây dựng một **hệ thống gợi ý sản phẩm thông minh** sử dụng **Machine Learning (Linear Regression)** kết hợp với giao diện GUI bằng PyQt5.  

---

## 🎯 2. Objectives  

- Xây dựng mô hình dự đoán khả năng mua sản phẩm  
- Áp dụng Linear Regression vào bài toán thực tế  
- Thiết kế GUI trực quan giống hệ thống e-commerce  
- Trực quan hóa dữ liệu và kết quả  

---

## 🧠 3. Machine Learning Model  

### 3.1 Linear Regression  

Mô hình dự đoán:  

$$
\hat{y} = w_1 x_1 + w_2 x_2 + w_3 x_3 + w_4 x_4 + b
$$  

Trong đó:  

- $x_1$: rating  
- $x_2$: price  
- $x_3$: popularity  
- $x_4$: views  

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

### 3.5 Feature Scaling  

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
Recommend(u) = \text{TopK}_i \left( Score(u, i) \right)
$$  

---

### 4.3 Hybrid  

$$
Score = \alpha \cdot ContentScore + (1 - \alpha) \cdot MLScore
$$  

---

## 📊 5. Dataset  

Dataset gồm các thuộc tính:  

- product_name  
- category  
- rating  
- price  
- popularity  
- views  
- purchased  
- score  

📦 Kích thước: ~5000 sản phẩm  

---

## ⚙️ 6. System Architecture  

Hệ thống được xây dựng theo pipeline gồm các bước chính:

### 6.1 User Input  
Người dùng nhập:  
- Từ khóa tìm kiếm  
- Danh mục  
- Khoảng giá  

---

### 6.2 Data Preprocessing  
- Xử lý dữ liệu thiếu  
- Chuẩn hóa dữ liệu  
- Lọc theo yêu cầu  

---

### 6.3 Feature Engineering  

Các đặc trưng: rating, price, popularity, views  

Chuẩn hóa:  

$$
x' = \frac{x - x_{min}}{x_{max} - x_{min}}
$$  

---

### 6.4 Prediction Model  

Sử dụng Linear Regression:  

$$
Score(u, i) = \mathbf{w}^T \mathbf{x}_i + b
$$  

---

### 6.5 Ranking & Recommendation  

Sắp xếp theo score và chọn Top-K:  

$$
Recommend(u) = \text{TopK}_i \left( Score(u, i) \right)
$$  

---

### 6.6 Presentation  

Hiển thị qua GUI:  

- Product cards  
- Danh sách gợi ý  
- Giỏ hàng  

---

## 🖥 7. GUI Features  

### 🎨 Interface  
- Grid layout  
- Product cards  

---

### 🔎 Functions  
- Search  
- Filter category  
- Filter price  
- Recommendation  

---

### 🧺 Shopping Cart  
- Add / Remove  
- Clear cart  

---

### 🌙 UI  
- Dark mode  
- Hover animation  

---

## 📈 8. Visualization  

- Category Distribution  
- Price Distribution  
- RMSE  

---

## 🚀 9. Installation  

### Clone project  

```bash
git clone <your-repo>
cd Mini_Project1/src
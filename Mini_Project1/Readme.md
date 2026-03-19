# 🛒 Smart Product Recommendation System (Machine Learning Project)

## 📌 1. Giới thiệu

Trong các hệ thống thương mại điện tử hiện đại, **Recommendation System (Hệ gợi ý)** đóng vai trò quan trọng trong việc:

* Cá nhân hóa trải nghiệm người dùng
* Tăng tỷ lệ chuyển đổi (conversion rate)
* Tối ưu doanh thu

Đề tài này xây dựng một **hệ thống gợi ý sản phẩm** sử dụng **Machine Learning (Linear Regression)** kết hợp với giao diện GUI bằng PyQt5 để mô phỏng hệ thống thực tế.

---

## 🎯 2. Mục tiêu

* Xây dựng mô hình dự đoán khả năng người dùng mua sản phẩm
* Thiết kế hệ thống gợi ý sản phẩm dựa trên điểm dự đoán
* Trực quan hóa kết quả bằng GUI
* Áp dụng kiến thức Machine Learning vào bài toán thực tế

---

## 📊 3. Dataset

Dataset gồm các thuộc tính:

* `product_name`: Tên sản phẩm
* `category`: Danh mục
* `rating`: Đánh giá (1 → 5)
* `price`: Giá sản phẩm
* `popularity`: Độ phổ biến
* `views`: Lượt xem
* `purchased`: Đã mua (0 hoặc 1)
* `score`: Điểm tổng hợp (target phụ)

Số lượng dữ liệu: ~5000 sản phẩm

---

## 🤖 4. Mô hình Machine Learning

### 4.1. Linear Regression

Mô hình sử dụng **Hồi quy tuyến tính** để dự đoán:

> Khả năng người dùng sẽ mua sản phẩm

Công thức tổng quát:

\hat{y} = w_1 x_1 + w_2 x_2 + w_3 x_3 + w_4 x_4 + b

Trong đó:

* (x_1): rating
* (x_2): price
* (x_3): popularity
* (x_4): views
* (w_i): trọng số
* (b): bias
* (\hat{y}): giá trị dự đoán (score)

---

### 4.2. Hàm mất mát (Loss Function)

Sử dụng **Mean Squared Error (MSE)**:

MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2

---

### 4.3. Root Mean Squared Error (RMSE)

Đánh giá mô hình:

RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}

Trong project:

```
RMSE ≈ 0.48
```

→ Sai số thấp, mô hình hoạt động ổn định.

---

### 4.4. Chuẩn hóa dữ liệu

Sử dụng **Min-Max Scaling**:

x' = \frac{x - x_{min}}{x_{max} - x_{min}}

Giúp:

* Đưa dữ liệu về [0,1]
* Tránh bias do scale
* Tăng tốc độ hội tụ

---

## 🧠 5. Cách hệ thống hoạt động

### Bước 1: Nhập dữ liệu người dùng

* Category
* Price
* Top-K
* Search

---

### Bước 2: Tiền xử lý

* Lọc theo category
* Lọc theo giá
* Chuẩn hóa dữ liệu

---

### Bước 3: Dự đoán

Model tính:

$$
Score = f(rating, price, popularity, views)
$$

---

### Bước 4: Recommendation

* Sắp xếp theo score giảm dần
* Lấy Top-K sản phẩm

---

## 🎨 6. Giao diện người dùng (GUI)

Hệ thống được xây dựng bằng **PyQt5**, bao gồm:

### 🔹 Product Card

* Ảnh sản phẩm
* Tên
* Rating ⭐
* Giá
* Score

---

### 🔹 Tính năng chính

* 🔎 Search sản phẩm
* 🎯 Filter category
* 💰 Filter price
* 📊 Hiển thị score ML

---

### 🧺 Shopping Cart

* Add to cart
* Remove item
* Clear cart

---

### 🌙 Dark Mode

* Chuyển đổi giao diện sáng/tối

---

## 📊 7. Visualization

Hệ thống hỗ trợ:

### 📈 Category Distribution

* Số lượng sản phẩm theo danh mục

### 📉 Price Distribution

* Histogram giá

### 📊 Model Evaluation

* RMSE

---

## 🔥 8. Kết quả đạt được

* Xây dựng thành công hệ thống gợi ý sản phẩm
* Áp dụng Linear Regression vào bài toán thực tế
* GUI trực quan, dễ sử dụng
* Có thể mở rộng thành hệ thống lớn

---

## 🚀 9. Hướng phát triển

* Content-based filtering
* Collaborative filtering
* Deep Learning (Neural Network)
* Hybrid Recommendation
* Web deployment (Flask / Streamlit)

---

## 🧾 10. Kết luận

Đề tài đã chứng minh rằng:

> Machine Learning có thể ứng dụng hiệu quả trong hệ thống gợi ý sản phẩm.

Hệ thống không chỉ giúp:

* Cá nhân hóa trải nghiệm
* Tăng hiệu quả kinh doanh

mà còn là nền tảng để phát triển các hệ thống recommendation phức tạp hơn.

---

## 👨‍💻 11. Thông tin

* Môn học: Machine Learning
* Đề tài: Product Recommendation System
* Công nghệ: Python, PyQt5, Scikit-learn

---

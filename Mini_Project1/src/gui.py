from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QScrollArea,
    QFrame,
    QComboBox
)

import matplotlib.pyplot as plt
import pandas as pd

from model.model import recommend_products, ALL_CATEGORIES, data, rmse


# ==============================
# PRODUCT CARD
# ==============================

class ProductCard(QFrame):

    def __init__(self, product, add_callback):
        super().__init__()

        self.product = product

        self.setFixedSize(230,280)

        self.setStyleSheet("""
        QFrame{
            background:white;
            border-radius:12px;
            border:1px solid #ddd;
        }

        QFrame:hover{
            border:2px solid #3498db;
        }

        QPushButton{
            background:#3498db;
            color:white;
            border-radius:6px;
            padding:6px;
        }

        QPushButton:hover{
            background:#2980b9;
        }
        """)

        layout = QVBoxLayout()

        img = QLabel()

        pix = QPixmap(200,120)
        pix.fill(Qt.lightGray)

        img.setPixmap(pix)

        name = QLabel(product["product_name"])
        name.setWordWrap(True)
        name.setStyleSheet("font-weight:bold")

        rating = QLabel("⭐"*int(round(product["rating"])))

        price = QLabel(f"$ {product['price']}")
        price.setStyleSheet("color:red;font-weight:bold")

        score = QLabel(f"Score: {product['score']:.2f}")

        btn = QPushButton("Add To Cart")

        btn.clicked.connect(lambda:add_callback(product["product_name"]))

        layout.addWidget(img)
        layout.addWidget(name)
        layout.addWidget(rating)
        layout.addWidget(price)
        layout.addWidget(score)
        layout.addWidget(btn)

        self.setLayout(layout)


# ==============================
# MAIN GUI
# ==============================

class ProductRecommendationGUI(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("🛒 Smart Shopping Recommendation")

        self.resize(1400,800)

        self.cart=[]

        self.dark=False

        main_layout = QHBoxLayout()

        # ==============================
        # LEFT PANEL
        # ==============================

        left = QVBoxLayout()

        title = QLabel("🛒 Smart Product Recommendation System")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("font-size:26px;font-weight:bold")

        left.addWidget(title)

        # filters

        filters = QHBoxLayout()

        self.category = QComboBox()
        self.category.addItem("All")

        for c in ALL_CATEGORIES:
            self.category.addItem(c)

        self.price = QLineEdit()
        self.price.setPlaceholderText("Max Price")

        self.topk = QLineEdit("8")

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search product")

        recommend_btn = QPushButton("Recommend")

        recommend_btn.clicked.connect(self.show_products)

        filters.addWidget(self.category)
        filters.addWidget(self.price)
        filters.addWidget(self.topk)
        filters.addWidget(self.search)
        filters.addWidget(recommend_btn)

        left.addLayout(filters)

        # scroll grid

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)

        self.container = QWidget()
        self.grid = QGridLayout()

        self.container.setLayout(self.grid)
        self.scroll.setWidget(self.container)

        left.addWidget(self.scroll)

        # buttons

        buttons = QHBoxLayout()

        chart_btn = QPushButton("📊 Model Charts")
        chart_btn.clicked.connect(self.show_charts)

        trending_btn = QPushButton("🔥 Trending")
        trending_btn.clicked.connect(self.show_trending)

        dark_btn = QPushButton("🌙 Dark Mode")
        dark_btn.clicked.connect(self.toggle_dark)

        buttons.addWidget(chart_btn)
        buttons.addWidget(trending_btn)
        buttons.addWidget(dark_btn)

        left.addLayout(buttons)

        main_layout.addLayout(left,4)

        # ==============================
        # RIGHT PANEL
        # ==============================

        right = QVBoxLayout()

        cart_title = QLabel("🧺 Shopping Cart")

        cart_title.setStyleSheet("font-size:18px;font-weight:bold")

        self.cart_label = QLabel("Items: 0")

        self.cart_list = QListWidget()

        remove_btn = QPushButton("Remove Selected")
        remove_btn.clicked.connect(self.remove_cart)

        clear_btn = QPushButton("Clear Cart")
        clear_btn.clicked.connect(self.clear_cart)

        stats = QLabel(f"""
Model RMSE : {rmse:.3f}

Dataset Statistics
Products : {len(data)}
Categories : {len(data['category'].unique())}
Average Rating : {data['rating'].mean():.2f}
""")

        right.addWidget(cart_title)
        right.addWidget(self.cart_label)
        right.addWidget(self.cart_list)
        right.addWidget(remove_btn)
        right.addWidget(clear_btn)
        right.addWidget(stats)

        main_layout.addLayout(right,1)

        self.setLayout(main_layout)

    # ==============================
    # SHOW PRODUCTS
    # ==============================

    def show_products(self):

        category = self.category.currentText()

        if category=="All":
            category=None

        max_price=None

        if self.price.text().isdigit():
            max_price=float(self.price.text())

        topk=8

        if self.topk.text().isdigit():
            topk=int(self.topk.text())

        keyword=self.search.text().lower()

        recs = recommend_products(category,max_price,topk)

        if keyword!="":
            recs = recs[recs["product_name"].str.lower().str.contains(keyword)]

        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().setParent(None)

        row=0
        col=0

        for _,product in recs.iterrows():

            card = ProductCard(product,self.add_cart)

            self.grid.addWidget(card,row,col)

            col+=1

            if col==4:
                col=0
                row+=1

    # ==============================
    # CART
    # ==============================

    def add_cart(self,name):

        self.cart.append(name)

        self.cart_list.addItem(name)

        self.cart_label.setText(f"Items: {len(self.cart)}")

    def remove_cart(self):

        row=self.cart_list.currentRow()

        if row>=0:
            self.cart_list.takeItem(row)
            self.cart.pop(row)

        self.cart_label.setText(f"Items: {len(self.cart)}")

    def clear_cart(self):

        self.cart=[]
        self.cart_list.clear()

        self.cart_label.setText("Items: 0")

    # ==============================
    # TRENDING
    # ==============================

    def show_trending(self):

        trending=data.sort_values("rating",ascending=False).head(12)

        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().setParent(None)

        row=0
        col=0

        for _,product in trending.iterrows():

            card=ProductCard(product,self.add_cart)

            self.grid.addWidget(card,row,col)

            col+=1

            if col==4:
                col=0
                row+=1

    # ==============================
    # CHARTS
    # ==============================

    def show_charts(self):

        fig,ax = plt.subplots(1,3,figsize=(12,4))

        data["category"].value_counts().plot(kind="bar",ax=ax[0])
        ax[0].set_title("Category Distribution")

        data["price"].plot(kind="hist",bins=20,ax=ax[1])
        ax[1].set_title("Price Distribution")

        ax[2].bar(["Model RMSE"],[rmse])
        ax[2].set_title("Model Evaluation")

        plt.show()

    # ==============================
    # DARK MODE
    # ==============================

    def toggle_dark(self):

        if not self.dark:

            self.setStyleSheet("""
            QWidget{background:#2f3640;color:white}
            QFrame{background:#353b48}
            QPushButton{background:#40739e;color:white}
            """)

        else:

            self.setStyleSheet("")

        self.dark=not self.dark
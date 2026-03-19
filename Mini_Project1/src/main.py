import sys
from PyQt5.QtWidgets import QApplication

from gui import ProductRecommendationGUI


def main():

    app = QApplication(sys.argv)

    window = ProductRecommendationGUI()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
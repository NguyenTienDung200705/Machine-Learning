import os

# thư mục src
_SRC_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# thư mục gốc project
_PROJECT_ROOT = os.path.dirname(_SRC_DIR)

# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------

DATASET_ROOT = os.path.join(_PROJECT_ROOT, "data")

DATA_PATH = os.path.join(DATASET_ROOT, "ecommerce_recommendation_fixed.csv")
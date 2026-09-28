from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "orders.csv"
OUTPUT = ROOT / "data" / "cleaned_orders.csv"


REQUIRED_COLUMNS = {
    "order_id",
    "customer_id",
    "order_date",
    "product",
    "quantity",
    "unit_price",
    "status",
}


def load_orders(path: Path = INPUT) -> pd.DataFrame:
    return pd.read_csv(path)


def validate_orders(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    if df["order_id"].duplicated().any():
        raise ValueError("Duplicate order_id values found")

    if (df["quantity"] <= 0).any():
        raise ValueError("Quantity must be greater than zero")

    if (df["unit_price"] < 0).any():
        raise ValueError("Unit price cannot be negative")


def transform_orders(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["order_date"] = pd.to_datetime(result["order_date"])
    result["status"] = result["status"].str.lower().str.strip()
    result["gross_value"] = result["quantity"] * result["unit_price"]
    result["recognized_revenue"] = np.where(
        result["status"].eq("paid"),
        result["gross_value"],
        0.0,
    )
    result["order_month"] = result["order_date"].dt.to_period("M").astype(str)
    return result


def summarize(df: pd.DataFrame) -> dict[str, float]:
    return {
        "orders": float(len(df)),
        "gross_value": float(df["gross_value"].sum()),
        "recognized_revenue": float(df["recognized_revenue"].sum()),
        "average_order_value": float(
            df.loc[df["status"].eq("paid"), "gross_value"].mean()
        ),
    }


def run() -> None:
    orders = load_orders()
    validate_orders(orders)
    cleaned = transform_orders(orders)
    cleaned.to_csv(OUTPUT, index=False)

    metrics = summarize(cleaned)
    for key, value in metrics.items():
        print(f"{key}: {value:.2f}")


if __name__ == "__main__":
    run()

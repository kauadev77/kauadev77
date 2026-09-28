import pandas as pd

from src.pipeline import summarize, transform_orders, validate_orders


def sample_orders() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "order_id": 1,
                "customer_id": "C1",
                "order_date": "2026-01-01",
                "product": "Keyboard",
                "quantity": 2,
                "unit_price": 100.0,
                "status": "paid",
            }
        ]
    )


def test_validation_accepts_valid_dataset() -> None:
    validate_orders(sample_orders())


def test_transform_calculates_revenue() -> None:
    transformed = transform_orders(sample_orders())
    assert transformed.loc[0, "gross_value"] == 200.0
    assert transformed.loc[0, "recognized_revenue"] == 200.0


def test_summary_returns_expected_metrics() -> None:
    transformed = transform_orders(sample_orders())
    metrics = summarize(transformed)
    assert metrics["orders"] == 1.0
    assert metrics["average_order_value"] == 200.0

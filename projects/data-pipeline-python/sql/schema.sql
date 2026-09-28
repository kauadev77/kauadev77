CREATE TABLE IF NOT EXISTS orders (
    order_id BIGINT PRIMARY KEY,
    customer_id TEXT NOT NULL,
    order_date DATE NOT NULL,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(12, 2) NOT NULL CHECK (unit_price >= 0),
    status TEXT NOT NULL,
    gross_value NUMERIC(12, 2) NOT NULL,
    recognized_revenue NUMERIC(12, 2) NOT NULL,
    order_month TEXT NOT NULL
);

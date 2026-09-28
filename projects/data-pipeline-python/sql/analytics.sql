-- Revenue by month
SELECT
    order_month,
    SUM(recognized_revenue) AS revenue
FROM orders
GROUP BY order_month
ORDER BY order_month;

-- Top products by recognized revenue
SELECT
    product,
    SUM(recognized_revenue) AS revenue
FROM orders
GROUP BY product
ORDER BY revenue DESC;

-- Order status distribution
SELECT
    status,
    COUNT(*) AS orders
FROM orders
GROUP BY status
ORDER BY orders DESC;

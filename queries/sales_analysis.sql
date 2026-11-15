-- Total revenue
SELECT SUM(revenue) AS total_revenue
FROM sales_data;

-- Revenue by region
SELECT region, SUM(revenue) AS total_revenue
FROM sales_data
GROUP BY region
ORDER BY total_revenue DESC;

-- Top products by revenue
SELECT product, SUM(revenue) AS total_revenue
FROM sales_data
GROUP BY product
ORDER BY total_revenue DESC;

-- Monthly sales trend
SELECT strftime('%Y-%m', order_date) AS month,
       SUM(revenue) AS total_revenue
FROM sales_data
GROUP BY month
ORDER BY month;

-- Sales by channel
SELECT sales_channel, SUM(revenue) AS total_revenue
FROM sales_data
GROUP BY sales_channel
ORDER BY total_revenue DESC;

-- Best-selling product by quantity
SELECT product, SUM(quantity) AS total_quantity
FROM sales_data
GROUP BY product
ORDER BY total_quantity DESC;
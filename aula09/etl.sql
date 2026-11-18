SELECT seller_id, sum(price) as totalRevenue, count(DISTINCT order_id) as qtSales
FROM tb_order_items
GROUP BY seller_id

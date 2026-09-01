CREATE DATABASE Schema_Environment;
  USE Schema_Environment ;
    
    CREATE TABLE users (
      user_id INT,
      username VARCHAR (50),
      country VARCHAR (50)
    );
    
    CREATE TABLE orders (
      order_id INT,
      user_id INT,
      order_amount DECIMAL(10,2),
      order_date DATE
    );
    
    CREATE TABLE fraud_flags (
    order_id INT,
    risk_status VARCHAR (10)
    );
    
    
    INSERT INTO users 
    (user_id,username,country)
    VALUES
    (1001, 'Amit', 'India'),
	(1002, 'Kavita', 'USA'),
    (1003, 'Rahul', 'Germany'),
    (1004, 'Priya', 'India');
    
    INSERT INTO orders
    (order_id, user_id, order_amount, order_date)
    VALUES
    (5001, 1001, 8500.00, '2026-08-01'),
    (5002, 1001, 9000.00, '2026-08-05'),
    (5003, 1002, 12000.00, '2026-08-06'),
    (5004, 1002, 1500.00, '2026-08-09'),
    (5005, 1003, 16500.00, '2026-08-12'),
    (5006, 1004, 3200.00, '2026-08-15');
    
    INSERT INTO fraud_flags 
    (order_id, risk_status) 
    VALUES
    (5001, 'Cleared'),
    (5002, 'Cleared'),
    (5003, 'Flagged'),
    (5004, 'Cleared'),
    (5005, 'Cleared'),
    (5006, 'Cleared');
    
SELECT users.username, SUM(orders.order_amount) AS total_spent
FROM users 
INNER JOIN orders
  ON users.user_id = orders.user_id
GROUP BY users.username
HAVING SUM(orders.order_amount) > 15000 ;



    
    
    
    
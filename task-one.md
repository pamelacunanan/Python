## Task #1
**Write a query which select all female customers**
SELECT * FROM customer WHERE gender = "female"


**Write a query which prints out all customer names with the number of orders they did**
DECLARE @customer_orders TABLE (
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    num_orders INTEGER NOT NULL,
)
INSERT INTO @customer_orders
SELECT customer.first_name, customer.last_name, count(`order`.fk_customer) AS num_orders
    FROM customer LEFT JOIN `order`
        ON customer.id = `order`.fk_customer
    GROUP BY customer.id
    ORDER BY customer.id
PRINT @customer_orders


**Write a query which prints out customers with the money they spend excluding customers without any orders**
DECLARE @customers_spending TABLE (
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    money_spent DEC(38,4) NOT NULL
)
INSERT INTO @customers_spending
SELECT customer.first_name, customer.last_name, sum(`order`.`sum`) AS money_spent
    FROM customer INNER JOIN `order`
        ON customer.id = `order`.fk_customer
    GROUP BY customer.first_name
PRINT @customers_spending


**Write a query which prints out the order_nr of all orders with at least 2 items**
DECLARE @order_numbers TABLE (
    order_nr INT NOT NULL
)
INSERT INTO @order_numbers
SELECT order_nr
    FROM `order` INNER JOIN order_item
        ON `order`.id = order_item.fk_order
    GROUP BY order_nr
    HAVING count(order_item.fk_order) >= 2
PRINT @order_numbers


**Write a query that will pair the oldest male customer with the oldest female customer**
SELECT M.id AS id_male, M.first_name AS name_male, MAX(M.age) AS age_male,
       F.id AS id_female, F.first_name AS name_female, MAX(F.age) AS age_female
    FROM (SELECT id, first_name, age FROM customer WHERE gender="male") AS M,
         (SELECT id, first_name, age FROM customer WHERE gender="female") AS F

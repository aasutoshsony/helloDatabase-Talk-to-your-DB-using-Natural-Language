few_shots = [
    {'Question' : "How many t-shirts do we have left for Nike in extra small size and white color?",
     'SQLQuery' : "SELECT SUM(`stock_quantity`) FROM `t_shirts` WHERE `brand` = 'Nike' AND `color` = 'White' AND `size` = 'XS';",
     'SQLResult': "Result of the SQL query",
     'Answer' : "There are 53 Nike t-shirts left in extra small (XS) size and white color."},
    
    {'Question': "What is the total number of states in nepal?",
     'SQLQuery':"SELECT 'The provided database does not contain information about the states in Nepal.' AS `message`;",
     'SQLResult': "Result of the SQL query",
     'Answer': "This information cannot be answered from the database, as the database only contains data related to t-shirts and discounts. However, in general knowledge, Nepal has 7 provinces (states)."},
    
    {'Question': "What is the total price of the inventory for all Large sized t-shirts?",
     'SQLQuery' : "SELECT SUM(`price` * `stock_quantity`) FROM `t_shirts` WHERE `size` = 'L';",
     'SQLResult': "Result of the SQL query",
     'Answer': "The total price of the inventory for all Large size t-shirts is 17,236."},

    {'Question': "For each brand identify the T-shirt size and color combination with the highest inventory value, showing its stock quantity, inventory value, and rank within that brand.",
    'SQLQuery': "WITH category_values AS (SELECT brand, size, color, SUM(stock_quantity) AS total_units, SUM(price * stock_quantity) AS inventory_value FROM t_shirts GROUP BY brand, size, color), ranked_categories AS (SELECT brand, size, color, total_units, inventory_value, RANK() OVER (PARTITION BY brand ORDER BY inventory_value DESC) AS category_rank FROM category_values) SELECT brand, size, color, total_units, inventory_value, category_rank FROM ranked_categories WHERE category_rank = 1 ORDER BY brand;",
    'SQLResult': "[('Van Huesen', 'XS', 'White', 70, 2940, 1), ('Levi', 'M', 'Black', 69, 2829, 1), ('Nike', 'XS', 'Red', 92, 3404, 1), ('Adidas', 'XL', 'Blue', 89, 3649, 1)]",
    'Answer': "The T-shirt size and color combination with the highest inventory value for Van Huesen is extra small (XS) and white, with a stock quantity of 70 and an inventory value of 2940 (ranking 1st). For Levi, it is medium (M) and black, with a stock quantity of 69 and an inventory value of 2829 (ranking 1st). For Nike, it is extra small (XS) and red, with a stock quantity of 92 and an inventory value of 3404 (ranking 1st). For Adidas, it is extra large (XL) and blue, with a stock quantity of 89 and an inventory value of 3649 (ranking 1st)."
    }
]
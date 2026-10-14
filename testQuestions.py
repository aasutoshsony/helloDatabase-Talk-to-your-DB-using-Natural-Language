# qns6 = {"For each brand, calculate the total inventory value, total units in stock, and percentage contribution to the overall inventory value. Sort by inventory value in descending order."}


qns7 = {"For each brand, identify the T-shirt size and color combination with the highest inventory value, showing its stock quantity, inventory value, and rank within that brand."}

# Entering new SQLDatabaseChain chain...
# SQLQuery:C:\Users\KIIT01\Desktop\LangChain\helloDatabase\lang-env\Lib\site-packages\langchain_google_genai\chat_models.py:3914: UserWarning: Model 'gemini-3.5-flash-lite' uses fixed sampling defaults; the sampling parameter(s) temperature will be ignored.
#   request = self._build_request_config(
# SELECT `brand`, `size`, `color`, `stock_quantity`, (`price` * `stock_quantity`) AS `inventory_value`, DENSE_RANK() OVER (PARTITION BY `brand` ORDER BY (`price` * `stock_quantity`) DESC) AS `rank` FROM `t_shirts` LIMIT 5
# SQLResult: [('Van Huesen', 'XS', 'White', 70, 2940, 1), ('Van Huesen', 'XL', 'Blue', 59, 2124, 2), ('Van Huesen', 'S', 'Red', 95, 1710, 3), ('Van Huesen', 'M', 'White', 86, 1634, 4), ('Van Huesen', 'L', 'White', 49, 1568, 5)]
# Answer:C:\Users\KIIT01\Desktop\LangChain\helloDatabase\lang-env\Lib\site-packages\langchain_google_genai\chat_models.py:3914: UserWarning: Model 'gemini-3.5-flash-lite' uses fixed sampling defaults; the sampling parameter(s) temperature will be ignored.
#   request = self._build_request_config(
# Answer: For Van Huesen, the top combination is XS size in White with 70 stock quantity and an inventory value of 2940 (Rank 1).


qns8={"For every brand(ie all brand), identify the T-shirt size and color combination with the highest inventory value, showing its stock quantity, inventory value, and rank within that brand."}
# Entering new SQLDatabaseChain chain...
# SQLQuery:C:\Users\KIIT01\Desktop\LangChain\helloDatabase\lang-env\Lib\site-packages\langchain_google_genai\chat_models.py:3914: UserWarning: Model 'gemini-3.5-flash-lite' uses fixed sampling defaults; the sampling parameter(s) temperature will be ignored.
#   request = self._build_request_config(
# SELECT `brand`, `size`, `color`, `stock_quantity`, (`price` * `stock_quantity`) AS `inventory_value`, RANK() OVER (PARTITION BY `brand` ORDER BY (`price` * `stock_quantity`) DESC) AS `rank` FROM `t_shirts` LIMIT 5
# SQLResult: [('Van Huesen', 'XS', 'White', 70, 2940, 1), ('Van Huesen', 'XL', 'Blue', 59, 2124, 2), ('Van Huesen', 'S', 'Red', 95, 1710, 3), ('Van Huesen', 'M', 'White', 86, 1634, 4), ('Van Huesen', 'L', 'White', 49, 1568, 5)]
# Answer:C:\Users\KIIT01\Desktop\LangChain\helloDatabase\lang-env\Lib\site-packages\langchain_google_genai\chat_models.py:3914: UserWarning: Model 'gemini-3.5-flash-lite' uses fixed sampling defaults; the sampling parameter(s) temperature will be ignored.
#   request = self._build_request_config(
# Answer: The T-shirt size and color combination with the highest inventory value for Van Huesen is extra small (XS) and white with a stock quantity of 70 and an inventory value of 2940 (ranking 1st).
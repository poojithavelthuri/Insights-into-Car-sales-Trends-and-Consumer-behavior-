select * from sales;

-- Checking column names --
SELECT COLUMN_NAME 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'sales';

-- Changed the column name --
#ALTER TABLE sales 
#CHANGE COLUMN `Price ($)` Price DECIMAL(10, 2);

-- Total sales by Dealer Region --
SELECT Dealer_Region, SUM(Price) AS Total_Sales
FROM sales
GROUP BY Dealer_Region;

-- Sales analysis by car model --
SELECT Model, COUNT(*) AS Total_Sales, AVG(Price) AS Average_Price
FROM sales
GROUP BY Model;

-- Sales by engine type --
SELECT Engine, AVG(Price) AS Average_Price
FROM sales
GROUP BY Engine;

-- Sales by body style --
#ALTER TABLE sales 
#CHANGE COLUMN `Body Style` Body_style VARCHAR(100);

SELECT Body_Style, COUNT(*) AS Total_Sales, AVG(Price) AS Average_Price
FROM sales
GROUP BY Body_Style;

-- Gender-based Sales Analysis---
SELECT Gender, COUNT(*) AS Total_Sales, AVG(Price) AS Average_Price
FROM sales
GROUP BY Gender;

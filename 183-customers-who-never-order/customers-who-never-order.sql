# Write your MySQL query statement below
SELECT name as Customers from Customers left join Orders ON Customers.Id=Orders.customerId WHERE Orders.customerId Is Null;
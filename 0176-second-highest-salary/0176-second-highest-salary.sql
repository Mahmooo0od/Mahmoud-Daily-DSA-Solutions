/* Write your PL/SQL query statement below */
SELECT MAX(salary)  as SecondHighestSalary
FROM (
SELECT id,
salary,
DENSE_RANK() OVER(ORDER BY salary DESC) as rnk
FROM employee)
WHERE rnk = 2;
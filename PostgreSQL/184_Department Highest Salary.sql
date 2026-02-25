-- Write your PostgreSQL query statement below
SELECT D.name as Department, E.name as Employee, E.salary as Salary
FROM Employee as E
JOIN Department as D on E.departmentId = D.id
WHERE(E.departmentId, E.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
)
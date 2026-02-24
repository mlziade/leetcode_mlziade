-- Write your PostgreSQL query statement below
SELECT DISTINCT L1.num as ConsecutiveNums
FROM Logs as L1, Logs as L2, Logs as L3
WHERE L1.Id = L2.Id - 1 AND L2.Id = L3.Id - 1 AND L1.Num = L2.Num AND L2.Num = L3.Num
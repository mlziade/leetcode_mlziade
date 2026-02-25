-- Write your PostgreSQL query statement below
SELECT W2.id
FROM Weather as W1
JOIN Weather as W2 ON W2.recordDate = W1.recordDate + INTERVAL '1 day'
WHERE W2.temperature > W1.temperature;